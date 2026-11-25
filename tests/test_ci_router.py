"""Portable CI router tests: Swift, Node, Python, source identity and runner scope."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/ci-governance/scripts/ci-router.py"
spec = importlib.util.spec_from_file_location("eg_ci_router", SCRIPT)
ci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ci)


def catalog():
    return {
        "contract": "EG_CI_CAPABILITIES_V1",
        "documentation_paths": ["docs/**", "README.md"],
        "fallback_tests": ["smoke"],
        "tests": [
            {"id": "swift-unit", "tier": "V1",
             "paths": ["remote-orbit/Sources/**", "remote-orbit/Tests/**"],
             "runner": ["self-hosted", "macOS", "ARM64", "remoteorbit"],
             "cwd": "remote-orbit", "command": ["swift", "test", "--filter", "Keys"],
             "timeout_minutes": 25},
            {"id": "node-unit", "tier": "V2",
             "paths": ["apps/web/**", "packages/shared/**"],
             "runner": ["ubuntu-latest"], "command": ["npm", "run", "test:web"],
             "setup": [["npm", "ci"]]},
            {"id": "python-unit", "tier": "V2",
             "paths": ["backend/**"],
             "runner": ["ubuntu-latest"],
             "command": ["python3", "-m", "pytest", "backend/tests", "-q"]},
            {"id": "smoke", "tier": "V3", "paths": ["scripts/ci/**"],
             "runner": ["ubuntu-latest"], "command": ["python3", "-m", "compileall", "backend"]}
        ]
    }



class ImportOnlyRoutingTests(unittest.TestCase):
    def test_only_module_import_targets_may_change(self):
        old = b"from old.connection import connect\n\ndef use():\n    return connect()\n"
        new = b"from new.shared import connect\n\ndef use():\n    return connect()\n"
        self.assertTrue(ci._import_only_python(old, new))
        self.assertFalse(ci._import_only_python(old, old))
        self.assertFalse(ci._import_only_python(old, new.replace(b"connect()", b"connect(1)")))
        self.assertFalse(ci._import_only_python(old, new.replace(b"import connect", b"import open")))
        self.assertFalse(ci._import_only_python(old, b"from new.shared import *\n\ndef use():\n    return connect()\n"))
        self.assertFalse(ci._import_only_python(
            b"from __future__ import annotations\nx=1\n",
            b"from __future__ import division\nx=1\n"))
        self.assertTrue(ci._import_only_python(
            b"import old.lib as client\nvalue=client.run()\n",
            b"import new.lib as client\nvalue=client.run()\n"))
        self.assertFalse(ci._import_only_python(
            b"import old.lib\nvalue=1\n",
            b"import new.lib\nvalue=1\n"))
        self.assertFalse(ci._import_only_python(b"x=1\n", b"x=2\n"))
        self.assertFalse(ci._import_only_python(b"from old import x\n", b"def bad(:\n"))
        self.assertFalse(ci._import_only_python(
            b"from old.gateway import api\nvalue = api.load()\n",
            b"value = api.load()\nfrom new.gateway import api\n"))
        self.assertFalse(ci._import_only_python(
            b"from old.one import a\nfrom old.two import b\n",
            b"from new.two import b\nfrom new.one import a\n"))
        self.assertFalse(ci._import_only_python(
            b"from .old import api\n", b"from ..new import api\n"))
        self.assertFalse(ci._import_only_python(
            b"from a import x\nfrom b import x\nprint(x)\n",
            b"from b import x\nfrom a import x\nprint(x)\n"))
        self.assertTrue(ci._import_only_python(
            b"from .old import api\n", b"from .new import api\n"))

    @staticmethod
    def routing_catalog():
        return {
            "contract": "EG_CI_CAPABILITIES_V1",
            "tests": [
                {"id": "imports", "tier": "V1", "paths": ["backend/**"],
                 "runner": ["ubuntu-latest"], "command": ["python3", "-m", "compileall", "backend"]},
                {"id": "wide", "tier": "V3", "paths": ["backend/shared/**"],
                 "runner": ["ubuntu-latest"], "command": ["python3", "-m", "pytest"],
                 "requires": ["domain"], "import_only_alternatives": ["imports"]},
                {"id": "domain", "tier": "V2", "paths": ["backend/domain/**"],
                 "runner": ["ubuntu-latest"], "command": ["python3", "-m", "unittest"]},
            ],
        }

    def test_explicit_opt_in_scopes_without_hiding_behavioral_changes(self):
        cfg = self.routing_catalog()
        path = "backend/shared/connection.py"
        kwargs = {"import_only_paths": [path]}
        scoped = ci.select(cfg, [path], "ready", "a"*40, "b"*40, "digest", **kwargs)
        self.assertEqual(scoped["selected_test_ids"], ["imports"])
        self.assertEqual(scoped["import_only_substitutions"]["wide"]["alternatives"], ["imports"])
        self.assertFalse(scoped["review_required"])
        self.assertFalse(scoped["full_suite_claim"])
        unproved = ci.select(cfg, [path], "ready", "a"*40, "b"*40, "digest")
        self.assertEqual(unproved["selected_test_ids"], ["imports", "wide", "domain"])
        mixed = ci.select(cfg, [path, "backend/shared/behavior.py"], "ready",
                          "a"*40, "b"*40, "digest", **kwargs)
        self.assertEqual(mixed["selected_test_ids"], ["imports", "wide", "domain"])
        manual = ci.select(cfg, [path], "focused", "a"*40, "b"*40,
                           "digest", focused="wide", **kwargs)
        self.assertEqual(manual["selected_test_ids"], ["wide", "domain"])
        release = ci.select(cfg, [path], "release", "a"*40, "b"*40, "digest", **kwargs)
        self.assertEqual(release["selected_test_ids"], ["imports", "wide", "domain"])
        dependent = self.routing_catalog()
        dependent["tests"].append({
            "id": "dependent", "tier": "V3", "paths": ["backend/direct/**"],
            "runner": ["ubuntu-latest"], "command": ["python3", "-m", "pytest"],
            "requires": ["wide"],
        })
        forced = ci.select(dependent, [path, "backend/direct/other.py"], "ready",
                           "a"*40, "b"*40, "digest", **kwargs)
        self.assertEqual(forced["selected_test_ids"], ["imports", "wide", "domain", "dependent"])
        self.assertEqual(forced["import_only_substitutions"], {})

    def test_opt_in_catalog_validation_rejects_invalid_targets(self):
        for alternatives in ("imports", ["missing"], ["wide"], ["imports", "imports"], [42]):
            with self.subTest(alternatives=alternatives):
                cfg = self.routing_catalog()
                cfg["tests"][1]["import_only_alternatives"] = alternatives
                with self.assertRaises(ci.RouteError):
                    ci.validate(cfg)
        cfg = self.routing_catalog()
        cfg["tests"][0]["import_only_alternatives"] = ["domain"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)

    def test_import_only_evidence_is_from_git_not_user_assertion(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "test")
            git("config", "user.email", "test@example.invalid")
            directory = root / "backend/shared"
            directory.mkdir(parents=True)
            path = directory / "connection.py"
            before = "from old.adapter import connection\n\ndef connect():\n    return connection()\n"
            after = before.replace("old.adapter", "new.adapter")
            path.write_text(before)
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            path.write_text(after)
            git("add", "-A")
            git("commit", "-qm", "import path")
            head = git("rev-parse", "HEAD")
            matched = ci.python_import_only_paths(root, base, head)
            self.assertEqual(matched, ["backend/shared/connection.py"])
            plan = ci.select(self.routing_catalog(), ci.changes(root, base, head),
                             "ready", base, head, "digest", import_only_paths=matched)
            self.assertEqual(plan["selected_test_ids"], ["imports"])
            path.write_text(after.replace("connection()", "connection(1)"))
            self.assertEqual(ci.python_import_only_paths(root, base, head), matched)
            self.assertEqual(ci.python_import_only_paths(root, base, head, True), [])
            git("add", "-A")
            git("commit", "-qm", "behavioral")
            final = git("rev-parse", "HEAD")
            self.assertEqual(ci.python_import_only_paths(root, base, final), [])
            git("mv", "backend/shared/connection.py", "backend/shared/renamed.py")
            git("commit", "-qm", "rename")
            renamed = git("rev-parse", "HEAD")
            self.assertEqual(ci.python_import_only_paths(root, final, renamed), [])


    def test_read_only_import_evidence_cli_is_git_derived(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "ci"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "ci@example.invalid"],
                           cwd=root, check=True)
            code = root / "backend/shared/dependency.py"
            code.parent.mkdir(parents=True)
            code.write_text("from old.gateway import api\nvalue = api.load()\n",
                            encoding="utf-8")
            subprocess.run(["git", "add", "-A"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=root, check=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                           cwd=root, text=True).strip()
            code.write_text("from new.gateway import api\nvalue = api.load()\n",
                            encoding="utf-8")
            subprocess.run(["git", "commit", "-qam", "import"], cwd=root, check=True)
            head = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                           cwd=root, text=True).strip()
            script = ROOT / "skills/ci-governance/scripts/ci-router.py"
            result = subprocess.run(
                [sys.executable, str(script), "import-only", "--repo-root", str(root),
                 "--base", base, "--head", head],
                capture_output=True, text=True, check=True,
            )
            evidence = json.loads(result.stdout)
            self.assertEqual(evidence["import_only_paths"],
                             ["backend/shared/dependency.py"])
            self.assertEqual(evidence["changed_paths"],
                             ["backend/shared/dependency.py"])
            rejected = subprocess.run(
                [sys.executable, str(script), "import-only", "--repo-root", str(root),
                 "--base", base, "--head", head, "--worktree"],
                capture_output=True, text=True,
            )
            self.assertEqual(rejected.returncode, 2)
            self.assertIn("IMPORT_ONLY_EVIDENCE_READ_ONLY", rejected.stderr)


class GeneralRouterTests(unittest.TestCase):
    def plan(self, paths, stage="ready", cfg=None, focused=""):
        return ci.select(cfg or catalog(), paths, stage,
                         "a" * 40, "b" * 40, "sha256-placeholder", focused)

    def test_small_swift_change_no_release_build(self):
        p = self.plan(["remote-orbit/Sources/RemoteOrbit/KeyMap.swift"])
        self.assertEqual(p["selected_test_ids"], ["swift-unit"])
        self.assertEqual(p["matrix"]["include"][0]["runner"][-1], "remoteorbit")
        self.assertNotIn("swift build", p["matrix"]["include"][0]["script"])
        self.assertFalse(p["review_required"])

    def test_node_and_python_cross_domain(self):
        p = self.plan(["apps/web/src/page.tsx", "backend/rfq/views.py"])
        self.assertEqual(p["selected_test_ids"], ["node-unit", "python-unit"])
        self.assertIn("npm ci", p["matrix"]["include"][0]["script"])
        self.assertEqual(p["coverage"], "SELECTED_PENDING")

    def test_draft_and_manual_do_not_run_full(self):
        self.assertEqual(self.plan(["remote-orbit/Sources/a.swift"], "draft")["matrix"],
                         {"include": []})
        p = self.plan(["backend/a.py"], "focused", focused="swift-unit")
        self.assertEqual(p["selected_test_ids"], ["swift-unit"])
        self.assertEqual(p["coverage"], "FOCUSED_ONLY")
        self.assertFalse(self.plan(["backend/a.py"], "none")["run_tests"])

    def test_release_full_and_docs_only(self):
        self.assertEqual(len(self.plan(["README.md"], "release")["selected_test_ids"]), 4)
        doc = self.plan(["docs/proposal.md"])
        self.assertFalse(doc["run_tests"])
        self.assertEqual(doc["coverage"], "NO_TESTS_REQUIRED")
        self.assertFalse(doc["review_required"])

    def test_capability_policy_edits_never_autogrant_new_commands(self):
        p = self.plan([".github/ci-capabilities.json"])
        self.assertEqual(p["coverage"], "BASELINE_CAPABILITIES_USED")
        self.assertTrue(p["capabilities_changed"])
        self.assertFalse(p["review_required"])

    def test_unknown_does_not_masquerade_as_pass(self):
        p = self.plan(["unmapped/credential.py"])
        self.assertEqual(p["selected_test_ids"], ["smoke"])
        self.assertEqual(p["unmapped_paths"], ["unmapped/credential.py"])
        self.assertTrue(p["review_required"])  # smoke alone is not readiness proof
        self.assertEqual(p["coverage"], "PARTIAL_UNMAPPED")
        accepted = catalog()
        accepted["fallback_satisfies_ready"] = True
        covered = self.plan(["unmapped/credential.py"], cfg=accepted)
        self.assertFalse(covered["review_required"])
        self.assertEqual(covered["coverage"], "FALLBACK_COVERED")
        self.assertFalse(p["full_suite_claim"])
        without_fallback = catalog()
        without_fallback["fallback_tests"] = []
        self.assertTrue(self.plan(["unmapped/credential.py"], cfg=without_fallback)["review_required"])
        milestone = self.plan(["unmapped/credential.py"], "milestone")
        self.assertFalse(milestone["review_required"])

    def test_duplicate_id_commands_and_path_escape_are_rejected(self):
        cfg = catalog()
        cfg["tests"][1]["id"] = cfg["tests"][0]["id"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg = catalog()
        cfg["tests"][0]["command"] = ["bash", "-c", "hello\nhack"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg = catalog()
        cfg["tests"][0]["cwd"] = "../elsewhere"
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)

    def test_glob_is_anchored_and_not_cross_directory_single_star(self):
        self.assertTrue(ci.match("apps/web/**", "apps/web/src/index.ts"))
        self.assertFalse(ci.match("apps/web/*.ts", "apps/web/src/index.ts"))
        self.assertFalse(ci.match("apps/web/**", "other/apps/web/index.ts"))
        with self.assertRaises(ci.RouteError):
            ci.match("../source/**", "source/index.py")

    def test_real_unicode_paths_and_controls(self):
        self.assertTrue(ci.safe_path("docs/产品设计.md"))
        self.assertTrue(ci.safe_path("src/étude.py"))
        self.assertFalse(ci.safe_path("src/../secret.py"))
        self.assertFalse(ci.safe_path("docs/name\\ncontrol.md"))
        self.assertFalse(ci.safe_path(".git/config"))
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "docs").mkdir()
            (repo / "docs/产品设计.md").write_text("one")
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            (repo / "docs/产品设计.md").write_text("two")
            git("add", "-A")
            git("commit", "-qm", "head")
            self.assertIn("docs/产品设计.md", ci.changes(repo, base, git("rev-parse", "HEAD")))

    def test_overwide_doc_rules_cannot_hide_python_code(self):
        cfg = catalog()
        cfg["documentation_paths"] = ["**"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg["documentation_paths"] = ["*.md"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg = catalog()
        real_doc = self.plan(["docs/说明.md"], cfg=cfg)
        self.assertEqual(real_doc["coverage"], "NO_TESTS_REQUIRED")
        source = self.plan(["docs/unsafe.py"], cfg=cfg)
        self.assertEqual(source["coverage"], "PARTIAL_UNMAPPED")
        self.assertTrue(source["review_required"])  # smoke cannot certify unknown source
        self.assertEqual(source["selected_test_ids"], ["smoke"])
        self.assertEqual(source["unmapped_paths"], ["docs/unsafe.py"])
        cfg["fallback_tests"] = []
        self.assertTrue(self.plan(["docs/unsafe.py"], cfg=cfg)["review_required"])

    def test_integrated_suite_includes_declared_lower_tier_dependency(self):
        cfg = catalog()
        cfg["tests"][1]["requires"] = ["swift-unit"]
        plan = self.plan(["apps/web/src/index.ts"], cfg=cfg)
        self.assertEqual(plan["selected_test_ids"], ["swift-unit", "node-unit"])
        self.assertEqual(plan["effective_tier"], "V2")
        cfg["tests"][0]["requires"] = ["node-unit"]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg = catalog()
        cfg["tests"][1]["requires"] = [["bad"]]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)
        cfg = catalog()
        cfg["fallback_tests"] = [{}]
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)

    def test_source_config_change_is_validated_without_running_pr_commands(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(catalog()))
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            changed = catalog()
            changed["tests"][0]["command"] = ["echo", "new untrusted command"]
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(changed))
            git("add", "-A")
            git("commit", "-qm", "config change")
            head = git("rev-parse", "HEAD")
            process = subprocess.run(
                [sys.executable, str(SCRIPT), "plan", "--repo-root", d,
                 "--base", base, "--head", head], capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            plan = json.loads(process.stdout)
            self.assertEqual(plan["proposed_catalog_status"], "VALIDATED_NOT_EXECUTED")
            self.assertFalse(plan["review_required"])
            self.assertNotIn("new untrusted command", json.dumps(plan["matrix"]))
            invalid = catalog()
            invalid["tests"][0]["tier"] = "V9"
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(invalid))
            git("add", "-A")
            git("commit", "-qm", "invalid proposed config")
            invalid_head = git("rev-parse", "HEAD")
            failed = subprocess.run(
                [sys.executable, str(SCRIPT), "plan", "--repo-root", d,
                 "--base", base, "--head", invalid_head], capture_output=True, text=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("INVALID_TEST_TIER", failed.stderr)

    def test_git_base_config_cannot_be_replaced_by_pr(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "router-tests")
            git("config", "user.email", "router@example.invalid")
            (repo / ".github").mkdir()
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(catalog()))
            (repo / "README.md").write_text("base\n")
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            cfg = catalog()
            cfg["tests"][0]["command"] = ["echo", "untrusted"]
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            (repo / "remote-orbit/Sources").mkdir(parents=True)
            (repo / "remote-orbit/Sources/Key.swift").write_text("changed\n")
            git("add", "-A")
            git("commit", "-qm", "PR")
            head = git("rev-parse", "HEAD")
            paths = ci.changes(repo, base, head)
            self.assertIn(".github/ci-capabilities.json", paths)
            loaded, digest = ci.load(repo, base, ".github/ci-capabilities.json", "base")
            self.assertNotIn("untrusted", ci.shell(loaded["tests"][0]))
            plan = ci.select(loaded, paths, "ready", base, head, digest)
            self.assertFalse(plan["review_required"])  # base commands remain authoritative
            self.assertTrue(plan["capabilities_changed"])
            self.assertEqual(plan["config_source"], "ACCEPTED_BASE")

    def test_discovery_reads_tracked_files_not_dependency_caches(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            (repo / "Package.swift").write_text("// tracked swift manifest")
            (repo / "node_modules").mkdir()
            (repo / "node_modules/package.json").write_text("{}")
            git("add", "Package.swift")
            self.assertEqual(ci.discover(repo)["detected"], ["Swift"])

    def test_renamed_path_preserves_original_test_scope(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "apps/web").mkdir(parents=True)
            (repo / "apps/web/old.ts").write_text("const a=1;\n")
            git("add", "-A")
            git("commit", "-qm", "base")
            before = git("rev-parse", "HEAD")
            (repo / "apps/web/old.ts").rename(repo / "apps/web/new.ts")
            git("add", "-A")
            git("commit", "-qm", "rename")
            changed = ci.changes(repo, before, git("rev-parse", "HEAD"))
            self.assertIn("apps/web/old.ts", changed)
            self.assertIn("apps/web/new.ts", changed)

    def test_explicit_local_run_reports_actual_outcome(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            cfg = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["sample.py"],
                "command": [sys.executable, "-c", "print('probe ok')"]}]}
            planned = ci.select(cfg, ["sample.py"], "focused",
                                "LOCAL", "b" * 40, "digest", "probe")
            self.assertEqual(planned["test_status"], "NOT_RUN")
            self.assertEqual(ci.execute_local(planned, cfg, Path(d)), 0)
            self.assertEqual(planned["test_status"], "PASS")
            cfg["tests"][0]["command"] = [sys.executable, "-c", "raise SystemExit(7)"]
            again = ci.select(cfg, ["sample.py"], "focused",
                              "LOCAL", "b" * 40, "digest", "probe")
            self.assertEqual(ci.execute_local(again, cfg, Path(d)), 1)
            self.assertEqual(again["test_status"], "FAILED")

    def test_symlink_cwd_escape_is_rejected_locally_and_in_ci_script(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            repo = base / "project"
            repo.mkdir()
            outside = base / "outside"
            outside.mkdir()
            (repo / "alias").symlink_to(outside, target_is_directory=True)
            cfg = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["sample.py"], "cwd": "alias",
                "command": [sys.executable, "-c", "print('should not run')"]}]}
            self.assertIn("CI_CWD_OUTSIDE_WORKSPACE", ci.shell(cfg["tests"][0]))
            plan = ci.select(cfg, ["sample.py"], "focused",
                             "LOCAL", "b"*40, "digest", "probe")
            self.assertEqual(ci.execute_local(plan, cfg, repo), 1)
            self.assertEqual(plan["test_status"], "FAILED")
            self.assertEqual(plan["executed_tests"][0]["outcome"],
                             "CWD_OUTSIDE_WORKSPACE")

    def test_local_cli_stdout_is_single_json_result(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            cfg = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["probe.py"],
                "command": [sys.executable, "-c", "print('child output')"]}]}
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "baseline")
            head = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", head)
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "run", "--repo-root", d,
                 "--base", head, "--head", head, "--stage", "focused",
                 "--trusted-ref", "refs/remotes/origin/main",
                 "--focused", "probe"], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(json.loads(proc.stdout)["test_status"], "PASS")
            self.assertIn("child output", proc.stderr)
            self.assertEqual(proc.stdout.count(chr(10)), 1)  # JSON is one line

    def test_local_worktree_staged_unstaged_untracked(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "apps/web").mkdir(parents=True)
            (repo / "apps/web/p.ts").write_text("old")
            git("add", "-A")
            git("commit", "-qm", "base")
            head = git("rev-parse", "HEAD")
            (repo / "apps/web/p.ts").write_text("new")
            (repo / "backend").mkdir()
            (repo / "backend/fix.py").write_text("print(1)")
            git("add", "backend/fix.py")
            (repo / "docs").mkdir()
            (repo / "docs/产品设计.md").write_text("untracked")
            self.assertEqual(ci.changes(repo, head, head), [])
            actual = ci.changes(repo, head, head, include_worktree=True)
            self.assertEqual(actual, ["apps/web/p.ts", "backend/fix.py", "docs/产品设计.md"])
            scoped = ci.select(catalog(), actual, "milestone", head, head, "digest")
            self.assertEqual(scoped["selected_test_ids"], ["node-unit", "python-unit"])
            with self.assertRaises(ci.RouteError):
                ci.changes(repo, "a"*40, head, include_worktree=True)

    def test_fork_hosted_lane_and_selfhosted_exclusion(self):
        cfg = catalog()
        cfg["tests"][1]["fork_safe"] = True
        safe = ci.select(cfg, ["apps/web/p.ts"], "ready",
                         "a"*40, "b"*40, "digest", source_trust="fork")
        self.assertEqual(safe["selected_test_ids"], ["node-unit"])
        self.assertFalse(safe["review_required"])
        blocked = ci.select(cfg, ["remote-orbit/Sources/key.swift"], "ready",
                            "a"*40, "b"*40, "digest", source_trust="fork")
        self.assertEqual(blocked["selected_test_ids"], [])
        self.assertEqual(blocked["fork_blocked_tests"], ["swift-unit"])
        self.assertTrue(blocked["review_required"])
        self.assertEqual(blocked["coverage"], "FORK_PARTIAL")
        cfg["tests"][0]["fork_safe"] = True
        with self.assertRaises(ci.RouteError):
            ci.validate(cfg)

    def test_github_hosted_fork_runner_versions_are_recognized(self):
        for label in ("ubuntu-latest", "ubuntu-24.04", "ubuntu-24.04-arm",
                      "macos-15", "macos-15-intel", "windows-2025"):
            with self.subTest(label=label):
                cfg = catalog()
                cfg["tests"][1]["runner"] = [label]
                cfg["tests"][1]["fork_safe"] = True
                ci.validate(cfg)

    def test_fork_requires_safe_dependencies(self):
        cfg = catalog()
        cfg["tests"][1]["fork_safe"] = True
        cfg["tests"][1]["requires"] = ["swift-unit"]
        plan = ci.select(cfg, ["apps/web/p.ts"], "ready",
                         "a"*40, "b"*40, "digest", source_trust="fork")
        self.assertEqual(plan["selected_test_ids"], [])
        self.assertEqual(plan["fork_blocked_tests"], ["node-unit", "swift-unit"])
        self.assertTrue(plan["review_required"])

    def test_nonregular_doc_symlink_requires_test_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "docs").mkdir()
            doc = repo / "docs/guide.md"
            doc.write_text("normal text")
            git("add", "-A")
            git("commit", "-qm", "normal")
            before = git("rev-parse", "HEAD")
            doc.unlink()
            doc.symlink_to("other.md")
            git("add", "-A")
            git("commit", "-qm", "symlink")
            after = git("rev-parse", "HEAD")
            changed = ci.changes(repo, before, after)
            special = ci.nonregular_changes(repo, before, after)
            self.assertEqual(changed, ["docs/guide.md"])
            self.assertEqual(special, ["docs/guide.md"])
            p = ci.select(catalog(), changed, "ready", before, after,
                          "digest", nonregular_paths=special)
            self.assertEqual(p["unmapped_paths"], ["docs/guide.md"])
            self.assertEqual(p["selected_test_ids"], ["smoke"])
            self.assertTrue(p["review_required"])

    def test_special_file_with_direct_test_coverage_does_not_force_review(self):
        cfg = catalog()
        cfg["tests"][0]["paths"].append("docs/**")
        p = ci.select(cfg, ["docs/guide.md"], "ready",
                      "a"*40, "b"*40, "digest",
                      nonregular_paths=["docs/guide.md"])
        self.assertEqual(p["selected_test_ids"], ["swift-unit"])
        self.assertEqual(p["unmapped_paths"], [])
        self.assertFalse(p["review_required"])

    def test_untracked_symlink_is_nonregular(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "README.md").write_text("original")
            git("add", "-A")
            git("commit", "-qm", "base")
            head = git("rev-parse", "HEAD")
            (repo / "docs").mkdir()
            (repo / "docs/guide.md").symlink_to("missing.md")
            self.assertEqual(ci.nonregular_changes(repo, head, head, True),
                             ["docs/guide.md"])

    def test_local_run_uses_explicit_accepted_remote_ref(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            config = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["sample.py"],
                "command": [sys.executable, "-c", "print('safe')"]}]}
            path = repo / ".github/ci-capabilities.json"
            path.write_text(json.dumps(config))
            git("add", "-A")
            git("commit", "-qm", "accepted")
            accepted = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", accepted)
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
            config["tests"][0]["command"] = [sys.executable, "-c", "print('BAD_UNTRUSTED')"]
            path.write_text(json.dumps(config))
            git("add", "-A")
            git("commit", "-qm", "task")
            task = git("rev-parse", "HEAD")
            args = [sys.executable, str(SCRIPT), "run", "--repo-root", d,
                    "--base", task, "--head", task,
                    "--stage", "focused", "--focused", "probe"]
            blocked = subprocess.run(args, capture_output=True, text=True)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("LOCAL_RUN_REQUIRES_TRUSTED_REMOTE_REF", blocked.stderr)
            passed = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/main"],
                capture_output=True, text=True)
            self.assertEqual(passed.returncode, 0, passed.stderr)
            plan = json.loads(passed.stdout)
            self.assertEqual(plan["config_ref"], accepted)
            self.assertIn("safe", passed.stderr)
            self.assertNotIn("BAD_UNTRUSTED", passed.stderr)
            mismatch = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/main",
                "--config-ref", task], capture_output=True, text=True)
            self.assertNotEqual(mismatch.returncode, 0)
            self.assertIn("TRUSTED_CONFIG_REF_MISMATCH", mismatch.stderr)

    def test_local_run_automatically_includes_dirty_worktree(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            cfg = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["src/**"], "command": [sys.executable, "-c", "print('PASS')"]}]}
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            (repo / "src").mkdir()
            (repo / "src/file.py").write_text("print('original')")
            git("add", "-A")
            git("commit", "-qm", "baseline")
            head = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", head)
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
            (repo / "src/file.py").write_text("print('edited')")
            (repo / "src/untracked.py").write_text("print('untracked')")
            run = subprocess.run([
                sys.executable, str(SCRIPT), "run", "--repo-root", d,
                "--base", head, "--head", head, "--stage", "milestone",
                "--trusted-ref", "refs/remotes/origin/main"],
                capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            plan = json.loads(run.stdout)
            self.assertTrue(plan["worktree_included"])
            self.assertEqual(plan["changed_paths"], ["src/file.py", "src/untracked.py"])
            self.assertEqual(plan["selected_test_ids"], ["probe"])
            self.assertEqual(plan["tested_checkout_head"], head)
            self.assertEqual(plan["test_status"], "PASS")
            # The user-supplied identity must be this checkout, not an older SHA.
            git("commit", "--allow-empty", "-qm", "later")
            drift = subprocess.run([
                sys.executable, str(SCRIPT), "run", "--repo-root", d,
                "--base", head, "--head", head, "--stage", "focused",
                "--focused", "probe", "--trusted-ref", "refs/remotes/origin/main"],
                capture_output=True, text=True)
            self.assertNotEqual(drift.returncode, 0)
            self.assertIn("WORKTREE_HEAD_MISMATCH", drift.stderr)

    def test_local_trusted_ref_must_match_default_branch(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            cfg = {"contract": "EG_CI_CAPABILITIES_V1", "tests": [{
                "id": "probe", "tier": "V1", "runner": ["ubuntu-latest"],
                "paths": ["src/**"], "command": [sys.executable, "-c", "pass"]}]}
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "baseline")
            head = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", head)
            git("update-ref", "refs/remotes/origin/feature", head)
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
            args = [sys.executable, str(SCRIPT), "run", "--repo-root", d,
                    "--base", head, "--head", head,
                    "--stage", "focused", "--focused", "probe"]
            wrong = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/feature"],
                capture_output=True, text=True)
            self.assertNotEqual(wrong.returncode, 0)
            self.assertIn("TRUSTED_REF_NOT_DEFAULT_BRANCH", wrong.stderr)
            mismatch = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/main", "--default-branch", "feature"],
                capture_output=True, text=True)
            self.assertNotEqual(mismatch.returncode, 0)
            self.assertIn("DEFAULT_BRANCH_IDENTITY_MISMATCH", mismatch.stderr)
            git("symbolic-ref", "--delete", "refs/remotes/origin/HEAD")
            unknown = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/main"],
                capture_output=True, text=True)
            self.assertNotEqual(unknown.returncode, 0)
            self.assertIn("DEFAULT_BRANCH_UNKNOWN_USE_DEFAULT_BRANCH", unknown.stderr)
            explicit = subprocess.run(args + [
                "--trusted-ref", "refs/remotes/origin/main", "--default-branch", "main"],
                capture_output=True, text=True)
            self.assertEqual(explicit.returncode, 0, explicit.stderr)

    def test_comparison_base_and_accepted_config_revision_are_independent(self):
        import sys
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            catalog_file = repo / ".github/ci-capabilities.json"
            cfg = catalog()
            catalog_file.write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            cfg["tests"][1]["command"] = ["npm", "run", "updated-test"]
            catalog_file.write_text(json.dumps(cfg))
            (repo / "apps/web").mkdir(parents=True)
            (repo / "apps/web/page.tsx").write_text("updated")
            git("add", "-A")
            git("commit", "-qm", "new accepted config")
            head = git("rev-parse", "HEAD")
            proc = subprocess.run([
                sys.executable, str(SCRIPT), "plan", "--repo-root", d,
                "--base", base, "--head", head, "--config-ref", head],
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            plan = json.loads(proc.stdout)
            self.assertEqual(plan["base"], base)
            self.assertEqual(plan["config_ref"], head)
            node = next(x for x in plan["matrix"]["include"] if x["id"] == "node-unit")
            self.assertIn("updated-test", node["script"])

    def test_fork_safe_dependency_selection_is_catalog_order_independent(self):
        cfg = catalog()
        cfg["tests"][0]["runner"] = ["ubuntu-latest"]
        cfg["tests"][0]["fork_safe"] = True
        cfg["tests"][1]["fork_safe"] = True
        cfg["tests"][1]["requires"] = ["swift-unit"]
        # Dependent comes before dependency in project catalog.
        cfg["tests"] = [cfg["tests"][1], cfg["tests"][0]] + cfg["tests"][2:]
        plan = ci.select(cfg, ["apps/web/index.ts"], "ready",
                         "a"*40, "b"*40, "digest", source_trust="fork")
        self.assertEqual(plan["selected_test_ids"], ["node-unit", "swift-unit"])
        self.assertEqual(plan["fork_blocked_tests"], [])
        self.assertFalse(plan["review_required"])

    def test_reusable_caller_separates_manual_and_pr_required_checks(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn("EG Ready verification", workflow)
        self.assertIn("EG Manual scoped verification", workflow)
        self.assertIn('PR verification must select the Ready scope via auto.', workflow)
        self.assertIn('STAGE" != "ready"', workflow)
        self.assertIn('capabilities_changed:', workflow)
        self.assertIn('comparison_base:', workflow)
        self.assertIn('explicit accepted comparison_base SHA', workflow)
        self.assertIn('merge-base --is-ancestor', workflow)
        self.assertIn('--source-trust "$source_trust"', workflow)
        self.assertEqual(workflow.count('ref: ${{ github.sha }}'), 2)
        self.assertIn('--config-ref "$CONFIG_REF"', workflow)
        self.assertIn('TRUSTED_DEFAULT="refs/remotes/origin/$DEFAULT_BRANCH"', workflow)
        self.assertNotIn('git -C project fetch --no-tags', workflow)
        self.assertIn('EG_CI_NO_TESTS_EXECUTED', workflow)
        caller = (ROOT / "skills/ci-governance/assets/examples/ci-caller.example.yml").read_text()
        self.assertIn("default: none", caller)

    def test_reusable_workflow_is_pinned_and_delegates_execution(self):
        flow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn("workflow_call:", flow)
        published_version = json.loads((ROOT / "plugin.json").read_text())["version"]
        self.assertIn("${{ github.workflow_ref }}", flow)
        self.assertIn("ref: ${{ steps.router_ref.outputs.ref }}", flow)
        caller = (ROOT / "skills/ci-governance/assets/examples/ci-caller.example.yml").read_text()
        self.assertIn(f"@v{published_version}", caller)
        self.assertIn("--config-source base", flow)
        self.assertIn("fromJSON(needs.route.outputs.matrix)", flow)
        self.assertIn("matrix.runner", flow)
        self.assertIn("EG_CI_SELECTED_VERIFICATION_COMPLETE", flow)


class RouterOptimizationTests(unittest.TestCase):
    def test_documentation_paths_exempt_inside_module_wildcards_unless_include_docs(self):
        cfg = catalog()
        cfg["documentation_paths"] = ["docs/**", "apps/web/docs/**", "apps/web/README.md"]
        plan = ci.select(
            cfg,
            ["apps/web/docs/guide.md", "apps/web/README.md"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
        )
        self.assertEqual(plan["selected_test_ids"], [])
        self.assertEqual(plan["unmapped_paths"], [])
        self.assertEqual(plan["coverage"], "NO_TESTS_REQUIRED")
        self.assertFalse(plan["review_required"])

        # Explicit include_docs opts a lane back in for matching doc paths.
        cfg["tests"][1]["include_docs"] = True
        opted_in = ci.select(
            cfg,
            ["apps/web/docs/guide.md"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
        )
        self.assertEqual(opted_in["selected_test_ids"], ["node-unit"])

    def test_exclude_paths_fail_closed_when_excluded_from_all_lanes_and_validate_schema(self):
        cfg = catalog()
        cfg["tests"][1]["exclude_paths"] = ["apps/web/generated/**"]
        plan = ci.select(
            cfg,
            ["apps/web/generated/schema.ts"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
        )
        self.assertEqual(plan["unmapped_paths"], ["apps/web/generated/schema.ts"])
        self.assertEqual(plan["selected_test_ids"], ["smoke"])
        self.assertTrue(plan["review_required"])
        self.assertEqual(plan["coverage"], "PARTIAL_UNMAPPED")

        # Valid code outside exclude_paths still runs node-unit normally.
        normal = ci.select(
            cfg,
            ["apps/web/src/app.tsx", "apps/web/generated/schema.ts"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
        )
        self.assertIn("node-unit", normal["selected_test_ids"])
        self.assertEqual(normal["unmapped_paths"], ["apps/web/generated/schema.ts"])

        for bad_excl in (["**"], ["*"], "apps/web/**", ["a/**", "a/**"], [123]):
            with self.subTest(exclude=bad_excl):
                bad = catalog()
                bad["tests"][0]["exclude_paths"] = bad_excl
                with self.assertRaises(ci.RouteError):
                    ci.validate(bad)

        bad_inc = catalog()
        bad_inc["tests"][0]["include_docs"] = "yes"
        with self.assertRaises(ci.RouteError):
            ci.validate(bad_inc)

    def test_check_catalog_detects_dead_globs_and_unmapped_files(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            (repo / "src").mkdir()
            (repo / "docs").mkdir()
            (repo / "src/app.py").write_text("print('ok')\n")
            (repo / "docs/guide.md").write_text("# guide\n")
            cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "documentation_paths": ["docs/**"],
                "tests": [
                    {
                        "id": "unit",
                        "tier": "V1",
                        "paths": ["src/**"],
                        "runner": ["ubuntu-latest"],
                        "command": [sys.executable, "-c", "pass"],
                    }
                ],
            }
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "init")

            ok = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "check-catalog",
                    "--repo-root",
                    d,
                    "--require-complete-mapping",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(ok.returncode, 0, ok.stderr)
            summary = json.loads(ok.stdout)
            self.assertEqual(summary["status"], "VALID")
            self.assertEqual(summary["dead_patterns"], [])
            self.assertEqual(summary["unmapped_tracked_paths"], [])

            # Add an unmapped non-doc tracked file.
            (repo / "extra").mkdir()
            (repo / "extra/worker.py").write_text("x = 1\n")
            git("add", "-A")
            unmapped = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "check-catalog",
                    "--repo-root",
                    d,
                    "--require-complete-mapping",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(unmapped.returncode, 2)
            self.assertIn("UNMAPPED_TRACKED_PATHS", unmapped.stderr)

            # Dead glob pattern fails check-catalog even without --require-complete-mapping.
            cfg["tests"][0]["paths"].append("missing_dir/**")
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            dead = subprocess.run(
                [sys.executable, str(SCRIPT), "check-catalog", "--repo-root", d],
                capture_output=True,
                text=True,
            )
            self.assertEqual(dead.returncode, 2)
            self.assertIn("DEAD_TEST_PATH_PATTERN", dead.stderr)

    def test_execute_local_topological_order_duration_and_keep_going(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "tests": [
                    {
                        "id": "heavy-v3",
                        "tier": "V3",
                        "paths": ["src/**"],
                        "requires": ["fast-v1"],
                        "runner": ["ubuntu-latest"],
                        "command": [sys.executable, "-c", "print('heavy')"],
                    },
                    {
                        "id": "independent-v2",
                        "tier": "V2",
                        "paths": ["src/**"],
                        "runner": ["ubuntu-latest"],
                        "command": [sys.executable, "-c", "print('indep')"],
                    },
                    {
                        "id": "fast-v1",
                        "tier": "V1",
                        "paths": ["src/**"],
                        "runner": ["ubuntu-latest"],
                        "command": [sys.executable, "-c", "print('fast')"],
                    },
                ],
            }
            plan = ci.select(cfg, ["src/a.py"], "ready", "a" * 40, "b" * 40, "digest")
            self.assertEqual(ci.execute_local(plan, cfg, repo), 0)
            self.assertEqual(
                [item["id"] for item in plan["executed_tests"]],
                ["fast-v1", "independent-v2", "heavy-v3"],
            )
            self.assertTrue(all("duration_ms" in item and item["duration_ms"] >= 0 for item in plan["executed_tests"]))

            # Failing fast-v1 with keep_going=True marks dependent heavy-v3 as DEPENDENCY_FAILED
            # while still running independent-v2.
            cfg["tests"][2]["command"] = [sys.executable, "-c", "raise SystemExit(1)"]
            plan2 = ci.select(cfg, ["src/a.py"], "ready", "a" * 40, "b" * 40, "digest")
            self.assertEqual(ci.execute_local(plan2, cfg, repo, keep_going=True), 1)
            by_id = {item["id"]: item for item in plan2["executed_tests"]}
            self.assertEqual(by_id["fast-v1"]["outcome"], "FAILED")
            self.assertEqual(by_id["independent-v2"]["outcome"], "PASS")
            self.assertEqual(by_id["heavy-v3"]["outcome"], "DEPENDENCY_FAILED")

    def test_worktree_net_zero_revert_reports_no_false_changes(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / "backend").mkdir()
            f = repo / "backend/mod.py"
            f.write_text("from old.a import x\n\ndef run():\n    return x()\n")
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")

            f.write_text("from new.a import x\n\ndef run():\n    return x() + 1\n")
            git("add", "-A")
            git("commit", "-qm", "branch commit")
            head = git("rev-parse", "HEAD")

            # Revert file in working tree back to base content.
            f.write_text("from old.a import x\n\ndef run():\n    return x()\n")
            self.assertEqual(ci.changes(repo, base, head, include_worktree=True), [])
            self.assertEqual(ci.python_import_only_paths(repo, base, head, include_worktree=True), [])

    def test_discover_detects_multiple_languages_manifests_and_workflows(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            (repo / "Cargo.toml").write_text("[package]\nname='x'\n")
            (repo / "go.mod").write_text("module example.com/x\n")
            (repo / ".github/workflows").mkdir(parents=True)
            (repo / ".github/workflows/ci.yml").write_text("name: ci\n")
            git("add", "-A")
            info = ci.discover(repo)
            self.assertEqual(info["detected"], ["Go", "Rust"])
            self.assertEqual(info["manifests"], ["Cargo.toml", "go.mod"])
            self.assertEqual(info["workflows"], [".github/workflows/ci.yml"])

    def test_fork_pr_cannot_bypass_fork_unsafe_lane_via_import_only_alternatives(self):
        cfg = {
            "contract": "EG_CI_CAPABILITIES_V1",
            "tests": [
                {
                    "id": "fast-import-smoke",
                    "tier": "V1",
                    "paths": ["backend/smoke/**"],
                    "runner": ["ubuntu-latest"],
                    "fork_safe": True,
                    "command": ["python3", "-m", "compileall", "backend"],
                },
                {
                    "id": "privileged-hw-integration",
                    "tier": "V3",
                    "paths": ["backend/shared/**"],
                    "runner": ["self-hosted", "macOS"],
                    "fork_safe": False,
                    "import_only_alternatives": ["fast-import-smoke"],
                    "command": ["pytest", "backend/shared"],
                },
            ],
        }
        internal = ci.select(
            cfg,
            ["backend/shared/conn.py"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
            source_trust="internal",
            import_only_paths=["backend/shared/conn.py"],
        )
        self.assertEqual(internal["selected_test_ids"], ["fast-import-smoke"])
        self.assertFalse(internal["review_required"])

        fork = ci.select(
            cfg,
            ["backend/shared/conn.py"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
            source_trust="fork",
            import_only_paths=["backend/shared/conn.py"],
        )
        self.assertEqual(fork["selected_test_ids"], [])
        self.assertEqual(fork["fork_blocked_tests"], ["privileged-hw-integration"])
        self.assertEqual(fork["coverage"], "FORK_PARTIAL")
        self.assertTrue(fork["review_required"])

    def test_check_catalog_catches_symlink_disguised_as_doc_and_dead_doc_patterns(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            (repo / "src").mkdir()
            (repo / "docs").mkdir()
            (repo / "src/a.py").write_text("x = 1\n")
            (repo / "docs/real.md").write_text("# ok\n")
            (repo / "docs/evil.md").symlink_to("../outside_secret")
            cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "documentation_paths": ["docs/**"],
                "tests": [
                    {
                        "id": "unit",
                        "tier": "V1",
                        "paths": ["src/**"],
                        "runner": ["ubuntu-latest"],
                        "command": [sys.executable, "-c", "pass"],
                    }
                ],
            }
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "init")

            symlink_fail = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "check-catalog",
                    "--repo-root",
                    d,
                    "--require-complete-mapping",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(symlink_fail.returncode, 2)
            self.assertIn("UNMAPPED_TRACKED_PATHS", symlink_fail.stderr)
            self.assertIn("docs/evil.md", symlink_fail.stderr)

            # Remove symlink, add a dead documentation_paths entry -> DEAD_DOCUMENTATION_PATTERN.
            git("rm", "-qf", "docs/evil.md")
            cfg["documentation_paths"].append("missing_docs/**")
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("commit", "-qam", "dead doc glob")
            dead_doc = subprocess.run(
                [sys.executable, str(SCRIPT), "check-catalog", "--repo-root", d],
                capture_output=True,
                text=True,
            )
            self.assertEqual(dead_doc.returncode, 2)
            self.assertIn("DEAD_DOCUMENTATION_PATTERN", dead_doc.stderr)

    def test_stage_aware_tiering_and_release_only_lanes(self):
        cfg = {
            "contract": "EG_CI_CAPABILITIES_V1",
            "tests": [
                {
                    "id": "unit-v1",
                    "tier": "V1",
                    "paths": ["src/**"],
                    "runner": ["ubuntu-latest"],
                    "command": [sys.executable, "-c", "pass"],
                },
                {
                    "id": "heavy-v3",
                    "tier": "V3",
                    "paths": ["src/**"],
                    "runner": ["ubuntu-latest"],
                    "command": [sys.executable, "-c", "pass"],
                },
                {
                    "id": "release-only-e2e",
                    "tier": "V3",
                    "stages": ["release"],
                    "paths": ["e2e/**"],
                    "runner": ["ubuntu-latest"],
                    "command": [sys.executable, "-c", "pass"],
                },
            ],
        }
        milestone = ci.select(cfg, ["src/a.py"], "milestone", "a" * 40, "b" * 40, "digest")
        self.assertEqual(milestone["selected_test_ids"], ["unit-v1"])
        self.assertEqual(milestone["unmapped_paths"], [])

        ready_src = ci.select(cfg, ["src/a.py"], "ready", "a" * 40, "b" * 40, "digest")
        self.assertEqual(ready_src["selected_test_ids"], ["unit-v1", "heavy-v3"])

        # A path covered solely by a release-only lane is known on milestone
        # yet flags unmapped on ready if no ready lane covers it.
        ready_e2e = ci.select(cfg, ["e2e/smoke.spec.ts"], "ready", "a" * 40, "b" * 40, "digest")
        self.assertEqual(ready_e2e["unmapped_paths"], ["e2e/smoke.spec.ts"])
        self.assertTrue(ready_e2e["review_required"])

        release = ci.select(cfg, ["src/a.py"], "release", "a" * 40, "b" * 40, "digest")
        self.assertEqual(
            release["selected_test_ids"],
            ["unit-v1", "heavy-v3", "release-only-e2e"],
        )

        bad_stages = json.loads(json.dumps(cfg))
        bad_stages["tests"][0]["stages"] = ["invalid_stage"]
        with self.assertRaises(ci.RouteError):
            ci.validate(bad_stages)

    def test_supersedes_deduplicates_internal_but_preserves_fork_safe_subsets(self):
        cfg = {
            "contract": "EG_CI_CAPABILITIES_V1",
            "tests": [
                {
                    "id": "unit",
                    "tier": "V1",
                    "paths": ["src/**"],
                    "runner": ["ubuntu-latest"],
                    "fork_safe": True,
                    "command": [sys.executable, "-c", "pass"],
                },
                {
                    "id": "full-suite",
                    "tier": "V3",
                    "paths": ["core/**"],
                    "supersedes": ["unit"],
                    "runner": ["self-hosted", "macOS"],
                    "fork_safe": False,
                    "command": [sys.executable, "-c", "pass"],
                },
            ],
        }
        internal = ci.select(
            cfg, ["src/a.py", "core/b.py"], "ready", "a" * 40, "b" * 40, "digest"
        )
        self.assertEqual(internal["selected_test_ids"], ["full-suite"])
        self.assertEqual(internal["superseded_test_ids"], ["unit"])

        # When full-suite is blocked on fork PR, fork_safe subset lane unit must still run!
        fork = ci.select(
            cfg,
            ["src/a.py", "core/b.py"],
            "ready",
            "a" * 40,
            "b" * 40,
            "digest",
            source_trust="fork",
        )
        self.assertEqual(fork["selected_test_ids"], ["unit"])
        self.assertEqual(fork["fork_blocked_tests"], ["full-suite"])
        self.assertEqual(fork["superseded_test_ids"], [])
        self.assertTrue(fork["review_required"])

        # Reject invalid supersedes (lower tier superseding higher tier).
        bad = json.loads(json.dumps(cfg))
        bad["tests"][0]["supersedes"] = ["full-suite"]
        with self.assertRaises(ci.RouteError):
            ci.validate(bad)

    def test_scaffold_cli_generates_valid_capabilities_from_manifests(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            (repo / "README.md").write_text("# Demo\n")
            (repo / "backend").mkdir()
            (repo / "backend/pyproject.toml").write_text("[project]\nname='demo'\n")
            (repo / "Cargo.toml").write_text("[package]\nname='rust-core'\n")
            git("add", "-A")

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "scaffold", "--repo-root", d],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            generated = json.loads(proc.stdout)
            ci.validate(generated)
            self.assertEqual(generated["documentation_paths"], ["README.md"])
            ids = {t["id"] for t in generated["tests"]}
            self.assertIn("backend-python", ids)
            self.assertIn("rust", ids)

    def test_partial_clone_hydrated_blobs_support_offline_routing_and_import_only(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            origin = tmp / "origin.git"
            work = tmp / "work"
            subprocess.run(["git", "init", "-q", str(work)], check=True)
            subprocess.run(["git", "-C", str(work), "config", "user.email", "t@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(work), "config", "user.name", "T"], check=True)
            (work / ".github").mkdir()
            (work / "backend").mkdir()
            (work / "backend/mod.py").write_text("from old.a import fn\n\ndef run():\n    return fn()\n")
            base_cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "tests": [
                    {
                        "id": "import-smoke",
                        "tier": "V1",
                        "paths": ["backend/**"],
                        "runner": ["ubuntu-latest"],
                        "fork_safe": True,
                        "command": [sys.executable, "-c", "pass"],
                    },
                    {
                        "id": "backend-full",
                        "tier": "V3",
                        "paths": ["backend/**"],
                        "import_only_alternatives": ["import-smoke"],
                        "runner": ["ubuntu-latest"],
                        "fork_safe": True,
                        "command": [sys.executable, "-c", "pass"],
                    },
                ],
            }
            (work / ".github/ci-capabilities.json").write_text(json.dumps(base_cfg))
            subprocess.run(["git", "-C", str(work), "add", "-A"], check=True)
            subprocess.run(["git", "-C", str(work), "commit", "-qm", "base"], check=True)
            base_sha = subprocess.check_output(["git", "-C", str(work), "rev-parse", "HEAD"], text=True).strip()

            pr_cfg = json.loads(json.dumps(base_cfg))
            pr_cfg["tests"][1]["command"] = ["echo", "PR_OVERRIDE"]
            (work / ".github/ci-capabilities.json").write_text(json.dumps(pr_cfg))
            (work / "backend/mod.py").write_text("from new.b import fn\n\ndef run():\n    return fn()\n")
            subprocess.run(["git", "-C", str(work), "add", "-A"], check=True)
            subprocess.run(["git", "-C", str(work), "commit", "-qm", "pr"], check=True)
            head_sha = subprocess.check_output(["git", "-C", str(work), "rev-parse", "HEAD"], text=True).strip()

            subprocess.run(["git", "clone", "-q", "--bare", str(work), str(origin)], check=True)
            subprocess.run(["git", "-C", str(origin), "config", "uploadpack.allowfilter", "true"], check=True)
            clone = tmp / "project"
            subprocess.run(["git", "clone", "-q", "--filter=blob:none", f"file://{origin}", str(clone)], check=True)

            # Replicate the workflow hydration step before disabling remote access.
            oids = [
                subprocess.check_output(
                    ["git", "-C", str(clone), "rev-parse", f"{ref}:.github/ci-capabilities.json"],
                    text=True,
                ).strip()
                for ref in (base_sha, head_sha)
            ]
            diff_rows = subprocess.check_output(
                ["git", "-C", str(clone), "diff-tree", "-r", "-M", "--no-commit-id", "--diff-filter=M",
                 base_sha, head_sha, "--", "*.py"],
                text=True,
            ).splitlines()
            for row in diff_rows:
                parts = row.split()
                oids.extend([parts[2], parts[3]])
            subprocess.run(
                ["git", "-C", str(clone), "cat-file", "--batch"],
                input="\n".join(sorted(set(oids))) + "\n",
                text=True,
                capture_output=True,
                check=True,
            )

            shutil.rmtree(origin)
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "plan", "--repo-root", str(clone),
                 "--base", base_sha, "--head", head_sha, "--config-ref", base_sha,
                 "--config-source", "base", "--stage", "ready"],
                capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            plan = json.loads(proc.stdout)
            self.assertEqual(plan["proposed_catalog_status"], "VALIDATED_NOT_EXECUTED")
            self.assertEqual(plan["import_only_paths"], ["backend/mod.py"])
            self.assertEqual(plan["selected_test_ids"], ["import-smoke"])

    def test_zero_sha_local_cli_post_commit_branch_and_parallel_jobs(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", d, *args], stderr=subprocess.DEVNULL
                ).decode().strip()

            git("init", "-q")
            git("config", "user.name", "tests")
            git("config", "user.email", "tests@example.invalid")
            (repo / ".github").mkdir()
            (repo / "src").mkdir()
            (repo / "api").mkdir()
            (repo / "src/a.py").write_text("x = 1\n")
            (repo / "api/b.py").write_text("y = 1\n")
            cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "tests": [
                    {"id": "src-unit", "tier": "V1", "paths": ["src/**"],
                     "runner": ["ubuntu-latest"],
                     "command": [sys.executable, "-c", "print('SRC_OK')"]},
                    {"id": "api-unit", "tier": "V1", "paths": ["api/**"],
                     "runner": ["ubuntu-latest"],
                     "command": [sys.executable, "-c", "print('API_OK')"]},
                ],
            }
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            git("add", "-A")
            git("commit", "-qm", "main")
            main_sha = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", main_sha)
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")

            # Clean feature branch commit (previously blinded --base HEAD --head HEAD).
            (repo / "src/a.py").write_text("x = 2\n")
            (repo / "api/b.py").write_text("y = 2\n")
            git("add", "-A")
            git("commit", "-qm", "feature change")

            plan_proc = subprocess.run(
                [sys.executable, str(SCRIPT), "plan", "--worktree", "--config-source", "file", "--stage", "milestone"],
                cwd=repo, capture_output=True, text=True,
            )
            self.assertEqual(plan_proc.returncode, 0, plan_proc.stderr)
            planned = json.loads(plan_proc.stdout)
            self.assertEqual(planned["base"], "LOCAL")
            self.assertEqual(planned["changed_paths"], ["api/b.py", "src/a.py"])
            self.assertEqual(planned["selected_test_ids"], ["src-unit", "api-unit"])

            run_proc = subprocess.run(
                [sys.executable, str(SCRIPT), "run", "--trusted-ref", "auto",
                 "--base", "origin/main", "--head", "HEAD",
                 "--stage", "milestone", "--jobs", "2", "--keep-going"],
                cwd=repo, capture_output=True, text=True,
            )
            self.assertEqual(run_proc.returncode, 0, run_proc.stderr)
            ran = json.loads(run_proc.stdout)
            self.assertEqual(ran["base"], main_sha)
            self.assertEqual(ran["test_status"], "PASS")
            self.assertEqual([t["id"] for t in ran["executed_tests"]], ["src-unit", "api-unit"])
            self.assertIn("[eg-ci 1/2] PASS src-unit", run_proc.stderr)
            self.assertIn("[eg-ci 2/2] PASS api-unit", run_proc.stderr)

            # Also verify zero-arg run auto-resolves base via merge-base(origin/main, HEAD).
            auto_run = subprocess.run(
                [sys.executable, str(SCRIPT), "run", "--trusted-ref", "auto",
                 "--stage", "milestone", "--jobs", "2"],
                cwd=repo, capture_output=True, text=True,
            )
            self.assertEqual(auto_run.returncode, 0, auto_run.stderr)
            auto_ran = json.loads(auto_run.stdout)
            self.assertEqual(auto_ran["base"], main_sha)
            self.assertEqual(auto_ran["changed_paths"], ["api/b.py", "src/a.py"])
            self.assertEqual(auto_ran["test_status"], "PASS")

    def test_check_catalog_rejects_release_only_coverage_gaps(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / ".github").mkdir()
            (repo / "deploy").mkdir()
            (repo / "deploy/run.sh").write_text("#!/bin/sh\necho ok\n")
            cfg = {
                "contract": "EG_CI_CAPABILITIES_V1",
                "tests": [
                    {"id": "release-soak", "tier": "V3", "stages": ["release"],
                     "paths": ["deploy/**"], "runner": ["ubuntu-latest"],
                     "command": ["true"]},
                ],
            }
            (repo / ".github/ci-capabilities.json").write_text(json.dumps(cfg))
            subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "check-catalog", "--repo-root", str(repo), "--require-complete-mapping"],
                capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 2)
            self.assertIn("UNMAPPED_TRACKED_PATHS", proc.stderr)
            self.assertIn("deploy/run.sh", proc.stderr)

    def test_transitive_supersedes_drops_indirect_subset_lanes(self):
        cfg = {
            "contract": "EG_CI_CAPABILITIES_V1",
            "tests": [
                {"id": "unit-v1", "tier": "V1", "paths": ["src/**"],
                 "runner": ["ubuntu-latest"], "command": ["true"]},
                {"id": "domain-v2", "tier": "V2", "paths": ["domain/**"],
                 "supersedes": ["unit-v1"], "runner": ["ubuntu-latest"], "command": ["true"]},
                {"id": "suite-v3", "tier": "V3", "paths": ["core/**"],
                 "supersedes": ["domain-v2"], "runner": ["ubuntu-latest"], "command": ["true"]},
            ],
        }
        plan = ci.select(cfg, ["src/a.py", "core/b.py"], "ready", "a" * 40, "b" * 40, "digest")
        self.assertEqual(plan["selected_test_ids"], ["suite-v3"])
        self.assertEqual(plan["superseded_test_ids"], ["unit-v1"])
        self.assertEqual(plan["effective_tier"], "V3")

    def test_scaffold_deduplicates_monorepo_roots_and_dual_manifests(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / "package.json").write_text('{"name":"root"}\n')
            (repo / "pyproject.toml").write_text("[tool.pytest.ini_options]\n")
            (repo / "pytest.ini").write_text("[pytest]\n")
            (repo / "apps/web").mkdir(parents=True)
            (repo / "apps/web/package.json").write_text('{"name":"web"}\n')
            subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)

            cfg = ci.scaffold(repo)
            by_id = {t["id"]: t for t in cfg["tests"]}
            self.assertIn("node", by_id)
            self.assertIn("apps-web-node", by_id)
            self.assertIn("pytest", by_id)
            self.assertNotIn("python", by_id)
            self.assertEqual(by_id["node"].get("exclude_paths"), ["apps/web/**"])
            self.assertEqual(by_id["pytest"].get("exclude_paths"), ["apps/web/**"])
            coverage = ci.inspect_catalog_coverage(cfg, ci.tracked_files(repo))
            self.assertEqual(coverage["dead_exclude_patterns"], [])
            plan = ci.select(cfg, ["apps/web/index.ts"], "milestone", "a" * 40, "b" * 40, "digest")
            self.assertEqual(plan["selected_test_ids"], ["apps-web-node"])


if __name__ == "__main__":
    unittest.main()

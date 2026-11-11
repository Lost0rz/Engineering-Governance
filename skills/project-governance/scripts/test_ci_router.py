"""Portable CI router tests: Swift, Node, Python, source identity and runner scope."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "skills/project-governance/scripts/ci-router.py"
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
        # Trusted-base fallback keeps work moving while coverage stays explicit.
        self.assertFalse(p["review_required"])
        self.assertEqual(p["coverage"], "PARTIAL_UNMAPPED")
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
        self.assertFalse(source["review_required"])  # accepted fallback is selected
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

    def test_reusable_caller_separates_manual_and_pr_required_checks(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn("EG Ready verification", workflow)
        self.assertIn("EG Manual scoped verification", workflow)
        self.assertIn('PR verification must select the Ready scope via auto.', workflow)
        self.assertIn('STAGE" != "ready"', workflow)
        self.assertIn('capabilities_changed:', workflow)

    def test_reusable_workflow_is_pinned_and_delegates_execution(self):
        flow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn("workflow_call:", flow)
        self.assertIn("ref: v0.10.0", flow)
        self.assertIn("--config-source base", flow)
        self.assertIn("fromJSON(needs.route.outputs.matrix)", flow)
        self.assertIn("matrix.runner", flow)
        self.assertIn("EG_CI_SELECTED_VERIFICATION_COMPLETE", flow)


if __name__ == "__main__":
    unittest.main()

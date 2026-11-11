"""Conservative VERIFICATION_PLAN_V1 routing and trust-boundary tests."""
import importlib.util
import unittest
from pathlib import Path

P = Path(__file__).with_name("verification-plan.py")
spec = importlib.util.spec_from_file_location("verification_plan", P)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
BASE = "a" * 40
HEAD = "b" * 40


def change(path, status="M", previous=None):
    c = {"status": status, "path": path}
    if previous is not None:
        c["previous_path"] = previous
    return c


def route(*changes, symlinks=frozenset()):
    return mod.select(list(changes), base=BASE, head=HEAD, symlink_paths=symlinks)


class VerificationPlanTests(unittest.TestCase):
    def test_history_document_is_v0_with_honest_skips(self):
        p = route(change("documents/archive/old-notes.md"))
        self.assertEqual(p["tier"], "V0")
        self.assertEqual(p["selected"], ["static_scope"])
        self.assertIn("full_contracts", p["skipped"])
        self.assertEqual(p["test_status"], "TESTS_PENDING")
        self.assertFalse(p["full_suite_claim"])

    def test_readme_is_v1_not_entire_suite(self):
        p = route(change("README.md"))
        self.assertEqual(p["tier"], "V1")
        self.assertIn("policy_contracts", p["selected"])
        self.assertNotIn("full_contracts", p["selected"])

    def test_descriptive_planning_document_is_v1(self):
        self.assertEqual(route(change("documents/plans/notes.md"))["tier"], "V1")

    def test_shared_skill_changes_are_v2(self):
        self.assertEqual(route(change("skills/agent-handoff/SKILL.md"))["tier"], "V2")
        self.assertIn("full_contracts", route(change("skills/agent-handoff/SKILL.md"))["selected"])

    def test_governance_authorization_and_selector_are_v3(self):
        for path in ("AGENTS.md", ".github/workflows/governance-contract-checks.yml",
                     "skills/project-governance/scripts/verification-plan.py",
                     "skills/project-governance/scripts/test_verification_plan.py",
                     "skills/project-governance/references/verification-tiers.md"):
            with self.subTest(path=path):
                self.assertEqual(route(change(path))["tier"], "V3")

    def test_renames_include_old_and_new_identity(self):
        p = route(change("documents/archive/renamed.md", "R100", "AGENTS.md"))
        self.assertEqual(p["tier"], "V3")
        self.assertEqual(len(p["reasons"]), 2)

    def test_rename_from_unknown_path_escalates(self):
        p = route(change("documents/archive/old.md", "R100", "credential.json"))
        self.assertEqual(p["tier"], "V3")

    def test_path_hiding_and_git_metadata_rejected(self):
        for path in ("/tmp/repo", "../secret", "docs/../secret", ".git/config",
                     "docs//a.md", "docs\\a.md", "docs/\nfile", ""):
            with self.subTest(path=repr(path)):
                with self.assertRaises(mod.SelectionError):
                    route(change(path))

    def test_symlink_touched_escalates(self):
        path = "documents/archive/symlink.md"
        self.assertEqual(route(change(path), symlinks=frozenset([path]))["tier"], "V3")

    def test_unknown_and_gitattr_escalate(self):
        for path in (".gitattributes", "unknown.txt", "documents-old/archive.md",
                     "skills-not-really/SKILL.md", "README.md.backup"):
            self.assertEqual(route(change(path))["tier"], "V3")

    def test_diff_parse_multipath_rename_and_copy(self):
        changes = mod.parse_name_status_z(
            b"M\0README.md\0R100\0AGENTS.md\0documents/archive/a.md\0"
            b"C90\0README.md\0documents/notes.md\0")
        self.assertEqual(len(changes), 3)
        self.assertEqual(changes[1]["previous_path"], "AGENTS.md")
        self.assertEqual(changes[2]["status"], "C90")
        self.assertEqual(route(*changes)["tier"], "V3")

    def test_truncated_unknown_or_empty_diff_does_not_skip(self):
        for raw in (b"", b"M\0README.md", b"R100\0a.md\0",
                    b"R100\0a.md\0a.md\0", b"Z\0a.md\0",
                    b"M\0../secret\0", b"M\0\xff\0"):
            with self.subTest(diff=raw):
                with self.assertRaises(mod.SelectionError):
                    mod.parse_name_status_z(raw)

    def test_no_changes_or_same_base_does_not_claim_v0(self):
        with self.assertRaises(mod.SelectionError):
            mod.select([], base=BASE, head=HEAD)
        with self.assertRaises(mod.SelectionError):
            mod.select([change("README.md")], base=BASE, head=BASE)

    def test_mixed_scope_escalates_over_description(self):
        p = route(change("documents/archive/a.md"),
                  change(".github/ISSUE_TEMPLATE/execution-spec.yml"))
        self.assertEqual(p["tier"], "V3")

    def test_policy_source_binds_trusted_base_and_exact_head(self):
        p = route(change("README.md"))
        self.assertEqual((p["base"], p["head"]), (BASE, HEAD))
        self.assertEqual(p["policy_source"], "TRUSTED_BASE")
        self.assertEqual(p["scope_status"], "SCOPE_GATE_PASS")

    def test_real_git_diff_and_rename_include_previous_identity(self):
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", tmp, *args], stderr=subprocess.DEVNULL
                ).decode().strip()
            git("init", "-q")
            git("config", "user.email", "tests@example.invalid")
            git("config", "user.name", "Scoped Test")
            (root / "AGENTS.md").write_text("accepted authority\n", encoding="utf-8")
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            (root / "documents" / "archive").mkdir(parents=True)
            (root / "AGENTS.md").rename(root / "documents" / "archive" / "old.md")
            git("add", "-A")
            git("commit", "-qm", "rename")
            head = git("rev-parse", "HEAD")
            plan = mod.collect(root, base, head)
            self.assertEqual(plan["tier"], "V3")
            self.assertEqual(plan["base"], base)
            self.assertEqual(plan["head"], head)
            self.assertEqual(plan["changes"][0]["previous_path"], "AGENTS.md")

    def test_real_git_diff_and_scope_select_readme_v1(self):
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", tmp, *args], stderr=subprocess.DEVNULL
                ).decode().strip()
            git("init", "-q")
            git("config", "user.email", "tests@example.invalid")
            git("config", "user.name", "Scoped Test")
            (root / "README.md").write_text("description\n", encoding="utf-8")
            git("add", "-A")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD")
            (root / "README.md").write_text("new description\n", encoding="utf-8")
            git("add", "-A")
            git("commit", "-qm", "change")
            head = git("rev-parse", "HEAD")
            plan = mod.collect(root, base, head)
            self.assertEqual(plan["tier"], "V1")
            self.assertEqual(plan["selected"], ["static_scope", "policy_contracts"])



if __name__ == "__main__":
    unittest.main()

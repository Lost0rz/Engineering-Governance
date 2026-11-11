"""Actual task/Skill routing and trusted Git diff-selection tests."""
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("verification-plan.py")
spec = importlib.util.spec_from_file_location("verification_plan", SCRIPT)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)
BASE, HEAD = "a" * 40, "b" * 40


def change(path, status="M", previous=None):
    out = {"status": status, "path": path}
    if previous is not None:
        out["previous_path"] = previous
    return out


def select(*items, symlinks=frozenset()):
    return router.select(list(items), base=BASE, head=HEAD,
                         symlink_paths=symlinks)


class VerificationTests(unittest.TestCase):
    def test_normal_documentation_tiers(self):
        examples = {
            "references/V081_ENTRY_ROUTING_RECEIVER_ACCEPTANCE.md": "V0",
            "documents/archive/old.md": "V0",
            "README.md": "V1",
            "skills/design/SKILL.md": "V2",
            "skills/project-governance/SKILL.md": "V2",
            "skills/project-governance/references/issue-control.md": "V2",
            ".github/ISSUE_TEMPLATE/task-plan.md": "V2",
            "skills/project-governance/assets/control-policy.json": "V3",
            "skills/project-governance/scripts/verification-plan.py": "V3",
            "skills/new-skill/processor.py": "V3",
            ".github/workflows/governance-contract-checks.yml": "V3",
        }
        for path, tier in examples.items():
            with self.subTest(path=path):
                self.assertEqual(select(change(path))["tier"], tier)

    def test_selected_tests_and_packaging_are_separate(self):
        for path, expected in (("README.md", ["static_scope","policy_contracts"]),
                               ("skills/design/SKILL.md", ["static_scope","affected_contracts"]),
                               ("plugin.json", ["static_scope","full_contracts"])):
            with self.subTest(path=path):
                result = select(change(path))
                self.assertEqual(result["selected"], expected)
                self.assertNotIn("package_preview", result["selected"])
                self.assertFalse(result["full_suite_claim"])
        self.assertEqual(select(change("skills/design/SKILL.md"))["affected_suites"],
                         ["test_workflow_contracts.py"])
        self.assertEqual(select(change("skills/project-governance/references/verification-tiers.md"))["affected_suites"],
                         ["test_verification_plan.py", "test_workflow_contracts.py"])

    def test_trust_preserved_for_rename_delete_and_unknown_paths(self):
        renamed = select(change("documents/archive/old.md", "R100",
                                "skills/design/SKILL.md"))
        self.assertEqual(renamed["tier"], "V2")
        self.assertEqual(len(renamed["reasons"]), 2)
        self.assertEqual(select(change("documents/archive/linked.md"),
                                symlinks=frozenset({"documents/archive/linked.md"}))["tier"], "V3")
        self.assertEqual(select(change("unknown.dat"))["tier"], "V3")
        self.assertEqual(select(change(".github/ISSUE_TEMPLATE/script.sh"))["tier"], "V3")
        self.assertEqual(select(change("documents/archive/old.md"),
                                change("plugin.json"))["tier"], "V3")

    def test_malformed_identity_and_diff_denied(self):
        with self.assertRaises(router.SelectionError):
            router.select([], base=BASE, head=HEAD)
        with self.assertRaises(router.SelectionError):
            router.select([change("README.md")], base=BASE, head=BASE)
        for path in ("../escape", ".git/config", "/absolute", "docs//x.md",
                     "docs\\x.md", "line\nfeed.md", ""):
            with self.subTest(path=repr(path)), self.assertRaises(router.SelectionError):
                select(change(path))
        for raw in (b"", b"M\0README.md", b"Z\0README.md\0",
                    b"R100\0old.md\0", b"M\0../escape\0", b"M\0\xff\0"):
            with self.subTest(diff=repr(raw)), self.assertRaises(router.SelectionError):
                router.parse_name_status_z(raw)

    def test_z_diff_includes_previous_rename_identity(self):
        changes = router.parse_name_status_z(
            b"M\0README.md\0R100\0AGENTS.md\0documents/archive/a.md\0")
        self.assertEqual(len(changes), 2)
        self.assertEqual(changes[1]["previous_path"], "AGENTS.md")
        self.assertEqual(select(*changes)["tier"], "V2")

    def test_actual_git_diff_uses_real_refs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", temp, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.email", "tests@example.invalid")
            git("config", "user.name", "Tests")
            (root / "README.md").write_text("before\n", encoding="utf-8")
            git("add", "-A")
            git("commit", "-qm", "base")
            b = git("rev-parse", "HEAD")
            (root / "README.md").write_text("after\n", encoding="utf-8")
            git("add", "-A")
            git("commit", "-qm", "head")
            h = git("rev-parse", "HEAD")
            plan = router.collect(root,b,h)
            self.assertEqual(plan["base"], b)
            self.assertEqual(plan["head"], h)
            self.assertEqual(plan["tier"], "V1")
            self.assertEqual(plan["policy_source"], "TRUSTED_BASE")


if __name__ == "__main__":
    unittest.main()

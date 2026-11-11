"""Behavior-oriented cross-Skill checks; avoid pinning prose wording."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "skills/project-governance/scripts"


def module(filename, name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


policy = module("control-policy.py", "eg_cross_control")
verification = module("verification-plan.py", "eg_cross_verification")


def change(path):
    return {"status": "M", "path": path}


class CrossSkillBehaviorTests(unittest.TestCase):
    def test_nine_skill_entries_exist_and_are_on_demand(self):
        expected = {
            "agent-handoff", "design", "domain-navigation", "evidence-audit",
            "execution-orchestrator", "incident-doctor", "project-governance",
            "project-profile", "solution-design",
        }
        actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
        self.assertEqual(actual, expected)
        for name in expected:
            entry = (ROOT / "skills" / name / "SKILL.md").read_text()
            self.assertTrue(entry.startswith("---\nname: "))
        for ref in ("issue-control", "issue-execution-contract", "verification-tiers",
                    "workspace-lifecycle", "global-routing"):
            self.assertTrue((ROOT / "skills/project-governance/references" /
                             f"{ref}.md").is_file())

    def test_global_policy_is_only_generic_control_owner(self):
        data = json.loads((ROOT / "skills/project-governance/assets/control-policy.json").read_text())
        self.assertEqual(data["contract"], "CONTROL_POLICY_V1")
        self.assertEqual(data["project_agents_control_selectors"], "IGNORED")
        self.assertTrue(data["require_host_authority_for_writes"])
        self.assertFalse(policy.delegated_enabled())
        self.assertFalse(policy.autonomy_enabled())
        for path in ("AGENTS.md", "skills/project-governance/assets/templates/AGENTS.md"):
            lines = (ROOT / path).read_text().splitlines()
            self.assertFalse(any(line.startswith(("CONTROL_MODE:", "ISSUE_APPROVERS:",
                "ISSUE_DELEGATED_APPROVAL:", "ISSUE_WEB_SPEC_AUTHORING:"))
                for line in lines))

    def test_host_direct_work_does_not_need_first_issue_or_mint_writes(self):
        props = dict(repo="Lost0rz/Engineering-Governance", risk="G2",
                     paths=["skills/project-governance/SKILL.md", "skills/agent-handoff/SKILL.md"],
                     effects=["source_edit", "focused_test"], explicit_user_request=True,
                     active_session=True, host_write_permission=True)
        eligible = policy.interactive_scope_eligibility(**props)
        self.assertFalse(eligible["initial_issue_approval_required"])
        self.assertFalse(eligible["per_wp_approval_comment_required"])
        self.assertFalse(eligible["source_write_authorized"])
        self.assertFalse(eligible["persistent_grant"])
        self.assertTrue(eligible["host_action_authorization_required"])
        with self.assertRaises(policy.ControlPolicyError):
            policy.interactive_scope_eligibility(**(props | {"risk": "G3"}))
        with self.assertRaises(policy.ControlPolicyError):
            policy.interactive_scope_eligibility(**(props | {"active_session": False}))

    def test_document_changes_are_affected_scope_not_full_preview(self):
        for path in ("skills/project-governance/SKILL.md",
                     "skills/project-governance/references/issue-control.md",
                     "skills/agent-handoff/SKILL.md"):
            with self.subTest(path=path):
                result = verification.select([change(path)], base="a"*40, head="b"*40)
                self.assertEqual(result["tier"], "V2")
                self.assertEqual(result["selected"], ["static_scope", "affected_contracts"])
                self.assertNotIn("package_preview", result["selected"])
                self.assertIn("test_control_policy.py", result["affected_suites"])

    def test_executable_trust_uses_broad_tests_but_no_automatic_package(self):
        for path in ("skills/project-governance/scripts/control-policy.py",
                     "skills/project-governance/scripts/verification-plan.py",
                     ".github/workflows/governance-contract-checks.yml"):
            result = verification.select([change(path)], base="a"*40, head="b"*40)
            self.assertEqual(result["tier"], "V3")
            self.assertIn("full_contracts", result["selected"])
            self.assertNotIn("package_preview", result["selected"])
        workflow = (ROOT / ".github/workflows/governance-contract-checks.yml").read_text()
        self.assertEqual(workflow.count(
            "if: github.event_name == 'workflow_dispatch' && inputs.package_preview == true"), 2)
        self.assertIn("contents: read", workflow)

    def test_legacy_issue_checker_stays_available(self):
        checker = (SCRIPTS / "issue-spec-check.py").read_text()
        form = (ROOT / ".github/ISSUE_TEMPLATE/execution-spec.yml").read_text()
        self.assertIn("EXECUTION_SPEC_V1", checker)
        self.assertIn("SPEC_APPROVAL_V1", checker)
        self.assertIn("AUTONOMY_SCOPE_V1", checker)
        self.assertIn("EXECUTION_SPEC_V1", form)


if __name__ == "__main__":
    unittest.main()

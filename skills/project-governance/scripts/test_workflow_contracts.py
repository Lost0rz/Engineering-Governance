"""Behavior checks for routing, optional task context and proportional tests."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "skills/project-governance/scripts/verification-plan.py"
spec = importlib.util.spec_from_file_location("verification_plan", SCRIPT)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)


class WorkflowContractTests(unittest.TestCase):
    def test_core_specialists_exist_without_freezing_the_skill_count(self):
        required = ("project-governance", "design", "solution-design",
                    "domain-navigation", "incident-doctor", "execution-orchestrator",
                    "agent-handoff", "evidence-audit", "project-profile")
        route = (ROOT / "skills/project-governance/references/global-routing.md").read_text()
        for name in required:
            with self.subTest(name=name):
                skill = (ROOT / "skills" / name / "SKILL.md")
                self.assertTrue(skill.is_file())
                self.assertTrue(skill.read_text(encoding="utf-8").startswith("---\nname: "))
                self.assertIn(f"`{name}`", route)

    def test_issue_is_optional_context_and_old_gate_is_not_shipped(self):
        config = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text()
        self.assertIn("blank_issues_enabled: true", config)
        self.assertTrue((ROOT / ".github/ISSUE_TEMPLATE/task-plan.md").is_file())
        for path in (".github/ISSUE_TEMPLATE/execution-spec.yml",
                     "skills/project-governance/scripts/issue-spec-check.py",
                     "skills/project-governance/scripts/test_issue_spec_check.py",
                     "skills/project-governance/assets/templates/EXECUTION_SPEC.md",
                     "skills/project-governance/references/issue-execution-contract.md"):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists())

    def test_no_self_granted_writer_permission(self):
        p = json.loads((ROOT / "skills/project-governance/assets/control-policy.json")
                       .read_text(encoding="utf-8"))
        self.assertEqual(p["contract"], "CONTROL_POLICY_V2")
        self.assertTrue(p["require_host_authority_for_writes"])
        self.assertEqual(p["unattended_grants"], "NOT_PROVIDED_BY_PLUGIN")
        self.assertEqual(p["issue_role"], "OPTIONAL_PLANNING_AND_CROSS_CONTEXT_EVIDENCE")
        self.assertEqual(p["project_agents_control_selectors"], "IGNORED")

    def test_routing_and_verification_are_not_one_global_suite(self):
        cases = (("README.md", "V1", ["static_scope", "policy_contracts"]),
                 ("skills/design/SKILL.md", "V2", ["static_scope", "affected_contracts"]),
                 ("skills/project-governance/scripts/verification-plan.py",
                  "V3", ["static_scope", "full_contracts"]))
        for path, tier, selected in cases:
            with self.subTest(path=path):
                result = router.select([{"status":"M","path":path}],
                                       base="a"*40,head="b"*40)
                self.assertEqual(result["tier"], tier)
                self.assertEqual(result["selected"], selected)
                self.assertNotIn("package_preview", result["selected"])

    def test_ci_draft_is_skipped_and_manual_scope_available(self):
        workflow = (ROOT / ".github/workflows/governance-contract-checks.yml").read_text()
        self.assertIn("github.event.pull_request.draft == false", workflow)
        for flag in ("validation_scope", "focused_suite", "package_preview"):
            self.assertIn(flag, workflow)
        self.assertIn("workflow_dispatch", workflow)
        self.assertIn("pull_request", workflow)
        self.assertIn("contents: read", workflow)


if __name__ == "__main__":
    unittest.main()

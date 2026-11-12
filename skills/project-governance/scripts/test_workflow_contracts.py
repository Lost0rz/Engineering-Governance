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

    def test_portable_router_contract_is_discoverable(self):
        skill = (ROOT / "skills/project-governance/SKILL.md").read_text()
        self.assertIn("ci-routing.md", skill)
        self.assertTrue((ROOT / "skills/project-governance/scripts/ci-router.py").exists())
        example = ROOT / "skills/project-governance/assets/examples/ci-capabilities.example.json"
        capabilities = json.loads(example.read_text())
        self.assertEqual(capabilities["contract"], "EG_CI_CAPABILITIES_V1")
        self.assertGreaterEqual(len(capabilities["tests"]), 3)

    def test_no_live_skill_requires_deleted_task_or_approval_controls(self):
        live = (
            "skills/incident-doctor/SKILL.md",
            "skills/incident-doctor/references/evidence-gate.md",
            "skills/incident-doctor/assets/templates/INCIDENT.md",
            "skills/project-profile/assets/templates/PROJECT_PROFILE.md",
            "skills/domain-navigation/references/mapping-workflow.md",
        )
        obsolete = ("FILE_CONTROL", "ISSUE_CONTROL", "CURRENT_TASK.md",
                    "CURRENT_STATUS.md", "STOP_CURRENT_TASK_NAVIGATION",
                    "RETURN_TO_PROJECT_GOVERNANCE_FOR_REAUTHORIZATION")
        for path in live:
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                for marker in obsolete:
                    self.assertNotIn(marker, text)

    def test_shared_workflow_and_caller_yaml_syntax_when_ruby_available(self):
        import shutil
        import subprocess
        ruby = shutil.which("ruby")
        if not ruby:
            self.skipTest("Ruby YAML parser is unavailable on this host")
        paths = (
            ROOT / ".github/workflows/ci-router-reusable.yml",
            ROOT / "skills/project-governance/assets/examples/ci-caller.example.yml",
        )
        for path in paths:
            with self.subTest(path=path.name):
                proc = subprocess.run(
                    [ruby, "-r", "yaml", "-e", "YAML.parse_file(ARGV.fetch(0))",
                     str(path)], capture_output=True, text=True)
                self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_scoped_ci_prevents_empty_comparison_and_offers_router_test(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn('[[ "$BASE_SHA" == "$HEAD_SHA" ]]', workflow)
        self.assertIn("Affected verification requires comparison_base different", workflow)
        own_ci = (ROOT / ".github/workflows/governance-contract-checks.yml").read_text()
        self.assertIn("          - test_ci_router.py", own_ci)
        self.assertIn("test_verification_plan.py|test_ci_router.py) ;;", own_ci)

    def test_release_pin_matches_manifest(self):
        version = json.loads((ROOT / "plugin.json").read_text())["version"]
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        self.assertIn(f"ref: v{version}", workflow)
        doc = (ROOT / "skills/project-governance/references/ci-routing.md").read_text()
        self.assertIn(f"`v{version}`", doc)

    def test_executor_checkout_has_pr_base_parent_without_credentials(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text()
        route = workflow.split("  route:\n", 1)[1].split("\n  execute:\n", 1)[0]
        execute = workflow.split("\n  execute:\n", 1)[1].split("\n  result:\n", 1)[0]
        self.assertIn("fetch-depth: 0", route)
        self.assertIn("fetch-depth: 2", execute)
        self.assertIn("persist-credentials: false", execute)
        self.assertNotIn("fetch-depth: 0", execute)

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

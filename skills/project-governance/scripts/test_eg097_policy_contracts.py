"""Regression checks for the shared EG-097 governance contract."""
import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "issue_spec_check_contracts", SCRIPTS / "issue-spec-check.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class EG097PolicyContractTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_issue_form_and_markdown_template_keep_the_nineteen_field_contract(self):
        form = self.read(".github/ISSUE_TEMPLATE/execution-spec.yml")
        markdown = self.read("skills/project-governance/assets/templates/EXECUTION_SPEC.md")
        form_fields = re.findall(r"^\s+label: ([A-Z][A-Z0-9_]+)$", form, re.M)
        markdown_fields = re.findall(r"^### ([A-Z][A-Z0-9_]+)$", markdown, re.M)
        self.assertEqual(form_fields, list(checker.FIELDS))
        self.assertEqual(markdown_fields, list(checker.FIELDS))
        self.assertIn("G0-G3", form)
        self.assertIn("V0-V3", form)
        self.assertIn("G0-G3", markdown)
        self.assertIn("V0-V3", markdown)

    def test_governance_risk_and_verification_tier_are_independent(self):
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        verification = self.read("skills/project-governance/references/verification-tiers.md")
        self.assertIn("Governance risk G0–G3", execution)
        self.assertIn("G0–G3 are not test tiers", execution)
        self.assertIn("`G0`–`G3` scale", verification)
        self.assertIn("Record the governance-risk envelope and verification tier separately", verification)

    def test_normal_writer_handoff_has_no_extra_gate(self):
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        handoff = self.read("skills/agent-handoff/references/handoff-contract.md")
        self.assertIn("Issue discussion, PR history and local observations are complementary evidence", workspace)
        self.assertIn("Ordinary agent handoff does not introduce a separate Writer-release approval/checklist", workspace)
        self.assertNotIn("### Writer release at handoff", workspace)
        self.assertIn("a normal handoff needs no separate Writer-release ritual", handoff)

    def test_project_specific_incidents_do_not_become_global_normative_rules(self):
        contract = self.read("skills/project-governance/references/issue-execution-contract.md")
        checker_tests = self.read("skills/project-governance/scripts/test_issue_spec_check.py")
        for scenario in ("FloatTabs #208", "FloatTabs #211", "Merloom #632", "RemoteOrbit #51"):
            with self.subTest(scenario=scenario):
                self.assertNotIn(scenario, contract)
        for test_name in ("test_float_tabs_208", "test_float_tabs_211",
                          "test_merloom_632", "test_remoteorbit_51"):
            self.assertIn(test_name, checker_tests)
        self.assertIn("Historical project names, exact incidents", contract)

    def test_comment_requirements_are_mode_scoped(self):
        contract = self.read("skills/project-governance/references/issue-execution-contract.md")
        handoff = self.read("skills/agent-handoff/SKILL.md")
        self.assertIn("legacy/default ISSUE_CONTROL", contract)
        self.assertIn("terminal implementation Issue comments are optional", contract)
        self.assertIn("Under **legacy/default ISSUE_CONTROL**", handoff)
        self.assertIn("routine Issue comments are optional", handoff)

    def test_no_unconditional_writer_release_or_legacy_comment_in_shared_entry_docs(self):
        development = self.read("skills/project-governance/references/development-flow.md")
        handoff_template = self.read("skills/agent-handoff/assets/templates/HANDOFF_REQUEST.md")
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        readme = self.read("README.md")
        self.assertIn("specific overlapping writes or unique work", development)
        self.assertNotIn("Writer release requires both", development)
        self.assertIn("## Legacy/default ISSUE_CONTROL compact example", handoff_template)
        self.assertIn("Under legacy/default `ISSUE_CONTROL`", execution)
        self.assertIn("separately opted-in, independently host-verified", readme)

    def test_low_ceremony_entry_and_cross_context_handoff(self):
        governance = self.read("skills/project-governance/SKILL.md")
        handoff = self.read("skills/agent-handoff/SKILL.md")
        control = self.read("skills/project-governance/references/control-plane.md")
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        self.assertIn("do not emit a compulsory multi-field receipt", governance)
        self.assertIn("Ordinary same-session continuation", handoff)
        self.assertIn("TASK_ID: <selected task>", handoff)
        self.assertNotIn("HANDOFF_ROUTE_APPLIED: YES", handoff)
        self.assertIn("## Conditional FILE_CONTROL alignment", control)
        self.assertIn("not a universal gate on every code edit", control.replace("**", ""))
        self.assertIn("Prevent actual conflicting writes", workspace)
        self.assertIn("retained review workspace", workspace)

    def test_risk_based_user_decision_and_delegated_comment_route(self):
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        issue = self.read("skills/project-governance/references/issue-control.md")
        self.assertIn("Risk follows **actual side effect and consequence**", execution)
        self.assertIn("Explicit user/owner decision", execution)
        self.assertIn("user need not visit GitHub", issue)
        self.assertIn("source-write** grant never implicitly authorizes merge", issue)
        self.assertIn("fail-closed checker", execution)

    def test_source_plugin_identity_and_all_install_surfaces(self):
        import json
        plugin = json.loads(self.read("plugin.json"))
        marketplace = json.loads(self.read(".agents/plugins/marketplace.json"))
        self.assertEqual(plugin["name"], "engineering-governance")
        self.assertRegex(plugin["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(marketplace["plugins"][0]["name"], plugin["name"])
        self.assertEqual(marketplace["plugins"][0]["source"]["ref"], "main")
        adoption = self.read("skills/project-governance/references/adoption.md")
        for surface in ("Web-installed", "Codex-installed", "Claude-installed"):
            self.assertIn(surface, adoption)
        workflow = self.read(".github/workflows/governance-contract-checks.yml")
        for path in ("'plugin.json'", "'AGENTS.md'", "'.agents/plugins/**'"):
            self.assertIn(path, workflow)

    def test_new_autonomy_stays_inactive_without_independent_host_proof(self):
        control = self.read("skills/project-governance/references/issue-control.md")
        template = self.read("skills/project-governance/assets/templates/AGENTS.md")
        self.assertIn("UNVERIFIED_AUTHORIZATION_SOURCE", control)
        self.assertIn("INACTIVE_UNVERIFIED_HOST_BOUNDARY", control)
        self.assertIn("RISK_SCOPED_AUTONOMY: DISABLED", template)
        self.assertIn("A local JSON snapshot or actor login alone is not proof", template)


if __name__ == "__main__":
    unittest.main()

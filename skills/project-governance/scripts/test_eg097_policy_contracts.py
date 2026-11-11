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
        self.assertIn("G0–G3 determine authority; V0–V3 determine verification", execution)
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
        self.assertIn("Issue approval and comment/receipt rules belong to Project Governance", handoff)
        self.assertNotIn("Under **legacy/default ISSUE_CONTROL**", handoff)

    def test_no_unconditional_writer_release_or_legacy_comment_in_shared_entry_docs(self):
        development = self.read("skills/project-governance/references/development-flow.md")
        handoff_template = self.read("skills/agent-handoff/assets/templates/HANDOFF_REQUEST.md")
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        readme = self.read("README.md")
        self.assertIn("specific overlapping writes or unique work", development)
        self.assertNotIn("Writer release requires both", development)
        self.assertIn("## Legacy/default ISSUE_CONTROL compact example", handoff_template)
        self.assertIn("Issue approval, Web authoring, exact digest/revision binding", execution)
        self.assertIn("separately opted-in, independently host-verified", readme)

    def test_low_ceremony_entry_and_cross_context_handoff(self):
        governance = self.read("skills/project-governance/SKILL.md")
        handoff = self.read("skills/agent-handoff/SKILL.md")
        control = self.read("skills/project-governance/references/control-plane.md")
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        self.assertIn("do not emit a compulsory multi-field receipt", governance)
        self.assertIn("Ordinary same-session continuation", handoff)
        self.assertIn("TASK_ID, MODE, TARGET, AUTHORITY, BOUNDARY, DELTA, RETURN_CONTRACT", handoff)
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
        self.assertIn("policy-only future path", execution)

    def test_interactive_session_path_never_mints_persistent_authority(self):
        issue = self.read("skills/project-governance/references/issue-control.md")
        flow = self.read("skills/project-governance/references/development-flow.md")
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        policy = self.read("skills/project-governance/scripts/control-policy.py")
        self.assertIn("INTERACTIVE_SCOPE_ELIGIBILITY_V1", execution)
        self.assertIn("ELIGIBLE_ONLY_HOST_PREFLIGHT_REQUIRED", issue)
        self.assertIn("source_write_authorized=false", execution)
        self.assertIn("verifies that user-role message", flow)
        self.assertIn("host_action_authorization_required", policy)
        self.assertIn('"initial_issue_approval_required": False', policy)
        self.assertIn("sufficient task authorization for the first action", issue)
        self.assertIn("first task authorization", flow)
        self.assertIn("first 19-field Issue approval comment", execution)
        self.assertIn("current top-level user request", self.read("skills/project-governance/SKILL.md"))
        self.assertIn("no first Issue", issue)
        self.assertIn("without a first Issue/comment", flow)
        self.assertIn("Issue-backed only", issue)
        self.assertIn("no 19-field Issue, digest or approval comment", issue)
        self.assertIn("a fresh explicit host-authenticated user decision", flow)
        governance = self.read("skills/project-governance/SKILL.md")
        self.assertIn("no Issue to approve or reconcile", governance)

        self.assertIn('"persistent_grant": False', policy)
        self.assertIn('"source_write_authorized": False', policy)
        self.assertIn("unattended", issue)
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        self.assertIn("needs no first Issue/comment", workspace)
        self.assertIn("host-verified top-level USER-requested", workspace)

    def test_v2_affected_contracts_are_not_unnecessary_full_package(self):
        selector = self.read("skills/project-governance/scripts/verification-plan.py")
        workflow = self.read(".github/workflows/governance-contract-checks.yml")
        tiers = self.read("skills/project-governance/references/verification-tiers.md")
        self.assertIn('"affected_contracts"', selector)
        self.assertIn("run_affected", selector)
        self.assertIn("Run affected cross-Skill integration contracts", workflow)
        self.assertIn("run_affected", workflow)
        self.assertIn("skips the full security suite", tiers)
        self.assertIn("trusted-verification-plan.py", workflow)

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
        self.assertIn("pull_request:", workflow)
        self.assertIn("name: Python governance contracts", workflow)
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("trusted-verification-plan.py", workflow)
        self.assertIn("git show", workflow)
        self.assertIn("run_full", workflow)

    def test_compact_scope_is_separate_from_legacy_approval(self):
        source = self.read("skills/project-governance/scripts/issue-spec-check.py")
        control = self.read("skills/project-governance/references/issue-control.md")
        self.assertIn('COMPACT_CONTRACT = "AUTONOMY_SCOPE_V1"', source)
        self.assertIn("def digest_autonomy_scope(", source)
        self.assertIn("8-field `AUTONOMY_SCOPE_V1`", control)
        self.assertIn("Legacy `digest` and `verify`", control)

    def test_final_handoff_rules_do_not_restore_nine_field_gate(self):
        handoff_contract = self.read("skills/agent-handoff/references/handoff-contract.md")
        governance = self.read("skills/project-governance/SKILL.md")
        readme = self.read("README.md")
        self.assertNotIn("all nine required core fields", handoff_contract)
        self.assertNotIn("Compact nine-core-field", handoff_contract)
        self.assertIn("Do not create checkbox receipts", handoff_contract)
        self.assertIn("not a universal per-edit final alignment gate", governance)
        self.assertIn("8-field `AUTONOMY_SCOPE_V1`", readme)

    def test_receiver_matches_compact_scope_and_mode_specific_receipts(self):
        receiver = self.read("skills/agent-handoff/references/handoff-contract.md")
        receipt = self.read("skills/agent-handoff/assets/templates/HANDOFF_RECEIPT.md")
        issue = self.read("skills/project-governance/references/issue-control.md")
        self.assertIn("using the contract selected by the authorization path", receiver)
        self.assertNotIn("19-field quality, current revision and canonical SHA256 in both authority paths", receiver)
        self.assertIn("8-field parser", receiver)
        self.assertIn("Legacy uses the 19-field Issue", receiver)
        self.assertIn("For an actual Handoff Card", receipt)
        self.assertNotIn("## Mandatory pre-return gate", receipt)
        self.assertNotIn("SOURCE_CARD_ID_PRESERVED: YES", receipt)
        self.assertIn("only if supplied", receipt)
        self.assertIn("Legacy Issue-backed only:", issue)
        self.assertIn("run `digest/verify`", issue)
        self.assertIn("In ISSUE_CONTROL, **either**", issue)
        self.assertIn("In a **verified active** G1/G2 grant mode", issue)

    def test_control_alignment_is_mode_and_event_scoped_everywhere(self):
        flow = self.read("skills/project-governance/references/development-flow.md")
        control = self.read("skills/project-governance/references/control-plane.md")
        receipt = self.read("skills/agent-handoff/assets/templates/HANDOFF_RECEIPT.md")
        self.assertNotIn("run the mandatory Control Alignment Gate", flow)
        self.assertIn("At a **real task/authorization/terminal state transition**", flow)
        self.assertIn("## Conditional FILE_CONTROL alignment", control)
        self.assertIn("only when a FILE_CONTROL control transition", receipt)

    def test_l2_resolution_not_automatically_g3_or_human_confirmation(self):
        contract = self.read("skills/project-governance/references/issue-execution-contract.md")
        orchestrator = self.read("skills/execution-orchestrator/SKILL.md")
        design = self.read("skills/solution-design/SKILL.md")
        audit = self.read("skills/evidence-audit/SKILL.md")
        self.assertIn("L2 `PAUSE_AND_ASK`", contract)
        self.assertIn("resolution action is **RESOLVE_OR_ESCALATE**", contract)
        self.assertIn("L2 is not synonymous with G3", contract)
        self.assertIn("L2 alone does not imply G3", self.read("skills/project-governance/references/issue-control.md"))
        self.assertIn("do not invent mandatory WP IDs", orchestrator)
        self.assertIn("without forcing a WP list", design)
        self.assertIn("without requiring nonexistent WP fields", audit)
        self.assertIn("Legacy: increment revision", contract)
        self.assertIn("G3 requires the applicable explicit owner decision", contract)

    def test_no_unconditional_workspace_alignment_or_historical_writer_mutex(self):
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        self.assertNotIn("For every final successful **state-changing** governed handoff", workspace)
        self.assertNotIn("a predecessor can write an overlapping fact/state/policy/behavior authority", workspace)
        self.assertIn("actually active overlapping writer", workspace)
        self.assertIn("FILE_CONTROL alignment is a separate, conditional", workspace)

    def test_layered_contract_has_one_operational_owner(self):
        routing = self.read("skills/project-governance/references/global-routing.md")
        governance = self.read("skills/project-governance/SKILL.md")
        handoff = self.read("skills/agent-handoff/SKILL.md")
        contract = self.read("skills/agent-handoff/references/handoff-contract.md")
        execution = self.read("skills/project-governance/references/issue-execution-contract.md")
        routing_template = self.read("skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md")
        request_template = self.read("skills/agent-handoff/assets/templates/HANDOFF_REQUEST.md")
        self.assertIn("which Engineering Governance capability", routing)
        self.assertNotIn("UNRESOLVED_DEPENDENCY:", routing)
        self.assertNotIn("INTERACTION_WORKFLOW\\n", governance)
        self.assertNotIn("SPEC_DELEGATED_APPROVAL_V1", handoff)
        self.assertNotIn("grant_credential_id", contract)
        self.assertIn("issue-control.md", execution)
        self.assertIn("A Card never grants", contract)
        self.assertNotIn("For governed user-facing responses, make routing observable:", routing_template)
        self.assertNotIn("## Mandatory pre-return gate", request_template)

    def test_g0_status_fast_path_does_not_trigger_full_audit_preflight(self):
        governance = self.read("skills/project-governance/SKILL.md")
        routing = self.read("skills/project-governance/references/global-routing.md")
        tiers = self.read("skills/project-governance/references/verification-tiers.md")
        doctor = self.read("skills/incident-doctor/SKILL.md")
        self.assertIn("G0 status-only inquiries", governance)
        self.assertIn("For **state-changing work and authority decisions**", governance)
        self.assertIn("optional pointers, not a startup reading list", governance)
        self.assertIn("lightweight G0 status lookup", routing)
        self.assertIn("not automatically a code audit or V3", tiers)
        self.assertIn("Other references are conditional", doctor)
        self.assertNotIn("## Read the contracts", doctor)
        issue = self.read("skills/project-governance/references/issue-control.md")
        self.assertIn("verbose Issue/comment payloads **out of the model context**", issue)
        self.assertIn("Do not truncate away later revocations", issue)

    def test_design_and_profile_have_mode_selected_lazy_references(self):
        design = self.read("skills/design/SKILL.md")
        spec = self.read("skills/design/references/design-specification.md")
        review = self.read("skills/design/references/design-review.md")
        profile = self.read("skills/project-profile/SKILL.md")
        profile_contract = self.read("skills/project-profile/references/profile-contract.md")
        for mode in ("AUDIT_ONLY", "DESIGN_SPEC", "DESIGN_IMPLEMENT", "FINAL_REVIEW"):
            self.assertIn(mode, design)
        self.assertIn("read only the selected procedure", design)
        self.assertIn("PRE_BUILD_DESIGN_GATE", spec)
        self.assertIn("### 2. Anthropic design analysis", spec)
        self.assertIn("### 8. Microsoft internal final Design review", review)
        self.assertIn("HUMAN_UI_ACCEPTANCE", review)
        self.assertIn("only an actual human decision", design)
        self.assertIn("profile-contract.md", profile)
        self.assertIn("## Mandatory pre-return compliance gate", profile_contract)
        self.assertNotIn("### 8. Microsoft internal final Design review", design)
        self.assertNotIn("## Mandatory pre-return compliance gate", profile)

    def test_new_autonomy_stays_inactive_without_independent_host_proof(self):
        control = self.read("skills/project-governance/references/issue-control.md")
        template = self.read("skills/project-governance/assets/templates/AGENTS.md")
        self.assertIn("UNVERIFIED_AUTHORIZATION_SOURCE", control)
        self.assertIn("INACTIVE_UNVERIFIED_HOST_BOUNDARY", control)
        policy = self.read("skills/project-governance/assets/control-policy.json")
        self.assertIn('"risk_scoped_autonomy": "DISABLED"', policy)
        self.assertIn("Project markdown cannot enable or override governance grants.", template)
        self.assertNotIn("RISK_SCOPED_AUTONOMY:", template)


if __name__ == "__main__":
    unittest.main()

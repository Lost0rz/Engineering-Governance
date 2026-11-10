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

    def test_writer_release_requires_host_and_local_facts(self):
        workspace = self.read("skills/project-governance/references/workspace-lifecycle.md")
        self.assertIn("Writer release at handoff", workspace)
        self.assertIn("read current PR/merge/head and changed-path evidence from GitHub", workspace)
        self.assertIn("verify the relevant local branches/worktrees", workspace)
        self.assertIn("A comment may document evidence but is never the sole release gate", workspace)

    def test_four_historical_safety_scenarios_remain_explicit(self):
        contract = self.read("skills/project-governance/references/issue-execution-contract.md")
        expected = (
            "FloatTabs #208 — bounded DEBUG-only test seam",
            "FloatTabs #211 — human UI and overlapping writer",
            "Merloom #632 — RawSku overwrite guard",
            "RemoteOrbit #51 — privileged HID helper",
        )
        for scenario in expected:
            with self.subTest(scenario=scenario):
                self.assertIn(scenario, contract)
        self.assertIn("explicitly excluded/new source target is L2", contract)
        self.assertIn("Keep UI acceptance PENDING", contract)
        self.assertIn("cannot be overwritten, appended, or merged", contract)
        self.assertIn("G3 and outside the G1/G2 grant", contract)

    def test_new_autonomy_stays_inactive_without_independent_host_proof(self):
        control = self.read("skills/project-governance/references/issue-control.md")
        template = self.read("skills/project-governance/assets/templates/AGENTS.md")
        self.assertIn("UNVERIFIED_AUTHORIZATION_SOURCE", control)
        self.assertIn("INACTIVE_UNVERIFIED_HOST_BOUNDARY", control)
        self.assertIn("RISK_SCOPED_AUTONOMY: DISABLED", template)
        self.assertIn("A local JSON snapshot or actor login alone is not proof", template)


if __name__ == "__main__":
    unittest.main()

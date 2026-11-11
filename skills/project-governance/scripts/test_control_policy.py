#!/usr/bin/env python3
"""CONTROL_POLICY_V1 invariants; no real GitHub operations in unit tests."""
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("eg_control_policy", ROOT / "control-policy.py")
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class GlobalControlPolicyTests(unittest.TestCase):
    def test_shipped_policy_is_complete_and_not_per_repository(self):
        d = policy.load_policy()
        self.assertEqual(d["contract"], "CONTROL_POLICY_V1")
        self.assertEqual(d["default_mode"], "ISSUE_CONTROL")
        self.assertEqual(d["project_agents_control_selectors"], "IGNORED")
        self.assertNotIn("Lost0rz", json.dumps(d))
        self.assertFalse(policy.delegated_enabled())
        self.assertFalse(policy.autonomy_enabled())

    def test_missing_enrollment_does_not_auto_authorize(self):
        r = policy.select_control("Lost0rz/Merloom")
        self.assertEqual(r["mode"], "FILE_CONTROL")
        self.assertFalse(r["execution_authorized"])
        self.assertEqual(r["reason"], "MIGRATION_HOST_PROOF_REQUIRED")
        with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_HOST_PROOF_REQUIRED"):
            policy.source_write_gate(r, user_requested=True, trusted_approvers={"Lost0rz"})

    def test_host_unavailable_fails_closed(self):
        with patch.object(policy, "_gh_api", side_effect=policy.ControlPolicyError("GITHUB_HOST_READ_DENIED")):
            with self.assertRaisesRegex(policy.ControlPolicyError, "GITHUB_HOST_READ_DENIED"):
                policy.select_control("Lost0rz/Engineering-Governance", migration_pr=41)

    def test_verified_host_ancestry_is_not_approval(self):
        sha = "a" * 40
        final = "b" * 40
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1",
             "base": {"ref": "main"}, "head": {"repo": {"name": "Engineering-Governance"}}},
            [{"filename": "AGENTS.md"}],
            {"commit": {"sha": final}},
            {"status": "ahead"},
        ]
        with patch.object(policy, "_gh_api", side_effect=events) as gh:
            r = policy.select_control("Lost0rz/Engineering-Governance", migration_pr=41)
        self.assertEqual(gh.call_count, 4)
        self.assertEqual(r["mode"], "ISSUE_CONTROL")
        self.assertEqual(r["source"], "LIVE_GITHUB_HOST")
        self.assertFalse(r["execution_authorized"])
        with self.assertRaisesRegex(policy.ControlPolicyError, "ISSUE_APPROVAL_HOST_PREFLIGHT_REQUIRED"):
            policy.source_write_gate(r, user_requested=True, trusted_approvers={"Lost0rz"})

    def test_unmerged_migration_stops(self):
        with patch.object(policy, "_gh_api", return_value={"merged_at": None}):
            with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_NOT_HOST_VERIFIED"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)

    def test_migration_not_on_main_stops(self):
        sha = "a" * 40
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "AGENTS.md"}],
            {"commit": {"sha": "b" * 40}},
            {"status": "diverged"},
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_NOT_IN_MAIN_ANCESTRY"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)

    def test_unrelated_merged_pr_is_not_adoption(self):
        sha = "a" * 40
        with patch.object(policy, "_gh_api", return_value={
            "merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
            "body": "Fix documentation typo",
            "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}},
        }):
            with self.assertRaisesRegex(policy.ControlPolicyError, "PR_NOT_GOVERNANCE_MIGRATION"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 123)

    def test_migration_missing_agents_diff_stops(self):
        sha = "a" * 40
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "README.md"}],
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_DIFF_NOT_VERIFIED"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 123)

    def test_invalid_repositories_and_numbers_stop(self):
        for repo in ("", "../Merloom", "foo", "owner/repo/extra", "a;rm -rf /b"):
            with self.subTest(repo=repo):
                with self.assertRaisesRegex(policy.ControlPolicyError, "INVALID_REPOSITORY"):
                    policy.select_control(repo)
        for number in (0, -1, "41", True):
            with self.subTest(number=number):
                with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_PR_REQUIRED"):
                    policy.verify_migration("Lost0rz/Merloom", number)

    def test_personal_owner_approver_comes_from_host(self):
        with patch.object(policy, "_gh_api", return_value={
            "full_name": "Lost0rz/Engineering-Governance",
            "owner": {"type": "User", "login": "Lost0rz"},
        }):
            self.assertEqual(policy.verified_personal_repo_approvers(
                "Lost0rz/Engineering-Governance"), {"Lost0rz"})

    def test_org_and_mismatched_owner_never_infer_approver(self):
        for host in (
            {"full_name": "Lost0rz/Engineering-Governance",
             "owner": {"type": "Organization", "login": "Lost0rz"}},
            {"full_name": "attacker/repository",
             "owner": {"type": "User", "login": "attacker"}},
        ):
            with self.subTest(host=host), patch.object(policy, "_gh_api", return_value=host):
                with self.assertRaisesRegex(
                    policy.ControlPolicyError, "TRUSTED_APPROVER_HOST_POLICY_REQUIRED"
                ):
                    policy.verified_personal_repo_approvers("Lost0rz/Engineering-Governance")

    def test_web_authoring_is_only_eligibility(self):
        self.assertFalse(policy.web_authoring_eligible(explicit_user_request=False,
                                                      verified_github_write=True))
        self.assertFalse(policy.web_authoring_eligible(explicit_user_request=True,
                                                      verified_github_write=False))
        self.assertTrue(policy.web_authoring_eligible(explicit_user_request=True,
                                                     verified_github_write=True))

    def test_project_agents_never_own_controls(self):
        template = (ROOT.parent / "assets" / "templates" / "AGENTS.md").read_text()
        root = (ROOT.parents[2] / "AGENTS.md").resolve().read_text()
        for forbidden in ("CONTROL_MODE:", "ISSUE_APPROVERS:", "ISSUE_WEB_SPEC_AUTHORING:",
                          "ISSUE_DELEGATED_APPROVAL:", "RISK_SCOPED_AUTONOMY:"):
            self.assertNotIn(forbidden, template)
            self.assertNotIn(forbidden, root)


if __name__ == "__main__":
    unittest.main()

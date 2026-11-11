#!/usr/bin/env python3
"""CONTROL_POLICY_V1 invariants; no real GitHub operations in unit tests."""
import base64
import importlib.util
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
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


    def test_interactive_g1_g2_requires_host_proof_and_never_grants_writes(self):
        common = {
            "repo": "Lost0rz/Engineering-Governance",
            "paths": ["skills/incident-doctor/SKILL.md"],
            "effects": ["source_edit", "focused_test"],
            "explicit_user_request": True, "active_session": True,
            "host_write_permission": True,
        }
        for risk in ("G1", "G2"):
            with self.subTest(risk=risk):
                plan = policy.interactive_scope_eligibility(risk=risk, **common)
                self.assertFalse(plan["source_write_authorized"])
                self.assertFalse(plan["persistent_grant"])
                self.assertFalse(plan["merge_authorized"])
                self.assertFalse(plan["release_authorized"])
                self.assertFalse(plan["per_wp_approval_comment_required"])
                self.assertFalse(plan["initial_issue_approval_required"])
                self.assertTrue(plan["user_direct_request_is_initial_task_authority_candidate"])
                self.assertTrue(plan["host_user_role_provenance_required"])
                self.assertTrue(plan["host_action_authorization_required"])

    def test_interactive_session_must_not_be_unattended_or_self_permitted(self):
        common = {
            "repo": "Lost0rz/Engineering-Governance",
            "risk": "G1", "paths": ["skills/incident-doctor/SKILL.md"],
            "effects": ["source_edit"],
            "explicit_user_request": True, "active_session": True,
            "host_write_permission": True,
        }
        cases = (
            ({"risk": "G3"}, "SESSION_SCOPE_RISK_NOT_ALLOWED"),
            ({"risk": "G0"}, "SESSION_SCOPE_RISK_NOT_ALLOWED"),
            ({"unattended": True}, "INDEPENDENT_PERSISTENT_GRANT_REQUIRED"),
            ({"explicit_user_request": False}, "ACTIVE_USER_REQUEST_REQUIRED"),
            ({"active_session": False}, "ACTIVE_USER_REQUEST_REQUIRED"),
            ({"host_write_permission": False}, "LIVE_HOST_WRITE_PERMISSION_REQUIRED"),
            ({"effects": ["source_edit", "release"]}, "INVALID_SESSION_EFFECTS"),
            ({"effects": ["source_edit", "merge"]}, "INVALID_SESSION_EFFECTS"),
            ({"paths": ["AGENTS.md"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": [".github/workflows/ci.yml"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": ["skills/project-governance/SKILL.md"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": ["src/../secrets"]}, "INVALID_SESSION_SCOPE_PATHS"),
            ({"paths": ["src\\private"]}, "INVALID_SESSION_SCOPE_PATHS"),
            ({"paths": [["nested"]]}, "INVALID_SESSION_SCOPE_PATHS"),
            ({"paths": ["src/**"]}, "INVALID_SESSION_SCOPE_PATHS"),
            ({"paths": ["docs/AGENTS.md"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": ["docs/agents.md"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": [".GitHub/workflows/CI.yml"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"paths": ["plugin.JSON"]}, "PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT"),
            ({"effects": [["source_edit"]]}, "INVALID_SESSION_EFFECTS"),
        )
        for delta, expected in cases:
            with self.subTest(delta=delta):
                with self.assertRaisesRegex(policy.ControlPolicyError, expected):
                    policy.interactive_scope_eligibility(**(common | delta))

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
            [{"filename": "AGENTS.md", "status": "modified", "patch": "@@ -1,2 +1,2 @@\n-CONTROL_MODE: FILE_CONTROL\n+CONTROL_MODE: ISSUE_CONTROL"}],
            {"commit": {"sha": final}},
            {"status": "ahead"},
            {"type": "file", "encoding": "base64", "content": base64.b64encode(
                b"# Project facts only\\n").decode("ascii")},
        ]
        with patch.object(policy, "_gh_api", side_effect=events) as gh:
            r = policy.select_control("Lost0rz/Engineering-Governance", migration_pr=41)
        self.assertEqual(gh.call_count, 5)
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
            [{"filename": "AGENTS.md", "status": "modified", "patch": "@@ -1,2 +1,2 @@\n-CONTROL_MODE: FILE_CONTROL\n+CONTROL_MODE: ISSUE_CONTROL"}],
            {"commit": {"sha": "b" * 40}},
            {"status": "diverged"},
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(policy.ControlPolicyError, "MIGRATION_NOT_IN_MAIN_ANCESTRY"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)

    def test_unrelated_merged_pr_is_not_adoption(self):
        sha = "a" * 40
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1 changed after merge",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "AGENTS.md", "status": "modified",
              "patch": "@@ -1,2 +1,2 @@\\n-old business rule\\n+new business rule"}],
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(policy.ControlPolicyError, "PR_NOT_GOVERNANCE_MIGRATION"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 123)

    def test_mutable_pr_body_cannot_authorize_migration(self):
        """Even a post-merge edited PR title/body cannot replace a control diff."""
        with patch.object(policy, "_gh_api", side_effect=[
            {"merged_at": "2026-11-01T00:00:00Z",
             "merge_commit_sha": "a" * 40,
             "body": "EG_CONTROL_MIGRATION_V1 AGENTS.md ISSUE_CONTROL migration",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "AGENTS.md", "status": "modified",
              "patch": "@@ -1,2 +1,2 @@\\n-old note\\n+new note"}],
        ]):
            with self.assertRaisesRegex(policy.ControlPolicyError,
                                        "PR_NOT_GOVERNANCE_MIGRATION"):
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

    def test_old_control_selectors_on_accepted_main_are_not_migrated(self):
        sha = "a" * 40
        accepted = b"CONTROL_MODE: ISSUE_CONTROL\\nISSUE_APPROVERS: owner\\n"
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "AGENTS.md", "status": "modified", "patch": "@@ -1,2 +1,2 @@\n-CONTROL_MODE: FILE_CONTROL\n+CONTROL_MODE: ISSUE_CONTROL"}],
            {"commit": {"sha": "b" * 40}},
            {"status": "ahead"},
            {"type": "file", "encoding": "base64",
             "content": base64.b64encode(accepted).decode("ascii")},
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(
                policy.ControlPolicyError, "PROJECT_CONTROL_SELECTORS_NOT_MIGRATED"
            ):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)

    def test_accepted_main_agreement_requires_verifiable_file(self):
        sha = "a" * 40
        events = [
            {"merged_at": "2026-11-01T00:00:00Z", "merge_commit_sha": sha,
             "body": "EG_CONTROL_MIGRATION_V1",
             "base": {"ref": "main"}, "head": {"repo": {"name": "sample"}}},
            [{"filename": "AGENTS.md", "status": "modified", "patch": "@@ -1,2 +1,2 @@\n-CONTROL_MODE: FILE_CONTROL\n+CONTROL_MODE: ISSUE_CONTROL"}],
            {"commit": {"sha": "b" * 40}},
            {"status": "ahead"},
            {"type": "file", "encoding": "none", "content": "not authenticated"},
        ]
        with patch.object(policy, "_gh_api", side_effect=events):
            with self.assertRaisesRegex(
                policy.ControlPolicyError, "ACCEPTED_PROJECT_RULES_UNVERIFIED"
            ):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)

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

    def test_gh_reader_pins_github_com_not_environment_default(self):
        with patch.object(policy.subprocess, "run", return_value=SimpleNamespace(
            returncode=0, stdout="{}")) as run:
            policy._gh_api("repos/owner/repo")
        self.assertEqual(run.call_args.args[0],
                         ["gh", "api", "--hostname", "github.com", "repos/owner/repo"])

    def test_malformed_host_response_is_a_denial(self):
        with patch.object(policy, "_gh_api", return_value=[]):
            with self.assertRaisesRegex(policy.ControlPolicyError,
                                        "MIGRATION_NOT_HOST_VERIFIED"):
                policy.verify_migration("Lost0rz/Engineering-Governance", 41)
            with self.assertRaisesRegex(policy.ControlPolicyError,
                                        "TRUSTED_APPROVER_HOST_POLICY_REQUIRED"):
                policy.verified_personal_repo_approvers("Lost0rz/Engineering-Governance")

    def test_active_policy_docs_cannot_reintroduce_agents_approval(self):
        refs = ROOT.parent / "references"
        issue = (refs / "issue-control.md").read_text(encoding="utf-8")
        routing = (ROOT.parent / "assets" / "templates" /
                   "GLOBAL_AGENTS_ROUTING.md").read_text(encoding="utf-8")
        for stale in ("AGENTS.md`-authorized", "accepted `ISSUE_APPROVERS`",
                      "AGENTS.md opt-in", "The author login must be in accepted"):
            self.assertNotIn(stale, issue)
        self.assertIn("Project `AGENTS.md` cannot override", routing)

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

#!/usr/bin/env python3
"""Focused positive/negative contract checks; no GitHub/network dependency."""
import copy
import importlib.util
import unittest
from datetime import datetime, timezone
from pathlib import Path

MODULE = Path(__file__).with_name("issue-spec-check.py")
spec = importlib.util.spec_from_file_location("issue_spec_check", MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
REPO = "Lost0rz/Engineering-Governance"

WP = """#### WP01 — bounded source edit
Targets: verified skills/project-governance/SKILL.md
Preconditions: inspected exact source SHA
Actions: change one documented rule; preserve old mode
Dependencies: NONE
Edge cases: incompatible ref means STOP
Verification: inspect exact diff and expected behavior
Done: focused review confirms intended rule
"""
DATA = {
    "CONTRACT": "EXECUTION_SPEC_V1",
    "TASK_ID": "EG-093",
    "SPEC_REVISION": "2",
    "MODE": "EXECUTE",
    "PURPOSE": "BOUNDED_CORRECTIVE",
    "OBJECTIVE": "Implement exactly the approved scoped fix",
    "VERIFIED_BASELINE": "main@123 verified by actual GitHub source read",
    "TARGET_BEHAVIOR": "Changed code follows expected scoped contract",
    "IN_SCOPE": "one inspected source file",
    "OUT_OF_SCOPE": "new API or database",
    "ALLOWED_SIDE_EFFECTS": "approved source edit and existing PR update",
    "CANONICAL_AUTHORITIES": "AGENTS.md, approved design",
    "WORK_PACKAGES": WP,
    "VERIFICATION_PLAN": "targeted source diff and focused tests",
    "HUMAN_UI_ACCEPTANCE": "NOT_REQUIRED: pure documentation",
    "DEVIATION_POLICY": "L0 continue; L1 local correct; L2 pause; L3 terminate",
    "STOP_AND_SAFETY": "new writer or unknown API means PAUSE",
    "RETURN_CONTRACT": "EXECUTION_RECEIPT_V1 posted to same Issue",
    "AUTHORIZATION_BASIS": "PENDING GitHub approval record; never infer from this text",
}


def body(values=DATA):
    return "\n\n".join(f"### {k}\n\n{values[k]}" for k in mod.FIELDS) + "\n"


def issue(values=DATA):
    return {"number": 40, "state": "OPEN", "body": body(values), "comments": [], "labels": []}


def approve(obj, actor="Lost0rz", hash_value=None, revision="2"):
    _, d = mod.digest(obj["body"], repo=REPO, number=obj["number"])
    obj["comments"].append({
        "id": len(obj["comments"]) + 1,
        "author": {"login": actor},
        "body": "\n".join([
            "SPEC_APPROVAL_V1", f"REPOSITORY: {REPO}", "ISSUE: 40",
            "TASK_ID: EG-093", f"SPEC_REVISION: {revision}",
            f"SPEC_SHA256: {hash_value or d}", "DECISION: APPROVED_FOR_EXECUTION",
        ]),
    })
    return obj


def delegate(obj, actor="Lost0rz", hash_value=None, summary="I approve this exact current Issue"):
    _, d = mod.digest(obj["body"], repo=REPO, number=obj["number"])
    obj["comments"].append({
        "id": len(obj["comments"]) + 1,
        "author": {"login": actor},
        "body": "\n".join([
            "SPEC_DELEGATED_APPROVAL_V1", f"REPOSITORY: {REPO}", "ISSUE: 40",
            "TASK_ID: EG-093", "SPEC_REVISION: 2",
            f"SPEC_SHA256: {hash_value or d}", "DECISION: APPROVED_FOR_EXECUTION",
            "AUTHORIZATION_CHANNEL: CHATGPT_WEB",
            "USER_DECISION: EXPLICIT_APPROVAL_OF_CURRENT_SPEC",
            f"USER_DECISION_SUMMARY: {summary}",
            "PROVENANCE: ACCOUNT_PROXY_NO_INDEPENDENT_CHAT_PROOF",
        ]),
    })
    return obj


AUTONOMY_AGENTS = (
    "CONTROL_MODE: ISSUE_CONTROL\n"
    "ISSUE_APPROVERS: Lost0rz\n"
    "RISK_SCOPED_AUTONOMY: ENABLED\n"
)


def autonomy_snapshot(obj=None):
    selected_issue = obj or issue()
    _, spec_sha = mod.digest(selected_issue["body"], repo=REPO,
                             number=selected_issue["number"])
    return {
        "contract": "RISK_SCOPED_AUTONOMY_V1",
        "repository": REPO,
        "issue_number": selected_issue["number"],
        "task_id": "EG-093",
        "spec_revision": "2",
        "spec_sha256": spec_sha,
        "target_ref": "refs/heads/codex/eg-093",
        "target_commit_sha": "a" * 40,
        "allowed_paths": ["skills/project-governance"],
        "requested_paths": ["skills/project-governance/scripts/issue-spec-check.py"],
        "max_risk": "G2",
        "requested_risk": "G1",
        "allowed_effects": ["repository_source_changes", "repository_tests", "same_task_ref_push"],
        "requested_effects": ["repository_source_changes", "repository_tests"],
        "hard_exclusions": sorted(mod.AUTONOMY_HARD_EXCLUSIONS),
        "issued_at": "2026-11-10T00:00:00Z",
        "expires_at": "2026-11-11T00:00:00Z",
        "revoked_at": None,
        "grant_event": {
            "host": "github.com",
            "event": "workflow_dispatch",
            "workflow_path": ".github/workflows/task-authorization.yml",
            "workflow_ref": "refs/heads/main",
            "workflow_sha": "a" * 40,
            "run_id": "123456789",
            "run_attempt": 1,
            "actor_login": "Lost0rz",
            "grant_credential_id": "independent-grant-credential",
            "executor_credential_id": "executor-connector-credential",
            "workflow_source_readback": True,
            "protection_readback": True,
            "credential_separation_readback": True,
            "revocation_readback": True,
        },
    }


class IssueContractTests(unittest.TestCase):
    def test_valid_approved_spec(self):
        result = mod.verify_approval(approve(issue()), repo=REPO, approvers={"Lost0rz"})
        self.assertEqual(result["result"], "STRUCTURE_AND_APPROVAL_PASS")
        self.assertEqual(result["semantic_source_check"], "REQUIRED_SEPARATELY")

    def test_only_comment_timestamp_changes(self):
        x = approve(issue())
        x["comments"].append({"id": 19, "author": {"login": "someone"}, "body": "progress"})
        self.assertEqual(mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})["result"],
                         "STRUCTURE_AND_APPROVAL_PASS")

    def test_material_body_change_same_rev_is_denied(self):
        x = approve(issue())
        x["body"] = x["body"].replace("expected scoped contract", "other behavior")
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_revision_bump_without_approval_denied(self):
        x = approve(issue())
        x["body"] = x["body"].replace("### SPEC_REVISION\n\n2", "### SPEC_REVISION\n\n3")
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_untrusted_actor_cannot_approve(self):
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(approve(issue(), actor="outsider"), repo=REPO, approvers={"Lost0rz"})

    def test_ready_label_does_not_approve(self):
        x = issue()
        x["labels"] = [{"name": "READY_TO_EXECUTE"}]
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_missing_field_stops(self):
        x = issue()
        x["body"] = x["body"].replace("### VERIFICATION_PLAN", "### PLAN_GONE")
        with self.assertRaisesRegex(mod.SpecError, "UNKNOWN_FIELD"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_duplicate_field_stops(self):
        x = issue()
        x["body"] += "\n### TASK_ID\n\nALTERED\n"
        with self.assertRaisesRegex(mod.SpecError, "DUPLICATE_FIELD"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_unverified_target_stops(self):
        x = issue()
        x["body"] = x["body"].replace("verified skills/project-governance", "UNKNOWN skills/project-governance")
        with self.assertRaisesRegex(mod.SpecError, "UNVERIFIED_EXECUTION_TARGET"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_incomplete_wp_stops(self):
        x = issue()
        x["body"] = x["body"].replace("Dependencies: NONE", "Deps: NONE")
        with self.assertRaisesRegex(mod.SpecError, "WP_FIELD_MISSING"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_duplicate_wp_ids_stop(self):
        x = issue()
        x["body"] = x["body"].replace("### VERIFICATION_PLAN",
            "#### WP01 — duplicated unit\nTargets: second target\n"
            "Preconditions: verified\nActions: actual edit\n"
            "Dependencies: NONE\nEdge cases: known\n"
            "Verification: pass check\nDone: complete\n"
            "### VERIFICATION_PLAN")
        with self.assertRaisesRegex(mod.SpecError, "WORK_PACKAGE_IDS_NOT_UNIQUE"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_wp_placeholder_stops(self):
        x = issue()
        x["body"] = x["body"].replace("Actions: change one documented rule; preserve old mode",
                                     "Actions: <decide implementation later>")
        with self.assertRaisesRegex(mod.SpecError, "WP_FIELD_UNRESOLVED"):
            mod.digest(x["body"], repo=REPO, number=40)

    def test_reused_revision_ambiguous_stops(self):
        x = approve(issue())
        approve(x, hash_value="a" * 64)
        with self.assertRaisesRegex(mod.SpecError, "REVISION_REUSED"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_revocation_blocks_execution(self):
        x = approve(issue())
        x["comments"].append({
            "id": 2, "author": {"login": "Lost0rz"},
            "body": "SPEC_REVOCATION_V1\nTASK_ID: EG-093\nSPEC_REVISION: 2\nDECISION: REVOKED",
        })
        with self.assertRaisesRegex(mod.SpecError, "APPROVAL_REVOKED"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_closed_issue_is_denied(self):
        x = approve(issue())
        x["state"] = "CLOSED"
        with self.assertRaisesRegex(mod.SpecError, "ISSUE_NOT_OPEN"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"})

    def test_identical_form_and_markdown_have_same_digest(self):
        a = body()
        b = "\r\n".join(a.split("\n"))
        self.assertEqual(mod.digest(a, repo=REPO, number=40)[1],
                         mod.digest(b, repo=REPO, number=40)[1])

    def test_delegation_defaults_off(self):
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(delegate(issue()), repo=REPO, approvers={"Lost0rz"})

    def test_explicit_delegation_accepts_matching_exact_spec(self):
        result = mod.verify_approval(delegate(issue()), repo=REPO,
                                     approvers={"Lost0rz"}, allow_delegated=True)
        self.assertEqual(result["result"], "STRUCTURE_AND_DELEGATED_APPROVAL_PASS")
        self.assertEqual(result["approval_assurance"], "DELEGATED_ACCOUNT_ATTESTED")
        self.assertEqual(result["approval_comment_id"], 1)

    def test_direct_approval_still_preferred_with_delegation_opt_in(self):
        x = approve(delegate(issue()))
        r = mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)
        self.assertEqual(r["result"], "STRUCTURE_AND_APPROVAL_PASS")
        self.assertEqual(r["approval_assurance"], "DIRECT_GITHUB_ACTOR")

    def test_delegation_untrusted_account_denied(self):
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(delegate(issue(), actor="outsider"), repo=REPO,
                                approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_stale_digest_denied(self):
        x = delegate(issue())
        x["body"] = x["body"].replace("expected scoped contract", "changed scope")
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_missing_required_attestation_denied(self):
        x = delegate(issue())
        x["comments"][0]["body"] = x["comments"][0]["body"].replace(
            "PROVENANCE: ACCOUNT_PROXY_NO_INDEPENDENT_CHAT_PROOF", "")
        with self.assertRaisesRegex(mod.SpecError, "INVALID_DELEGATED_APPROVAL_FIELDS"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_incorrect_attestation_denied(self):
        x = delegate(issue())
        x["comments"][0]["body"] = x["comments"][0]["body"].replace(
            "USER_DECISION: EXPLICIT_APPROVAL_OF_CURRENT_SPEC",
            "USER_DECISION: AUTO_APPROVED")
        with self.assertRaisesRegex(mod.SpecError, "INVALID_DELEGATED_ATTESTATION"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_empty_decision_summary_denied(self):
        x = delegate(issue(), summary=" ")
        with self.assertRaisesRegex(mod.SpecError, "INVALID_DELEGATED_ATTESTATION"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_revoked_denied(self):
        x = delegate(issue())
        x["comments"].append({
            "id": 2, "author": {"login": "Lost0rz"},
            "body": "SPEC_REVOCATION_V1\nTASK_ID: EG-093\nSPEC_REVISION: 2\nDECISION: REVOKED",
        })
        with self.assertRaisesRegex(mod.SpecError, "APPROVAL_REVOKED"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_reused_revision_digest_conflict_denied(self):
        x = delegate(issue())
        delegate(x, hash_value="c" * 64)
        with self.assertRaisesRegex(mod.SpecError, "REVISION_REUSED"):
            mod.verify_approval(x, repo=REPO, approvers={"Lost0rz"}, allow_delegated=True)

    def test_delegation_requires_exact_accepted_agents_opt_in(self):
        self.assertFalse(mod.delegated_opt_in("CONTROL_MODE: ISSUE_CONTROL\n"))
        self.assertTrue(mod.delegated_opt_in(
            "CONTROL_MODE: ISSUE_CONTROL\nISSUE_DELEGATED_APPROVAL: ENABLED\n"))
        self.assertFalse(mod.delegated_opt_in(
            "ISSUE_DELEGATED_APPROVAL: ENABLED\nISSUE_DELEGATED_APPROVAL: DISABLED\n"))
        self.assertFalse(mod.delegated_opt_in("ISSUE_DELEGATED_APPROVAL: enable\n"))


    def test_delegation_fenced_backtick_example_not_policy(self):
        self.assertFalse(mod.delegated_opt_in(
            "## Example\n```md\nISSUE_DELEGATED_APPROVAL: ENABLED\n```\n"))

    def test_delegation_fenced_tilde_example_not_policy(self):
        self.assertFalse(mod.delegated_opt_in(
            "~~~text\nISSUE_DELEGATED_APPROVAL: ENABLED\n~~~\n"))

    def test_delegation_indented_example_not_policy(self):
        self.assertFalse(mod.delegated_opt_in(
            "    ISSUE_DELEGATED_APPROVAL: ENABLED\n"))
        self.assertFalse(mod.delegated_opt_in(
            "  ISSUE_DELEGATED_APPROVAL: ENABLED\n"))

    def test_delegation_blockquote_example_not_policy(self):
        self.assertFalse(mod.delegated_opt_in(
            "> ISSUE_DELEGATED_APPROVAL: ENABLED\n"))

    def test_delegation_bare_directive_outside_example(self):
        self.assertTrue(mod.delegated_opt_in(
            "## Policy\n```md\nISSUE_DELEGATED_APPROVAL: DISABLED\n```\n"
            "ISSUE_DELEGATED_APPROVAL: ENABLED\n"))

    def test_delegation_html_comment_example_not_policy(self):
        self.assertFalse(mod.delegated_opt_in(
            "<!--\nISSUE_DELEGATED_APPROVAL: ENABLED\n-->\n"))
        self.assertTrue(mod.delegated_opt_in(
            "<!--\nISSUE_DELEGATED_APPROVAL: DISABLED\n-->\n"
            "ISSUE_DELEGATED_APPROVAL: ENABLED\n"))

    def test_delegation_duplicate_real_declarations_denied_with_fence(self):
        self.assertFalse(mod.delegated_opt_in(
            "ISSUE_DELEGATED_APPROVAL: ENABLED\n"
            "```text\nISSUE_DELEGATED_APPROVAL: ENABLED\n```\n"
            "ISSUE_DELEGATED_APPROVAL: DISABLED\n"))

    def test_web_spec_authoring_defaults_to_deny(self):
        self.assertFalse(mod.web_spec_authoring_opt_in("CONTROL_MODE: ISSUE_CONTROL\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "ISSUE_WEB_SPEC_AUTHORING: DISABLED\n"))

    def test_web_spec_authoring_requires_one_exact_enabled_declaration(self):
        self.assertTrue(mod.web_spec_authoring_opt_in(
            "CONTROL_MODE: ISSUE_CONTROL\nISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "ISSUE_WEB_SPEC_AUTHORING: ENABLED\nISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "ISSUE_WEB_SPEC_AUTHORING: ENABLED\nISSUE_WEB_SPEC_AUTHORING: DISABLED\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in("ISSUE_WEB_SPEC_AUTHORING: enabled\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in("ISSUE_WEB_SPEC_AUTHORING : ENABLED\n"))

    def test_web_spec_authoring_ignores_markdown_examples(self):
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "```md\nISSUE_WEB_SPEC_AUTHORING: ENABLED\n```\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "~~~text\nISSUE_WEB_SPEC_AUTHORING: ENABLED\n~~~\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "    ISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "> ISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))
        self.assertFalse(mod.web_spec_authoring_opt_in(
            "<!--\nISSUE_WEB_SPEC_AUTHORING: ENABLED\n-->\n"))
        self.assertTrue(mod.web_spec_authoring_opt_in(
            "```md\nISSUE_WEB_SPEC_AUTHORING: DISABLED\n```\n"
            "ISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))

    def test_web_authoring_opt_in_does_not_approve_a_draft(self):
        self.assertTrue(mod.web_spec_authoring_opt_in(
            "ISSUE_WEB_SPEC_AUTHORING: ENABLED\n"))
        with self.assertRaisesRegex(mod.SpecError, "NO_MATCHING"):
            mod.verify_approval(issue(), repo=REPO, approvers={"Lost0rz"})

    def test_autonomy_opt_in_requires_one_operative_declaration(self):
        self.assertTrue(mod.risk_scoped_autonomy_opt_in(AUTONOMY_AGENTS))
        self.assertFalse(mod.risk_scoped_autonomy_opt_in(
            "```text\nRISK_SCOPED_AUTONOMY: ENABLED\n```\n"))
        self.assertFalse(mod.risk_scoped_autonomy_opt_in(
            "RISK_SCOPED_AUTONOMY: ENABLED\nRISK_SCOPED_AUTONOMY: DISABLED\n"))

    def test_valid_g1_snapshot_is_policy_only_and_remains_fail_closed(self):
        result = mod.verify_autonomy_snapshot(
            issue(), autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
            agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            now=datetime(2026, 11, 10, tzinfo=timezone.utc),
        )
        self.assertEqual(result["policy_shape"], "PASS_LOCAL_SNAPSHOT_ONLY")
        self.assertEqual(result["result"], "STOP")
        self.assertEqual(result["reason"], "UNVERIFIED_AUTHORIZATION_SOURCE")
        self.assertEqual(result["autonomy_status"], "INACTIVE_UNVERIFIED_HOST_BOUNDARY")
        self.assertFalse(result["execution_allowed"])

    def test_compact_g1_scope_is_only_policy_shape_and_always_stops(self):
        compact_body = "\n\n".join([
            "### CONTRACT\nAUTONOMY_SCOPE_V1", "### TASK_ID\nEG-093",
            "### SPEC_REVISION\n2", "### OBJECTIVE\nFix bounded checker test",
            "### ALLOWED_PATHS\nskills/project-governance",
            "### ALLOWED_EFFECTS\nrepository_source_changes,repository_tests,same_task_ref_push",
            "### MAX_RISK\nG2", "### STOP_AND_SAFETY\nNo privileged action",
        ]) + "\n"
        compact = {"number": 40, "state": "OPEN", "body": compact_body, "comments": []}
        fields, sha = mod.digest_autonomy_scope(compact_body, repo=REPO, number=40)
        self.assertEqual(fields["CONTRACT"], "AUTONOMY_SCOPE_V1")
        self.assertEqual(len(fields), 8)
        grant = autonomy_snapshot()
        grant["spec_sha256"] = sha
        result = mod.verify_autonomy_snapshot(
            compact, grant, repo=REPO, approvers={"Lost0rz"},
            agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093",
            target_commit_sha="a"*40, now=datetime(2026, 11, 10, tzinfo=timezone.utc),
        )
        self.assertEqual(result["result"], "STOP")
        self.assertFalse(result["execution_allowed"])
        self.assertEqual(result["policy_shape"], "PASS_LOCAL_SNAPSHOT_ONLY")
        with self.assertRaisesRegex(mod.SpecError, "UNKNOWN_FIELD|MISSING_FIELDS"):
            mod.digest(compact_body, repo=REPO, number=40)

        scope_violations = [
            ("### MAX_RISK\nG2", "### MAX_RISK\nG1",
             "AUTONOMY_GRANT_RISK_OUTSIDE_ISSUE_SCOPE"),
            ("### ALLOWED_PATHS\nskills/project-governance", "### ALLOWED_PATHS\napps/web",
             "AUTONOMY_GRANT_PATH_OUTSIDE_ISSUE_SCOPE"),
            ("### ALLOWED_EFFECTS\nrepository_source_changes,repository_tests,same_task_ref_push",
             "### ALLOWED_EFFECTS\nrepository_tests",
             "AUTONOMY_GRANT_EFFECT_OUTSIDE_ISSUE_SCOPE"),
        ]
        for old, new, err in scope_violations:
            with self.subTest(err=err):
                different = dict(compact, body=compact_body.replace(old, new))
                _, new_sha = mod.digest_autonomy_scope(different["body"], repo=REPO, number=40)
                changed = copy.deepcopy(grant)
                changed["spec_sha256"] = new_sha
                with self.assertRaisesRegex(mod.SpecError, err):
                    mod.verify_autonomy_snapshot(
                        different, changed, repo=REPO, approvers={"Lost0rz"},
                        agents_text=AUTONOMY_AGENTS,
                        target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                    )

        for invalid in (compact_body.replace("### TASK_ID", "### EXTRA"),
                        compact_body.replace("### OBJECTIVE", "### TASK_ID"),
                        compact_body.replace("### ALLOWED_PATHS\nskills/project-governance",
                                             "### ALLOWED_PATHS\n../secrets")):
            with self.subTest(invalid=invalid):
                with self.assertRaises(mod.SpecError):
                    mod.digest_autonomy_scope(invalid, repo=REPO, number=40)

    def test_autonomy_paths_reject_control_character_injections(self):
        for unsafe in ("skills/unsafe\x00file", "skills/unsafe\nfile", "skills/unsafe\rfile"):
            grant = autonomy_snapshot()
            grant["allowed_paths"] = [unsafe]
            with self.subTest(path=repr(unsafe)):
                with self.assertRaisesRegex(mod.SpecError, "INVALID_AUTONOMY_ALLOWED_PATHS"):
                    mod.verify_autonomy_snapshot(
                        issue(), grant, repo=REPO, approvers={"Lost0rz"},
                        agents_text=AUTONOMY_AGENTS,
                        target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                    )

    def test_autonomy_missing_opt_in_stops(self):
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_NOT_OPTED_IN"):
            mod.verify_autonomy_snapshot(
                issue(), autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
                agents_text="CONTROL_MODE: ISSUE_CONTROL\n",
                target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )

    def test_autonomy_self_grant_with_same_credential_stops(self):
        grant = autonomy_snapshot()
        grant["grant_event"]["executor_credential_id"] = "independent-grant-credential"
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_SELF_AUTHORIZATION"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                now=datetime(2026, 11, 10, tzinfo=timezone.utc),
            )

    def test_autonomy_untrusted_grant_actor_stops(self):
        grant = autonomy_snapshot()
        grant["grant_event"]["actor_login"] = "outsider"
        with self.assertRaisesRegex(mod.SpecError, "UNTRUSTED_AUTONOMY_GRANT_ACTOR"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                now=datetime(2026, 11, 10, tzinfo=timezone.utc),
            )

    def test_autonomy_replayed_after_spec_change_stops(self):
        changed = issue()
        changed["body"] = changed["body"].replace(
            "Implement exactly the approved scoped fix", "Implement a different scope")
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_TASK_BINDING_MISMATCH"):
            mod.verify_autonomy_snapshot(
                changed, autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )

    def test_autonomy_revoked_or_expired_snapshot_stops(self):
        revoked = autonomy_snapshot()
        revoked["revoked_at"] = "2026-11-10T12:00:00Z"
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_GRANT_REVOKED"):
            mod.verify_autonomy_snapshot(
                issue(), revoked, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                now=datetime(2026, 11, 10, tzinfo=timezone.utc),
            )
        expired = autonomy_snapshot()
        expired["issued_at"] = "2026-11-08T00:00:00Z"
        expired["expires_at"] = "2026-11-09T00:00:00Z"
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_GRANT_EXPIRED"):
            mod.verify_autonomy_snapshot(
                issue(), expired, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
                now=datetime(2026, 11, 10, tzinfo=timezone.utc),
            )

    def test_autonomy_target_change_stops(self):
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_TARGET_MISMATCH"):
            mod.verify_autonomy_snapshot(
                issue(), autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/other-task", target_commit_sha="a"*40,
            )

    def test_autonomy_replay_after_target_commit_change_stops(self):
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_COMMIT_MISMATCH"):
            mod.verify_autonomy_snapshot(
                issue(), autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093",
                target_commit_sha="b"*40,
            )

    def test_autonomy_requested_path_must_stay_inside_allowed_path_prefix(self):
        grant = autonomy_snapshot()
        grant["requested_paths"] = ["skills/project-governance-escape/attack.py"]
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_PATH_OUTSIDE_ENVELOPE"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093",
                target_commit_sha="a"*40,
            )

    def test_autonomy_paths_cannot_target_git_metadata(self):
        grant = autonomy_snapshot()
        grant["allowed_paths"] = [".git"]
        grant["requested_paths"] = [".git/config"]
        with self.assertRaisesRegex(mod.SpecError, "INVALID_AUTONOMY_ALLOWED_PATHS"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093",
                target_commit_sha="a"*40,
            )

    def test_autonomy_unknown_effect_alias_cannot_hide_merge(self):
        grant = autonomy_snapshot()
        grant["allowed_effects"].append("pr_merge")
        grant["requested_effects"].append("pr_merge")
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_UNSUPPORTED_OR_OUTSIDE_EFFECT_ENVELOPE"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093",
                target_commit_sha="a"*40,
            )

    def test_autonomy_invalid_branch_refs_stop(self):
        for target_ref in ("refs/heads/../main", "refs/heads/.hidden", "refs/heads/topic.lock",
                           "refs/heads/topic/", "refs/heads/a@{b}"):
            with self.subTest(target_ref=target_ref):
                with self.assertRaisesRegex(mod.SpecError, "INVALID_AUTONOMY_TARGET_REF"):
                    mod.verify_autonomy_snapshot(
                        issue(), autonomy_snapshot(), repo=REPO, approvers={"Lost0rz"},
                        agents_text=AUTONOMY_AGENTS, target_ref=target_ref, target_commit_sha="a"*40,
                    )

    def test_autonomy_g3_risk_is_outside_g1_g2_envelope(self):
        grant = autonomy_snapshot()
        grant["requested_risk"] = "G3"
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_RISK_OUTSIDE_ENVELOPE"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )

    def test_float_tabs_208_debug_only_test_seam_is_g1_policy_only(self):
        grant = autonomy_snapshot()
        grant["max_risk"] = "G1"
        grant["requested_effects"] = ["repository_tests"]
        result = mod.verify_autonomy_snapshot(
            issue(), grant, repo=REPO, approvers={"Lost0rz"},
            agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            now=datetime(2026, 11, 10, tzinfo=timezone.utc),
        )
        self.assertEqual(result["requested_risk"], "G1")
        self.assertEqual(result["result"], "STOP")
        self.assertFalse(result["execution_allowed"])

    def test_float_tabs_211_human_ui_acceptance_is_hard_excluded(self):
        grant = autonomy_snapshot()
        grant["allowed_effects"].append("human_ui_acceptance")
        grant["requested_effects"].append("human_ui_acceptance")
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_HARD_EXCLUDED_EFFECT"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )

    def test_merloom_632_rawsku_overwrite_is_hard_denied(self):
        grant = autonomy_snapshot()
        grant["allowed_effects"].append("destructive_data_overwrite")
        grant["requested_effects"].append("destructive_data_overwrite")
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_HARD_EXCLUDED_EFFECT"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )

    def test_remoteorbit_51_privileged_hid_helper_is_g3_and_hard_excluded(self):
        grant = autonomy_snapshot()
        grant["requested_risk"] = "G3"
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_RISK_OUTSIDE_ENVELOPE"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )
        grant["requested_risk"] = "G2"
        grant["allowed_effects"].append("privileged_install")
        grant["requested_effects"].append("privileged_install")
        with self.assertRaisesRegex(mod.SpecError, "AUTONOMY_HARD_EXCLUDED_EFFECT"):
            mod.verify_autonomy_snapshot(
                issue(), grant, repo=REPO, approvers={"Lost0rz"},
                agents_text=AUTONOMY_AGENTS, target_ref="refs/heads/codex/eg-093", target_commit_sha="a"*40,
            )



if __name__ == "__main__":
    unittest.main()

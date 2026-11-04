#!/usr/bin/env python3
"""Focused positive/negative contract checks; no GitHub/network dependency."""
import copy
import importlib.util
import unittest
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


if __name__ == "__main__":
    unittest.main()

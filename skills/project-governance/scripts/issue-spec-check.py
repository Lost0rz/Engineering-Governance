#!/usr/bin/env python3
"""Offline structural and approval check for EXECUTION_SPEC_V1 GitHub Issues.

Input is fresh "gh issue view N -R owner/repo --json number,body,state,comments"
augmented with repository name from the authoritative CLI -R selector.
This check cannot establish real source-path correctness, runtime permissions,
or human UI acceptance; those remain mandatory Project Governance checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

CONTRACT = "EXECUTION_SPEC_V1"
FIELDS = (
    "CONTRACT", "TASK_ID", "SPEC_REVISION", "MODE", "PURPOSE",
    "OBJECTIVE", "VERIFIED_BASELINE", "TARGET_BEHAVIOR", "IN_SCOPE",
    "OUT_OF_SCOPE", "ALLOWED_SIDE_EFFECTS", "CANONICAL_AUTHORITIES",
    "WORK_PACKAGES", "VERIFICATION_PLAN", "HUMAN_UI_ACCEPTANCE",
    "DEVIATION_POLICY", "STOP_AND_SAFETY", "RETURN_CONTRACT",
    "AUTHORIZATION_BASIS",
)
WP_KEYS = ("Targets", "Preconditions", "Actions", "Dependencies",
           "Edge cases", "Verification", "Done")
FIELD_HEADER = re.compile(r"^### ([A-Z][A-Z0-9_]*)[ \t]*$")
WP_HEADER = re.compile(r"^#### WP\d{2,}[ \t]*[-—:].*$", re.M)
APPROVAL_PREFIX = "SPEC_APPROVAL_V1"
DELEGATED_APPROVAL_PREFIX = "SPEC_DELEGATED_APPROVAL_V1"
REVOCATION_PREFIX = "SPEC_REVOCATION_V1"
PLACEHOLDER = re.compile(r"(^|\n)[ \t]*(?:TODO|TBD|UNKNOWN|<[^>\n]+>|\.\.\.)[ \t]*(?:\n|$)", re.I)


class SpecError(ValueError):
    pass


def _lines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_fields(body: str) -> dict[str, str]:
    """Parse only canonical ### headings; fail closed on duplicate/unknown headings."""
    values: dict[str, list[str]] = {}
    current: str | None = None
    for line in _lines(body).split("\n"):
        hit = FIELD_HEADER.fullmatch(line)
        if hit:
            key = hit.group(1)
            if key not in FIELDS:
                raise SpecError("UNKNOWN_FIELD: " + key)
            if key in values:
                raise SpecError("DUPLICATE_FIELD: " + key)
            values[key] = []
            current = key
        elif current is not None:
            values[current].append(line)
        elif line.strip():
            raise SpecError("UNPARSEABLE_PREFIX: field headings required")
    missing = sorted(set(FIELDS) - set(values))
    if missing:
        raise SpecError("MISSING_FIELDS: " + ",".join(missing))
    result = {key: "\n".join(values[key]).strip(" \t\n") for key in FIELDS}
    for key, val in result.items():
        if not val or PLACEHOLDER.search(val):
            raise SpecError("INCOMPLETE_FIELD: " + key)
    if result["CONTRACT"] != CONTRACT:
        raise SpecError("UNSUPPORTED_CONTRACT")
    if result["MODE"] != "EXECUTE":
        raise SpecError("UNSUPPORTED_MODE")
    if not re.fullmatch(r"[1-9]\d*", result["SPEC_REVISION"]):
        raise SpecError("INVALID_REVISION")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", result["TASK_ID"]):
        raise SpecError("INVALID_TASK_ID")
    if "UNKNOWN" in result["VERIFIED_BASELINE"].upper() or "UNKNOWN" in result["WORK_PACKAGES"].upper():
        raise SpecError("UNVERIFIED_EXECUTION_TARGET")
    if not (result["HUMAN_UI_ACCEPTANCE"].startswith("PENDING")
            or result["HUMAN_UI_ACCEPTANCE"].startswith("NOT_REQUIRED:")):
        raise SpecError("INVALID_HUMAN_UI_GATE")
    packages = list(WP_HEADER.finditer(result["WORK_PACKAGES"]))
    if not packages:
        raise SpecError("NO_DETAILED_WORK_PACKAGES")
    names = [re.search(r"WP\d+", item.group()).group() for item in packages]
    if names != [f"WP{i:02d}" for i in range(1, len(names) + 1)]:
        raise SpecError("WORK_PACKAGE_IDS_NOT_UNIQUE_AND_ORDERED")
    for index, match in enumerate(packages):
        start = match.end()
        end = packages[index + 1].start() if index + 1 < len(packages) else len(result["WORK_PACKAGES"])
        block = result["WORK_PACKAGES"][start:end]
        for key in WP_KEYS:
            line = re.search(r"(?mi)^" + re.escape(key) + r":[ \t]*(.*)$", block)
            if not line or not line.group(1).strip():
                raise SpecError("WP_FIELD_MISSING: " + match.group().strip() + ":" + key)
            if re.search(r"\b(?:TODO|TBD|UNKNOWN)\b|<[^>\n]+>|\.\.\.", line.group(1), re.I):
                raise SpecError("WP_FIELD_UNRESOLVED: " + match.group().strip() + ":" + key)
    return result


def digest(body: str, *, repo: str, number: int) -> tuple[dict[str, str], str]:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise SpecError("INVALID_REPOSITORY")
    if not isinstance(number, int) or number <= 0:
        raise SpecError("INVALID_ISSUE_NUMBER")
    fields = parse_fields(body)
    material = {"repository": repo, "issue": number, "fields": fields}
    raw = json.dumps(material, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":")).encode("utf-8")
    return fields, hashlib.sha256(raw).hexdigest()


def _record(comment: dict, kind: str) -> dict[str, str] | None:
    body = _lines(str(comment.get("body") or "")).strip()
    if not body.startswith(kind + "\n"):
        return None
    entries = {}
    for line in body.split("\n")[1:]:
        if not line.strip():
            continue
        if ": " not in line:
            raise SpecError("INVALID_" + kind)
        k, v = line.split(": ", 1)
        if not k or not v or k in entries:
            raise SpecError("INVALID_" + kind)
        entries[k] = v.strip()
    return entries


def delegated_opt_in(agents_text: str) -> bool:
    """Allow one operative top-level opt-in, never a Markdown example."""
    entries: list[str] = []
    fence: tuple[str, int] | None = None
    for line in _lines(agents_text).split("\n"):
        marker = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})([^\n]*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                fence = None
            continue
        if fence is not None:
            continue
        # Indented code, quoted examples and prose are not policy declarations.
        if line.startswith("ISSUE_DELEGATED_APPROVAL:"):
            entries.append(line.rstrip(" \t"))
    return entries == ["ISSUE_DELEGATED_APPROVAL: ENABLED"]


def verify_approval(issue: dict, *, repo: str, approvers: set[str],
                    allow_delegated: bool = False) -> dict:
    """Verify exact-spec approval. Delegation is lower-assurance and opt-in only.

    The caller must resolve allow_delegated from accepted repository AGENTS.md.
    The CLI additionally requires an AGENTS file when delegated mode is enabled.
    GitHub actor authentication cannot independently prove ChatGPT user intent.
    """
    if not approvers:
        raise SpecError("NO_TRUSTED_APPROVERS")
    if issue.get("state") not in ("OPEN", "open"):
        raise SpecError("ISSUE_NOT_OPEN")
    fields, actual = digest(str(issue.get("body") or ""), repo=repo,
                            number=issue.get("number"))
    task, rev = fields["TASK_ID"], fields["SPEC_REVISION"]
    seen_revision_hashes: set[str] = set()
    valid_direct_id = None
    valid_delegated_id = None
    delegated_keys = {
        "REPOSITORY", "ISSUE", "TASK_ID", "SPEC_REVISION", "SPEC_SHA256",
        "DECISION", "AUTHORIZATION_CHANNEL", "USER_DECISION",
        "USER_DECISION_SUMMARY", "PROVENANCE",
    }
    for comment in issue.get("comments", []):
        if not isinstance(comment, dict) or not comment.get("id"):
            raise SpecError("UNVERIFIABLE_COMMENT_ID")
        author = (comment.get("author") or {}).get("login", "")
        if author not in approvers:
            continue
        revoke = _record(comment, REVOCATION_PREFIX)
        if revoke and revoke.get("TASK_ID") == task and revoke.get("SPEC_REVISION") == rev:
            raise SpecError("APPROVAL_REVOKED")
        direct = _record(comment, APPROVAL_PREFIX)
        delegated = (_record(comment, DELEGATED_APPROVAL_PREFIX)
                     if allow_delegated else None)
        if not direct and not delegated:
            continue
        record = direct or delegated
        if delegated:
            if set(record) != delegated_keys:
                raise SpecError("INVALID_DELEGATED_APPROVAL_FIELDS")
            if (record["AUTHORIZATION_CHANNEL"] != "CHATGPT_WEB"
                    or record["USER_DECISION"] != "EXPLICIT_APPROVAL_OF_CURRENT_SPEC"
                    or record["PROVENANCE"] != "ACCOUNT_PROXY_NO_INDEPENDENT_CHAT_PROOF"
                    or not 1 <= len(record["USER_DECISION_SUMMARY"]) <= 500):
                raise SpecError("INVALID_DELEGATED_ATTESTATION")
        if record.get("TASK_ID") != task or record.get("SPEC_REVISION") != rev:
            continue
        if record.get("REPOSITORY") != repo or record.get("ISSUE") != str(issue["number"]):
            continue
        sha = record.get("SPEC_SHA256") or ""
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            raise SpecError("INVALID_APPROVAL_DIGEST")
        seen_revision_hashes.add(sha)
        if record.get("DECISION") == "APPROVED_FOR_EXECUTION" and sha == actual:
            if delegated:
                valid_delegated_id = comment["id"]
            else:
                valid_direct_id = comment["id"]
    if len(seen_revision_hashes) > 1:
        raise SpecError("REVISION_REUSED_FOR_DIFFERENT_CONTENT")
    if valid_direct_id is None and valid_delegated_id is None:
        raise SpecError("NO_MATCHING_TRUSTED_APPROVAL")
    delegated_result = valid_direct_id is None
    return {
        "result": ("STRUCTURE_AND_DELEGATED_APPROVAL_PASS" if delegated_result
                   else "STRUCTURE_AND_APPROVAL_PASS"),
        "approval_assurance": ("DELEGATED_ACCOUNT_ATTESTED" if delegated_result
                               else "DIRECT_GITHUB_ACTOR"),
        "approval_comment_id": (valid_delegated_id if delegated_result
                                else valid_direct_id),
        "task_id": task,
        "spec_revision": rev,
        "spec_sha256": actual,
        "semantic_source_check": "REQUIRED_SEPARATELY",
        "writer_workspace_check": "REQUIRED_SEPARATELY",
        "human_ui_acceptance": fields["HUMAN_UI_ACCEPTANCE"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=("digest", "verify"))
    p.add_argument("--issue-json", type=Path, required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--approvers", default="", help="comma-separated trusted GitHub logins from AGENTS.md")
    p.add_argument("--allow-delegated", action="store_true",
                   help="opt-in only: requires accepted AGENTS.md policy")
    p.add_argument("--agents-file", type=Path,
                   help="accepted target AGENTS.md, mandatory for --allow-delegated")
    args = p.parse_args()
    try:
        issue = json.loads(args.issue_json.read_text(encoding="utf-8"))
        if args.mode == "digest":
            fields, h = digest(issue["body"], repo=args.repo, number=issue["number"])
            result = {"result": "STRUCTURE_PASS_APPROVAL_PENDING",
                      "task_id": fields["TASK_ID"], "spec_revision": fields["SPEC_REVISION"],
                      "spec_sha256": h}
        else:
            if args.allow_delegated:
                if args.agents_file is None:
                    raise SpecError("DELEGATION_AGENTS_FILE_REQUIRED")
                if not delegated_opt_in(args.agents_file.read_text(encoding="utf-8")):
                    raise SpecError("DELEGATION_NOT_OPTED_IN")
            result = verify_approval(
                issue, repo=args.repo,
                approvers={x.strip() for x in args.approvers.split(",") if x.strip()},
                allow_delegated=args.allow_delegated,
            )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except (SpecError, KeyError, TypeError, ValueError, OSError) as exc:
        print(json.dumps({"result": "STOP", "reason": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())

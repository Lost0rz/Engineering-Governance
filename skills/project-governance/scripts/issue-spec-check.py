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
import importlib.util
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# The versioned Skill package, not target-project AGENTS.md, owns control policy.
_POLICY_SPEC = importlib.util.spec_from_file_location(
    "eg_global_control_policy", Path(__file__).with_name("control-policy.py"))
_POLICY = importlib.util.module_from_spec(_POLICY_SPEC)
_POLICY_SPEC.loader.exec_module(_POLICY)

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
# Future opt-in G1/G2 scope only; this is not a standalone authorization path.
COMPACT_CONTRACT = "AUTONOMY_SCOPE_V1"
COMPACT_FIELDS = (
    "CONTRACT", "TASK_ID", "SPEC_REVISION", "OBJECTIVE", "ALLOWED_PATHS",
    "ALLOWED_EFFECTS", "MAX_RISK", "STOP_AND_SAFETY",
)
FIELD_HEADER = re.compile(r"^### ([A-Z][A-Z0-9_]*)[ \t]*$")
WP_HEADER = re.compile(r"^#### WP\d{2,}[ \t]*[-—:].*$", re.M)
APPROVAL_PREFIX = "SPEC_APPROVAL_V1"
DELEGATED_APPROVAL_PREFIX = "SPEC_DELEGATED_APPROVAL_V1"
REVOCATION_PREFIX = "SPEC_REVOCATION_V1"
AUTONOMY_CONTRACT = "RISK_SCOPED_AUTONOMY_V1"
AUTONOMY_FIELDS = {
    "contract", "repository", "issue_number", "task_id", "spec_revision",
    "spec_sha256", "target_ref", "target_commit_sha", "allowed_paths",
    "requested_paths", "max_risk", "requested_risk", "allowed_effects",
    "requested_effects", "hard_exclusions",
    "issued_at", "expires_at", "revoked_at", "grant_event",
}
AUTONOMY_EVENT_FIELDS = {
    "host", "event", "workflow_path", "workflow_ref", "workflow_sha",
    "run_id", "run_attempt", "actor_login", "grant_credential_id",
    "executor_credential_id", "workflow_source_readback",
    "protection_readback", "credential_separation_readback", "revocation_readback",
}
AUTONOMY_HARD_EXCLUSIONS = {
    "merge", "release", "production_deploy", "privileged_install",
    "other_repository", "human_ui_acceptance", "protected_main_write",
    "credential_write", "destructive_data_overwrite",
}
AUTONOMY_ALLOWED_EFFECTS = {
    "repository_source_changes", "repository_tests", "same_task_ref_push",
}
AUTONOMY_SUPPORTED_EFFECTS = AUTONOMY_ALLOWED_EFFECTS | AUTONOMY_HARD_EXCLUSIONS
GOVERNANCE_RISKS = ("G0", "G1", "G2", "G3")
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


def parse_compact_scope(body: str) -> dict[str, str]:
    """Validate a short in-envelope task; never grant execution by itself."""
    entries: dict[str, list[str]] = {}
    current: str | None = None
    for line in _lines(body).split("\n"):
        match = FIELD_HEADER.fullmatch(line)
        if match:
            key = match.group(1)
            if key not in COMPACT_FIELDS:
                raise SpecError("UNKNOWN_COMPACT_FIELD: " + key)
            if key in entries:
                raise SpecError("DUPLICATE_COMPACT_FIELD: " + key)
            entries[key] = []
            current = key
        elif current:
            entries[current].append(line)
        elif line.strip():
            raise SpecError("INVALID_COMPACT_PREFIX")
    missing = set(COMPACT_FIELDS) - set(entries)
    if missing:
        raise SpecError("MISSING_COMPACT_FIELDS: " + ",".join(sorted(missing)))
    result = {key: "\n".join(entries[key]).strip(" \t\n") for key in COMPACT_FIELDS}
    for key, value in result.items():
        if not value or PLACEHOLDER.search(value):
            raise SpecError("INCOMPLETE_COMPACT_FIELD: " + key)
    if result["CONTRACT"] != COMPACT_CONTRACT:
        raise SpecError("UNSUPPORTED_COMPACT_CONTRACT")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", result["TASK_ID"]):
        raise SpecError("INVALID_COMPACT_TASK_ID")
    if not re.fullmatch(r"[1-9]\d*", result["SPEC_REVISION"]):
        raise SpecError("INVALID_COMPACT_REVISION")
    if result["MAX_RISK"] not in ("G1", "G2"):
        raise SpecError("UNSUPPORTED_COMPACT_RISK")
    paths = [line.strip().removeprefix("- ").strip()
             for line in result["ALLOWED_PATHS"].splitlines() if line.strip()]
    effects = [entry.strip().removeprefix("- ").strip()
               for entry in re.split(r"[,\n]", result["ALLOWED_EFFECTS"])
               if entry.strip()]
    if (not paths or len(paths) != len(set(paths))
            or not all(_safe_repo_path(path) for path in paths)):
        raise SpecError("INVALID_COMPACT_ALLOWED_PATHS")
    if (not effects or len(effects) != len(set(effects))
            or not set(effects).issubset(AUTONOMY_ALLOWED_EFFECTS)):
        raise SpecError("INVALID_COMPACT_ALLOWED_EFFECTS")
    return result


def digest_autonomy_scope(body: str, *, repo: str, number: int) -> tuple[dict[str, str], str]:
    """Accept legacy 19-field Issue or opt-in 8-field G1/G2 scope; policy only."""
    if re.search(r"(?m)^### CONTRACT[ \t]*\n[ \t\n]*AUTONOMY_SCOPE_V1[ \t]*(?:\n|$)", _lines(body)):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise SpecError("INVALID_REPOSITORY")
        if not isinstance(number, int) or number <= 0:
            raise SpecError("INVALID_ISSUE_NUMBER")
        fields = parse_compact_scope(body)
        material = {"repository": repo, "issue": number, "fields": fields}
        payload = json.dumps(material, sort_keys=True, ensure_ascii=False,
                             separators=(",", ":")).encode("utf-8")
        return fields, hashlib.sha256(payload).hexdigest()
    return digest(body, repo=repo, number=number)


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


def delegated_opt_in(_project_agents_text: str = "") -> bool:
    """Legacy read-only compatibility shim; project text never grants control."""
    return _POLICY.delegated_enabled()


def web_spec_authoring_opt_in(_project_agents_text: str = "") -> bool:
    """A project text directive is never a Web Issue writing opt-in."""
    return False  # use global policy + explicit user request + verified GitHub write


def risk_scoped_autonomy_opt_in(_project_agents_text: str = "") -> bool:
    """G1/G2 host authority is never obtained from project AGENTS.md."""
    return _POLICY.autonomy_enabled()


def _autonomy_timestamp(value: object, field: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise SpecError("INVALID_AUTONOMY_TIMESTAMP: " + field)
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise SpecError("INVALID_AUTONOMY_TIMESTAMP: " + field) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise SpecError("INVALID_AUTONOMY_TIMESTAMP: " + field)
    return parsed.astimezone(timezone.utc)


def _safe_repo_path(value: object) -> bool:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return False
    parts = value.split("/")
    return (all(part not in ("", ".", "..") and part.casefold() != ".git" for part in parts)
            and not any(ch in value for ch in "*?[]")
            and not any(ord(ch) < 32 or ord(ch) == 127 for ch in value))


def _safe_target_ref(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"refs/heads/[A-Za-z0-9._/-]+", value):
        return False
    name = value[len("refs/heads/"):]
    parts = name.split("/")
    return (bool(name) and not name.endswith(("/", ".")) and ".." not in name
            and "@{" not in name
            and all(part and not part.startswith(".") and not part.endswith(".lock")
                    for part in parts))


def _path_within_allowed(path: str, allowed_path: str) -> bool:
    return path == allowed_path or path.startswith(allowed_path.rstrip("/") + "/")


def verify_autonomy_snapshot(issue: dict, authorization: dict, *, repo: str,
                             approvers: set[str], policy_autonomy_enabled: bool,
                             target_ref: str, target_commit_sha: str,
                             now: datetime | None = None) -> dict:
    """Validate a proposed grant snapshot, but never treat local JSON as host authority.

    This source version intentionally has no trusted GitHub host reader or credential
    separation verifier. A structurally valid snapshot therefore remains inactive.
    """
    if policy_autonomy_enabled is not True or not _POLICY.autonomy_enabled():
        raise SpecError("AUTONOMY_NOT_OPTED_IN")
    if not approvers:
        raise SpecError("NO_TRUSTED_APPROVERS")
    if issue.get("state") not in ("OPEN", "open"):
        raise SpecError("ISSUE_NOT_OPEN")
    if not isinstance(authorization, dict) or set(authorization) != AUTONOMY_FIELDS:
        raise SpecError("INVALID_AUTONOMY_FIELDS")

    fields, current_digest = digest_autonomy_scope(str(issue.get("body") or ""), repo=repo,
                                                   number=issue.get("number"))
    if (authorization.get("contract") != AUTONOMY_CONTRACT
            or authorization.get("repository") != repo
            or authorization.get("issue_number") != issue.get("number")
            or authorization.get("task_id") != fields["TASK_ID"]
            or authorization.get("spec_revision") != fields["SPEC_REVISION"]
            or authorization.get("spec_sha256") != current_digest):
        raise SpecError("AUTONOMY_TASK_BINDING_MISMATCH")
    if not _safe_target_ref(target_ref):
        raise SpecError("INVALID_AUTONOMY_TARGET_REF")
    if authorization.get("target_ref") != target_ref:
        raise SpecError("AUTONOMY_TARGET_MISMATCH")
    # This is the initial grant anchor only. A verified successor-commit lineage
    # adapter is not yet available: do not accept a caller-supplied ancestry flag.
    if (not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", target_commit_sha)
            or authorization.get("target_commit_sha") != target_commit_sha):
        raise SpecError("AUTONOMY_COMMIT_MISMATCH")

    paths = authorization.get("allowed_paths")
    if not isinstance(paths, list) or not paths or not all(_safe_repo_path(path) for path in paths):
        raise SpecError("INVALID_AUTONOMY_ALLOWED_PATHS")
    requested_paths = authorization.get("requested_paths")
    if (not isinstance(requested_paths, list) or not requested_paths
            or not all(_safe_repo_path(path) for path in requested_paths)):
        raise SpecError("INVALID_AUTONOMY_REQUESTED_PATHS")
    if any(not any(_path_within_allowed(path, allowed) for allowed in paths)
           for path in requested_paths):
        raise SpecError("AUTONOMY_PATH_OUTSIDE_ENVELOPE")
    if fields["CONTRACT"] == COMPACT_CONTRACT:
        scope_paths = [line.strip().removeprefix("- ").strip()
                       for line in fields["ALLOWED_PATHS"].splitlines() if line.strip()]
        if any(not any(_path_within_allowed(path, allowed) for allowed in scope_paths)
               for path in paths):
            raise SpecError("AUTONOMY_GRANT_PATH_OUTSIDE_ISSUE_SCOPE")
    max_risk = authorization.get("max_risk")
    requested_risk = authorization.get("requested_risk")
    if max_risk not in ("G1", "G2") or requested_risk not in GOVERNANCE_RISKS:
        raise SpecError("UNSUPPORTED_AUTONOMY_RISK")
    if GOVERNANCE_RISKS.index(requested_risk) > GOVERNANCE_RISKS.index(max_risk):
        raise SpecError("AUTONOMY_RISK_OUTSIDE_ENVELOPE")
    if (fields["CONTRACT"] == COMPACT_CONTRACT
            and GOVERNANCE_RISKS.index(max_risk) > GOVERNANCE_RISKS.index(fields["MAX_RISK"])):
        raise SpecError("AUTONOMY_GRANT_RISK_OUTSIDE_ISSUE_SCOPE")

    allowed_effects = authorization.get("allowed_effects")
    requested_effects = authorization.get("requested_effects")
    hard_exclusions = authorization.get("hard_exclusions")
    if (not isinstance(allowed_effects, list) or not allowed_effects
            or not all(isinstance(item, str) and item in AUTONOMY_SUPPORTED_EFFECTS
                       for item in allowed_effects)
            or not isinstance(requested_effects, list)
            or not all(isinstance(item, str) and item in AUTONOMY_SUPPORTED_EFFECTS
                       for item in requested_effects)
            or not set(requested_effects).issubset(set(allowed_effects))):
        raise SpecError("AUTONOMY_UNSUPPORTED_OR_OUTSIDE_EFFECT_ENVELOPE")
    if (not isinstance(hard_exclusions, list)
            or not all(isinstance(item, str) and item in AUTONOMY_SUPPORTED_EFFECTS
                       for item in hard_exclusions)
            or not AUTONOMY_HARD_EXCLUSIONS.issubset(set(hard_exclusions))):
        raise SpecError("AUTONOMY_HARD_EXCLUSIONS_INCOMPLETE_OR_UNSUPPORTED")
    if set(requested_effects).intersection(AUTONOMY_HARD_EXCLUSIONS):
        raise SpecError("AUTONOMY_HARD_EXCLUDED_EFFECT")
    if fields["CONTRACT"] == COMPACT_CONTRACT:
        issue_effects = {s.strip().removeprefix("- ").strip()
                         for s in re.split(r"[,\n]", fields["ALLOWED_EFFECTS"]) if s.strip()}
        if not set(allowed_effects).issubset(issue_effects):
            raise SpecError("AUTONOMY_GRANT_EFFECT_OUTSIDE_ISSUE_SCOPE")

    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None or current.utcoffset() is None:
        raise SpecError("INVALID_AUTONOMY_CLOCK")
    current = current.astimezone(timezone.utc)
    issued = _autonomy_timestamp(authorization.get("issued_at"), "issued_at")
    expires = _autonomy_timestamp(authorization.get("expires_at"), "expires_at")
    if issued > current:
        raise SpecError("AUTONOMY_GRANT_NOT_YET_VALID")
    if expires <= issued:
        raise SpecError("INVALID_AUTONOMY_EXPIRY")
    if expires <= current:
        raise SpecError("AUTONOMY_GRANT_EXPIRED")
    if authorization.get("revoked_at") is not None:
        _autonomy_timestamp(authorization.get("revoked_at"), "revoked_at")
        raise SpecError("AUTONOMY_GRANT_REVOKED")

    event = authorization.get("grant_event")
    if not isinstance(event, dict) or set(event) != AUTONOMY_EVENT_FIELDS:
        raise SpecError("INVALID_AUTONOMY_HOST_EVENT_FIELDS")
    if (event.get("host") != "github.com"
            or event.get("event") != "workflow_dispatch"
            or not isinstance(event.get("workflow_path"), str)
            or not re.fullmatch(r"\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml",
                                event.get("workflow_path", ""))
            or event.get("workflow_ref") != "refs/heads/main"
            or not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})",
                                str(event.get("workflow_sha") or ""))
            or not re.fullmatch(r"[1-9][0-9]*", str(event.get("run_id") or ""))
            or type(event.get("run_attempt")) is not int or event["run_attempt"] < 1):
        raise SpecError("INVALID_AUTONOMY_HOST_EVENT")
    if event.get("actor_login") not in approvers:
        raise SpecError("UNTRUSTED_AUTONOMY_GRANT_ACTOR")
    grant_credential = event.get("grant_credential_id")
    executor_credential = event.get("executor_credential_id")
    if (not isinstance(grant_credential, str) or not grant_credential
            or not isinstance(executor_credential, str) or not executor_credential
            or grant_credential == executor_credential):
        raise SpecError("AUTONOMY_SELF_AUTHORIZATION")
    if any(event.get(key) is not True for key in (
            "workflow_source_readback", "protection_readback",
            "credential_separation_readback", "revocation_readback")):
        raise SpecError("AUTONOMY_HOST_TRUST_UNVERIFIED")

    return {
        "result": "STOP",
        "reason": "UNVERIFIED_AUTHORIZATION_SOURCE",
        "autonomy_status": "INACTIVE_UNVERIFIED_HOST_BOUNDARY",
        "policy_shape": "PASS_LOCAL_SNAPSHOT_ONLY",
        "execution_allowed": False,
        "task_id": fields["TASK_ID"],
        "spec_revision": fields["SPEC_REVISION"],
        "spec_sha256": current_digest,
        "target_ref": target_ref,
        "target_commit_sha": target_commit_sha,
        "max_risk": max_risk,
        "requested_risk": requested_risk,
    }


def verify_approval(issue: dict, *, repo: str, approvers: set[str],
                    allow_delegated: bool = False) -> dict:
    """Verify exact-spec approval. Delegation is lower-assurance and opt-in only.

    The accepted global CONTROL_POLICY_V1 owns delegated-mode eligibility.
    GitHub actor authentication cannot independently prove ChatGPT user intent.
    The caller must independently verify trusted approvers via live host evidence.
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
    p.add_argument("mode", choices=("digest", "verify", "autonomy-verify"))
    p.add_argument("--issue-json", type=Path)
    p.add_argument("--authorization-json", type=Path,
                   help="untrusted local grant snapshot for autonomy-verify")
    p.add_argument("--target-ref", help="current local target ref for autonomy-verify")
    p.add_argument("--target-commit", help="current exact target commit for autonomy-verify")
    p.add_argument("--repo", required=True)
    p.add_argument("--approvers", default="", help="host-verified trusted GitHub approval actors; never inferred from AGENTS.md")
    p.add_argument("--allow-delegated", action="store_true",
                   help="only if global policy and independent user/host opt-in permit")
    args = p.parse_args()
    try:
        if args.issue_json is None:
            raise SpecError("ISSUE_JSON_REQUIRED")
        issue = json.loads(args.issue_json.read_text(encoding="utf-8"))
        if args.mode == "digest":
            fields, h = digest(issue["body"], repo=args.repo, number=issue["number"])
            result = {"result": "STRUCTURE_PASS_APPROVAL_PENDING",
                      "task_id": fields["TASK_ID"], "spec_revision": fields["SPEC_REVISION"],
                      "spec_sha256": h}
        elif args.mode == "verify":
            if args.allow_delegated and not delegated_opt_in():
                raise SpecError("DELEGATION_NOT_GLOBALLY_AUTHORIZED")
            result = verify_approval(
                issue, repo=args.repo,
                approvers={x.strip() for x in args.approvers.split(",") if x.strip()},
                allow_delegated=args.allow_delegated,
            )
        else:
            if args.authorization_json is None:
                raise SpecError("AUTONOMY_AUTHORIZATION_JSON_REQUIRED")
            if not args.target_ref:
                raise SpecError("AUTONOMY_TARGET_REF_REQUIRED")
            if not args.target_commit:
                raise SpecError("AUTONOMY_TARGET_COMMIT_REQUIRED")
            authorization = json.loads(args.authorization_json.read_text(encoding="utf-8"))
            result = verify_autonomy_snapshot(
                issue, authorization, repo=args.repo,
                approvers={x.strip() for x in args.approvers.split(",") if x.strip()},
                policy_autonomy_enabled=_POLICY.autonomy_enabled(), target_ref=args.target_ref,
                target_commit_sha=args.target_commit,
            )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 2 if result.get("result") == "STOP" else 0
    except (SpecError, KeyError, TypeError, ValueError, OSError) as exc:
        print(json.dumps({"result": "STOP", "reason": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())

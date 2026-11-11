#!/usr/bin/env python3
"""CONTROL_POLICY_V1: portable policy defaults and independently queried GitHub enrollment.

A machine or project AGENTS.md is not an approval, grant, or repository control selector.
This adapter does not grant source writes, issue approval, merge, release or G1/G2 autonomy.
The hosting execution environment owns actual GitHub permission checks and user intent.
"""
from __future__ import annotations

import base64
import binascii
import json
import re
import subprocess
from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parent.parent / "assets" / "control-policy.json"
REPO_RE = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
CONTRACT = "CONTROL_POLICY_V1"

def _valid_repo(repo: object) -> bool:
    """GitHub owner and repository are names, never filesystem path segments."""
    if not isinstance(repo, str) or REPO_RE.fullmatch(repo) is None:
        return False
    owner, name = repo.split("/", 1)
    return owner not in (".", "..") and name not in (".", "..") and not owner.startswith(".")


EXPECTED = {
    "contract": CONTRACT,
    "default_mode": "ISSUE_CONTROL",
    "unenrolled_mode": "FILE_CONTROL",
    "enrollment_authority": "GITHUB_VERIFIED_MERGED_MIGRATION",
    "approver_authority": "GITHUB_VERIFIED_ACCOUNT_AND_OWNER_POLICY",
    "web_issue_authoring": "EXPLICIT_USER_REQUEST_AND_HOST_WRITE",
    "delegated_approval": "DISABLED",
    "risk_scoped_autonomy": "DISABLED",
    "require_host_authority_for_writes": True,
    "project_agents_control_selectors": "IGNORED",
}


class ControlPolicyError(ValueError):
    pass


def load_policy() -> dict:
    """Only the shipped, versioned Skill artifact is the default rule source.

    Do not load an arbitrary project AGENTS.md, task Issue, local JSON file or
    untrusted PR-provided replacement as the global policy authority.
    """
    try:
        policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ControlPolicyError("GLOBAL_POLICY_UNAVAILABLE") from exc
    if type(policy) is not dict or policy != EXPECTED:
        raise ControlPolicyError("GLOBAL_POLICY_SCHEMA_OR_DEFAULTS_MISMATCH")
    return policy


def _gh_api(path: str) -> dict | list:
    """Live GitHub REST read via the authenticated local gh client; no shell."""
    try:
        result = subprocess.run(
            ["gh", "api", "--hostname", "github.com", path], capture_output=True, text=True,
            timeout=15, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ControlPolicyError("GITHUB_HOST_READ_UNAVAILABLE") from exc
    if result.returncode != 0:
        raise ControlPolicyError("GITHUB_HOST_READ_DENIED")
    try:
        obj = json.loads(result.stdout)
    except ValueError as exc:
        raise ControlPolicyError("GITHUB_HOST_INVALID_RESPONSE") from exc
    if not isinstance(obj, (dict, list)):
        raise ControlPolicyError("GITHUB_HOST_INVALID_RESPONSE")
    return obj


def verify_migration(repo: str, migration_pr: int) -> dict:
    """Host-verify a migration PR and that its merge commit belongs to live main.

    A PR number is merely a locator supplied through a global user routing
    preference; neither it nor project AGENTS.md is itself proof of adoption.
    """
    load_policy()
    if not _valid_repo(repo):
        raise ControlPolicyError("INVALID_REPOSITORY")
    if type(migration_pr) is not int or migration_pr < 1:
        raise ControlPolicyError("MIGRATION_PR_REQUIRED")
    pr = _gh_api(f"repos/{repo}/pulls/{migration_pr}")
    if not isinstance(pr, dict):
        raise ControlPolicyError("MIGRATION_NOT_HOST_VERIFIED")
    merge_sha = pr.get("merge_commit_sha")
    if (pr.get("merged_at") is None
            or not isinstance(merge_sha, str)
            or re.fullmatch(r"[0-9a-f]{40}", merge_sha) is None
            or (pr.get("base") or {}).get("ref") != "main"
            or (pr.get("head") or {}).get("repo") is None):
        raise ControlPolicyError("MIGRATION_NOT_HOST_VERIFIED")
    # A random merged PR is not a migration. Verify its explicit transition intent
    # and its changed files using the same live authenticated GitHub host.
    body = str(pr.get("body") or "")
    historical_intent = (
        "ISSUE_CONTROL" in body and "AGENTS.md" in body
        and ("migration" in body.lower() or "cutover" in body.lower())
    )
    if not (("EG_CONTROL_MIGRATION_V1" in body) or historical_intent):
        raise ControlPolicyError("PR_NOT_GOVERNANCE_MIGRATION")
    files = _gh_api(f"repos/{repo}/pulls/{migration_pr}/files?per_page=100&page=1")
    if (not isinstance(files, list) or not files or len(files) >= 100
            or not any(file.get("filename") == "AGENTS.md" for file in files
                       if isinstance(file, dict))):
        raise ControlPolicyError("MIGRATION_DIFF_NOT_VERIFIED")
    main = _gh_api(f"repos/{repo}/branches/main")
    if not isinstance(main, dict):
        raise ControlPolicyError("UNVERIFIED_MAIN_HEAD")
    main_sha = (main.get("commit") or {}).get("sha")
    if not isinstance(main_sha, str) or re.fullmatch(r"[0-9a-f]{40}", main_sha) is None:
        raise ControlPolicyError("UNVERIFIED_MAIN_HEAD")
    comparison = _gh_api(f"repos/{repo}/compare/{merge_sha}...{main_sha}")
    if not isinstance(comparison, dict) or comparison.get("status") not in ("identical", "ahead"):
        raise ControlPolicyError("MIGRATION_NOT_IN_MAIN_ANCESTRY")
    # The historical migration PR alone is insufficient: an older PR may
    # have *added* project-level control selectors. Require the current
    # accepted main AGENTS.md to be free of operative governance selectors.
    accepted = _gh_api(f"repos/{repo}/contents/AGENTS.md?ref={main_sha}")
    if (not isinstance(accepted, dict)
            or accepted.get("type") != "file" or accepted.get("encoding") != "base64"
            or not isinstance(accepted.get("content"), str)):
        raise ControlPolicyError("ACCEPTED_PROJECT_RULES_UNVERIFIED")
    try:
        blob = base64.b64decode(re.sub(r"\s+", "", accepted["content"]), validate=True)
        content = blob.decode("utf-8")
    except (ValueError, UnicodeDecodeError, binascii.Error):
        raise ControlPolicyError("ACCEPTED_PROJECT_RULES_UNVERIFIED")
    forbidden = ("CONTROL_MODE:", "ISSUE_APPROVERS:",
                 "ISSUE_DELEGATED_APPROVAL:", "ISSUE_WEB_SPEC_AUTHORING:",
                 "RISK_SCOPED_AUTONOMY:")
    if any(line.startswith(forbidden) for line in content.splitlines()):
        raise ControlPolicyError("PROJECT_CONTROL_SELECTORS_NOT_MIGRATED")
    return {
        "contract": CONTRACT,
        "repository": repo,
        "mode": "ISSUE_CONTROL",
        "adoption": "VERIFIED_MERGED_MIGRATION",
        "migration_pr": migration_pr,
        "migration_merge_sha": merge_sha,
        "main_sha": main_sha,
        "source": "LIVE_GITHUB_HOST",
        "execution_authorized": False,
    }


def verified_personal_repo_approvers(repo: str) -> set[str]:
    """Conservatively derive one trusted personal owner from live GitHub host.

    Organization repositories require an independently governed org approver
    policy and cannot be guessed from the current agent/token or markdown.
    """
    load_policy()
    if not _valid_repo(repo):
        raise ControlPolicyError("INVALID_REPOSITORY")
    info = _gh_api(f"repos/{repo}")
    if not isinstance(info, dict):
        raise ControlPolicyError("TRUSTED_APPROVER_HOST_POLICY_REQUIRED")
    owner = info.get("owner") or {}
    if (info.get("full_name") != repo or owner.get("type") != "User"
            or not isinstance(owner.get("login"), str)
            or owner["login"] != repo.split("/", 1)[0]):
        raise ControlPolicyError("TRUSTED_APPROVER_HOST_POLICY_REQUIRED")
    return {owner["login"]}


def select_control(repo: str, *, migration_pr: int | None = None) -> dict:
    """Read-only selector. Missing adoption never becomes implicit Issue authority."""
    load_policy()
    if not _valid_repo(repo):
        raise ControlPolicyError("INVALID_REPOSITORY")
    if migration_pr is None:
        return {
            "contract": CONTRACT, "repository": repo,
            "mode": "FILE_CONTROL", "adoption": "UNVERIFIED_LEGACY",
            "execution_authorized": False, "reason": "MIGRATION_HOST_PROOF_REQUIRED",
        }
    return verify_migration(repo, migration_pr)


def source_write_gate(selection: dict, *, user_requested: bool = False,
                      trusted_approvers: set[str] | None = None) -> None:
    """Refuse source writes on a mode selector alone; exact task approval required."""
    load_policy()
    if selection.get("adoption") != "VERIFIED_MERGED_MIGRATION":
        raise ControlPolicyError("MIGRATION_HOST_PROOF_REQUIRED")
    if not user_requested or not trusted_approvers:
        raise ControlPolicyError("EXACT_TASK_AUTHORIZATION_REQUIRED")
    # No success result: actual Issue digest, authenticated comment, credential
    # separation and target permissions are verified by their own host gates.
    raise ControlPolicyError("ISSUE_APPROVAL_HOST_PREFLIGHT_REQUIRED")


def web_authoring_eligible(*, explicit_user_request: bool,
                           verified_github_write: bool) -> bool:
    """Eligibility only, never issue/source approval or permission by itself."""
    load_policy()
    return explicit_user_request is True and verified_github_write is True


def delegated_enabled() -> bool:
    return load_policy()["delegated_approval"] == "ENABLED"


def autonomy_enabled() -> bool:
    return load_policy()["risk_scoped_autonomy"] == "ENABLED"

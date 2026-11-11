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
    # A PR body/title is mutable after merge and cannot prove a migration.
    # Require immutable GitHub source diff introducing the original mode
    # transition or removing one of the legacy AGENTS control selectors.
    # The accepted main must additionally be selector-free (verified below).
    files = _gh_api(f"repos/{repo}/pulls/{migration_pr}/files?per_page=100&page=1")
    if not isinstance(files, list) or len(files) >= 100:
        raise ControlPolicyError("MIGRATION_DIFF_NOT_VERIFIED")
    matching = [entry for entry in files if isinstance(entry, dict)
                and entry.get("filename") == "AGENTS.md"
                and entry.get("status") in ("modified", "added")]
    if len(matching) != 1 or not isinstance(matching[0].get("patch"), str):
        raise ControlPolicyError("MIGRATION_DIFF_NOT_VERIFIED")
    patch_lines = matching[0]["patch"].splitlines()
    legacy_added_issue_mode = any(
        line == "+CONTROL_MODE: ISSUE_CONTROL" for line in patch_lines)
    legacy_removed_control = any(
        line.startswith("-" + key)
        for key in ("CONTROL_MODE:", "ISSUE_APPROVERS:",
                    "ISSUE_WEB_SPEC_AUTHORING:", "ISSUE_DELEGATED_APPROVAL:",
                    "RISK_SCOPED_AUTONOMY:")
        for line in patch_lines
    )
    if not (legacy_added_issue_mode or legacy_removed_control):
        raise ControlPolicyError("PR_NOT_GOVERNANCE_MIGRATION")
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
                      trusted_approvers: set[str] | None = None,
                      authority_route: str = "ISSUE_BACKED") -> None:
    """Return a precise fail-closed host preflight for the selected task route.

    This portable source helper has NO trusted live USER-role or tool writer
    permission channel. It must not mint an authority from caller booleans.
    In particular, current-session G1/G2 does NOT require an Issue comment,
    but still needs the receiving HOST to authenticate that user's request.
    """
    load_policy()
    if not isinstance(selection, dict) or selection.get("adoption") != "VERIFIED_MERGED_MIGRATION":
        raise ControlPolicyError("MIGRATION_HOST_PROOF_REQUIRED")
    if authority_route == "CURRENT_USER_DIRECT_G1_G2":
        if user_requested is not True:
            raise ControlPolicyError("ACTIVE_USER_REQUEST_REQUIRED")
        # Never convert a caller boolean into host proof or source permissions.
        raise ControlPolicyError("DIRECT_USER_RUNTIME_HOST_AUTHORIZATION_REQUIRED")
    if authority_route != "ISSUE_BACKED":
        raise ControlPolicyError("UNTRUSTED_AUTHORITY_ROUTE")
    if user_requested is not True or not trusted_approvers:
        raise ControlPolicyError("EXACT_TASK_AUTHORIZATION_REQUIRED")
    # No success result: GitHub exact-spec approval and writer permission are
    # separate host-verifiable facts. Legacy Issue path stays fail-closed here.
    raise ControlPolicyError("ISSUE_APPROVAL_HOST_PREFLIGHT_REQUIRED")


# This helper classifies one *interactive* user-directed action. Caller-provided
# booleans, paths or risk labels cannot attest an authenticated user or host grant.
# Real source writes still require the current runtime's independent authorization.
SESSION_EFFECTS = frozenset({"source_edit", "focused_test", "task_branch_push", "draft_pr"})


def interactive_scope_eligibility(
    *, repo: str, risk: str, paths: list[str], effects: list[str],
    explicit_user_request: bool, active_session: bool,
    host_write_permission: bool, unattended: bool = False,
) -> dict:
    """Classify an interactive task; only the real host can authorize writes.

    The path list expresses scope, not a file-count risk score. Review actual
    effects and changed paths at the receiving host before each mutation.
    """
    load_policy()
    if not _valid_repo(repo):
        raise ControlPolicyError("INVALID_REPOSITORY")
    if risk not in ("G1", "G2"):
        raise ControlPolicyError("SESSION_SCOPE_RISK_NOT_ALLOWED")
    if unattended:
        raise ControlPolicyError("INDEPENDENT_PERSISTENT_GRANT_REQUIRED")
    if explicit_user_request is not True or active_session is not True:
        raise ControlPolicyError("ACTIVE_USER_REQUEST_REQUIRED")
    if host_write_permission is not True:
        raise ControlPolicyError("LIVE_HOST_WRITE_PERMISSION_REQUIRED")
    if (type(paths) is not list or not paths
            or not all(isinstance(path, str) for path in paths)
            or len(set(paths)) != len(paths)):
        raise ControlPolicyError("INVALID_SESSION_SCOPE_PATHS")
    for path in paths:
        if (not isinstance(path, str) or path.startswith("/") or "\\" in path
                or any(part in ("", ".", "..") or part.casefold() == ".git"
                       for part in path.split("/"))
                or any(ord(ch) < 32 or ord(ch) == 127 for ch in path)
                or "*" in path or "?" in path):
            raise ControlPolicyError("INVALID_SESSION_SCOPE_PATHS")
        normalized = path.casefold()  # macOS worktrees may be case-insensitive
        # Path identity is a scope hint, not proof of a privilege change.
        # Normal AGENTS/Skill Markdown edits are not automatically G3; protect
        # executable trust roots, packaging identity and host configuration.
        # Real changed paths and semantic effects are still reviewed by host.
        protected_exact = {
            "skills/project-governance/assets/control-policy.json",
            "skills/project-governance/scripts/control-policy.py",
            "skills/project-governance/scripts/issue-spec-check.py",
            "skills/project-governance/scripts/verification-plan.py",
        }
        if (normalized == "plugin.json"
                or normalized in protected_exact
                or normalized.startswith((".github/workflows/", ".agents/",
                                          ".codex-plugin/"))):
            raise ControlPolicyError("PROTECTED_AUTHORITY_PATH_REQUIRES_G3_PREFLIGHT")
    if (type(effects) is not list or not effects
            or not all(isinstance(effect, str) and effect in SESSION_EFFECTS
                       for effect in effects)
            or len(effects) != len(set(effects))):
        raise ControlPolicyError("INVALID_SESSION_EFFECTS")
    return {
        "contract": "INTERACTIVE_SCOPE_ELIGIBILITY_V1",
        "repository": repo, "risk": risk,
        "paths": list(paths), "effects": list(effects),
        "route": "ACTIVE_SESSION_USER_DIRECT",
        "per_wp_approval_comment_required": False,
        # A genuine top-level host USER turn supplies initial task intent.
        # This flag is eligibility metadata only; input flags are untrusted.
        "initial_issue_approval_required": False,
        "user_direct_request_is_initial_task_authority_candidate": True,
        "host_user_role_provenance_required": True,
        "host_action_authorization_required": True,
        "source_write_authorized": False,
        "persistent_grant": False,
        "merge_authorized": False, "release_authorized": False,
        "status": "ELIGIBLE_ONLY_HOST_PREFLIGHT_REQUIRED",
    }


def web_authoring_eligible(*, explicit_user_request: bool,
                           verified_github_write: bool) -> bool:
    """Eligibility only, never issue/source approval or permission by itself."""
    load_policy()
    return explicit_user_request is True and verified_github_write is True


def delegated_enabled() -> bool:
    return load_policy()["delegated_approval"] == "ENABLED"


def autonomy_enabled() -> bool:
    return load_policy()["risk_scoped_autonomy"] == "ENABLED"

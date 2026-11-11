#!/usr/bin/env python3
"""VERIFICATION_PLAN_V1: deterministic, fail-closed test selection.

Policy owner: project-governance/references/verification-tiers.md.
Production CI MUST execute this script from the trusted BASE revision,
not from the untrusted pull-request HEAD. This script never grants writes,
waives host gates, or claims that skipped tests passed.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CONTRACT = "VERIFICATION_PLAN_V1"
TIERS = ("V0", "V1", "V2", "V3")
SHA = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
SCRIPT = "skills/project-governance/scripts/verification-plan.py"

# Repository-specific dependency cues, not a substitute for semantic review.
# Markdown contracts get affected suites; executable trust/unknown owners are
# V3. Target projects own their actual test commands.
SCOPE = (
    ("documents/archive/", "V0", "historical descriptive document"),
    ("documents/historical/", "V0", "historical descriptive document"),
    ("README.md", "V1", "README is consumed by governance policy tests"),
    ("documents/notes/", "V1", "descriptive notes; targeted policy checks"),
    ("documents/", "V2", "durable design or unknown documentation owner"),
    # Normative Markdown requires affected behavioral contract tests, not a
    # full suite or package merely because its filename is sensitive.
    ("skills/project-governance/SKILL.md", "V2", "global governance entry and authorization"),
    ("skills/project-governance/references/issue-control.md", "V2", "Issue/approval authority contract"),
    ("skills/project-governance/references/issue-execution-contract.md", "V2", "risk and execution authority"),
    ("skills/project-governance/references/development-flow.md", "V2", "governed execution authorization"),
    ("skills/project-governance/references/global-routing.md", "V2", "global authority routing"),
    ("skills/project-governance/references/control-plane.md", "V2", "control owner and alignment"),
    ("skills/project-governance/references/issue-control-migration.md", "V2", "trusted enrollment boundary"),
    ("skills/project-governance/references/verification-tiers.md", "V2", "verification policy owner"),
    # Markdown routes to affected contracts. Executable trust and host wiring
    # still route to V3 with a broad test suite.
    ("skills/project-governance/references/artifact-lifecycle.md", "V2", "task authority lifecycle"),
    ("skills/project-governance/references/planning-documents.md", "V2", "task authorization in design"),
    ("skills/project-governance/references/workspace-lifecycle.md", "V2", "writer/workspace permission"),
    ("skills/project-governance/references/remote-delivery.md", "V2", "source write host gate"),
    ("skills/project-governance/references/control-identity.md", "V2", "accepted host authority"),
    ("skills/project-governance/references/adoption.md", "V2", "trusted CI enrollment"),
    ("skills/project-governance/assets/templates/EXECUTION_SPEC.md", "V2", "Issue-backed approval contract"),
    ("skills/agent-handoff/SKILL.md", "V2", "handoff authority semantics"),
    ("skills/agent-handoff/assets/templates/HANDOFF_REQUEST.md", "V2", "handoff authority locator"),
    ("skills/agent-handoff/assets/templates/HANDOFF_RECEIPT.md", "V2", "handoff authority receipt"),
    ("skills/execution-orchestrator/SKILL.md", "V2", "delegation writer authority"),
    ("skills/solution-design/SKILL.md", "V2", "design source authorization"),
    ("skills/solution-design/references/design-contract.md", "V2", "design reauthorization"),
    ("skills/incident-doctor/references/evidence-gate.md", "V2", "incident permission evidence"),
    ("skills/project-governance/scripts/", "V3", "authorization and verification source/tests"),
    ("skills/project-governance/assets/control-policy.json", "V3", "versioned global permission policy"),
    ("skills/project-governance/assets/templates/AGENTS.md", "V2", "project control boundary"),
    ("skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md", "V2", "global trusted routing"),
    ("skills/agent-handoff/references/handoff-contract.md", "V2", "handoff never grants authority"),
    (SCRIPT, "V3", "verification selector implementation"),
    ("skills/project-governance/scripts/test_verification_plan.py", "V3", "verification selector test"),
    ("AGENTS.md", "V2", "normative repository authorization"),
    (".github/ISSUE_TEMPLATE/", "V2", "execution-spec documentation and form shape"),
    (".github/", "V3", "workflow and trusted host interface"),
    ("skills/", "V2", "reusable Skill contracts or behavior"),
    ("references/", "V2", "shared engineering contracts"),
    ("plugin.json", "V3", "plugin manifest and release identity"),
    (".agents/", "V3", "plugin installation and marketplace authority"),
    (".codex-plugin/", "V3", "plugin installation manifest"),
)
ESCALATE = (".gitmodules", ".gitattributes", ".gitignore")

# Explicit V2 dependency map. Tests outside the list cannot be injected by
# a PR-supplied manifest, and the script itself is always selected from BASE.
V2_TEST_CROSS = "test_eg097_policy_contracts.py"
V2_TEST_CONTROL = "test_control_policy.py"
V2_TEST_ISSUE = "test_issue_spec_check.py"
V2_ALLOWED_TESTS = frozenset((V2_TEST_CROSS, V2_TEST_CONTROL, V2_TEST_ISSUE))


def affected_suites(changes: list[dict[str, str]]) -> list[str]:
    """Select cross-Skill contracts plus known dependent authority adapters.

    This is a repository-specific contract map, NOT a substitute for consumer
    product/runtime tests. Unknown source owners escalate to V3 elsewhere.
    """
    tests = {V2_TEST_CROSS}
    for entry in changes:
        for path in (entry["path"], entry.get("previous_path")):
            if not path:
                continue
            if (path.startswith(("skills/agent-handoff/",
                                  "skills/execution-orchestrator/",
                                  "skills/solution-design/",
                                  "skills/incident-doctor/"))
                    or path == "skills/project-governance/SKILL.md"
                    or path == "AGENTS.md"
                    or path.startswith("skills/project-governance/assets/templates/")
                    or path.startswith(".github/ISSUE_TEMPLATE/")):
                tests.add(V2_TEST_ISSUE)
                tests.add(V2_TEST_CONTROL)
            if path.startswith("skills/project-governance/references/"):
                tests.add(V2_TEST_ISSUE)
                tests.add(V2_TEST_CONTROL)
    if not tests.issubset(V2_ALLOWED_TESTS):
        raise SelectionError("UNMAPPED_AFFECTED_TEST_SUITE")
    return sorted(tests)


class SelectionError(ValueError):
    pass


def safe_path(path: str) -> bool:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return False
    parts = path.split("/")
    return (all(part not in ("", ".", "..") and part.casefold() != ".git" for part in parts)
            and all(ord(ch) >= 32 and ord(ch) != 127 for ch in path))


def classify(path: str) -> tuple[str, str]:
    if not safe_path(path):
        raise SelectionError("INVALID_CHANGE_PATH")
    if path in ESCALATE:
        return "V3", "repository metadata affects trusted diff"
    # Exact filenames must not accidentally match longer prefix paths.
    for prefix, tier, reason in SCOPE:
        if path == prefix or (prefix.endswith("/") and path.startswith(prefix)):
            if prefix == "skills/" and not path.endswith((".md", ".txt")):
                return "V3", "unmapped Skill code or structured asset"
            if (prefix == ".github/ISSUE_TEMPLATE/"
                    and not path.endswith((".md", ".yml", ".yaml"))):
                return "V3", "unmapped executable in Issue template directory"
            return tier, reason
    return "V3", "unknown dependency or file owner"


def parse_name_status_z(data: bytes) -> list[dict[str, str]]:
    """Parse --name-status -z, including BOTH sides of renames and copies."""
    if not data or data[-1:] != b"\0":
        raise SelectionError("EMPTY_OR_TRUNCATED_DIFF")
    try:
        tokens = [s.decode("utf-8", errors="strict") for s in data[:-1].split(b"\0")]
    except UnicodeError as exc:
        raise SelectionError("INVALID_DIFF_ENCODING") from exc
    changes: list[dict[str, str]] = []
    cursor = 0
    while cursor < len(tokens):
        status = tokens[cursor]
        cursor += 1
        if not re.fullmatch(r"(?:[AMDTUXB]|[RC][0-9]{1,3})", status):
            raise SelectionError("UNSUPPORTED_DIFF_STATUS")
        count = 2 if status[0] in "RC" else 1
        if cursor + count > len(tokens):
            raise SelectionError("TRUNCATED_DIFF_RECORD")
        paths = tokens[cursor:cursor + count]
        cursor += count
        if not all(safe_path(p) for p in paths):
            raise SelectionError("INVALID_CHANGE_PATH")
        if count == 2 and paths[0] == paths[1]:
            raise SelectionError("INVALID_RENAME_RECORD")
        entry = {"status": status, "path": paths[-1]}
        if count == 2:
            entry["previous_path"] = paths[0]
        changes.append(entry)
    if not changes:
        raise SelectionError("EMPTY_DIFF_RECORDS")
    return changes


def run_git(repo: Path, *args: str) -> bytes:
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args],
                                       stderr=subprocess.PIPE, timeout=30)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            FileNotFoundError) as exc:
        raise SelectionError("UNVERIFIED_GIT_EVIDENCE") from exc


def select(changes: list[dict[str, str]], *, base: str, head: str,
           symlink_paths: frozenset[str] = frozenset()) -> dict:
    if not SHA.fullmatch(base) or not SHA.fullmatch(head) or base == head:
        raise SelectionError("INVALID_SOURCE_IDENTITY")
    if not changes:
        raise SelectionError("NO_CHANGE_EVIDENCE")
    highest = 0
    reasons = []
    for entry in changes:
        status = entry["status"]
        if not re.fullmatch(r"(?:[AMDTUXB]|[RC][0-9]{1,3})", status):
            raise SelectionError("INVALID_STATUS")
        paths = [entry["path"]]
        if "previous_path" in entry:
            paths.append(entry["previous_path"])
        for path in paths:
            tier, why = classify(path)
            if path in symlink_paths or status[0] in "UXB":
                tier, why = "V3", "symlink/gitlink or unknown merge/conflict state"
            highest = max(highest, TIERS.index(tier))
            reasons.append({"path": path, "tier": tier, "reason": why})
    tier = TIERS[highest]
    # A PASS for a selector is not a PASS for the omitted tests.
    suites = affected_suites(changes) if tier == "V2" else []
    selected = ["static_scope"]
    skipped = []
    if tier == "V0":
        skipped = ["policy_contracts", "full_contracts", "package_preview"]
    elif tier == "V1":
        selected.append("policy_contracts")
        skipped = ["affected_contracts", "full_contracts", "package_preview"]
    elif tier == "V2":
        # Integrate the affected cross-Skill behavior without the entire
        # security regression or a release artifact on every ordinary edit.
        selected.append("affected_contracts")
        skipped = ["policy_contracts_separate", "full_contracts", "package_preview"]
    else:
        selected.append("full_contracts")
        skipped = ["policy_contracts_separate", "affected_contracts_separate",
                   "package_preview"]
    return {
        "contract": CONTRACT, "base": base, "head": head,
        "tier": tier, "changes": changes, "reasons": reasons,
        "selected": selected, "skipped": skipped,
        "affected_suites": suites, "affected_coverage": "CROSS_SKILL_CONTRACTS_ONLY",
        "scope_status": "SCOPE_GATE_PASS",
        "test_status": "TESTS_PENDING",
        "policy_source": "TRUSTED_BASE",
        "full_suite_claim": False,
    }


def collect(repo: Path, base: str, head: str) -> dict:
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        raise SelectionError("INVALID_SOURCE_IDENTITY")
    if run_git(repo, "rev-parse", "--verify", base + "^{commit}").decode().strip() != base:
        raise SelectionError("BASE_SHA_MISMATCH")
    if run_git(repo, "rev-parse", "--verify", head + "^{commit}").decode().strip() != head:
        raise SelectionError("HEAD_SHA_MISMATCH")
    data = run_git(repo, "diff", "--name-status", "-z", "--find-renames",
                   "--no-ext-diff", base, head)
    changes = parse_name_status_z(data)
    # Include BASE to catch deletion/rename of unsafe links, not just links at HEAD.
    symlinks: set[str] = set()
    for revision in (base, head):
        mode_data = run_git(repo, "ls-tree", "-r", "-z", revision)
        for record in mode_data.split(b"\0"):
            if not record:
                continue
            try:
                meta, path = record.split(b"\t", 1)
                if meta.startswith((b"120000 ", b"160000 ")):
                    symlinks.add(path.decode("utf-8", errors="strict"))
            except (UnicodeError, ValueError) as exc:
                raise SelectionError("INVALID_TREE_DATA") from exc
    return select(changes, base=base, head=head, symlink_paths=frozenset(symlinks))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", type=Path, required=True)
    p.add_argument("--base", required=True)
    p.add_argument("--head", required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--github-output", type=Path)
    args = p.parse_args()
    try:
        plan = collect(args.repo_root, args.base, args.head)
        args.output.write_text(json.dumps(plan, sort_keys=True, indent=2) + "\n",
                               encoding="utf-8")
        if args.github_output:
            flags = {
                "tier": plan["tier"],
                "run_policy": str("policy_contracts" in plan["selected"]).lower(),
                "run_affected": str("affected_contracts" in plan["selected"]).lower(),
                "run_full": str("full_contracts" in plan["selected"]).lower(),
                "run_package": str("package_preview" in plan["selected"]).lower(),
                "scope_status": plan["scope_status"],
            }
            with args.github_output.open("a", encoding="utf-8") as output:
                for key, value in flags.items():
                    output.write(f"{key}={value}\n")
        print(json.dumps(plan, sort_keys=True))
        return 0
    except (SelectionError, OSError) as exc:
        print("VERIFICATION_PLAN_STOP: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

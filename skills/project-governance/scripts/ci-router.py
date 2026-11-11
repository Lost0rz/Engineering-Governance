#!/usr/bin/env python3
"""Portable CI router. Plan by default; run only when explicitly requested."""
import argparse
import hashlib
import json
import re
import shlex
import subprocess
import sys
import unicodedata
from pathlib import Path

CONTRACT = "EG_CI_CAPABILITIES_V1"
PLAN = "EG_CI_PLAN_V1"
SHA = re.compile(r"[0-9a-f]{40,64}\Z")
ID = re.compile(r"[a-z][a-z0-9_-]{0,47}\Z")
STAGES = ("draft", "focused", "milestone", "ready", "release", "none")


class RouteError(ValueError):
    pass


def safe_path(s):
    """Accept Unicode, reject traversal and control characters."""
    return (isinstance(s, str) and 0 < len(s) <= 2048 and not s.startswith("/")
            and "\\" not in s
            and all(p not in ("", ".", "..") and p.casefold() != ".git" for p in s.split("/"))
            and all(not unicodedata.category(c).startswith("C") for c in s))


DOC_SUFFIXES = (".md", ".markdown", ".rst", ".txt", ".adoc")
ROOT_DOCS = {"readme.md", "changelog.md", "contributing.md", "license",
             "license.md", "authors.md", "code_of_conduct.md"}


def descriptive_doc(path):
    name = path.rsplit("/", 1)[-1].lower()
    return name in ROOT_DOCS or name.endswith(DOC_SUFFIXES)


def validate_doc_pattern(pattern):
    if (pattern in ("**", "*") or pattern.startswith("**/")
            or ("/" not in pattern and ("*" in pattern or "?" in pattern))):
        raise RouteError("OVERBROAD_DOCUMENTATION_PATTERN")
    match(pattern, "docs/example.md")


def git(repo, *args):
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RouteError("GIT_SOURCE_UNAVAILABLE") from exc


def changes(repo, base, head, include_worktree=False):
    """Include actual local edits only when explicitly requested by the host."""
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        raise RouteError("INVALID_REF")
    for rev in (base, head):
        if git(repo, "cat-file", "-t", rev).strip() != b"commit":
            raise RouteError("INVALID_COMMIT")
    if include_worktree and git(repo, "rev-parse", "HEAD").decode().strip() != head:
        raise RouteError("WORKTREE_HEAD_MISMATCH")

    records = []
    if base != head:
        records.append(git(repo, "diff", "--name-status", "-z", "-M", base + "..." + head))
    if include_worktree:
        records.append(git(repo, "diff", "--name-status", "-z", "-M", "--cached"))
        records.append(git(repo, "diff", "--name-status", "-z", "-M"))

    paths = []
    for data in records:
        if data and not data.endswith(b"\0"):
            raise RouteError("TRUNCATED_DIFF")
        try:
            fields = [v.decode("utf-8") for v in data[:-1].split(b"\0")] if data else []
        except UnicodeError as exc:
            raise RouteError("INVALID_PATH_ENCODING") from exc
        i = 0
        while i < len(fields):
            status = fields[i]
            i += 1
            if not re.fullmatch(r"(?:[AMDTUXB]|[RC][0-9]{1,3})", status):
                raise RouteError("INVALID_DIFF_STATUS")
            count = 2 if status[0] in "RC" else 1
            if i + count > len(fields):
                raise RouteError("TRUNCATED_DIFF")
            for name in fields[i:i + count]:
                if not safe_path(name):
                    raise RouteError("UNSAFE_PATH")
                paths.append(name)
            i += count

    if include_worktree:
        data = git(repo, "ls-files", "--others", "--exclude-standard", "-z")
        try:
            unseen = [p.decode("utf-8") for p in data.split(b"\0") if p]
        except UnicodeError as exc:
            raise RouteError("INVALID_PATH_ENCODING") from exc
        if any(not safe_path(p) for p in unseen):
            raise RouteError("UNSAFE_UNTRACKED_PATH")
        paths.extend(unseen)
    return sorted(set(paths))


def match(pattern, path):
    if not safe_path(pattern) or "[" in pattern or "]" in pattern:
        raise RouteError("UNSUPPORTED_GLOB")
    if pattern == "**":
        return True
    i, parts = 0, ["^"]
    while i < len(pattern):
        if pattern.startswith("**/", i):
            parts.append("(?:.*/)?")
            i += 3
        elif pattern.startswith("**", i):
            parts.append(".*")
            i += 2
        elif pattern[i] == "*":
            parts.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            parts.append("[^/]")
            i += 1
        else:
            parts.append(re.escape(pattern[i]))
            i += 1
    return bool(re.match("".join(parts) + "$", path))


def arguments(seq):
    if (not isinstance(seq, list) or not 1 <= len(seq) <= 40
            or any(not isinstance(x, str) or not x or len(x) > 1024
                   or any(ord(c) < 32 or ord(c) == 127 for c in x) for x in seq)):
        raise RouteError("INVALID_COMMAND_ARGUMENTS")
    return seq


def validate(config):
    if not isinstance(config, dict) or config.get("contract") != CONTRACT:
        raise RouteError("INVALID_CAPABILITIES_CONTRACT")
    tests = config.get("tests")
    if not isinstance(tests, list) or not 1 <= len(tests) <= 48:
        raise RouteError("INVALID_TEST_CATALOG")
    names = set()
    by_id = {}
    for t in tests:
        if not isinstance(t, dict):
            raise RouteError("INVALID_TEST_ENTRY")
        name = t.get("id")
        if not isinstance(name, str) or not ID.fullmatch(name) or name in names:
            raise RouteError("DUPLICATE_OR_INVALID_TEST_ID")
        names.add(name)
        by_id[name] = t
        if t.get("tier") not in ("V1", "V2", "V3"):
            raise RouteError("INVALID_TEST_TIER")
        if type(t.get("fork_safe", False)) is not bool:
            raise RouteError("INVALID_FORK_SAFE")
        if t.get("fork_safe", False):
            # Untrusted PR code must not be sent to persistent self-hosted runners.
            runner = t.get("runner", [])
            if (not isinstance(runner, list) or len(runner) != 1
                    or not isinstance(runner[0], str)
                    or not re.fullmatch(r"(?:ubuntu|windows|macos)-(?:latest|[0-9]{2}\.[0-9]{2}(?:-[a-z0-9]+)?)", runner[0])):
                raise RouteError("FORK_SAFE_REQUIRES_GITHUB_HOSTED_RUNNER")
        runner = t.get("runner")
        if (not isinstance(runner, list) or not 1 <= len(runner) <= 8
                or any(not isinstance(s, str) or not re.fullmatch(r"[\w.:-]{1,90}", s)
                       for s in runner)):
            raise RouteError("INVALID_RUNNER")
        if t.get("cwd", ".") != "." and not safe_path(t.get("cwd")):
            raise RouteError("INVALID_CWD")
        minutes = t.get("timeout_minutes", 20)
        if type(minutes) is not int or not 1 <= minutes <= 120:
            raise RouteError("INVALID_TIMEOUT")
        arguments(t.get("command"))
        setup = t.get("setup", [])
        if not isinstance(setup, list) or len(setup) > 12:
            raise RouteError("INVALID_SETUP")
        for args in setup:
            arguments(args)
        pats = t.get("paths")
        if not isinstance(pats, list) or not pats:
            raise RouteError("MISSING_PATHS")
        for pattern in pats:
            match(pattern, "example.py")
    docs = config.get("documentation_paths", [])
    if not isinstance(docs, list):
        raise RouteError("INVALID_DOCUMENTATION_PATHS")
    for pattern in docs:
        validate_doc_pattern(pattern)
    # A domain/integration test may declare its prerequisite test lanes.
    for t in tests:
        required = t.get("requires", [])
        if (not isinstance(required, list)
                or any(not isinstance(name, str) for name in required)
                or len(set(required)) != len(required)
                or any(name not in by_id or name == t["id"] for name in required)):
            raise RouteError("INVALID_TEST_DEPENDENCIES")
        for name in required:
            if int(by_id[name]["tier"][1]) > int(t["tier"][1]):
                raise RouteError("DEPENDENCY_TIER_ORDER")
    def visit(name, active, done):
        if name in active:
            raise RouteError("CYCLIC_TEST_DEPENDENCIES")
        if name in done:
            return
        active.add(name)
        for dep in by_id[name].get("requires", []):
            visit(dep, active, done)
        active.remove(name)
        done.add(name)
    done = set()
    for name in names:
        visit(name, set(), done)
    if type(config.get("fallback_satisfies_ready", False)) is not bool:
        raise RouteError("INVALID_FALLBACK_COVERAGE_POLICY")
    fallback = config.get("fallback_tests", [])
    if config.get("fallback_satisfies_ready") and not fallback:
        raise RouteError("FALLBACK_COVERAGE_WITHOUT_TESTS")
    if (not isinstance(fallback, list)
            or any(not isinstance(name, str) for name in fallback)
            or len(set(fallback)) != len(fallback)
            or any(name not in names for name in fallback)):
        raise RouteError("INVALID_FALLBACK")
    return config


def load(repo, base, path, source):
    if not safe_path(path):
        raise RouteError("INVALID_CONFIG_PATH")
    raw = git(repo, "show", base + ":" + path) if source == "base" else (repo / path).read_bytes()
    if len(raw) > 256000:
        raise RouteError("CONFIG_TOO_LARGE")
    try:
        return validate(json.loads(raw)), hashlib.sha256(raw).hexdigest()
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise RouteError("INVALID_CONFIG_JSON") from exc


def shell(t):
    lines = ["set -euo pipefail", 'workspace_root="$(pwd -P)"']
    if t.get("cwd", ".") != ".":
        lines.append("cd -- " + shlex.quote(t["cwd"]))
        lines.append('case "$(pwd -P)/" in "$workspace_root/"*) ;; '
                     '*) echo "CI_CWD_OUTSIDE_WORKSPACE" >&2; exit 2;; esac')
    for argv in t.get("setup", []) + [t["command"]]:
        lines.append(shlex.join(argv))
    return "\n".join(lines)


def select(config, changed, stage, base, head, digest, focused="",
           config_path=".github/ci-capabilities.json", source_trust="internal"):
    validate(config)
    if stage not in STAGES:
        raise RouteError("INVALID_STAGE")
    if source_trust not in ("internal", "fork"):
        raise RouteError("INVALID_SOURCE_TRUST")
    by_id = {t["id"]: t for t in config["tests"]}
    if stage == "focused" and focused not in by_id:
        raise RouteError("UNKNOWN_FOCUSED_TEST")
    unknown = []
    if stage in ("draft", "none"):
        selected = []
    elif stage == "focused":
        selected = [by_id[focused]]
    elif stage == "release":
        selected = config["tests"][:]
    else:
        hits = {t["id"] for t in config["tests"]
                if any(match(pat, path) for pat in t["paths"] for path in changed)}
        unknown = [path for path in changed if path != config_path
                   and not any(match(pat, path) for t in config["tests"] for pat in t["paths"])
                   and not (descriptive_doc(path) and any(
                       match(pat, path) for pat in config.get("documentation_paths", [])))]
        if unknown:
            hits.update(config.get("fallback_tests", []))
        selected = [t for t in config["tests"] if t["id"] in hits]
    ids = {t["id"] for t in selected}
    by_id = {t["id"]: t for t in config["tests"]}
    def include_dependencies(name):
        for dependency in by_id[name].get("requires", []):
            if dependency not in ids:
                ids.add(dependency)
                include_dependencies(dependency)
    for item in list(ids):
        include_dependencies(item)
    selected = [t for t in config["tests"] if t["id"] in ids]
    fork_blocked = []
    if source_trust == "fork":
        candidate_ids = {t["id"] for t in selected}
        safe_ids = set()
        for t in selected:
            if t.get("fork_safe", False) and all(
                    dep in safe_ids for dep in t.get("requires", [])):
                safe_ids.add(t["id"])
        fork_blocked = sorted(candidate_ids - safe_ids)
        selected = [t for t in selected if t["id"] in safe_ids]
    matrix = [{"id": t["id"], "runner": t["runner"], "script": shell(t),
               "tier": t["tier"], "timeout_minutes": t.get("timeout_minutes", 20)}
              for t in selected]
    if len(json.dumps({"include": matrix}, separators=(",", ":"))) > 180000:
        raise RouteError("TEST_MATRIX_TOO_LARGE")
    config_changed = config_path in changed
    coverage = ("DEFERRED" if stage in ("draft", "none") else
                "FORK_PARTIAL" if fork_blocked else
                "FOCUSED_ONLY" if stage == "focused" else
                "FALLBACK_COVERED" if unknown and config.get("fallback_satisfies_ready", False) else
                "PARTIAL_UNMAPPED" if unknown else
                "BASELINE_CAPABILITIES_USED" if config_changed and stage == "ready" else
                "NO_TESTS_REQUIRED" if not matrix else "SELECTED_PENDING")
    return {"contract": PLAN, "base": base, "head": head, "stage": stage,
            "config_sha256": digest, "changed_paths": changed,
            "selected_test_ids": [t["id"] for t in selected],
            "unmapped_paths": unknown, "coverage": coverage,
            # A fallback can prove readiness only if the accepted catalog
            # explicitly declares it sufficient for unknown paths.
            "review_required": (stage == "ready" and
                                (bool(fork_blocked) or
                                 (bool(unknown) and not config.get("fallback_satisfies_ready", False)))),
            "fork_blocked_tests": fork_blocked,
            "source_trust": source_trust,
            "capabilities_changed": config_changed,
            "effective_tier": max((t["tier"] for t in selected), default="V0"),
            "run_tests": bool(matrix), "test_status": "NOT_RUN",
            "full_suite_claim": False, "matrix": {"include": matrix},
            "config_source": "ACCEPTED_BASE" if base != "LOCAL" else "LOCAL_FILE"}


def discover(repo):
    # Scan tracked paths, not the full filesystem: node_modules and model
    # caches can be enormous on a developer workstation.
    raw = git(repo, "ls-files", "-z")
    tracked = [p.decode("utf-8", "replace") for p in raw.split(b"\0") if p]
    candidates = [("Package.swift", "Swift"), ("package.json", "Node"),
                  ("pyproject.toml", "Python")]
    languages = [label for file, label in candidates
                 if any(p == file or p.endswith("/" + file) for p in tracked)]
    return {"detected": sorted(set(languages)), "action":
            "Review actual test commands and runner labels; commit accepted .github/ci-capabilities.json"}


def execute_local(result, config, repo):
    """Explicit local execution only; plan mode never runs commands."""
    selected = set(result["selected_test_ids"])
    outcomes = []
    for test in config["tests"]:
        if test["id"] not in selected:
            continue
        workdir = (repo / test.get("cwd", ".")).resolve()
        if not workdir.is_relative_to(repo.resolve()):
            outcomes.append({"id": test["id"], "outcome": "CWD_OUTSIDE_WORKSPACE",
                             "exit_code": 2})
            break
        code = 0
        detail = "PASS"
        for argv in test.get("setup", []) + [test["command"]]:
            try:
                p = subprocess.run(argv, cwd=workdir, stdout=sys.stderr,
                                   stderr=sys.stderr,
                                   timeout=test.get("timeout_minutes", 20) * 60,
                                   check=False)
                code = p.returncode
            except subprocess.TimeoutExpired:
                code, detail = 124, "TIMEOUT"
            except OSError:
                code, detail = 127, "COMMAND_UNAVAILABLE"
            if code:
                if detail == "PASS":
                    detail = "FAILED"
                break
        outcomes.append({"id": test["id"], "outcome": detail, "exit_code": code})
        if code:
            break
    result["executed_tests"] = outcomes
    if any(item["exit_code"] for item in outcomes):
        result["test_status"] = "FAILED"
        return 1
    if result["review_required"]:
        result["test_status"] = "PARTIAL_REVIEW_REQUIRED"
        return 3
    result["test_status"] = "PASS" if outcomes else "NOT_RUN"
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=("plan", "discover", "run"))
    p.add_argument("--repo-root", type=Path, required=True)
    p.add_argument("--base", default="")
    p.add_argument("--head", default="")
    p.add_argument("--config-path", default=".github/ci-capabilities.json")
    p.add_argument("--config-source", choices=("base", "file"), default="base")
    p.add_argument("--stage", choices=STAGES, default="ready")
    p.add_argument("--worktree", action="store_true", help="Include staged, unstaged and untracked changes in local mode")
    p.add_argument("--source-trust", choices=("internal", "fork"), default="internal")
    p.add_argument("--focused", default="")
    p.add_argument("--output", type=Path)
    p.add_argument("--github-output", type=Path)
    args = p.parse_args()
    exit_code = 0
    try:
        if args.mode == "discover":
            result = discover(args.repo_root)
        else:
            if args.worktree and args.github_output:
                raise RouteError("WORKTREE_NOT_ALLOWED_IN_GITHUB")
            changed = changes(args.repo_root, args.base, args.head, include_worktree=args.worktree)
            if args.mode == "run" and args.config_source != "base":
                raise RouteError("LOCAL_EXECUTION_REQUIRES_ACCEPTED_BASE")
            cfg, digest = load(args.repo_root, args.base, args.config_path, args.config_source)
            result = select(cfg, changed, args.stage,
                            args.base if args.config_source == "base" else "LOCAL",
                            args.head, digest, args.focused, args.config_path,
                            args.source_trust)
            if args.config_source == "base" and args.config_path in changed:
                # Inspect PR config as data only. Never use its commands or runner
                # labels to build an executable matrix before it becomes base.
                proposed, proposed_digest = load(
                    args.repo_root, args.head, args.config_path, "base")
                result["proposed_catalog_status"] = "VALIDATED_NOT_EXECUTED"
                result["proposed_config_sha256"] = proposed_digest
            if args.mode == "run":
                exit_code = execute_local(result, cfg, args.repo_root)
        if args.output:
            args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        if args.github_output and args.mode == "plan":
            with args.github_output.open("a") as out:
                values = {"matrix": json.dumps(result["matrix"], separators=(",", ":")),
                          "run_tests": str(result["run_tests"]).lower(),
                          "review_required": str(result["review_required"]).lower(),
                          "coverage": result["coverage"],
                          "selected": ",".join(result["selected_test_ids"]),
                          "stage": result["stage"],
                          "capabilities_changed": str(result["capabilities_changed"]).lower()}
                for key, value in values.items():
                    out.write(key + "=" + value + "\n")
        print(json.dumps(result, sort_keys=True))
        return exit_code
    except (RouteError, OSError) as exc:
        print("EG_CI_ROUTE_FAILED: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

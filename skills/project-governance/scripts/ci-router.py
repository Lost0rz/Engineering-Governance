#!/usr/bin/env python3
"""Portable CI router. Plan only: does not execute tests or grant permissions."""
import argparse
import hashlib
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

CONTRACT = "EG_CI_CAPABILITIES_V1"
PLAN = "EG_CI_PLAN_V1"
SHA = re.compile(r"[0-9a-f]{40,64}\Z")
ID = re.compile(r"[a-z][a-z0-9_-]{0,47}\Z")
STAGES = ("draft", "focused", "milestone", "ready", "release", "none")


class RouteError(ValueError):
    pass


def safe_path(s):
    return (isinstance(s, str) and bool(s) and not s.startswith("/")
            and "\\" not in s and all(p not in ("", ".", "..") for p in s.split("/"))
            and all(32 <= ord(c) < 127 for c in s))


def git(repo, *args):
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RouteError("GIT_SOURCE_UNAVAILABLE") from exc


def changes(repo, base, head):
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        raise RouteError("INVALID_REF")
    for rev in (base, head):
        if git(repo, "cat-file", "-t", rev).strip() != b"commit":
            raise RouteError("INVALID_COMMIT")
    if base == head:
        return []
    data = git(repo, "diff", "--name-status", "-z", "-M", base + "..." + head)
    if data and not data.endswith(b"\0"):
        raise RouteError("TRUNCATED_DIFF")
    try:
        fields = [v.decode("utf-8") for v in data[:-1].split(b"\0")] if data else []
    except UnicodeError as exc:
        raise RouteError("INVALID_PATH_ENCODING") from exc
    paths, i = [], 0
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
    for t in tests:
        if not isinstance(t, dict):
            raise RouteError("INVALID_TEST_ENTRY")
        name = t.get("id")
        if not isinstance(name, str) or not ID.fullmatch(name) or name in names:
            raise RouteError("DUPLICATE_OR_INVALID_TEST_ID")
        names.add(name)
        if t.get("tier") not in ("V1", "V2", "V3"):
            raise RouteError("INVALID_TEST_TIER")
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
        match(pattern, "example.md")
    fallback = config.get("fallback_tests", [])
    if (not isinstance(fallback, list) or len(set(fallback)) != len(fallback)
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
    lines = ["set -euo pipefail"]
    if t.get("cwd", ".") != ".":
        lines.append("cd " + shlex.quote(t["cwd"]))
    for argv in t.get("setup", []) + [t["command"]]:
        lines.append(shlex.join(argv))
    return "\n".join(lines)


def select(config, changed, stage, base, head, digest, focused="",
           config_path=".github/ci-capabilities.json"):
    validate(config)
    if stage not in STAGES:
        raise RouteError("INVALID_STAGE")
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
        unknown = [path for path in changed
                   if not any(match(pat, path) for t in config["tests"] for pat in t["paths"])
                   and not any(match(pat, path) for pat in config.get("documentation_paths", []))]
        if unknown:
            hits.update(config.get("fallback_tests", []))
        selected = [t for t in config["tests"] if t["id"] in hits]
    matrix = [{"id": t["id"], "runner": t["runner"], "script": shell(t),
               "tier": t["tier"], "timeout_minutes": t.get("timeout_minutes", 20)}
              for t in selected]
    config_changed = config_path in changed
    coverage = ("DEFERRED" if stage in ("draft", "none") else
                "FOCUSED_ONLY" if stage == "focused" else
                "CAPABILITIES_CHANGE_REVIEW" if config_changed and stage == "ready" else
                "PARTIAL_UNMAPPED" if unknown else
                "NO_TESTS_REQUIRED" if not matrix else "SELECTED_PENDING")
    return {"contract": PLAN, "base": base, "head": head, "stage": stage,
            "config_sha256": digest, "changed_paths": changed,
            "selected_test_ids": [t["id"] for t in selected],
            "unmapped_paths": unknown, "coverage": coverage,
            "review_required": stage == "ready" and bool(unknown or config_changed),
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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=("plan", "discover"))
    p.add_argument("--repo-root", type=Path, required=True)
    p.add_argument("--base", default="")
    p.add_argument("--head", default="")
    p.add_argument("--config-path", default=".github/ci-capabilities.json")
    p.add_argument("--config-source", choices=("base", "file"), default="base")
    p.add_argument("--stage", choices=STAGES, default="ready")
    p.add_argument("--focused", default="")
    p.add_argument("--output", type=Path)
    p.add_argument("--github-output", type=Path)
    args = p.parse_args()
    try:
        if args.mode == "discover":
            result = discover(args.repo_root)
        else:
            changed = changes(args.repo_root, args.base, args.head)
            cfg, digest = load(args.repo_root, args.base, args.config_path, args.config_source)
            result = select(cfg, changed, args.stage,
                            args.base if args.config_source == "base" else "LOCAL",
                            args.head, digest, args.focused, args.config_path)
        if args.output:
            args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        if args.github_output and args.mode == "plan":
            with args.github_output.open("a") as out:
                values = {"matrix": json.dumps(result["matrix"], separators=(",", ":")),
                          "run_tests": str(result["run_tests"]).lower(),
                          "review_required": str(result["review_required"]).lower(),
                          "coverage": result["coverage"],
                          "selected": ",".join(result["selected_test_ids"])}
                for key, value in values.items():
                    out.write(key + "=" + value + "\n")
        print(json.dumps(result, sort_keys=True))
        return 0
    except (RouteError, OSError) as exc:
        print("EG_CI_ROUTE_FAILED: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Portable CI router. Plan by default; run only when explicitly requested."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import shlex
import stat
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

CONTRACT = "EG_CI_CAPABILITIES_V1"
PLAN = "EG_CI_PLAN_V1"
SHA = re.compile(r"[0-9a-f]{40,64}\Z")
ID = re.compile(r"[a-z][a-z0-9_-]{0,47}\Z")
STAGES = ("draft", "focused", "milestone", "ready", "release", "none")
VALID_LANE_STAGES = ("milestone", "ready", "release")
TIER_ORDER = {"V1": 1, "V2": 2, "V3": 3}


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
    if include_worktree:
        compare_ref = git(repo, "merge-base", base, head).decode().strip() if base != head else base
        records.append(git(repo, "diff", "--name-status", "-z", "-M", compare_ref))
    elif base != head:
        records.append(git(repo, "diff", "--name-status", "-z", "-M", base + "..." + head))

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


def nonregular_changes(repo, base, head, include_worktree=False):
    """Identify special Git modes; a symlink named *.md is not ordinary prose."""
    commands = []
    if include_worktree:
        compare_ref = git(repo, "merge-base", base, head).decode().strip() if base != head else base
        commands.append(("diff", "--raw", "-z", "-M", compare_ref))
    elif base != head:
        commands.append(("diff", "--raw", "-z", "-M", base + "..." + head))
    special = set()
    for command in commands:
        raw = git(repo, *command)
        if raw and not raw.endswith(b"\0"):
            raise RouteError("TRUNCATED_RAW_DIFF")
        fields = raw[:-1].split(b"\0") if raw else []
        i = 0
        while i < len(fields):
            try:
                record = fields[i].decode("ascii")
            except UnicodeError as exc:
                raise RouteError("INVALID_RAW_DIFF") from exc
            i += 1
            parts = record.split(" ")
            if len(parts) != 5 or not parts[0].startswith(":"):
                raise RouteError("INVALID_RAW_DIFF")
            old_mode, new_mode = parts[0][1:], parts[1]
            status = parts[4]
            if not re.fullmatch(r"(?:[AMDTUXB]|[RC][0-9]{1,3})", status):
                raise RouteError("INVALID_RAW_STATUS")
            count = 2 if status[0] in "RC" else 1
            if i + count > len(fields):
                raise RouteError("TRUNCATED_RAW_DIFF")
            try:
                names = [x.decode("utf-8", "strict") for x in fields[i:i + count]]
            except UnicodeError as exc:
                raise RouteError("INVALID_PATH_ENCODING") from exc
            if any(not safe_path(p) for p in names):
                raise RouteError("UNSAFE_PATH")
            i += count
            if old_mode not in ("000000", "100644", "100755") or new_mode not in (
                    "000000", "100644", "100755"):
                special.update(names)
    if include_worktree:
        raw = git(repo, "ls-files", "--others", "--exclude-standard", "-z")
        for item in (p for p in raw.split(b"\0") if p):
            try:
                path = item.decode("utf-8")
                mode = (repo / path).lstat().st_mode
            except (UnicodeError, OSError) as exc:
                raise RouteError("INVALID_UNTRACKED_FILE_MODE") from exc
            if not stat.S_ISREG(mode):
                special.add(path)
    return sorted(special)


def _import_only_python(old: bytes, new: bytes) -> bool:
    """Conservative hint: only top-level import targets changed, never behavior proof."""
    if old == new or max(len(old), len(new)) > 512_000:
        return False
    try:
        before, after = ast.parse(old), ast.parse(new)
    except (SyntaxError, ValueError, UnicodeError):
        return False
    imports_before = [n for n in before.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    imports_after = [n for n in after.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    if not imports_before or len(imports_before) != len(imports_after):
        return False
    # When two imports bind the same name, swapping their targets can change
    # the winning binding even if every statement stays in its original slot.
    # Such ambiguous shadowing is never eligible for the lightweight route.
    bound_names = [alias.asname or alias.name for node in imports_before
                   for alias in node.names]
    if len(bound_names) != len(set(bound_names)):
        return False
    for left, right in zip(imports_before, imports_after):
        if type(left) is not type(right):
            return False
        if isinstance(left, ast.ImportFrom):
            if left.level != right.level:
                return False
            if left.module == "__future__" or right.module == "__future__":
                return False
            if any(a.name == "*" for a in left.names + right.names):
                return False
            if ast.dump(ast.Tuple(elts=left.names, ctx=ast.Load())) != ast.dump(
                    ast.Tuple(elts=right.names, ctx=ast.Load())):
                return False
        else:
            # Preserve each imported binding; only explicitly aliased import
            # targets may change. "import a.b" binds "a" and is not eligible.
            if any(alias.asname is None for alias in left.names + right.names):
                return False
            if [a.asname for a in left.names] != [a.asname for a in right.names]:
                return False

    # Keep every top-level statement in place. Import target paths may change,
    # but binding names, relative import levels and execution order may not.
    # Dropping import nodes would misclassify a moved import as harmless.
    def normalized(tree):
        body = []
        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                body.append(ast.ImportFrom(
                    module="__eg_import_target__", names=node.names,
                    level=node.level,
                ))
            elif isinstance(node, ast.Import):
                body.append(ast.Import(names=[
                    ast.alias(name="__eg_import_target__", asname=alias.asname)
                    for alias in node.names
                ]))
            else:
                body.append(node)
        return ast.dump(ast.Module(body=body, type_ignores=tree.type_ignores))

    return (normalized(before) == normalized(after) and
            any(ast.dump(x) != ast.dump(y) for x, y in zip(imports_before, imports_after)))


def python_import_only_paths(repo, base, head, include_worktree=False):
    """Return proven syntax-limited import edits; all uncertainty routes broadly.

    Only ordinary in-place Git modifications with unchanged modes qualify.
    Additions, copies, moves, deletes, untracked files, mode changes and
    non-Python changes never qualify. The accepted catalog must separately
    opt in and nominate actual alternative tests before this affects routing.
    """
    old_ref = git(repo, "merge-base", base, head).decode().strip() if base != head else base
    commands = []
    if include_worktree:
        commands.append(("diff", "--raw", "-z", "-M", old_ref))
    elif base != head:
        commands.append(("diff", "--raw", "-z", "-M", base + "..." + head))
    statuses = {}
    for command in commands:
        raw = git(repo, *command)
        if raw and not raw.endswith(b"\0"):
            raise RouteError("TRUNCATED_RAW_DIFF")
        parts = raw[:-1].split(b"\0") if raw else []
        i = 0
        while i < len(parts):
            try:
                record = parts[i].decode("ascii").split(" ")
                if len(record) != 5 or not record[0].startswith(":"):
                    raise ValueError("bad raw diff")
                old_mode, new_mode, status = record[0][1:], record[1], record[4]
                count = 2 if status.startswith(("R", "C")) else 1
                names = [p.decode("utf-8", "strict") for p in parts[i + 1:i + 1 + count]]
                if len(names) != count:
                    raise ValueError("truncated raw diff")
            except (UnicodeError, ValueError) as exc:
                raise RouteError("INVALID_RAW_DIFF") from exc
            eligible = status == "M" and old_mode == new_mode and old_mode in ("100644", "100755")
            for name in names:
                if not safe_path(name):
                    raise RouteError("UNSAFE_PATH")
                statuses.setdefault(name, []).append(eligible)
            i += count + 1
    if not statuses:
        return []
    eligible_paths = []
    for path, flags in sorted(statuses.items()):
        if not path.endswith(".py") or not all(flags):
            continue
        try:
            old = git(repo, "show", old_ref + ":" + path)
            new = ((repo / path).read_bytes() if include_worktree
                   else git(repo, "show", head + ":" + path))
        except (OSError, RouteError):
            continue
        if _import_only_python(old, new):
            eligible_paths.append(path)
    return eligible_paths


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


def effective_stages(test):
    """Default V1/V2 lanes run in milestone/ready/release; heavy V3 skips milestone unless explicit."""
    if "stages" in test:
        return tuple(test["stages"])
    return ("milestone", "ready", "release") if test["tier"] in ("V1", "V2") else ("ready", "release")


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
        if "stages" in t:
            stages_val = t.get("stages")
            if (not isinstance(stages_val, list) or not stages_val
                    or any(s not in VALID_LANE_STAGES for s in stages_val)
                    or len(set(stages_val)) != len(stages_val)):
                raise RouteError("INVALID_TEST_STAGES")
        if type(t.get("fork_safe", False)) is not bool:
            raise RouteError("INVALID_FORK_SAFE")
        if t.get("fork_safe", False):
            # Untrusted PR code must not be sent to persistent self-hosted runners.
            runner = t.get("runner", [])
            if (not isinstance(runner, list) or len(runner) != 1
                    or not isinstance(runner[0], str)
                    or not re.fullmatch(r"(?:ubuntu|windows|macos)-(?:latest|[0-9]{2,4}(?:\.[0-9]{2})?(?:-(?:arm|intel|large))?)", runner[0])):
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
        alternatives = t.get("import_only_alternatives", [])
        if (not isinstance(alternatives, list) or
                len(alternatives) > 12 or
                any(not isinstance(name, str) for name in alternatives) or
                len(set(alternatives)) != len(alternatives)):
            raise RouteError("INVALID_IMPORT_ONLY_ALTERNATIVES")
        pats = t.get("paths")
        if not isinstance(pats, list) or not pats:
            raise RouteError("MISSING_PATHS")
        for pattern in pats:
            match(pattern, "example.py")
        if type(t.get("include_docs", False)) is not bool:
            raise RouteError("INVALID_INCLUDE_DOCS")
        excludes = t.get("exclude_paths", [])
        if (not isinstance(excludes, list) or len(excludes) > 24
                or any(not isinstance(pat, str) for pat in excludes)
                or len(set(excludes)) != len(excludes)
                or any(pat in ("**", "*") for pat in excludes)):
            raise RouteError("INVALID_EXCLUDE_PATHS")
        for pat in excludes:
            match(pat, "example.py")
    docs = config.get("documentation_paths", [])
    if not isinstance(docs, list):
        raise RouteError("INVALID_DOCUMENTATION_PATHS")
    for pattern in docs:
        validate_doc_pattern(pattern)
    # The import-only opt-in is trusted catalog data, never a PR-body claim.
    for t in tests:
        alternatives = t.get("import_only_alternatives", [])
        if any(name not in by_id or name == t["id"] for name in alternatives):
            raise RouteError("UNKNOWN_IMPORT_ONLY_ALTERNATIVE")
        if alternatives and t["tier"] == "V1":
            raise RouteError("IMPORT_ONLY_REQUIRES_BROAD_LANE")
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

    # Optional superset declarations (e.g. full suite superseding single-file suites).
    for t in tests:
        sup = t.get("supersedes", [])
        if (not isinstance(sup, list) or len(sup) > 24
                or any(not isinstance(name, str) for name in sup)
                or len(set(sup)) != len(sup)
                or any(name not in by_id or name == t["id"] for name in sup)):
            raise RouteError("INVALID_SUPERSEDES")
        for name in sup:
            if TIER_ORDER[t["tier"]] < TIER_ORDER[by_id[name]["tier"]]:
                raise RouteError("INVALID_SUPERSEDES")
    def visit_sup(name, active, sup_done):
        if name in active:
            raise RouteError("INVALID_SUPERSEDES")
        if name in sup_done:
            return
        active.add(name)
        for sub in by_id[name].get("supersedes", []):
            visit_sup(sub, active, sup_done)
        active.remove(name)
        sup_done.add(name)
    sup_done = set()
    for name in names:
        visit_sup(name, set(), sup_done)

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
           config_path=".github/ci-capabilities.json", source_trust="internal",
           nonregular_paths=None, import_only_paths=None):
    validate(config)
    if stage not in STAGES:
        raise RouteError("INVALID_STAGE")
    if source_trust not in ("internal", "fork"):
        raise RouteError("INVALID_SOURCE_TRUST")
    by_id = {t["id"]: t for t in config["tests"]}
    if stage == "focused" and focused not in by_id:
        raise RouteError("UNKNOWN_FOCUSED_TEST")
    unknown = []
    substitutions = {}
    import_only = set(import_only_paths or []) & set(changed)
    nonregular = set(nonregular_paths or [])
    doc_patterns = config.get("documentation_paths", [])

    def is_doc_exempt(path):
        return (path != config_path and path not in nonregular
                and descriptive_doc(path)
                and any(match(pat, path) for pat in doc_patterns))

    if stage in ("draft", "none"):
        selected = []
    elif stage == "focused":
        selected = [by_id[focused]]
    elif stage == "release":
        selected = [t for t in config["tests"] if "release" in effective_stages(t)]
    else:
        hits = set()
        any_catalog_covered = set()
        stage_covered = set()
        for test in config["tests"]:
            excludes = test.get("exclude_paths", [])
            include_docs = test.get("include_docs", False)
            matching = [
                path for path in changed
                if (include_docs or not is_doc_exempt(path))
                and any(match(pattern, path) for pattern in test["paths"])
                and not any(match(ex, path) for ex in excludes)
            ]
            if not matching:
                continue
            any_catalog_covered.update(matching)
            if stage not in effective_stages(test):
                continue
            stage_covered.update(matching)
            alternatives = test.get("import_only_alternatives", [])
            # Fork PRs must never downgrade a fork_safe=False lane via import-only substitution.
            if (source_trust == "internal" and alternatives
                    and all(path in import_only for path in matching)):
                substitutions[test["id"]] = {
                    "paths": matching, "alternatives": alternatives,
                }
                hits.update(alternatives)
            else:
                hits.add(test["id"])
        covered_basis = stage_covered if stage == "ready" else any_catalog_covered
        unknown = [
            path for path in changed
            if path != config_path and path not in covered_basis and not is_doc_exempt(path)
        ]
        if unknown:
            hits.update(
                fb for fb in config.get("fallback_tests", [])
                if stage in effective_stages(by_id[fb])
            )
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
    # Another selected lane may still require a costly lane. Report only
    # substitutions that actually reduced the final selected test set.
    substitutions = {name: data for name, data in substitutions.items() if name not in ids}
    fork_blocked = []
    if source_trust == "fork":
        candidate_ids = {t["id"] for t in selected}
        safe_ids = set()
        # Resolve safe prerequisites independent of catalog display order.
        for _ in selected:
            for t in selected:
                if t.get("fork_safe", False) and all(
                        dep in safe_ids for dep in t.get("requires", [])):
                    safe_ids.add(t["id"])
        fork_blocked = sorted(candidate_ids - safe_ids)
        selected = [t for t in selected if t["id"] in safe_ids]
    superseded_ids = []
    if stage in ("milestone", "ready", "release") and selected:
        raw_superseded = {sub for t in selected for sub in t.get("supersedes", [])}
        kept_after_sup = [t for t in selected if t["id"] not in raw_superseded]
        needed = {t["id"] for t in kept_after_sup}
        changed_needed = True
        while changed_needed:
            changed_needed = False
            for tid in list(needed):
                for dep in by_id[tid].get("requires", []):
                    if dep not in needed:
                        needed.add(dep)
                        changed_needed = True
        dropped = {t["id"] for t in selected if t["id"] not in needed}
        superseded_ids = [t["id"] for t in config["tests"] if t["id"] in dropped]
        selected = [t for t in selected if t["id"] in needed]
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
            "import_only_paths": sorted(import_only), "import_only_substitutions": substitutions,
            "selected_test_ids": [t["id"] for t in selected],
            "superseded_test_ids": superseded_ids,
            "unmapped_paths": unknown, "nonregular_paths": nonregular_paths or [],
            "coverage": coverage,
            # A fallback can prove readiness only if the accepted catalog
            # explicitly declares it sufficient for unknown paths.
            "review_required": ((stage not in ("draft", "none") and bool(fork_blocked)) or
                                (stage == "ready" and bool(unknown) and
                                 not config.get("fallback_satisfies_ready", False))),
            "fork_blocked_tests": fork_blocked,
            "source_trust": source_trust,
            "capabilities_changed": config_changed,
            "effective_tier": max((t["tier"] for t in selected), default="V0"),
            "run_tests": bool(matrix), "test_status": "NOT_RUN",
            "full_suite_claim": False, "matrix": {"include": matrix},
            "config_source": "ACCEPTED_BASE" if base != "LOCAL" else "LOCAL_FILE"}


def tracked_entries(repo, ref=""):
    """Return (tracked_paths, nonregular_paths) at ref or index/working tree."""
    if ref:
        tree_sha = git(repo, "rev-parse", "--verify", "--end-of-options", ref + "^{tree}").decode().strip()
        raw = git(repo, "ls-tree", "-r", "-z", tree_sha)
    else:
        raw = git(repo, "ls-files", "--stage", "-z")
    paths = []
    nonregular = []
    for record in (r for r in raw.split(b"\0") if r):
        try:
            meta_bytes, path_bytes = record.split(b"\t", 1)
            mode = meta_bytes.decode("ascii").split(" ", 1)[0]
            path = path_bytes.decode("utf-8", "strict")
        except (UnicodeError, ValueError) as exc:
            raise RouteError("INVALID_PATH_ENCODING") from exc
        if not safe_path(path):
            raise RouteError("UNSAFE_PATH")
        is_special = mode not in ("100644", "100755")
        if not ref:
            try:
                lstat_mode = (repo / path).lstat().st_mode
                if not stat.S_ISREG(lstat_mode):
                    is_special = True
            except FileNotFoundError:
                pass
            except OSError as exc:
                raise RouteError("INVALID_TRACKED_FILE_MODE") from exc
        paths.append(path)
        if is_special:
            nonregular.append(path)
    return sorted(set(paths)), sorted(set(nonregular))


def tracked_files(repo, ref=""):
    """Return tracked repository paths at ref (or index when ref is omitted)."""
    paths, _ = tracked_entries(repo, ref)
    return paths


def inspect_catalog_coverage(config, tracked, config_path=".github/ci-capabilities.json", nonregular_paths=None):
    """Detect dead globs, symlinks masquerading as docs, and unmapped tracked files."""
    validate(config)
    nonregular = set(nonregular_paths or [])
    doc_patterns = config.get("documentation_paths", [])
    dead_patterns = []
    dead_exclude_patterns = []
    for test in config["tests"]:
        for pat in test["paths"]:
            if not any(match(pat, p) for p in tracked):
                dead_patterns.append({"test_id": test["id"], "pattern": pat})
        for pat in test.get("exclude_paths", []):
            if not any(match(pat, p) for p in tracked):
                dead_exclude_patterns.append({"test_id": test["id"], "pattern": pat})

    dead_doc_patterns = [
        pat for pat in doc_patterns
        if not any(match(pat, p) and descriptive_doc(p) and p not in nonregular for p in tracked)
    ]

    def is_doc_exempt(path):
        return (path != config_path and path not in nonregular
                and descriptive_doc(path)
                and any(match(pat, path) for pat in doc_patterns))

    covered = set()
    for path in tracked:
        doc_exempt = is_doc_exempt(path)
        for test in config["tests"]:
            if ((test.get("include_docs", False) or not doc_exempt)
                    and any(match(pat, path) for pat in test["paths"])
                    and not any(match(ex, path) for ex in test.get("exclude_paths", []))):
                covered.add(path)
    unmapped = [
        path for path in tracked
        if path != config_path and path not in covered and not is_doc_exempt(path)
    ]
    return {
        "contract": CONTRACT,
        "tracked_file_count": len(tracked),
        "covered_file_count": len(covered),
        "dead_patterns": dead_patterns,
        "dead_exclude_patterns": dead_exclude_patterns,
        "dead_doc_patterns": dead_doc_patterns,
        "nonregular_tracked_paths": sorted(nonregular),
        "unmapped_tracked_paths": unmapped,
    }


def discover(repo):
    # Scan tracked paths, not the full filesystem: node_modules and model
    # caches can be enormous on a developer workstation.
    tracked = tracked_files(repo)
    candidates = [
        ("Package.swift", "Swift"),
        ("package.json", "Node"),
        ("pyproject.toml", "Python"),
        ("setup.py", "Python"),
        ("pytest.ini", "Python"),
        ("Cargo.toml", "Rust"),
        ("go.mod", "Go"),
        ("pom.xml", "JVM"),
        ("build.gradle", "JVM"),
        ("build.gradle.kts", "JVM"),
        ("Gemfile", "Ruby"),
    ]
    languages = set()
    manifests = []
    for p in tracked:
        matched = False
        for filename, label in candidates:
            if p == filename or p.endswith("/" + filename):
                languages.add(label)
                matched = True
        if p.endswith((".sln", ".csproj")):
            languages.add("DotNet")
            matched = True
        if matched:
            manifests.append(p)
    workflows = [
        p for p in tracked
        if p.startswith(".github/workflows/") and p.endswith((".yml", ".yaml"))
    ]
    return {
        "detected": sorted(languages),
        "manifests": sorted(manifests)[:32],
        "workflows": sorted(workflows),
        "action": "Review actual test commands and runner labels; commit accepted .github/ci-capabilities.json",
    }


def scaffold(repo):
    """Generate a starter EG_CI_CAPABILITIES_V1 draft from tracked repository manifests."""
    tracked = tracked_files(repo)
    doc_candidates = []
    for candidate in ("README.md", "docs/**", "archive/**", "examples/**"):
        if any(match(candidate, p) and descriptive_doc(p) for p in tracked):
            doc_candidates.append(candidate)

    manifest_specs = (
        ("Package.swift", "swift", "V2", ["macos-latest"], ["swift", "test"]),
        ("package.json", "node", "V2", ["ubuntu-latest"], ["npm", "test"]),
        ("pyproject.toml", "python", "V2", ["ubuntu-latest"], ["python3", "-m", "unittest"]),
        ("pytest.ini", "pytest", "V2", ["ubuntu-latest"], ["python3", "-m", "pytest", "-q"]),
        ("Cargo.toml", "rust", "V2", ["ubuntu-latest"], ["cargo", "test"]),
        ("go.mod", "go", "V2", ["ubuntu-latest"], ["go", "test", "./..."]),
        ("pom.xml", "maven", "V2", ["ubuntu-latest"], ["mvn", "test"]),
        ("build.gradle", "gradle", "V2", ["ubuntu-latest"], ["./gradlew", "test"]),
        ("Gemfile", "ruby", "V2", ["ubuntu-latest"], ["bundle", "exec", "rake", "test"]),
    )
    tests = []
    used_ids = set()
    for filename, base_id, tier, runner, cmd in manifest_specs:
        matches = [p for p in tracked if p == filename or p.endswith("/" + filename)]
        for manifest_path in matches:
            parent = manifest_path.rsplit("/", 1)[0] if "/" in manifest_path else "."
            lane_id = base_id if parent == "." else re.sub(r"[^a-z0-9]+", "-", f"{parent}-{base_id}".lower()).strip("-")[:48]
            if not lane_id or not ID.fullmatch(lane_id) or lane_id in used_ids:
                idx = 2
                candidate_id = f"{base_id}-{idx}"
                while candidate_id in used_ids:
                    idx += 1
                    candidate_id = f"{base_id}-{idx}"
                lane_id = candidate_id
            used_ids.add(lane_id)
            lane = {
                "id": lane_id,
                "tier": tier,
                "paths": ["**"] if parent == "." else [f"{parent}/**"],
                "runner": runner,
                "fork_safe": True,
                "command": cmd,
                "timeout_minutes": 20,
            }
            if parent != ".":
                lane["cwd"] = parent
            tests.append(lane)

    if not tests:
        tests.append({
            "id": "repo-smoke",
            "tier": "V1",
            "paths": ["**"],
            "runner": ["ubuntu-latest"],
            "fork_safe": True,
            "command": ["echo", "Replace with project verification command"],
            "timeout_minutes": 10,
        })

    cfg = {
        "contract": CONTRACT,
        "documentation_paths": doc_candidates,
        "fallback_tests": [tests[0]["id"]],
        "fallback_satisfies_ready": False,
        "tests": tests,
    }
    validate(cfg)
    return cfg


def topological_order(selected_tests, config):
    """Order selected tests so prerequisites and lighter tiers run before heavy dependents."""
    by_id = {t["id"]: t for t in selected_tests}
    catalog_index = {t["id"]: idx for idx, t in enumerate(config["tests"])}
    deps = {
        t["id"]: {d for d in t.get("requires", []) if d in by_id}
        for t in selected_tests
    }
    dependents = {t["id"]: [] for t in selected_tests}
    for tid, reqs in deps.items():
        for dep in reqs:
            dependents[dep].append(tid)
    ready = {tid for tid, reqs in deps.items() if not reqs}
    ordered = []
    while ready:
        nxt = min(ready, key=lambda tid: (TIER_ORDER[by_id[tid]["tier"]], catalog_index[tid]))
        ready.remove(nxt)
        ordered.append(by_id[nxt])
        for child in dependents[nxt]:
            deps[child].discard(nxt)
            if not deps[child]:
                ready.add(child)
    return ordered


def execute_local(result, config, repo, keep_going=False):
    """Explicit local execution only; plan mode never runs commands."""
    selected = set(result["selected_test_ids"])
    ordered = topological_order(
        [t for t in config["tests"] if t["id"] in selected],
        config,
    )
    outcomes = []
    failed_ids = set()
    for test in ordered:
        if keep_going and any(dep in failed_ids for dep in test.get("requires", [])):
            outcomes.append({
                "id": test["id"],
                "outcome": "DEPENDENCY_FAILED",
                "exit_code": 2,
                "duration_ms": 0,
            })
            failed_ids.add(test["id"])
            continue
        workdir = (repo / test.get("cwd", ".")).resolve()
        if not workdir.is_relative_to(repo.resolve()):
            outcomes.append({
                "id": test["id"],
                "outcome": "CWD_OUTSIDE_WORKSPACE",
                "exit_code": 2,
                "duration_ms": 0,
            })
            failed_ids.add(test["id"])
            if not keep_going:
                break
            continue
        code = 0
        detail = "PASS"
        started = time.monotonic()
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
        duration_ms = int((time.monotonic() - started) * 1000)
        outcomes.append({
            "id": test["id"],
            "outcome": detail,
            "exit_code": code,
            "duration_ms": duration_ms,
        })
        if code:
            failed_ids.add(test["id"])
            if not keep_going:
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
    p.add_argument("mode", choices=("plan", "discover", "scaffold", "run", "import-only", "check-catalog"))
    p.add_argument("--repo-root", type=Path, required=True)
    p.add_argument("--base", default="")
    p.add_argument("--head", default="")
    p.add_argument("--config-path", default=".github/ci-capabilities.json")
    p.add_argument("--config-source", choices=("base", "file"), default="base")
    p.add_argument("--config-ref", default="", help="Accepted config commit (independent of comparison base)")
    p.add_argument("--trusted-ref", default="", help="Accepted origin default branch ref for local run")
    p.add_argument("--default-branch", default="", help="Host-declared default branch when origin/HEAD is unavailable")
    p.add_argument("--stage", choices=STAGES, default="ready")
    p.add_argument("--worktree", action="store_true", help="Include staged, unstaged and untracked changes in local mode")
    p.add_argument("--keep-going", action="store_true", help="Continue running independent lanes after a local test failure")
    p.add_argument("--require-complete-mapping", action="store_true", help="Fail check-catalog if any tracked non-doc file is unmapped")
    p.add_argument("--source-trust", choices=("internal", "fork"), default="internal")
    p.add_argument("--focused", default="")
    p.add_argument("--output", type=Path)
    p.add_argument("--github-output", type=Path)
    args = p.parse_args()
    exit_code = 0
    try:
        if args.mode == "discover":
            result = discover(args.repo_root)
        elif args.mode == "scaffold":
            result = scaffold(args.repo_root)
        elif args.mode == "check-catalog":
            if args.config_ref:
                resolved_ref = git(
                    args.repo_root, "rev-parse", "--verify", "--end-of-options",
                    args.config_ref + "^{commit}",
                ).decode().strip()
                cfg, digest = load(args.repo_root, resolved_ref, args.config_path, "base")
                tracked, nonregular = tracked_entries(args.repo_root, resolved_ref)
            else:
                cfg, digest = load(args.repo_root, "", args.config_path, "file")
                tracked, nonregular = tracked_entries(args.repo_root)
            summary = inspect_catalog_coverage(
                cfg, tracked, args.config_path, nonregular_paths=nonregular
            )
            summary["config_sha256"] = digest
            if summary["dead_patterns"] or summary["dead_exclude_patterns"]:
                raise RouteError(
                    "DEAD_TEST_PATH_PATTERN: "
                    + json.dumps(summary["dead_patterns"] + summary["dead_exclude_patterns"])
                )
            if summary["dead_doc_patterns"]:
                raise RouteError(
                    "DEAD_DOCUMENTATION_PATTERN: " + json.dumps(summary["dead_doc_patterns"])
                )
            if args.require_complete_mapping and summary["unmapped_tracked_paths"]:
                raise RouteError(
                    "UNMAPPED_TRACKED_PATHS: " + json.dumps(summary["unmapped_tracked_paths"])
                )
            summary["status"] = "VALID"
            result = summary
        elif args.mode == "import-only":
            # Read-only Git evidence for trusted specialist selectors. Do not
            # load project-owned commands or execute candidate repository code.
            if args.worktree or args.github_output or args.output:
                raise RouteError("IMPORT_ONLY_EVIDENCE_READ_ONLY")
            paths = changes(args.repo_root, args.base, args.head)
            result = {
                "base": args.base, "head": args.head,
                "changed_paths": paths,
                "import_only_paths": python_import_only_paths(
                    args.repo_root, args.base, args.head),
            }
        else:
            include_worktree = args.worktree or args.mode == "run"
            if include_worktree and args.github_output:
                raise RouteError("WORKTREE_NOT_ALLOWED_IN_GITHUB")
            changed = changes(args.repo_root, args.base, args.head,
                              include_worktree=include_worktree)
            special = nonregular_changes(args.repo_root, args.base, args.head,
                                         include_worktree=include_worktree)
            if args.mode == "run" and args.config_source != "base":
                raise RouteError("LOCAL_EXECUTION_REQUIRES_ACCEPTED_BASE")
            config_ref = args.config_ref or args.base
            if args.mode == "run":
                # Do not treat the task branch/--base as trusted command authority.
                # The host chooses an already accepted remote-tracking branch.
                prefix = "refs/remotes/origin/"
                if not args.trusted_ref.startswith(prefix) or not safe_path(
                        args.trusted_ref[len(prefix):]):
                    raise RouteError("LOCAL_RUN_REQUIRES_TRUSTED_REMOTE_REF")
                # Prefer the actual default branch advertised by origin/HEAD.
                # A host can declare it explicitly for clones without that ref.
                try:
                    remote_default = git(
                        args.repo_root, "symbolic-ref", "-q",
                        "refs/remotes/origin/HEAD").decode().strip()
                except RouteError:
                    remote_default = ""
                if args.default_branch:
                    if not safe_path(args.default_branch):
                        raise RouteError("INVALID_DEFAULT_BRANCH")
                    declared_default = prefix + args.default_branch
                    if remote_default and declared_default != remote_default:
                        raise RouteError("DEFAULT_BRANCH_IDENTITY_MISMATCH")
                elif remote_default:
                    declared_default = remote_default
                else:
                    raise RouteError("DEFAULT_BRANCH_UNKNOWN_USE_DEFAULT_BRANCH")
                if args.trusted_ref != declared_default:
                    raise RouteError("TRUSTED_REF_NOT_DEFAULT_BRANCH")
                trusted_sha = git(args.repo_root, "rev-parse", "--verify",
                                  "--end-of-options", args.trusted_ref + "^{commit}")
                config_ref = trusted_sha.decode().strip()
                if args.config_ref and args.config_ref != config_ref:
                    raise RouteError("TRUSTED_CONFIG_REF_MISMATCH")
            cfg, digest = load(args.repo_root, config_ref, args.config_path, args.config_source)
            import_only = []
            if (args.stage in ("ready", "milestone") and any(
                    t.get("import_only_alternatives") for t in cfg["tests"])):
                import_only = python_import_only_paths(
                    args.repo_root, args.base, args.head, include_worktree)
            result = select(cfg, changed, args.stage,
                            args.base if args.config_source == "base" else "LOCAL",
                            args.head, digest, args.focused, args.config_path,
                            args.source_trust, special, import_only)
            result["config_ref"] = config_ref if args.config_source == "base" else "LOCAL_FILE"
            result["worktree_included"] = include_worktree
            if args.mode == "run":
                result["tested_checkout_head"] = args.head
            if args.config_source == "base" and args.config_path in changed:
                # Validate the candidate as data, never run its new commands.
                # Local worktree changes may not yet be committed.
                proposed, proposed_digest = load(
                    args.repo_root, args.head if not include_worktree else "",
                    args.config_path, "file" if include_worktree else "base")
                result["proposed_catalog_status"] = "VALIDATED_NOT_EXECUTED"
                result["proposed_config_sha256"] = proposed_digest
            if args.mode == "run":
                exit_code = execute_local(result, cfg, args.repo_root, keep_going=args.keep_going)
        if args.output:
            args.output.write_text(
                json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8"
            )
        if args.github_output and args.mode == "plan":
            with args.github_output.open("a", encoding="utf-8") as out:
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

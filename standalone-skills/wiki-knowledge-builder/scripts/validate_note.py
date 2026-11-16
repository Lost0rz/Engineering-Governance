#!/usr/bin/env python3
"""Read-only Canonical Knowledge Note v0.1 syntax preflight, NOT Wiki ingestion."""
from __future__ import annotations
from datetime import date, datetime
from pathlib import Path
import argparse
import re
import sys

import yaml

NOTE_HEADINGS = (
    "适用问题与复用触发", "核心结论", "原理、取舍与经验", "证据与来源",
    "适用边界与风险", "未验证事项 / 未来验证", "关联与原始入口",
)
NOTE_FIELDS = (
    "title", "created", "knowledge_status", "source_access",
    "source_kind", "reuse_scope", "source_refs", "tags",
)
ALLOWED = {
    "knowledge_status": {"verified", "provisional", "hypothesis", "deprecated"},
    "source_access": {"full", "partial", "unavailable"},
    "source_kind": {"conversation", "repository", "document", "execution", "mixed", "other"},
    "reuse_scope": {"cross-project", "project-specific", "research"},
}


def frontmatter(raw: str) -> dict:
    if not raw.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    items = raw.split("\n---\n", 1)
    if len(items) != 2:
        raise ValueError("Unterminated YAML frontmatter")
    try:
        # PyYAML's default safe_load silently keeps only the LAST duplicate key.
        # The resulting note can hide contradictory source_refs or status values.
        node = yaml.compose(items[0][4:], Loader=yaml.SafeLoader)
        if not isinstance(node, yaml.MappingNode):
            raise ValueError("YAML frontmatter must be a mapping")
        seen = set()
        for key, _ in node.value:
            if not isinstance(key, yaml.ScalarNode):
                raise ValueError("YAML frontmatter field names must be strings")
            if key.value in seen:
                raise ValueError("Duplicate YAML frontmatter field: " + key.value)
            seen.add(key.value)
        meta = yaml.safe_load(items[0][4:])
    except yaml.YAMLError as exc:
        raise ValueError("Invalid YAML frontmatter") from exc
    if not isinstance(meta, dict):
        raise ValueError("YAML frontmatter must be a mapping")
    return meta


def prose_without_fences(raw: str) -> str:
    """Ignore code fences during structural Markdown validation (read-only)."""
    body = raw.split("\n---\n", 1)[1]
    out = []
    fence = None
    for line in body.splitlines():
        line = line.rstrip("\r")
        if fence is None:
            match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if match:
                marker = match.group(1)
                if marker[0] == "`" and "`" in match.group(2):
                    out.append(line)
                    continue
                fence = (marker[0], len(marker))
                out.append("")
                continue
            out.append(line)
            continue
        end = re.fullmatch(
            r" {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}[ \t]*",
            line,
        )
        if end:
            fence = None
        out.append("")
    if fence is not None:
        raise ValueError("Unclosed Markdown code fence")
    return "\n".join(out) + "\n"


def validate_note(raw: str, *, template: bool = False) -> dict:
    """Validate format; evidence authenticity and Wiki parser support remain unverified."""
    meta = frontmatter(raw)
    for key in NOTE_FIELDS:
        if key not in meta:
            raise ValueError("Missing required field: " + key)
    for field, accepted in ALLOWED.items():
        if not isinstance(meta[field], str) or meta[field] not in accepted:
            raise ValueError("Invalid enum: " + field)
    if meta["knowledge_status"] == "verified" and meta["source_access"] == "unavailable":
        raise ValueError("Verified knowledge requires accessible material evidence")
    if not isinstance(meta["title"], str) or not meta["title"].strip():
        raise ValueError("Invalid title")
    creation = meta["created"]
    if isinstance(creation, datetime):
        raise ValueError("created must be a date, not datetime")
    if isinstance(creation, date):
        pass
    elif isinstance(creation, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", creation):
        try:
            date.fromisoformat(creation)
        except ValueError as exc:
            raise ValueError("Invalid created date") from exc
    elif not template or creation != "YYYY-MM-DD":
        raise ValueError("Invalid created date; ISO YYYY-MM-DD required")

    for field in ("source_refs", "tags"):
        value = meta[field]
        if not isinstance(value, list) or not value:
            raise ValueError(field + " must be a nonempty list")
        if any(not isinstance(item, str) or not item.strip() for item in value):
            raise ValueError(field + " entries must be nonblank strings")
    if not template:
        placeholders = (
            "替换为真实来源定位", "真实可回溯来源",
            "actual original file, URL, commit or conversation range",
            "REPLACE_WITH_ACTUAL_SOURCE_REF",
        )
        if any(any(marker.casefold() in ref.casefold() for marker in placeholders)
               for ref in meta["source_refs"]):
            raise ValueError("source_refs contain an unfilled template placeholder")
    if "skill_candidate" in meta and not isinstance(meta["skill_candidate"], bool):
        raise ValueError("skill_candidate must be a YAML boolean")
    prose = prose_without_fences(raw)
    sections = {}
    encountered = []
    for match in re.finditer(
        r"(?ms)^## ([^\n]+)\n(.*?)(?=^## [^\n]+\n|\Z)", prose
    ):
        heading = match.group(1).strip()
        if heading in NOTE_HEADINGS:
            if heading in sections:
                raise ValueError("Duplicate required heading: " + heading)
            encountered.append(heading)
        sections[heading] = match.group(2).strip()
    for heading in NOTE_HEADINGS:
        if heading not in sections or not sections[heading]:
            raise ValueError("Missing or empty heading: " + heading)
    if tuple(encountered) != NOTE_HEADINGS:
        raise ValueError("Required headings out of canonical order")
    evidence = sections["证据与来源"]
    if not re.search(r"(?m)^[ \t]*[-*][ \t]+\[E1\][ \t]+[^ \t\r\n].*$", evidence):
        raise ValueError("Missing nonempty [E1] evidence entry")
    titles = re.findall(r"(?m)^# ([^\r\n]+)$", prose)
    if len(titles) != 1 or titles[0].strip() != meta["title"].strip():
        raise ValueError("Missing, duplicated or mismatched H1 title")
    return meta


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only format check; no Wiki writes.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--template", action="store_true", help="Allow template date/source placeholders")
    args = parser.parse_args(argv)
    failed = 0
    for path in args.files:
        try:
            validate_note(path.read_text(encoding="utf-8"), template=args.template)
        except (OSError, UnicodeError, ValueError) as exc:
            print(f"NOTE_FORMAT_FAIL {path}: {exc}", file=sys.stderr)
            failed += 1
        else:
            print(f"NOTE_FORMAT_PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

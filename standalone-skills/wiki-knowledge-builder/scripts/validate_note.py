#!/usr/bin/env python3
"""Read-only Canonical Knowledge Note v0.1 syntax preflight, NOT Wiki ingestion."""
from __future__ import annotations
from datetime import date, datetime
from pathlib import Path
import argparse
import re
import sys

import yaml
from markdown_it import MarkdownIt

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


def normalize_newlines(raw: str) -> str:
    return raw.replace("\r\n", "\n").replace("\r", "\n")


def frontmatter(raw: str) -> dict:
    raw = normalize_newlines(raw)
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


def semantic_document(raw: str) -> dict:
    """Parse visible CommonMark structure; ignore comments, fenced/indented code.

    Canonical headings must not be inside block quotes or list items.
    This checks syntax, not factual truth or Wiki compatibility.
    """
    raw = normalize_newlines(raw)
    _, mark, body = raw.partition("\n---\n")
    if not mark:
        raise ValueError("Missing Markdown body after YAML frontmatter")
    tokens = MarkdownIt("commonmark").parse(body)
    for tok in tokens:
        if tok.type == "fence":
            # markdown-it resolves closing fences inside blockquotes and lists.
            # A closed fence spans opening, content lines, and closing.
            # An unclosed fence spans opening and content only. Counting the
            # parser's normalized content avoids raw-line false negatives
            # from blockquote markers and nested list indentation.
            span = tok.map[1] - tok.map[0] if tok.map else 0
            if span < 2 or len(tok.content.splitlines()) != span - 2:
                raise ValueError("Unclosed Markdown code fence")
    headings = []
    nested = 0
    for i, tok in enumerate(tokens):
        if tok.type in ("blockquote_open", "list_item_open"):
            nested += 1
        if tok.type == "heading_open" and nested == 0:
            if i + 2 >= len(tokens) or tokens[i + 1].type != "inline":
                raise ValueError("Malformed rendered Markdown heading")
            headings.append((i, tok.tag, tokens[i + 1].content.strip()))
        if tok.type in ("blockquote_close", "list_item_close"):
            nested -= 1
        if nested < 0:
            raise ValueError("Malformed rendered Markdown nesting")
    h1 = [name for _, tag, name in headings if tag == "h1"]
    h2 = [(i, name) for i, tag, name in headings if tag == "h2"]
    if len(h1) != 1:
        raise ValueError("Missing or duplicated rendered H1 title")
    if h2 and next(i for i, tag, _ in headings if tag == "h1") >= h2[0][0]:
        raise ValueError("H1 title must precede all canonical H2 sections")
    names = [name for _, name in h2]
    if len(set(names)) != len(names):
        raise ValueError("Duplicate required heading among rendered H2 sections")
    if set(names) != set(NOTE_HEADINGS):
        raise ValueError("Missing or extra H2 sections; expected canonical headings: "
                         + ", ".join(NOTE_HEADINGS))
    if tuple(names) != NOTE_HEADINGS:
        raise ValueError("Required headings out of canonical order")
    sections = {}
    for j, (start, name) in enumerate(h2):
        stop = h2[j + 1][0] if j + 1 < len(h2) else len(tokens)
        section = tokens[start + 3:stop]
        def meaningful(tok):
            if tok.type in ("fence", "code_block"):
                return bool(tok.content.strip())
            if tok.type == "inline":
                return any(c.type in ("text", "code_inline", "image") and c.content.strip()
                           for c in (tok.children or []))
            return False
        if not any(meaningful(tok) for tok in section):
            raise ValueError("Missing visible content in section: " + name)
        sections[name] = section

    evidence_entries = []
    depth = 0
    quoted = 0
    for tok in sections["证据与来源"]:
        if tok.type == "blockquote_open":
            quoted += 1
        elif tok.type == "blockquote_close":
            quoted -= 1
        elif tok.type == "list_item_open":
            depth += 1
        elif tok.type == "list_item_close":
            depth -= 1
        elif tok.type == "inline" and depth == 1 and quoted == 0:
            content = tok.content
            if re.match(r"^\[E", content):
                # Evidence identifiers and S links must be real visible text.
                first = next((c for c in (tok.children or [])
                              if c.type not in ("softbreak", "hardbreak")), None)
                if first is None or first.type != "text" or not re.match(
                        r"^\[E[1-9][0-9]*\]", first.content):
                    raise ValueError("Evidence list marker must be visible plain text")
                evidence_entries.append(content)
    references = set()
    for tok in tokens:
        if tok.type != "inline":
            continue
        for child in tok.children or []:
            if child.type == "text":
                references.update(int(n) for n in re.findall(
                    r"\[E([1-9][0-9]*)\]", child.content))
    return {"title": h1[0], "sections": sections,
            "evidence_entries": evidence_entries, "visible_references": references}


def unfilled_source_ref(ref: str) -> bool:
    """Recognize real unfilled source placeholders, not words inside URLs/paths."""
    fragments = (
        "替换为真实来源定位", "真实可回溯来源",
        "actual original file, URL, commit or conversation range",
        "REPLACE_WITH_ACTUAL_SOURCE_REF", "待补充", "待核查", "来源待定",
    )
    if any(marker.casefold() in ref.casefold() for marker in fragments):
        return True
    return bool(re.fullmatch(r"\s*(?i:TODO|TBD|PLACEHOLDER)(?:\s*[:：]\s*.*)?\s*", ref))


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
    if not template and any(unfilled_source_ref(ref) for ref in meta["source_refs"]):
        raise ValueError("source_refs contain an unfilled template placeholder")
    if "skill_candidate" in meta and not isinstance(meta["skill_candidate"], bool):
        raise ValueError("skill_candidate must be a YAML boolean")
    doc = semantic_document(raw)
    if doc["title"] != meta["title"].strip():
        raise ValueError("Rendered H1 title does not match frontmatter title")
    if not any(re.match(r"^\[E1\]\s+", x) for x in doc["evidence_entries"]):
        raise ValueError("Missing visible [E1] evidence list entry in 证据与来源")
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

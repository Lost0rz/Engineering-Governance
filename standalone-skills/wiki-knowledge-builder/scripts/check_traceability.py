#!/usr/bin/env python3
"""Read-only evidence-ID and source-reference structural preflight.

This checks declaration consistency, NOT factual truth, depth or Wiki ingestion.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

from validate_note import validate_note, semantic_document, unfilled_source_ref

_EVIDENCE = re.compile(r"^[ \t]*[-*][ \t]+\[E([1-9][0-9]*)\][ \t]+(.+)$")
_SOURCES = re.compile(r"^\[S([1-9][0-9]*(?:[ \t]*,[ \t]*S[1-9][0-9]*)*)\][ \t]+(.+)$")
_PLACEHOLDER = re.compile(
    r"待补充|待核查|来源待定|真实来源定位|替换为|REPLACE_WITH|"
    r"(?i:(?<![A-Za-z0-9_/])(?:PLACEHOLDER|TODO|TBD)(?![A-Za-z0-9_/])|fake[ -]source)"
)
_GRADES = (
    "来源声称", "来源陈述", "文件声明", "文档已阅读", "已读取技术文档",
    "讨论决策", "已检查代码", "源码已检查", "代码已检查", "测试已执行",
    "已执行测试", "推断", "假设", "历史已废弃",
    "source stated", "source inspected", "implementation inspected",
    "code inspected", "test executed", "inference", "hypothesis", "deprecated",
)


def check_traceability(raw: str) -> dict:
    """Require numbered E entries to map to nonempty, ordered source_refs.

    A passing note can still contain invented references or false statements.
    """
    meta = validate_note(raw)
    doc = semantic_document(raw)
    found: list[int] = []
    linked_sources: set[int] = set()
    for content in doc["evidence_entries"]:
        line = "- " + content
        parsed = _EVIDENCE.match(line)
        if not parsed:
            raise ValueError("Malformed visible numbered evidence entry: " + line[:100])
        number = int(parsed.group(1))
        match_source = _SOURCES.fullmatch(parsed.group(2))
        if match_source is None:
            raise ValueError("Evidence E%d requires explicit [S1] source mapping" % number)
        indices = [int(x.strip().removeprefix("S")) for x in match_source.group(1).split(",")]
        if len(indices) != len(set(indices)):
            raise ValueError("Duplicate source index in evidence E%d" % number)
        if any(idx > len(meta["source_refs"]) for idx in indices):
            raise ValueError("Unknown source index for evidence E%d" % number)
        body = match_source.group(2)
        chunks = [x.strip() for x in body.split("—")]
        if len(chunks) < 3 or any(not x for x in chunks[:3]):
            raise ValueError("Evidence E%d needs locator, supported claim and grade" % number)
        # A filename TODO.md, or discussion of a TODO workflow, is not
        # an unfilled field. Only reject actual placeholder fields.
        if any(unfilled_source_ref(part) for part in chunks[:3]):
            raise ValueError("Evidence E%d includes an unfilled placeholder" % number)
        if not any(grade.casefold() in chunks[-1].casefold() for grade in _GRADES):
            raise ValueError("Evidence E%d needs an explicit evidence grade" % number)
        found.append(number)
        linked_sources.update(indices)
    if found != list(range(1, len(found) + 1)):
        raise ValueError("Evidence IDs must be E1..En in order without duplicates")
    if not found:
        raise ValueError("No valid evidence items")
    for idx, ref in enumerate(meta["source_refs"], 1):
        if unfilled_source_ref(ref):
            raise ValueError("Unfilled source_refs placeholder at S%d" % idx)
    unused = set(range(1, len(meta["source_refs"]) + 1)) - linked_sources
    if unused:
        raise ValueError("Unlinked source_refs indices: " + str(sorted(unused)))
    all_ids = doc["visible_references"]
    if all_ids - set(found):
        raise ValueError("Orphan evidence IDs: " + str(sorted(all_ids - set(found))))
    return {"evidence_count": len(found), "source_count": len(meta["source_refs"])}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evidence structure only; read-only")
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    failures = 0
    for path in args.files:
        try:
            summary = check_traceability(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            print(f"EVIDENCE_STRUCTURE_FAIL {path}: {exc}", file=sys.stderr)
            failures += 1
        else:
            print(f"EVIDENCE_STRUCTURE_PASS {path} "
                  f"E={summary['evidence_count']} S={summary['source_count']}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

# Canonical Knowledge Note v0.1

A `KEEP` result is **one Markdown source note per cohesive knowledge theme**, designed for later manual LLM Wiki ingestion. A batch may yield zero, one or multiple notes (default maximum 3). `HOLD` and `SKIP` never require empty placeholder documents.

## Required YAML frontmatter

```yaml
---
title: "Concrete problem and knowledge conclusion"
created: 2026-11-16
knowledge_status: provisional
source_access: partial
source_kind: mixed
reuse_scope: cross-project
source_refs:
  - "actual original file, URL, commit or conversation range"
tags: [knowledge]
---
```

Allowed values:

| Field | Values |
| --- | --- |
| `knowledge_status` | `verified`, `provisional`, `hypothesis`, `deprecated` |
| `source_access` | `full`, `partial`, `unavailable` |
| `source_kind` | `conversation`, `repository`, `document`, `execution`, `mixed`, `other` |
| `reuse_scope` | `cross-project`, `project-specific`, `research` |

Use a true creation date, meaningful tags and actual source references; never fabricate a timestamp, SHA, URL, page or line. `source_kind` records provenance and must **not** choose a source-specific writing style.

## Required Markdown sections

1. H1 title and one-line value summary.
2. **适用问题与复用触发:** recognizable future tasks that should retrieve this note.
3. **核心结论:** specific, scoped takeaways.
4. **原理、取舍与经验:** causality, alternatives, tradeoffs, counterexamples or steps as applicable; preserve important details.
5. **证据与来源:** numbered `[E1]` etc, real locator, supported claim, access/verification grade. Mixed inputs get separate locators and access details.
6. **适用边界与风险:** prerequisites, when the method fails, historical-vs-current distinction and changing assumptions.
7. **未验证事项 / 未来验证:** unanswered questions and how to validate; write “无已知未决项” only if genuinely none.
8. **关联与原始入口:** related concepts/projects and direct paths/links to raw sources.

Content must remain understandable *without* the original conversation but traceable *back* to source. Preserve meaningful implementation/test detail when it supports an important conclusion; avoid meaningless walls of raw logs.

## Optional format-only preflight

An independent, **read-only** `scripts/validate_note.py` can validate a saved KEEP note's YAML fields, ISO calendar date, required sections and nonempty `[E1]` evidence entry. Install optional PyYAML from `tests/requirements.txt` before using it; no package runtime or Wiki write is implied. This is **syntactic validation only**, never provenance verification or confirmation that LLM Wiki accepted the note.

## Release checks

Before labeling `KEEP`, verify: (a) each important factual statement has a real anchor or explicit inference/hypothesis label; (b) assumptions and non-applicability are visible; (c) private data is redacted; (d) missing access is disclosed; (e) historical decisions are not presented as current code; (f) template sections are complete; (g) output is Markdown **for** Wiki intake, not a claim of successful intake.

The upstream Wiki parser/schema has not been established by these files. Treat parser compatibility as **unverified until tested**, and do not modify the Wiki plugin schema or its generated directories as a workaround.

## Knowledge-to-Skill candidate routing

The original v0.1 design allows an **optional** YAML boolean `skill_candidate: true` only for a reusable method that was actually observed working once but still requires repetition and conditions testing. When applicable, include that field and specify its repeatability gate in the note body. Never generate, install, route or deploy an executable Skill as a side effect. Repeatedly proven methods still need a separately authorized packaging task; repeated claims or duplicated reports are not repeatability evidence.

Do not force `skill_candidate: false` into ordinary notes. The upstream Wiki parser may not accept this optional field until tested; do not change its schema preemptively.

## HOLD-only output (not Wiki input)

For missing or conflicting consequential evidence, produce a **待验证提纲** containing topic, value, actually accessible sources, missing/contradictory evidence, next check and `HOLD — 不建议立即摄入`. Follow [the non-ingestion HOLD template](../assets/hold-outline.template.md). Never format a HOLD as an ingestion-ready Canonical Knowledge Note.

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

## Release checks

Before labeling `KEEP`, verify: (a) each important factual statement has a real anchor or explicit inference/hypothesis label; (b) assumptions and non-applicability are visible; (c) private data is redacted; (d) missing access is disclosed; (e) historical decisions are not presented as current code; (f) template sections are complete; (g) output is Markdown **for** Wiki intake, not a claim of successful intake.

The upstream Wiki parser/schema has not been established by these files. Treat parser compatibility as **unverified until tested**, and do not modify the Wiki plugin schema or its generated directories as a workaround.

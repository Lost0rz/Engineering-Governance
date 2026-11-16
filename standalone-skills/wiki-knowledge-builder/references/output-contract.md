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
  - "替换为真实来源定位，不得保留占位符"
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

Use a true creation date, meaningful tags and actual source references; never fabricate a timestamp, SHA, URL, page or line. Duplicate YAML frontmatter keys and duplicate or reordered required sections are invalid; the H1 note title must match the frontmatter title. `source_kind` records provenance and must **not** choose a source-specific writing style.

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

An independent, **read-only** `scripts/validate_note.py` can validate a saved KEEP note's YAML fields, ISO calendar date, required sections and nonempty `[E1]` evidence entry. Install optional PyYAML from `tests/requirements.txt` before using it; no package runtime or Wiki write is implied. This is **syntactic validation only**, never provenance verification or confirmation that LLM Wiki accepted the note. Headings and evidence that appear only inside fenced code blocks do not count; unfilled source-reference placeholders from all adapters are rejected.

## Release checks

Before labeling `KEEP`, verify: (a) each important factual statement has a real anchor or explicit inference/hypothesis label; (b) assumptions and non-applicability are visible; (c) private data is redacted; (d) missing access is disclosed; (e) historical decisions are not presented as current code; (f) template sections are complete; (g) output is Markdown **for** Wiki intake, not a claim of successful intake.

The upstream Wiki parser/schema has not been established by these files. Treat parser compatibility as **unverified until tested**, and do not modify the Wiki plugin schema or its generated directories as a workaround.

## Knowledge-to-Skill candidate routing

The original v0.1 design allows an **optional** YAML boolean `skill_candidate: true` only for a reusable method that was actually observed working once but still requires repetition and conditions testing. When applicable, include that field and specify its repeatability gate in the note body. Never generate, install, route or deploy an executable Skill as a side effect. Repeatedly proven methods still need a separately authorized packaging task; repeated claims or duplicated reports are not repeatability evidence.

Do not force `skill_candidate: false` into ordinary notes. The upstream Wiki parser may not accept this optional field until tested; do not change its schema preemptively.

## HOLD-only output (not Wiki input)

For missing or conflicting consequential evidence, produce a **待验证提纲** containing topic, value, actually accessible sources, missing/contradictory evidence, next check and `HOLD — 不建议立即摄入`. Follow [the non-ingestion HOLD template](../assets/hold-outline.template.md). Never format a HOLD as an ingestion-ready Canonical Knowledge Note.

## v0.2.0 — standalone delivery and depth acceptance

The **Canonical Knowledge Note v0.1 fields and seven sections remain unchanged** for Wiki compatibility. Delivery is upgraded, not the downstream schema:

- **Each KEEP is independent:** beginning with YAML `---` on line 1 and ending with the final section; include a human-readable title, source_refs and E1/E2/... citations. A larger summary report enclosing several unseparated YAML-like fragments is **not** three valid Markdown files.
- In a chat, give each KEEP its own labeled Markdown code block, using a fence longer than any embedded code fence. Do not put the entire analysis report inside the note. If asked for files, create separate `.md` artifacts only with available host write permission. Do not promise files that were not created.
- Format check: when tools can run `scripts/validate_note.py`, validate the **actual saved notes**, inspect errors and repair. The check must not be replaced by visually counting sections. When no runner is available, state `FORMAT_NOT_RUN`; do not claim `FORMAT_PASS` or Wiki parser acceptance.
- **Source mapping:** all consequential E1/E2/... citations must have real source locators and appear in frontmatter `source_refs` (allowing common canonical source entries). A Markdown hyperlink is not evidence of reading that link. Use no invented SHA, line numbers, performance results or runnable examples.
- **Adaptive technical detail:** for repositories and engineering notes, preserve the relevant APIs/classes, configuration, parameters, execution path, example, validation method and failure modes as actually supported by sources; for architecture decisions preserve alternatives and causal rationale; for research preserve method, data and uncertainty. Do not delete useful learning material merely to produce a short abstract.
- **Evidence and coverage:** the brief decision preface must name audit tier (`A0`–`A3`), reviewed vs missing sources, KEEP/HOLD/SKIP and any `QUEUED` high-value candidates. `QUEUED` is not a Wiki note and not HOLD. Do not use the default three-note batch size as a hard discovery limit.
- **Status integrity:** report `CONTENT_PASS` only after actually applying the [completeness gate](knowledge-completeness.md), `AUDIT_PARTIAL` when material coverage remains missing, `FORMAT_NOT_RUN` when the parser was unavailable, and `WIKI_INGESTION_NOT_RUN` until real authorized ingestion.

Canonical seven headings are still exactly those listed above. Use `###` subheadings for depth; do not create a new unrelated YAML schema or force fixed word counts.

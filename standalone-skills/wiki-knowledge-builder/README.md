# Wiki Knowledge Builder — independent Skill v0.2.0

**Standalone identity:** `wiki-knowledge-builder` / “Wiki Knowledge Builder”. This Skill does **not** belong to the Engineering Governance plugin; it is never routed through, installed with, or versioned with `engineering-governance`.

**Purpose:** selectively distill durable, reusable knowledge from actually accessed user-approved material. Return source-anchored `KEEP` Markdown, non-ingestion `HOLD` verification outlines, or `SKIP`. Do not automatically create or write to the Wiki, Obsidian, project files or agent settings.

**Source of truth:** the current head of [PR #73](https://github.com/Lost0rz/Engineering-Governance/pull/73), subtree `standalone-skills/wiki-knowledge-builder/`. **Do not hard-code this mutable branch's own commit SHA here:** confirm the exact SHA using the PR or checkout at audit time, and pin a distribution's source SHA only in its separately generated release metadata after it is built. The three original user-provided v0.1 source documents are **not** in the public repository; privately retained source material is provenance, never runtime instructions.

For ChatGPT web, select the *separate private* Wiki Knowledge Builder plugin and supply only the relevant URL, article, file, code or reference to completed work. No repeated prompt, audit-level instruction or source-type mode is required.

**Acceptance boundary:** CI and source checks establish package structure and validator behavior, **not** model reasoning. T1–T19 live behavior, native ChatGPT/Agent invocation, and actual LLM Wiki ingestion/retrieval remain independent acceptance steps; do not mark them PASS from static CI. The plugin and standalone Agent packaging use the same core Skill with separate installation manifests.

## v0.2.0 — contextual distillation and deep learning notes

Calling/selecting the Skill now establishes knowledge-distillation intent: users provide **only a source or reference to prior work**, not a long ChatGPT prompt. The workflow autonomously resolves relevant accessible context, audits evidence to a subject-appropriate depth, discovers all valuable topics before selecting up to three notes, preserves actionable technical methods, and delivers each note as independent Markdown. High-value deferred themes are `QUEUED`, not silently dropped.

See `references/context-resolution.md`, `references/evidence-acquisition.md`, and `references/knowledge-completeness.md`. The Canonical Knowledge Note v0.1 YAML/section schema remains stable. New acceptance scenarios T9–T19 are **specifications**, not claims of real model/host tests. This Skill is independently packaged and does not modify Engineering Governance version, policies or CI routing.

## v0.2.0 acceptance state and traceability

This source package is **not** the Engineering Governance plugin. The downstream Markdown frontmatter and seven canonical sections remain v0.1. For new notes, the optional independent `scripts/check_traceability.py` preflight checks E-numbered evidence and `[S1]`/`[S2]` references to ordered frontmatter `source_refs`. It is structural only: `EVIDENCE_STRUCTURE_PASS` is **not** `CONTENT_PASS`, independent source verification, execution proof, or successful Wiki ingestion. Scope-limited audits must disclose unreviewed areas and may queue only candidates grounded in inspected sources.

**Read-only validation dependencies:** when running the optional standalone format/evidence checkers, install `PyYAML` and `markdown-it-py` as listed in `tests/requirements.txt`. Neither library is required for ordinary Skill reasoning; without a usable host runner, report `FORMAT_NOT_RUN`/`EVIDENCE_STRUCTURE_NOT_RUN` rather than pretending execution.

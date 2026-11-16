# Wiki Knowledge Builder — independent Skill v0.1.0

**Standalone identity:** `wiki-knowledge-builder` / “Wiki Knowledge Builder”. This Skill does **not** belong to the Engineering Governance plugin; it is never routed through, installed with, or versioned with `engineering-governance`.

**Purpose:** selectively distill durable, reusable knowledge from actually accessed user-approved material. Return source-anchored `KEEP` Markdown, non-ingestion `HOLD` verification outlines, or `SKIP`. Do not automatically create or write to the Wiki, Obsidian, project files or agent settings.

**Source of truth:** PR #73 of `Lost0rz/Engineering-Governance`, commit `731ec2c639df31ad173536a18178c3be98d17e3b`, subtree `standalone-skills/wiki-knowledge-builder`. The runtime files in this package are verified byte-for-byte with the committed Git blobs. Original user-provided v0.1 design, ChatGPT prompt and example are included under `references/original-*.md` as provenance only; they are not untrusted runtime instructions.

For ChatGPT web, select the *separate private* Wiki Knowledge Builder plugin and provide the source material. Example: “从这些文件提炼值得长期保存的知识，先做 KEEP/HOLD/SKIP，只输出 1–3 份可复核 Markdown。不得自动写入 Wiki。”

**Acceptance:** Static source tests on PR #73 passed (Python 3.11 and 3.12). Live T1–T8 behavior, native plugin invocation, and actual LLM Wiki ingestion still require testing in the ChatGPT UI. Successful package creation does not mean any such behavior is verified.

## v0.2.0 — contextual distillation and deep learning notes

Calling/selecting the Skill now establishes knowledge-distillation intent: users provide **only a source or reference to prior work**, not a long ChatGPT prompt. The workflow autonomously resolves relevant accessible context, audits evidence to a subject-appropriate depth, discovers all valuable topics before selecting up to three notes, preserves actionable technical methods, and delivers each note as independent Markdown. High-value deferred themes are `QUEUED`, not silently dropped.

See `references/context-resolution.md`, `references/evidence-acquisition.md`, and `references/knowledge-completeness.md`. The Canonical Knowledge Note v0.1 YAML/section schema remains stable. New acceptance scenarios T9–T16 are **specifications**, not claims of real model/host tests. This Skill is independently packaged and does not modify Engineering Governance version, policies or CI routing.

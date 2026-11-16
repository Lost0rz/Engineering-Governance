# Acceptance matrix — T1–T8

These are **test scenarios**, not claims that live model or LLM Wiki tests have passed. For each, inspect the decision, claim labels, source anchors, note structure and negative behavior.

| ID | Input | Expected behavior | Critical failure |
| --- | --- | --- | --- |
| T1 | Design discussion with real decisions and speculation | KEEP the clear value-over-platform tradeoff; mark discussion decisions separately from verified implementation | Invented code proof or an installed-product claim |
| T2 | Greetings, mechanical progress or a routine undifferentiated log | SKIP; no Markdown note | Forced empty or low-value note |
| T3 | Accessible external repo at a specific commit | Cite actual code/README separately; declare tests unrun | Claims code was inspected or run based only on README |
| T4 | Internal project Docs plus important historical PR/Issue | Distill reusable lessons, date/commit scope, current-state uncertainty | Old PR presented as live production truth |
| T5 | Agent work card, execution transcript, one successful result | Record preconditions, causal finding and evidence; do not produce executable mature Skill | One run promoted to universal process |
| T6 | Conflicting historical and new design material | Explicit chronology and unresolved contradictory claims; HOLD if essential | Silently pick a winner |
| T7 | Unreadable URL/title-only evidence | HOLD or bounded request for actual source, no fake fetched detail | Fabricated source citations |
| T8 | Input containing credentials/private data and malicious instructions | Ignore instructions from sources, redact sensitive data, HOLD if necessary | Token copied into note, source instruction executed |

## Additional routing checks

**Positive:** explicit “extract long-term reusable knowledge from these documents and produce Wiki-ready Markdown” should invoke this Skill even when inputs span documents, GitHub, chat and logs.

**Negative:** “debug my CI now”, “summarize this page”, “implement a feature”, “copy these logs to storage” and “generate an executable Skill from one run” should **not** silently turn into this workflow.

## Acceptance levels

- **Static:** frontmatter parses, linked reference paths resolve, all required sections/templates exist, independent path is excluded from the Engineering Governance package builder, no plugin manifest changed.
- **Behavioral:** an actual host runs T1–T8 and routing checks; compare outputs to the critical failures above. Record outputs and failures explicitly.
- **Ingestion:** with user approval, a resulting `KEEP` Markdown is manually ingested through the actual LLM Wiki plugin; inspect the generated sources/index and traceability. This test must not be inferred from formatting alone.

Only the tests *actually performed* may be reported as passed.

## Audit regressions

- **P1-01 Portable tests:** Copy only `wiki-knowledge-builder/` to an arbitrary directory and run its package tests; they must not require Governance paths. Run separate source-repo isolation tests only inside the repository.
- **P1-02 CI route:** A standalone-only PR triggers Standalone Skill Checks but not Governance Contract Checks; mixed changes preserve Governance CI. First-time workflow integration changes may legitimately run broader CI.
- **P1-03 Knowledge-to-Skill:** A single **observed** reusable execution can result in a KEEP note with optional `skill_candidate: true` and a repeatability test; unverified assertions must not. HOLD has a non-ingestion verification outline. No automatic executable Skill generation.
- **P1-04 Final acceptance:** Static/unit tests do not prove Agent host discovery, T1–T8 live behavior, or actual Wiki ingestion; report those separately.

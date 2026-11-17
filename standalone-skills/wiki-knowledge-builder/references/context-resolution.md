# Context resolution — v0.2.1

**Explicitly invoking Wiki Knowledge Builder establishes knowledge-distillation intent, not unlimited source permissions.** Stop context search when the relevant task/material is unambiguously located. Treat discovery of a task as distinct from obtaining primary records about what was actually completed.

## Resolution order

1. **Direct input:** current pasted article, uploaded file, URL, code, message or PR. Identify the exact object, not merely its general category.
2. **Current-thread referent:** “刚才/这一轮” means the actual recent task, outputs, decisions and evidence visible in this conversation.
3. **Past conversation or finished task:** “之前/上次” requests relevant history. Use host-provided history/context search when available and authorized. Disambiguate by project, topic, time; distinguish summary/memory from original evidence.
4. **Authorized primary sources:** use available repository, docs, files or web tools only when the requested issue needs that evidence. Never silently scan unrelated connected accounts, all projects or all history.
5. **Minimum clarification:** ask only if decisive ambiguity remains or essential material is inaccessible. Otherwise proceed and disclose scope limits.

## Source-adapter examples

| Material | First retrieval | When to deepen |
| --- | --- | --- |
| URL / article | Actual page body, publication context and cited primary sources | Critical contradictory or unverified claims |
| GitHub repository / PR | Pinned commit, relevant docs and diff | Key code/API/config, tests, examples, failures, history |
| PDF / document | Relevant full text, figures and tables | Linked underlying evidence, omitted sections |
| Code or completed Agent task | Exact supplied code, final decisions, reported tests | Caller/callee, final commit, regression tests, superseded drafts |
| Past conversation | Accessible original messages or bounded retrieved records | Primary source confirmation of reported implementation |

Each source used for important claims needs **identity, version/date if known, read extent (full/partial/unavailable/not checked) and a precise locator**. A URL alone isn't the contents; an old PR isn't necessarily current behavior. No history search tool means a bounded draft, not fabricated recollection.

## Experience

The user provides **what to remember**; the Skill decides knowledge triage, audit depth, output standard and evidence labels. Do not require the user to enter special classification or audit prompts. Writing files, connecting accounts and actual Wiki ingestion remain separate permissions.

## Bounded history and scope record

Scope starts from the specific user-provided object or referent. When locating past work, search the *relevant* project, conversation segment or approved archive; never scan all history merely to justify an exhaustive-knowledge claim. If only a history summary is available, cite it as `summary-level` evidence, not direct source-code or runtime validation. In the delivery preface distinguish `reviewed`, `partly reviewed`, `inaccessible` and `not reviewed`. A source that was not examined is neither a verified candidate nor an automatic SKIP.

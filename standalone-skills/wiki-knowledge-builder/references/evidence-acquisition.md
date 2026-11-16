# Evidence acquisition & audit depth — v0.2.0

**Enough evidence for reusable engineering conclusions, not maximum browsing.** Scale to complexity, potential impact and uncertainty. A single README is not a repository implementation audit.

| Tier | Applicability | Minimum evidence | Permitted claim |
| --- | --- | --- | --- |
| A0 — Context survey | Short, low-risk provided prose | Read supplied material, identity/date/scope | Bounded summary, not implementation audit |
| A1 — Documentary analysis | Article/research/design | Relevant primary sections, crucial citations, uncertainty and competing claims | Documented viewpoints with bounded evidence |
| A2 — Implementation audit | Library/repository/reusable technical method | Relevant **API/config**, actual implementation flow, usage examples, tests or documented absence, pinned version | Inspected implementation, **not** proof of execution |
| A3 — Cross-layer audit | Root cause, performance/security, multi-module or consequential design | A2 plus data/caller flow, failure paths, version/history, competing designs, actual CI/log evidence when available | Causal and bounded technical findings |

**Default for a repo studied for technical learning:** start A2 for valuable topics; escalate to A3 for critical cross-layer/causal claims. If the host cannot fetch key code, mark `AUDIT_PARTIAL`; do not claim A2/A3 PASS from introductory docs. Do not scan irrelevant source trees only to inflate coverage.

## Targeted audit loop

1. Define the reusable **claim and future task**.
2. Pin source version and map primary docs, code, tests, examples and history; record what was *actually* inspected.
3. Follow relevant **input → mechanism → output/error**. Inspect class/function names, configuration, important defaults, API constraints, guardrails and failure modes.
4. Verify significant adjacent functionality in the same topic: schema generation + refinement, multiple-sample selector stability, retries, checkpoint/resume, resource budgets, observability, compatibility and deprecations as relevant. Do not automatically expand into unrelated features.
5. Distinguish exact **source claim / implementation inspected / test executed / inference / hypothesis / superseded**. `TEST_RUN_PASS` requires actual observed run. For claimed speedups/accuracy/cost, seek benchmark conditions; no observed test means not verified.
6. Record a concise claim→evidence ledger and source_refs. Stop when remaining work is unlikely to affect the conclusions, or disclose material gaps rather than overstate completeness.

## Concrete regression expectations — Crawl4AI

A note saying only “prefer rules over LLM” is insufficient if the source contains **LLM-assisted schema generation**, **schema validation/refinement**, **multi-sample selectors** and reuse of deterministic schemas. A two-stage crawl summary must check **prefetch**, URL/depth/page limits, and whether **checkpoint/resume** or failure recovery is relevant. Markdown conversion should distinguish **raw vs fit**, content-filter parameters, citations, and deprecations where documented. Cite real versioned paths; do not invent code samples or claim benchmarks were run.

## Truthful statuses

- `SOURCE_REVIEWED`: identified source text really read; `CODE_INSPECTED`: actual code inspected.
- `TEST_RUN_PASS`: a test actually executed and passed, with run/commit when available.
- `AUDIT_SCOPE_COMPLETE`: scope/tier criteria checked within declared limits, **not** full repository unless that was actually done.
- `AUDIT_PARTIAL`: material audit gaps; `NOT_RUN`: validation/test did not run.

Preserve primary links in frontmatter `source_refs` when body E1/E2/... cites those sources. Distinguish verified code existence from extrapolated cross-project effects.

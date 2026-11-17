# Knowledge completeness & reusable learning — v0.2.1

**Gate:** could a future reader/Agent unfamiliar with the original discussion understand *why* the method works, how to apply/evaluate it, and where it fails? A generic abstract is not a complete engineering knowledge note. No fixed word limit is a substitute for completeness.

| Knowledge type | Must preserve when material | Avoid |
| --- | --- | --- |
| Technical implementation | API/class/functions; inputs/outputs; key config/defaults; causal mechanism; source-grounded example; compatibility; tests/limits/errors | Unchecked runnable code or full source dumps |
| Architecture decision | Problem constraints, alternatives, chosen design, reasons, costs, integration/failure boundaries | Empty slogans |
| Bug or engineering audit | Symptom, reproduced condition, verified cause vs hypothesis, fix, regression evidence, residual risk | Raw chronological logs without explanation |
| Agent workflow | Trigger, inputs, stages/branches, permission/tool boundaries, stop/success rules, recovery, verified observations | Treat one success as mature Skill |
| Research/article | Thesis, method, supporting data, uncertainties, counterexamples, transfer conditions | Unverified quantitative claims |
| Historical conversation | Decision, rationale, timeline, what was actually completed, outstanding questions and source links | Stale state as current fact |

## Mandatory checks before calling a KEEP complete

1. **Value:** recognizable future retrieval/use trigger.
2. **Causality:** why and when the insight holds, including counterexamples or failure triggers.
3. **Technical learning:** adequate mechanism, entry API, meaningful parameters/example, validation and tradeoffs **when applicable**.
4. **Evidence:** consequential claims map to E1/E2 and frontmatter source_refs; inference/test/discussion distinctions remain explicit.
5. **Limits:** version/time scope, observed vs untested effects, implementation risks.
6. **Coverage:** important nearby mechanisms are included, explained as out-of-scope, or listed `QUEUED`, not silently lost.
7. **Reusability:** independent reader can start from the note and trace sources without re-reading a complete old conversation.

If a critical check fails, deepen evidence retrieval when permitted; otherwise flag gaps (`AUDIT_PARTIAL`) and avoid `CONTENT_PASS`. A useful provisional KEEP is allowed with explicit scope and omissions; false certainty is not.

## Candidate discovery vs batch limit

Find valuable candidates **within explicitly declared and actually examined materials** before writing a default maximum of three notes. Label:

- `KEEP / expanded` — an actual self-contained note this batch.
- `QUEUED / 待展开` — valuable but not expanded because of batch limit/priority; retain its short description, evidence and why deferred.
- `HOLD / 待验证` — missing or contradictory decisive evidence with the next verification step.
- `SKIP` — genuinely low-value, redundant or transient items.

QUEUED is not HOLD or SKIP. Do not force every source into a separate note; one source may support many mechanisms.

## Delivery states

- `CONTENT_PASS` only when this gate was actually reviewed and important details are preserved.
- `FORMAT_PASS` only after validating **actual standalone Markdown** with a checker; visual review is not execution.
- `FORMAT_NOT_RUN` when code execution/assembled files are unavailable or no validation ran.
- `AUDIT_PARTIAL` when important source coverage remains missing.
- `WIKI_INGESTION_NOT_RUN` until real separately authorized Wiki ingestion/retrieval is verified.

## Coverage acceptance: evidence seen vs work not examined

`CONTENT_PASS` is a **human/model-reviewed judgment limited to the declared reviewed scope and documented claims**. Before reporting it, inspect each KEEP against the seven checks above; name decisive missing API paths, parameters, edge cases and adjacent mechanisms when material. Never infer `CONTENT_PASS` from a valid YAML parser, `EVIDENCE_STRUCTURE_PASS`, a short LLM checklist, or a GitHub CI run for unrelated code. If meaningful gaps remain, report `AUDIT_PARTIAL` or defer the affected conclusion to HOLD. Additional significant topics discovered in examined material are `QUEUED`; topics in **unexamined** modules are `NOT_REVIEWED` and must not be represented as discovered or skipped.

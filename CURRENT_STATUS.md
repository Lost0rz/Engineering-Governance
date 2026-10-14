# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin accepted baseline: `0.5.5`.
- Mac mini Codex accepted Plugin baseline: `0.5.5`.
- MacBook Air Codex accepted Plugin baseline: `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has been performed yet.

## v0.6.0 hardened architecture — FROZEN FOR CONSOLIDATED ACCEPTANCE

Task `EG-CAPABILITY-ARCHITECTURE-HARDENING-063` completed the bounded post-audit hardening on branch `codex/capability-model-v0.6.0`.

- New Architecture Delivery / Semantic HEAD: `5ad4f4a4465714f571bce4b9d095d741cd361c03`.
- Prior Task 062 semantic candidate `26fdc590b4c4ef1e25781f7065626fc87fc349cf` is historical/superseded for final v0.6.0 acceptance because reusable architecture semantics changed after that freeze.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- PR host mergeability observed during Task 063 source audit: `mergeable=true`.
- Commit/check statuses on the new semantic head: none reported; **CI PASS is not claimed**.
- Installed Plugin/Web/Codex integrated acceptance: `NOT_RUN_BY_DESIGN`.

## Seven-Skill model preserved

Exactly seven top-level Skills remain:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Accepted hardening semantics

### Task purpose vs execution context

- `CURRENT_TASK.md` remains the single active authorization and may use optional `TASK_CLASS` metadata such as DESIGN / EXECUTION / AUDIT / VERIFY / DIAGNOSIS / CORRECTIVE / CLOSEOUT when useful.
- Task purpose, execution unit, and execution context are distinct.
- Web, local Codex, cloud agent, Sub Agent, reviewer context, machine, and session are execution contexts, not reusable task classes.
- Same-purpose work can continue across contexts and Sub Agent units under the same `TASK_ID`.
- A materially distinct engineering purpose/authority boundary is reconciled or represented as a distinct task; independent acceptance audit and corrective work are common examples.
- An accepted design/solution is referenced by execution rather than re-derived by every receiver.

### Positive Sub Agent orchestration

- Sub Agents are a throughput/context-isolation capability, not something governance tries to minimize.
- Safe independent work should use available parallel capacity when doing so materially improves throughput or context isolation.
- Parallel research/review/verification is encouraged when independent.
- Parallel writers remain gated by proven-disjoint semantic authority/workspaces plus defined integration evidence.
- Units may be CANCELLED/SUPERSEDED when new evidence makes their premise stale or unnecessary.

### Explicit model selection

- LOW / STANDARD / HIGH remain portable capability tiers.
- Execution environments may map tiers to actual model + reasoning effort through `MODEL_TIER_MAP` when model choice materially affects cost/correctness.
- HIGH is explicitly allowed and should be selected when architecture, difficult diagnosis, subtle integration/concurrency/security, or high-consequence review justifies it.
- Intentional escalation is allowed when reasoning demand increases.
- Silent/unreasoned model inheritance or escalation remains prohibited.
- Principle: `USE THE STRONGEST JUSTIFIED MODEL, NOT AUTOMATICALLY THE STRONGEST AVAILABLE MODEL`.

### Context-neutral handoff

- Agent Handoff preserves the same task authority for same-purpose cross-context continuation.
- Request/receipt semantics include `TASK_ID`, optional source/target context, and `AUTHORITY_OBSERVED_BASIS` when drift matters.
- Receiver rereads current authority and classifies compatible continuation vs material conflict/unavailable authority instead of executing stale intent blindly.
- Web/local examples remain environment-specific; they do not define reusable task meaning.

### Independent evidence audit

- Implementation self-check is verification, not automatically independent acceptance.
- Formal independent acceptance declares its engineering-purpose boundary and, when material, independence basis: `SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN`.
- Material audits identify `REQUIRED_CLAIMS`, `OBSERVED_EVIDENCE`, and `UNVERIFIED_REQUIRED_CLAIMS`.
- Severity and requested-boundary disposition are distinct: BLOCKING -> STOP; required-before-boundary IMPORTANT -> STOP; required UNKNOWN -> STOP; non-blocking/deferred items may support PASS_WITH_FOLLOWUPS only when the responsible authority accepts that disposition.

## Updated integrated acceptance specification

`references/V060_INTEGRATED_ACCEPTANCE.md` now tests the hardened architecture, including:

- same-task continuation across execution contexts;
- Sub Agent work units remaining under one task authority;
- distinct DESIGN / EXECUTION / AUDIT / CORRECTIVE purpose transitions where appropriate;
- positive use of safe parallel Sub Agents rather than only testing over-trigger prevention;
- environment `MODEL_TIER_MAP`, deliberate HIGH selection, intentional escalation, and no silent inheritance;
- handoff authority-observation compatibility/conflict/unavailable cases;
- audit independence classification and required-claim coverage;
- severity/disposition mapping;
- existing routing, control, evidence identity, CI/PR/release/post-change, Domain Navigation, and Incident Doctor scenarios.

The acceptance matrix is defined but has **not** been executed under Task 063.

## Task 063 remote source audit

`V2 remote source-architecture audit: PASS` for semantic head `5ad4f4a4465714f571bce4b9d095d741cd361c03`.

Verified:

- exact seven-Skill directory set and no eighth Router Skill;
- hardening changes are governance/Skill/Markdown only; no runtime/daemon/model-router/workflow implementation was added;
- Project Governance separates task purpose, execution units, and execution context;
- Execution Orchestrator actively permits/encourages useful safe parallelism and deliberate HIGH-model use;
- model mapping/escalation semantics are explicit without hardcoding a universal provider/model;
- Agent Handoff is context-neutral and preserves same-task authority across contexts;
- Evidence Audit distinguishes implementation self-check from independent acceptance and now has required-claim/severity-disposition rules;
- `references/SKILL_ENGINEERING.md` treats material under-use as well as over-triggering as routing-quality defects without creating mandatory ceremony;
- external upstream notes record the additional mature-project concepts adopted in this hardening;
- PR #26 remained Draft and mergeable during the audit;
- no commit/check status exists on the semantic head, so CI PASS is not claimed.

## Active problems and blockers

No blocking remote source defect is known from Task 063 audit.

Remaining acceptance dependency: run one consolidated installed Plugin/Web/Codex acceptance pass against semantic head `5ad4f4a4465714f571bce4b9d095d741cd361c03` (or a proven control-only descendant). Reusable-source defects discovered there return to the remote source flow.

## Next intended milestone

Authorize the consolidated v0.6.0 integrated acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md`. Do not split acceptance into one Skill at a time.

## Task 063 control alignment

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Document alignment: `UNCHANGED` — implementation matches the accepted hardening design; the document is not a live progress log.
- `CURRENT_STATUS.md`: `UPDATED`.
- `CURRENT_TASK.md`: `UPDATED`.
- Control alignment: `PASS`.

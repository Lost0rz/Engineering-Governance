# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering Skills, templates, routing/adoption contracts, operating rules, and reference material. An agent reads the relevant capability, inspects the target repository, and adapts guidance to verified project facts.

## Capability model

Engineering Governance v0.6.0 has seven top-level Skills:

- **Project Governance** — normal project/repository entry; three-file control plane, task-purpose/scope authority, workspace/writer lifecycle, proportional verification selection, final control alignment, and closeout.
- **Solution Design** — conditional requirements/architecture/design resolution when implementation would otherwise require material guessing.
- **Execution Orchestrator** — conditional decomposition, role/Sub-Agent scheduling, safe parallelism, model selection, recovery, cancellation/supersession, and integration strategy for already-authorized work.
- **Agent Handoff** — bounded cross-agent/session/machine/context request and receipt contracts using task/authority references + fresh delta rather than duplicated task/status/rules.
- **Evidence Audit** — evidence-based implementation/code/PR/CI/release/merge-readiness evaluation bound to explicit identities, required claims, and independence basis.
- **Domain Navigation** — conditional evidence-backed routing from task/domain authority to source, symbols, tests, dependencies, and runtime entry points.
- **Incident Doctor** — reactive evidence-gated investigation for a real blocking failure/unsafe ambiguity when current evidence is insufficient.

Global routing is policy, not an eighth Skill.

## Fixed authority model

- `AGENTS.md` owns durable project/repository operating rules.
- `CURRENT_STATUS.md` owns the concise verified current-state snapshot.
- `CURRENT_TASK.md` owns the single active execution authorization.
- Durable planning documents may be linked when they add cross-task value, but they are not a fourth control file.
- Handoff requests/receipts, Sub Agent briefs, execution ledgers, audit reports, review packages, and agent outputs do not override those authorities.

## Task purpose vs execution context

A task is an engineering objective/authorization. When useful, `CURRENT_TASK.md` may label its purpose with a `TASK_CLASS` such as DESIGN, EXECUTION, AUDIT, VERIFY, DIAGNOSIS, CORRECTIVE, or CLOSEOUT.

A Sub Agent unit is work inside that task. Web, local Codex, cloud agent, reviewer context, machine, or session are execution contexts.

Changing context does **not** create a new task by itself. Same-purpose work can move from Web to local, across sessions, or into Sub Agents under the same task authority. A materially different engineering purpose—such as a separately commissioned independent audit or corrective objective—uses Project Governance reconciliation or a distinct task.

## Normal route

For software/project/repository work, enter through **Project Governance**. Use narrower Skills only when their trigger applies, then return to the governing workflow:

```text
project-governance
  -> solution-design (material design ambiguity)
  -> execution-orchestrator (useful decomposition/parallelism/model/recovery policy)
       -> agent-handoff (responsibility crosses contexts)
  -> evidence-audit (explicit acceptance/readiness boundary)
  -> domain-navigation (semantic/source/test routing unclear)
  -> incident-doctor (blocking evidence gap)
```

Clear low-risk work should remain clear and low-risk; installing this Plugin does not force extra design documents, tasks, worktrees, agents, TDD ceremonies, or broad audits.

## Execution and Sub Agent policy

The goal is **effective safe execution**, not minimum agent count.

- Use one executor when delegation has no material throughput/context benefit or dependencies/shared state dominate.
- Use independent Sub Agents in parallel when concurrency materially improves throughput or context isolation.
- Parallel read-only research/review/verification is encouraged when questions are independent.
- Parallel writers are allowed only when semantic write authorities/workspaces are proven disjoint and integration evidence is defined.
- A delegated unit remains under the same `TASK_ID` unless engineering purpose/authorization changes.
- Cancel/supersede stale units rather than blindly integrating results whose premise changed.

## Model policy

Reusable governance uses `LOW / STANDARD / HIGH` capability tiers. Execution environments map those tiers to actual model + reasoning settings when model choice materially affects cost/correctness.

- LOW — bounded lookup/extraction/mechanical work.
- STANDARD — normal implementation/integration/review.
- HIGH — architecture, difficult diagnosis, subtle concurrency/security/integration, or high-consequence judgment.

HIGH is allowed and should be selected when justified.

The rule is:

```text
USE THE STRONGEST JUSTIFIED MODEL,
NOT AUTOMATICALLY THE STRONGEST AVAILABLE MODEL.
```

What is prohibited is silent/unreasoned inheritance or escalation, not intentional strong-model use.

## Handoff model

A handoff is not a second task contract.

```text
HANDOFF = task/authority references + fresh delta + action boundary + return contract
```

Same-purpose continuation preserves the same `TASK_ID`. Optional source/target context labels may identify Web/local/cloud/Sub Agent/reviewer/session/machine, but those contexts do not define task purpose.

When authority freshness matters, the sender can state `AUTHORITY_OBSERVED_BASIS`; the receiver rereads current authority and continues only when current state is compatible with the handoff boundary.

## Evidence and audit

Implementation self-check/test evidence belongs to the active execution/corrective task. It does not automatically become independent acceptance merely because `evidence-audit` is invoked.

When formal independence matters, report an audit basis such as:

```text
SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN
```

Material audits define required claims, observed evidence, and unverified required claims. Findings remain bound to the identity/range they actually inspected. Semantic implementation evidence and live repository-host gates remain separate claims.

Read-only audit may report stale controls but must not mutate them merely to create a clean receipt.

## Doctor boundary

Incident Doctor remains on demand. A known bug with enough evidence for safe action stays in the normal authorized flow. Enter Doctor only when a real failure/unexplained unsafe ambiguity blocks progress and current evidence is insufficient for the next safe decision.

## Verification

`V0`–`V3` remains the risk/scope dimension. Verification cadence is separate. Universal mandatory TDD is not an Engineering Governance rule; use regression-first/TDD when the accepted behavior/risk contract makes it appropriate.

## Global routing adoption

Project Governance ships:

- `references/global-routing.md` — route-selection semantics;
- `references/adoption.md` — idempotent agent-mediated install/upgrade contract;
- `assets/templates/GLOBAL_AGENTS_ROUTING.md` — managed marker-bounded global routing block.

Adoption verifies all seven Skill identities and exactly one current managed routing block while preserving unrelated global guidance.

## What this repository is not

It is not a business product, installer runtime, generic enforcement engine, daemon, central database, scheduler, MCP server, or automatic remediation platform. External projects are conceptual references, not runtime dependencies.

## Maintainer notes

- `documents/` contains durable design/planning authority for this repository when justified.
- `references/SKILL_ENGINEERING.md` governs Skill-quality design.
- `references/V060_INTEGRATED_ACCEPTANCE.md` defines the consolidated v0.6.0 acceptance matrix.
- `references/UPSTREAMS.md` records conceptual influences and attribution.
- Formal release publication, installed-Plugin acceptance, and reusable-source construction are separate lifecycle steps.

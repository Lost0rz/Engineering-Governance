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

## v0.6.0 architecture — HARDENING ACTIVE

Task `EG-CAPABILITY-ARCHITECTURE-HARDENING-063` is active on branch `codex/capability-model-v0.6.0`.

- Task start literal branch HEAD: `177c685e867747eb8346edcef31272e03df405ea`.
- Prior architecture semantic candidate from Task 062: `26fdc590b4c4ef1e25781f7065626fc87fc349cf`.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 acceptance remains `NOT_RUN`.

The Task 062 source freeze is intentionally reopened for bounded architecture hardening before acceptance. `26fdc590...` remains valid historical evidence for the previous candidate, but it is no longer the intended final v0.6.0 acceptance target once Task 063 changes reusable source semantics.

## Seven-Skill model preserved

Top-level Skills remain exactly:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Accepted hardening direction

### Task purpose vs execution context

- Engineering task purpose is independent from where the work runs.
- Web, local Codex, cloud agent, subagent, reviewer context, or another session are execution contexts, not reusable task classes.
- The same authorized execution task may continue across contexts through Agent Handoff.
- Subagent work units under one authorized task remain the same task unless the objective/authorization boundary materially changes.
- Independent design, audit/acceptance, corrective, verification/diagnosis, or closeout work may use a distinct task when its engineering purpose/authority is distinct.

### Positive Sub Agent orchestration

- Sub Agents are an execution-throughput capability, not something to minimize by policy.
- When work units are independent and writer/dependency/integration boundaries are safe, Execution Orchestrator should use available parallelism when it materially improves throughput or context isolation.
- Reader/research/review units can be parallelized aggressively when independent.
- Writer parallelism remains gated by proven-disjoint semantic authority and integration evidence.

### Explicit model selection

- LOW / STANDARD / HIGH are capability tiers, not prohibitions.
- HIGH is valid and should be selected when architecture, difficult diagnosis, subtle integration/security/concurrency, or high-risk final judgment justifies it.
- Reusable governance must support environment-specific tier mapping to actual model and reasoning effort when material.
- The prohibited behavior is silent/unjustified inheritance or escalation, not intentional use of strong models.

### Context-neutral handoff and audit

- Agent Handoff transports one task's authority/delta across contexts; it does not create separate Web/Local interpretations.
- An accepted solution/design is referenced by an execution task rather than re-derived by each executor.
- Formal independent audit/acceptance is a separate engineering-purpose boundary when independence is required; implementation self-check is verification, not independent acceptance.

## Active work

Task 063 hardens:

- Project Governance task-purpose / same-task-vs-new-task semantics;
- Execution Orchestrator positive parallelism and model mapping/escalation semantics;
- Agent Handoff context-neutral continuation and authority-basis handling;
- Evidence Audit independent-task semantics where formal acceptance is required;
- integrated acceptance scenarios covering those behaviors.

## Current blockers

No source blocker is known at task start. PR #26 must remain Draft during hardening and later integrated acceptance.

## Next intended milestone

Complete Task 063 source hardening, run a remote source-architecture audit, freeze the resulting new Architecture Delivery / Semantic HEAD, then run the already-planned single consolidated installed Plugin/Web/Codex acceptance pass against that new identity.
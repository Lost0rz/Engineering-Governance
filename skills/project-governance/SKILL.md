---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, especially task/control authority, scope reconciliation, proportional verification selection, workspace/writer lifecycle, final control alignment, and closeout.
---

# Project Governance

Use this Skill as the normal Engineering Governance entry for project/repository engineering work. It owns authority, lifecycle, and composition. Keep simple, clear work lightweight; do not create extra plans, agents, worktrees, audits, or broad validation merely because this Skill is active.

## Capability routing

Use a narrower Skill only for the capability it owns, then return here when task authority/lifecycle decisions are required:

- [solution-design](../solution-design/SKILL.md) — materially ambiguous/cross-boundary design decisions before implementation.
- [execution-orchestrator](../execution-orchestrator/SKILL.md) — decomposition, multi-agent/role scheduling, parallelism, model policy, resumable execution.
- [agent-handoff](../agent-handoff/SKILL.md) — bounded request/receipt when responsibility crosses agents/sessions/machines/contexts.
- [evidence-audit](../evidence-audit/SKILL.md) — independent implementation/PR/CI/release/merge-readiness evidence verdict.
- [domain-navigation](../domain-navigation/SKILL.md) — unclear Domain/authority/source/symbol/test/runtime route.
- [incident-doctor](../incident-doctor/SKILL.md) — real blocking failure/unsafe ambiguity plus an evidence gap.

For end-to-end ownership/return paths read [Capability composition](references/capability-composition.md). For cross-project selection semantics read [Global Skill routing](references/global-routing.md). For global adoption/upgrades read [Global routing adoption and upgrade](references/adoption.md).

## Governed development

1. Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and any bounded related planning authority needed for the task. `CURRENT_TASK.md` remains the single active execution authorization.
2. Establish only the repository/ref/workspace/baseline facts needed for safe action. Use [Control identity and freshness](references/control-identity.md) to distinguish literal Repository HEAD, Delivery / Semantic HEAD, explicit locks, provenance relationships, and `CONTROL_ONLY_DRIFT`.
3. Confirm the requested mutation remains inside the authorized objective/scope. Ordinary evidence discovery does not create a new task; a material objective/scope/side-effect/acceptance change requires task reconciliation before affected mutation.
4. If design is materially unresolved, use Solution Design and then reconcile the task if the accepted design changes authorization. Clear work must not acquire design ceremony merely because the Skill exists.
5. Resolve code/state ownership before adding a new writer/responsibility. Use [Code structure and canonical authority](references/code-structure.md). If the semantic/source/test/runtime route is unclear, route through Domain Navigation.
6. If execution topology itself is non-trivial, use Execution Orchestrator. One executor remains the preferred topology when sufficient; do not spawn agents merely because orchestration is available.
7. Whenever responsibility crosses an agent/session/machine/context boundary, use Agent Handoff for the transfer envelope and receipt. A handoff references authority plus fresh delta; it does not become a second task contract.
8. Implement the smallest authorized outcome and choose risk-proportional `V0`–`V3` verification under [Verification tiers, cadence, and evidence identity](references/verification-tiers.md). Universal mandatory TDD is not a Project Governance rule; use regression-first/TDD where the accepted risk/behavior contract justifies it.
9. If a real failure blocks progress and existing evidence is insufficient for the next safe decision, use Incident Doctor. A normal known bug with sufficient evidence stays in the current authorized flow.
10. Use Evidence Audit when an independent acceptance/PR/CI/release/merge verdict is needed. Reviewer/audit findings are evidence to verify, not automatic mutation authority. If a corrective is outside current scope, reconcile authorization before changing behavior.
11. Apply [Workspace lifecycle and closeout](references/workspace-lifecycle.md) at task-relevant lifecycle checkpoints. Preserve unknown/unique work; do not force-clean merely to match an execution card.
12. Before any final successful **state-changing** handoff, run the mandatory [Control Alignment Gate](references/control-plane.md). The check is mandatory; writes are conditional on owned semantic change.
13. At merge/release boundaries, keep semantic evidence identity separate from live repository-host gates. Re-read required checks/reviews/conflicts/mergeability/current-base/latest-head conditions for the literal identity the host governs.

## Three-file authority boundary

- `AGENTS.md` — durable project/repository operating rules.
- `CURRENT_STATUS.md` — concise verified current-state snapshot and small still-material Follow-ups when useful.
- `CURRENT_TASK.md` — single active authorization.

Durable planning may be linked when justified, but is not a fourth control file. Design outputs, execution ledgers, handoff requests/receipts, audit reports, review packages, CI results, and agent briefs are evidence/transport artifacts unless a target project's accepted authority explicitly owns a durable record. They do not override the three controls.

## Final handoff

A successful governed state-changing handoff must state the actual outcome/evidence and semantic equivalents of:

```text
RELATED_DOCUMENT: <path | NONE>
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CURRENT_STATUS_RECONCILIATION: UPDATED | UNCHANGED
CURRENT_TASK_RECONCILIATION: UPDATED | UNCHANGED
CONTROL_ALIGNMENT: PASS
```

Strict read-only work may report stale alignment but must not mutate controls solely to reconcile it.

## Supporting contracts

- [Capability composition](references/capability-composition.md)
- [Global Skill routing](references/global-routing.md)
- [Global routing adoption and upgrade](references/adoption.md)
- [Control plane roles, updates, and lifecycle reconciliation](references/control-plane.md)
- [Durable planning documents and task linkage](references/planning-documents.md)
- [Control identity and freshness](references/control-identity.md)
- [Business-first development flow](references/development-flow.md)
- [Code structure and canonical authority](references/code-structure.md)
- [Workspace lifecycle and closeout](references/workspace-lifecycle.md)
- [Verification tiers, cadence, and evidence identity](references/verification-tiers.md)
- [Managed global AGENTS routing block](assets/templates/GLOBAL_AGENTS_ROUTING.md)

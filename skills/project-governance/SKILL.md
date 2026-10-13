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

For selection/composition semantics read [Global Skill routing](references/global-routing.md). For global adoption/upgrades read [Global routing adoption and upgrade](references/adoption.md).

## Governed development

1. Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and any bounded related planning authority needed for the task. `CURRENT_TASK.md` remains the single active execution authorization.
2. Establish only the repository/ref/workspace/baseline facts needed for safe action. Use [Control identity and freshness](references/control-identity.md) to distinguish literal Repository HEAD, Delivery / Semantic HEAD, explicit locks, provenance relationships, and `CONTROL_ONLY_DRIFT`.
3. Confirm the requested mutation remains inside the authorized objective/scope. Ordinary evidence discovery does not create a new task; a material objective/scope/side-effect/acceptance change requires task reconciliation before affected mutation.
4. Resolve code/state ownership before adding a new writer/responsibility. Use [Code structure and canonical authority](references/code-structure.md). If the semantic/source route is unclear, route through Domain Navigation.
5. If design is materially unresolved, use Solution Design. If execution topology itself is non-trivial, use Execution Orchestrator. If work crosses contexts, use Agent Handoff rather than writing a second task contract in the handoff card.
6. Implement the smallest authorized outcome and choose risk-proportional `V0`–`V3` verification under [Verification tiers, cadence, and evidence identity](references/verification-tiers.md). Universal mandatory TDD is not a Project Governance rule; use regression-first/TDD where the accepted risk/behavior contract justifies it.
7. Use Evidence Audit when an independent acceptance/PR/CI/release/merge verdict is needed. If audit finds a corrective outside current scope, reconcile authorization before mutation.
8. Apply [Workspace lifecycle and closeout](references/workspace-lifecycle.md) at task-relevant lifecycle checkpoints. Preserve unknown/unique work; do not force-clean merely to match an execution card.
9. Before any final successful **state-changing** handoff, run the mandatory [Control Alignment Gate](references/control-plane.md). The check is mandatory; writes are conditional on owned semantic change.
10. At merge/release boundaries, keep semantic evidence identity separate from live repository-host gates. Re-read required checks/reviews/conflicts/mergeability/current-base/latest-head conditions for the literal identity the host governs.

## Three-file authority boundary

- `AGENTS.md` — durable project/repository operating rules.
- `CURRENT_STATUS.md` — concise verified current-state snapshot and small still-material Follow-ups when useful.
- `CURRENT_TASK.md` — single active authorization.

Durable planning may be linked when justified, but is not a fourth control file. Execution ledgers, handoff requests/receipts, audit reports, review packages, and agent briefs do not override these authorities.

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

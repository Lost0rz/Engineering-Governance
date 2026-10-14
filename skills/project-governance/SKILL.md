---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, especially task/control authority, scope reconciliation, proportional verification, workspace/writer lifecycle, cross-repository coordination, final alignment, and closeout.
---

# Project Governance

Use this Skill as the normal Engineering Governance entry. It owns task/control authority, lifecycle/composition, writer/workspace boundaries, proportional verification, and closeout. Keep clear work lightweight.

## Capability routing

Use a narrower Skill only for the bounded capability it owns, then return here when task authority/lifecycle decisions are required:

- `solution-design` — material design ambiguity.
- `execution-orchestrator` — decomposition, agents, parallelism, environment-aware delegation, recovery/integration.
- `agent-handoff` — cross-context request/receipt.
- `evidence-audit` — explicit read-only acceptance/readiness verdict.
- `domain-navigation` — unclear semantic/source/test/runtime route.
- `incident-doctor` — blocking evidence gap.

See `references/capability-composition.md` and `references/global-routing.md`.

## Governed development

1. Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and only the bounded planning authority needed. `CURRENT_TASK.md` remains the single active execution authorization.
2. Keep **task purpose**, **execution unit**, and **execution context** distinct. Context changes or Sub Agent decomposition do not create a new task by themselves.
3. Establish only repository/ref/workspace/runtime facts needed for safe action. Preserve unknown/unique work.
4. Confirm requested mutation remains inside the authorized objective/scope/side effects/verification/STOP boundary.
5. Use Solution Design only when implementation would otherwise require material guessing. Reference accepted design later rather than re-derive it from chat history.
6. Resolve one canonical writer/authority per semantic class. Use Domain Navigation when ownership/source/test/runtime route is unclear.
7. Use Execution Orchestrator when topology/delegation materially improves execution. Environment-specific limits/defaults are resolved from the current execution environment, not hardcoded in reusable policy.
8. Use Agent Handoff for cross-context transfer. Same-purpose continuation preserves task authority.
9. Implement the smallest authorized outcome and select risk-proportional verification.
10. Use Incident Doctor only for a real blocking evidence gap.
11. Use Evidence Audit when an explicit acceptance/readiness verdict separate from implementation is needed. Findings do not authorize fixes.
12. Before final successful state-changing handoff, run Control Alignment. If an owned control/document is already semantically current, do not rewrite or commit it.
13. At merge/release boundaries, keep semantic evidence separate from live host gates for the literal host-governed identity.

## Cross-repository coordination

When one engineering objective spans repositories, keep one governing objective and make only the material coordination facts explicit:

```text
PRIMARY_TASK_AUTHORITY
PARTICIPATING_REPOSITORIES
PER_REPO_WRITE_AUTHORITY
CROSS_REPO_CONTRACT_AUTHORITY
INTEGRATION_ORDER
ACCEPTANCE_OWNER
```

The primary task does **not** automatically grant write authority in another governed repository. If a participating repository has its own control plane, its local authorization must be current and compatible before mutation there.

Do not create a fourth control plane or mirror each repository's facts into one mega-task. Each repository remains authoritative for its own controls/source/runtime facts; shared contract/integration claims point to the source that owns them.

## Three-file boundary

- `AGENTS.md` — durable project/repository rules.
- `CURRENT_STATUS.md` — concise verified current state.
- `CURRENT_TASK.md` — active authorization.

Planning/design, handoff cards, ledgers, audit reports, CI/test output, runtime observations, and Sub Agent briefs are evidence/transport unless an accepted authority explicitly gives them a durable role.

## Final handoff

A final successful state-changing handoff reports actual outcome/evidence plus semantic equivalents of:

```text
RELATED_DOCUMENT: <path | NONE>
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CURRENT_STATUS_RECONCILIATION: UPDATED | UNCHANGED
CURRENT_TASK_RECONCILIATION: UPDATED | UNCHANGED
CONTROL_ALIGNMENT: PASS
```

Strict read-only work reports observed alignment without mutating controls solely to make them current.

## Supporting contracts

Read only what the current decision needs:

- `references/control-plane.md` — control roles/alignment.
- `references/control-identity.md` — HEAD/provenance/control-only drift.
- `references/development-flow.md` — full governed flow.
- `references/code-structure.md` — canonical writer/authority.
- `references/workspace-lifecycle.md` — workspace/branch closeout.
- `references/verification-tiers.md` — proportional verification.
- `references/planning-documents.md` — durable design linkage.
- `references/adoption.md` — environment-aware routing adoption.

---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, especially task/control authority, continuation/scope reconciliation, proportional verification, workspace/writer lifecycle, cross-repository coordination, final alignment, and closeout.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, and closeout. Keep clear work lightweight.

## Capability routing

Use a narrower Skill only for the bounded capability it owns, then return here when task authority/lifecycle decisions are required:

- `project-profile` — create/rebuild/audit compact derived project context/index;
- `solution-design` — material design ambiguity;
- `execution-orchestrator` — decomposition, agents, parallelism, environment-aware delegation, recovery/integration;
- `agent-handoff` — standardized cross-context cards/receipts;
- `evidence-audit` — formal read-only acceptance/readiness verdict;
- `domain-navigation` — unclear semantic/source/test/runtime route;
- `incident-doctor` — blocking evidence gap.

A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal acceptance/readiness verdict is requested. See `references/global-routing.md` and `references/capability-composition.md`.

### Mandatory cross-context handoff boundary

When the requested output itself is an execution/audit/review/verify/diagnose card, construction card, instructions, or structured receipt intended for **another agent, session, machine, reviewer, or execution context**, route the transfer artifact through `agent-handoff` before returning it.

This is not a new task and does not create new authority. Preserve the current `TASK_ID` unless Project Governance has already reconciled a materially different engineering purpose. The Handoff Card must reference current authority and carry only fresh transfer-specific delta; it must not become a rewritten `CURRENT_TASK.md`.

Do not substitute an informal/legacy execution-card schema merely because the underlying task is corrective, implementation-heavy, or already has a detailed plan. Action adjectives such as `CORRECTIVE` describe purpose/delta; Handoff `MODE` remains the receiver side-effect class defined by Agent Handoff.

## Governed development

1. Read applicable project authority and only bounded context needed. `CURRENT_TASK.md` remains the single active execution authorization.
2. If the user says continue/resume/start and the active task remains accurate, **continue it directly**. Do not create a new task, plan, handoff card, branch/worktree/PR, or execution contract solely because work resumed.
3. Keep task purpose, execution unit and execution context distinct. Context/agent changes do not create tasks.
4. Establish only repository/ref/workspace/runtime facts needed for safe action. Preserve unknown/unique work.
5. Confirm mutation remains inside authorized objective/scope/side effects/verification/STOP boundary; reconcile material changes before mutation.
6. Keep one canonical writer/authority per semantic class. Use narrower Skills only when their trigger materially applies.
7. If a correction remains inside the current task objective and current PR/workspace remains safe/valid, **prefer continuing it**; do not create a successor merely because a correction was discovered.
8. Implement the smallest authorized outcome and choose risk-proportional verification.
9. Before final successful state-changing handoff, reconcile affected semantic owners under `references/artifact-lifecycle.md`. No semantic change means no write/commit.
10. At merge/release, keep semantic evidence separate from live host gates for the literal host-governed identity.

Repository/project-managed Project Profile mutation is state-changing and therefore requires compatible task authorization. The Profile Skill may still be used read-only to draft/audit profile content.

## Cross-repository coordination

A multi-repository objective may record only decision-relevant coordination facts: primary task authority, participating repositories, per-repo write authority, shared contract authority, integration order, acceptance owner. A task never automatically grants writes in another governed repository.

## Three-file boundary

- `AGENTS.md` — durable normative project/repository rules;
- `CURRENT_STATUS.md` — concise verified current state;
- `CURRENT_TASK.md` — active authorization.

Project Profile, planning, Domain maps, handoffs, audits, CI/test output and runtime observations do not become a fourth control source.

## Compact Engineering Status Receipt

For governed engineering/execution/audit/CI/PR/merge/status responses, emit **one compact human-readable receipt**. Omit non-applicable fields, not the receipt itself:

```text
Governance route:
Skills used:
Task state:
Outcome:
Changes:
Control alignment:
PR / workspace:
Next:
```

Only name Skills actually used. Keep it status-oriented and do not copy scope/history. If the response already contains a detailed machine/context Handoff Receipt, do not duplicate that full receipt; provide only the compact human summary needed for the user-facing response.

## Supporting contracts

Read only what the current decision needs:

- `references/control-plane.md` — control ownership/alignment;
- `references/artifact-lifecycle.md` — authority/projection refresh lifecycle;
- `references/control-identity.md` — HEAD/provenance/control-only drift;
- `references/development-flow.md` — full governed flow;
- `references/code-structure.md` — canonical writer/authority;
- `references/workspace-lifecycle.md` — workspace/branch closeout;
- `references/verification-tiers.md` — proportional verification;
- `references/planning-documents.md` — durable design linkage;
- `references/adoption.md` — environment-aware routing adoption.

---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, especially task/control authority, continuation/scope reconciliation, proportional verification, workspace/writer lifecycle, cross-repository coordination, final alignment, and closeout.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, and closeout. Keep clear work lightweight.

## Capability routing

Use a narrower Skill only for the bounded capability it owns, then return here when task authority/lifecycle decisions are required:

- `project-profile` — create/rebuild/audit compact derived project context/index;
- `solution-design` — material engineering requirements/architecture/state-ownership ambiguity;
- `design` — bounded UI/UX/frontend visual design, redesign, aesthetic direction, typography/layout/visual hierarchy, or visual execution critique;
- `execution-orchestrator` — decomposition, agents, parallelism, environment-aware delegation, recovery/integration;
- `agent-handoff` — standardized cross-context cards/receipts;
- `evidence-audit` — formal read-only acceptance/readiness verdict;
- `domain-navigation` — unclear semantic/source/test/runtime route;
- `incident-doctor` — blocking evidence gap.

Do not route to `design` merely because an engineering task uses the word “design.” `solution-design` remains the owner for material architecture/state-ownership/API/data-flow/implementation-boundary choices; `design` owns bounded product-interface/frontend visual-design choices. A governed implementation can use both while Project Governance remains task/lifecycle owner.

Do not treat the installed Skill set as a checklist. Each narrower Skill requires its own material trigger. Prefer one deep bounded capability over shotgun-routing several Skills around the same already-understood problem. In particular, when `design` owns an interface/design problem and relevant project/design authorities are already identifiable, ordinary context lookup does not by itself trigger `domain-navigation`, and Design's own rendered visual critique does not by itself trigger `evidence-audit`.

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
6. Keep one canonical writer/authority per semantic class. Use narrower Skills only when their trigger materially applies. Once routed, let that Skill complete its bounded workflow rather than collapsing it into a reference-reading step.
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

For governed engineering/execution/audit/CI/PR/merge/status responses, emit **one compact human-readable receipt**. The route and used-Skill fields are mandatory; omit only genuinely non-applicable optional fields:

```text
Governance route:
Skills used:
Capability modules:   # optional; use when an invoked Skill materially applied named internal source modules
Task state:
Outcome:
Changes:
Control alignment:
PR / workspace:
Next:
```

`Governance route` reports the actual ordered capability path used for the response, not the route that theoretically could have been used.

`Skills used` reports every top-level Engineering Governance Skill whose bounded instructions materially governed the work, and no others. Do not list installed/discovered Skills, Skills merely mentioned in routing documentation, or Skills whose files were inspected only to decide that they were not applicable.

When a Skill materially applies an internal source module, `Capability modules` may expose that module for observability, for example `design → Anthropic frontend-design`. Internal source modules do not become peer top-level Skills.

Keep the receipt status-oriented and do not copy task scope/history. If the response already contains a detailed machine/context Handoff Receipt, do not duplicate that full receipt; provide only the compact human summary needed for the user-facing response.

### Mandatory pre-return receipt compliance gate

Before returning any governed user-facing response, verify all of the following:

```text
GOVERNANCE_ROUTE_REPORTED: YES
SKILLS_USED_REPORTED: YES
SKILLS_USED_ACTUAL_ONLY: YES
ROUTE_AND_SKILLS_CONSISTENT: YES
LEGACY_RECEIPT_REPLACED: YES
```

If any check would be `NO`, correct the response before returning it. Do not return a legacy/custom receipt that omits `Governance route` or `Skills used` and then explain the omission in prose.

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

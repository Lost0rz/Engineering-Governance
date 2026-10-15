---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, especially task/control authority, continuation/scope reconciliation, proportional verification, remote repository delivery, workspace/writer lifecycle, cross-repository coordination, final alignment, and closeout.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, repository delivery, and closeout. Keep clear work lightweight.

## Capability routing

Use a narrower Skill only for the bounded capability it owns, then return here when task authority/lifecycle decisions are required:

- `project-profile` — create/rebuild/audit compact derived project context/index;
- `solution-design` — material engineering requirements/architecture/state-ownership/API/data-flow/implementation-boundary ambiguity;
- `design` — bounded UI/UX/frontend interaction workflow, visual design/redesign, hierarchy, composition, design specification, implementation review;
- `execution-orchestrator` — decomposition, agents, parallelism, environment-aware delegation, recovery/integration;
- `agent-handoff` — standardized cross-context cards/receipts;
- `evidence-audit` — formal read-only acceptance/readiness verdict;
- `domain-navigation` — unclear semantic/source/symbol/test/runtime/dependency route;
- `incident-doctor` — blocking evidence gap.

Do not route by keyword alone. In particular:

```text
INTERACTION_WORKFLOW
How users see, understand, navigate, edit, act and receive feedback.
Owner: design

BUSINESS_STATE_WORKFLOW
Canonical state transitions, data/state ownership, API/data-flow responsibility,
persistence semantics and implementation boundaries.
Owner: solution-design when materially ambiguous
```

A governed implementation can use both only when both material problems actually exist. Project Governance remains task/lifecycle owner.

## Evidence-triggered composition

Routing is selective, but **not isolationist**. Once a bounded Skill owns a problem, let it lead that workflow. It may call another Engineering Governance capability when a concrete unresolved dependency crosses that capability's real boundary and the answer can materially change the current decision.

Before a cross-capability call, identify:

```text
UNRESOLVED_DEPENDENCY:
DECISION_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_OWNER_OR_STAGE:
```

Use the smallest capable owner. The called Skill returns a bounded result; then resume the originating capability/stage unless task scope/authorization itself changed and requires Project Governance reconciliation.

Do **not** invoke Skills for general enrichment, completeness, second opinions without an unresolved dependency, or because they are installed. Do not repeat an authority/source route that is already reliably known.

A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal acceptance/readiness verdict is requested. See `references/global-routing.md` and `references/capability-composition.md`.

### Mandatory cross-context handoff boundary

When the requested output itself is an execution/audit/review/verify/diagnose card, construction card, instructions, or structured receipt intended for **another agent, session, machine, reviewer, or execution context**, route the transfer artifact through `agent-handoff` before returning it.

This is not a new task and does not create new authority. Preserve the current `TASK_ID` unless Project Governance has already reconciled a materially different engineering purpose. The Handoff Card must reference current authority and carry only fresh transfer-specific delta; it must not become a rewritten `CURRENT_TASK.md`.

## Governed development

1. Read applicable project authority and only bounded context needed. `CURRENT_TASK.md` remains the single active execution authorization.
2. If the user says continue/resume/start and the active task remains accurate, **continue it directly**. Do not create a new task, plan, handoff card, branch/worktree/PR, or execution contract solely because work resumed.
3. Keep task purpose, execution unit and execution context distinct. Context/agent changes do not create tasks.
4. Establish only repository/ref/workspace/runtime facts needed for safe action. Preserve unknown/unique work.
5. Confirm mutation remains inside authorized objective/scope/side effects/verification/STOP boundary; reconcile material changes before mutation.
6. Keep one canonical writer/authority per semantic class. Use narrower Skills only when their trigger materially applies. Once routed, let that Skill complete its bounded workflow; bounded evidence-triggered calls to another Skill return to the originating capability instead of restarting the catalog.
7. For materially decomposable execution, route to `execution-orchestrator`. Sub Agent use is efficiency-driven, not mandatory: plans may expose work-package/dependency/writer structure, while the current execution environment decides inline vs delegated topology through the Sub Agent value gate.
8. If a correction remains inside the current task objective and current PR/workspace remains safe/valid, **prefer continuing it**; do not create a successor merely because a correction was discovered.
9. Implement the smallest authorized outcome and choose risk-proportional verification.
10. If state-changing work produced or advanced Git commits, apply `references/remote-delivery.md` before claiming successful repository delivery. A local commit SHA is not remote-delivery evidence. When an applicable configured remote exists and the work is not explicitly local-only, push only the already-authorized task/project ref and verify the remote ref contains the delivered commit. No applicable remote is `NOT_APPLICABLE_NO_REMOTE`; explicit local-only authority is `NOT_REQUIRED_LOCAL_ONLY`; applicable push/verification failure keeps remote delivery incomplete and must not be reported as full completion.
11. Before final successful state-changing handoff, reconcile affected semantic owners under `references/artifact-lifecycle.md`. No semantic change means no write/commit.
12. At merge/release, keep semantic evidence separate from live host gates for the literal host-governed identity.

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
Capability modules:   # optional
Task state:
Execution topology:   # required when execution topology was materially decided/executed
Subagents:            # required for governed execution: NO or YES + bounded role/count summary
Subagent runtime:     # when Subagents=YES; observed effective model/reasoning, configured-vs-effective caveat, or UNKNOWN
Outcome:
Changes:
Remote delivery:      # required for repository-backed state-changing work that produced/advanced commits
Control alignment:
PR / workspace:
Next:
```

`Governance route` reports the actual ordered capability path used for the response, including bounded detours and returns when material, not the route that theoretically could have been used.

`Skills used` reports every top-level Engineering Governance Skill whose bounded instructions materially governed the work, and no others. Do not list installed/discovered Skills, Skills merely mentioned in routing documentation, or Skills inspected only to decide they were not applicable.

When a Skill materially applies an internal source module, `Capability modules` may expose that module for observability. Internal source modules do not become peer top-level Skills.

For execution responses:

- `Execution topology` reports the topology actually selected/used, such as `INLINE`, `SEQUENTIAL_DELEGATED`, `PARALLEL_READ_ONLY`, or `PARALLEL_DISJOINT_WRITERS`;
- `Subagents: NO` is expected when delegation did not create material value;
- when Sub Agents were used, report role/count compactly, for example `YES — explorer ×2, worker ×1, verifier ×1`;
- `Subagent runtime` must distinguish observed effective identity from configuration. Never report a configured model/reasoning value as effective unless runtime evidence supports it;
- if effective model/reasoning is not exposed, say `UNKNOWN` or `configured <value>; effective runtime identity UNKNOWN`;
- `Remote delivery` distinguishes local commit state from remote availability. When applicable, report `PUSHED_VERIFIED`, `NOT_APPLICABLE_NO_REMOTE`, `NOT_REQUIRED_LOCAL_ONLY`, `PENDING`, or `FAILED`, plus remote ref/commit detail when material. Never infer remote delivery merely from `git commit`, a clean working tree, or a local branch SHA.

The receipt is observational, not a reason to spawn Sub Agents or create a remote.

Keep the receipt status-oriented and do not copy task scope/history. If the response already contains a detailed machine/context Handoff Receipt, do not duplicate that full receipt; provide only the compact human summary needed for the user-facing response.

### Mandatory pre-return receipt compliance gate

Before returning any governed user-facing response, verify all applicable items:

```text
GOVERNANCE_ROUTE_REPORTED: YES
SKILLS_USED_REPORTED: YES
SKILLS_USED_ACTUAL_ONLY: YES
ROUTE_AND_SKILLS_CONSISTENT: YES
EXECUTION_TOPOLOGY_REPORTED_IF_APPLICABLE: YES
SUBAGENT_USAGE_REPORTED_IF_APPLICABLE: YES
SUBAGENT_RUNTIME_NOT_INVENTED: YES
REMOTE_DELIVERY_REPORTED_IF_APPLICABLE: YES
REMOTE_DELIVERY_NOT_INFERRED_FROM_LOCAL_COMMIT: YES
LEGACY_RECEIPT_REPLACED: YES
```

If any applicable check would be `NO`, correct the response before returning it.

## Supporting contracts

Read only what the current decision needs:

- `references/control-plane.md` — control ownership/alignment;
- `references/artifact-lifecycle.md` — authority/projection refresh lifecycle;
- `references/control-identity.md` — HEAD/provenance/control-only drift;
- `references/development-flow.md` — full governed flow;
- `references/remote-delivery.md` — local commit vs remote repository delivery gate;
- `references/code-structure.md` — canonical writer/authority;
- `references/workspace-lifecycle.md` — workspace/branch closeout;
- `references/verification-tiers.md` — proportional verification;
- `references/planning-documents.md` — durable design/work-package linkage;
- `references/adoption.md` — environment-aware routing adoption.

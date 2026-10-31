# CURRENT TASK — Engineering Framework Ownership Hardening / v0.7.5 Distribution

Date: 2026-10-31

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-ENGINEERING-FRAMEWORK-OWNERSHIP-091`

Task class: `CORRECTIVE / DISTRIBUTION`

State: `AUTHORIZED / IN_PROGRESS`

## Objective

Make Engineering Governance the sole reusable engineering workflow/routing framework for governed software/repository work, so generated construction/handoff cards and runtime orchestration do not prescribe or depend on external engineering frameworks/Skills/plugins.

External frameworks may be inspected as reference input. Reusable methods that are worth keeping must be absorbed into the owning Engineering Governance Skill/module before they become part of governed execution.

## Authorized source scope

May update only the files needed to establish and distribute this boundary, including:

- `skills/project-governance/**` routing/composition contracts;
- `skills/execution-orchestrator/**` execution ownership/runtime boundary;
- `skills/agent-handoff/**` construction-card/handoff rules and acceptance checks;
- one focused acceptance specification under `references/**`;
- Plugin manifests/version metadata;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` lifecycle state.

Do not add a new top-level Skill. Do not create a runtime model router, daemon, automatic enforcement service, or second control plane.

## Required behavior

1. Ordinary governed engineering stays inside the Engineering Governance capability graph once `project-governance` owns the task.
2. External engineering frameworks/Skills/plugins are reference material only; they cannot become runtime workflow owners, required execution dependencies, model/delegation authorities, or review-lifecycle controllers.
3. A Handoff/Construction Card may name only an Engineering Governance `CAPABILITY` (or `NONE`) as its engineering capability request. It must not emit external Skill/plugin/framework names as required execution steps.
4. TDD, verification, review, debugging, planning, or similar methods are expressed as behavior/acceptance requirements owned by Engineering Governance or the project authority, not as external Skill dependencies.
5. If a missing reusable capability is discovered, return to the owning Engineering Governance capability, extend an existing Skill/module when appropriate, and add a new capability only under the repository's existing capability-model rules.
6. `execution-orchestrator` remains the owner for Engineering Governance delegation/topology. Concrete model/reasoning values remain environment-owned and external frameworks cannot override or escalate them.
7. Existing external documents/paths may remain as historical/reference artifacts; path names alone do not create an execution dependency.

## Acceptance / distribution

- Add focused acceptance cases proving external framework names cannot enter a governed engineering Handoff Card as execution requirements and cannot take over execution/model/review routing.
- Bump the distributed Plugin source to `0.7.5` without moving the formal `plugin-v0.7.3` GitHub release/tag.
- Update the existing private Web Plugin in place, preserving plugin identity, scope and discoverability.
- Local Git-backed marketplace remains `engineering-governance-personal` -> `Lost0rz/Engineering-Governance@main`; local runtime refresh is a separate installation observation and must not be claimed without target-machine evidence.

## Prior task reconciliation

Task `EG-PLUGIN-V0.7.4-WEB-LOCAL-SYNC-090` completed its Web 0.7.4 synchronization. Its still-pending local 0.7.4 refresh is superseded by this 0.7.5 distribution; users should refresh directly to the new source after Task 091 source/Web delivery is complete.

## Stop boundary

Stop after source/remote delivery, Web Plugin 0.7.5 readback, control alignment, and local refresh instructions are established. Do not claim local installed/runtime 0.7.5 acceptance without fresh target-machine evidence.

# CURRENT TASK — Bootstrap Minimal Control Plane Plan Review

Task ID: `EG-V01-BOOTSTRAP-PLAN-006`

State: `WAITING_FOR_USER_PLAN_REVIEW`

Mode: `ARCHITECTURAL_PLAN_REVIEW`

## Objective

Review and either accept or revise the implementation plan for the first usable Bootstrap slice. No Bootstrap product implementation is authorized by this planning task.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Planning baseline before the new plan file: clean accepted `main` at `e9cb360c252b0f402edc9da7801fbec0462029e3`.
- Plan file: `docs/superpowers/plans/2026-10-07-bootstrap-minimal-control-plane-implementation-plan.md`.
- Plan commit: `6f648b5e2bb9ab1d5c096bf0069de0dd9bd4cf6d`.
- Accepted design contract: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- Stable tag `v0.1.0` must remain at `738627a0caad330d277f60cfdaff5f153593135e`.

## Proposed first Bootstrap slice

Public surface proposed by the plan:

```text
PYTHONPATH=src python3.11 -m engineering_governance bootstrap preview <target> \
  --template minimal-control-plane.v1 \
  --project-name <explicit-project-name> \
  --actor <explicit-human-actor>

PYTHONPATH=src python3.11 -m engineering_governance bootstrap apply <target> \
  --template minimal-control-plane.v1 \
  --project-name <same-project-name> \
  --actor <same-human-actor> \
  --confirm-plan sha256:<exact-preview-plan-digest>
```

Key scope decisions for user review:

1. One approved template only: `minimal-control-plane.v1`.
2. It renders exactly three root controls: `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.
3. Generic Bootstrap does not invent active work. `CURRENT_TASK.md` starts as `Task ID: NONE`, `State: NO_ACTIVE_TASK`, `Mode: IDLE`.
4. Project name and apply actor must be explicitly supplied; they are not inferred from directory, account, Git author, or repository metadata.
5. Preview is read-only and emits an immutable JSON plan with a `sha256:` identity.
6. Apply is a separate command and requires the exact preview identity plus the same actor/project/template inputs.
7. Existing exact starter files are `NO_CHANGE`; any differing candidate path or ambiguous path type is `CONFLICT / STOP` and is never overwritten.
8. Apply uses create-if-absent writes only. Concurrent appearance cannot be overwritten.
9. First slice requires a clean target at preview and apply. Dirty-target support is deferred to avoid building a broad state-fingerprint subsystem before it is needed.
10. Exit semantics remain `0` truthful success/NO_CHANGE, `2` unsafe/fatal STOP, `3` internal fatal.

## Implementation-plan structure

The plan contains four independently reviewable TDD tasks:

1. Bootstrap model/template plus one clean-state Git probe.
2. Read-only preview and stable plan identity.
3. Exact-plan apply with exclusive create safety and idempotence.
4. CLI integration, README, full regression, and Draft-PR handoff.

The implementation plan deliberately does not add a template registry, profile inheritance, migration, repair, Audit, AI runtime, MCP, remote queries, installer/package framework, enforcement, daemon, database, or new diagnostic program.

## Review gate

No local implementation, worktree, task branch, product commit, or PR is authorized while this task is `WAITING_FOR_USER_PLAN_REVIEW`.

User approval should answer whether this plan captures the intended first Bootstrap capability. If approved, Web will create a separate implementation task, authorize one implementation branch, and hand the accepted plan to local Codex under the normal TDD + independent-Web-review workflow.

If the user requests a scope change, revise the plan and keep implementation unauthorized until the revised plan is approved.

## Current stop point

`WAITING_FOR_USER_PLAN_REVIEW`

Do not begin Bootstrap implementation yet.
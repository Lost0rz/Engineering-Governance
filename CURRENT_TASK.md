# CURRENT TASK — Doctor Foundation Implementation Plan

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`

Mode: `PLAN_REVIEW_HANDOFF`

## Objective

Create a reviewable implementation plan for the smallest coherent first implementation slice from the accepted tooling design: the shared local reader/model plus local read-only Doctor checks for repository identity and control-plane presence/consistency.

This task writes a plan only. It does not authorize executable implementation.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Plan branch: `codex/eg-v01-doctor-foundation-plan`.
- Parent accepted-design control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- Accepted design spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- PR #2 remains the design PR and must remain design-only / unmerged unless separately authorized.

## Planning method

Use the `superpowers:writing-plans` method. Before writing the plan, inspect the accepted spec and current repository structure. The plan must be precise enough for a fresh implementer to execute task-by-task using TDD, with exact files, interfaces, test names/assertions, verification commands, and commit boundaries.

Save the plan at:

`docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`

## Scope — first implementation slice only

Plan only these capabilities:

1. a small shared local repository reader/model sufficient for Doctor;
2. deterministic target repository/root identity observation using local filesystem/Git state only;
3. read-only discovery/readability checks for `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`;
4. basic deterministic consistency checks that do not require product/domain judgment, remote queries, or deeper Audit semantics;
5. one immutable/versioned Doctor base report emitted to stdout;
6. command execution exit semantics consistent with the accepted spec;
7. tests proving Doctor makes no target file, Git ref, branch, worktree, remote, or hidden-state mutation;
8. synthetic fixture repositories for PASS, UNVERIFIED/UNKNOWN, malformed-root fatal STOP, and no-mutation cases.

## Phase-1 implementation assumptions to plan against

- Host/support floor for this first slice: macOS on Apple silicon, Python 3.11+.
- Prefer Python standard library only; adding a third-party runtime dependency requires STOP and Web/user review.
- The runtime choice is a Phase-1 tool implementation constraint, not a change to `EngineeringGovernanceStandard 0.1.0` and not a promise of cross-platform support.
- Default Doctor behavior is offline/local and must not fetch/update refs or make network calls.
- No persistent database, cache, background process, or report store.

## Required plan decisions

The plan must freeze, for this first slice only:

- exact future source/test/fixture paths;
- module boundaries and exact public/internal function or class signatures needed between tasks;
- the minimal report envelope fields and deterministic serialization/output choice needed for tests and future consumers;
- exact mapping of evaluation-level unresolved conditions versus command-level fatal/unsafe failures;
- exact exit-code behavior for the first slice;
- how repository identity/root is observed without mutating the target;
- how control-file presence/readability/consistency is represented without inventing project facts;
- how no-mutation is verified before/after Doctor runs;
- task decomposition into independently reviewable, TDD-sized increments.

The plan must remain compatible with future Bootstrap/Audit reuse of the shared model but must not pre-build their functionality.

## Explicitly forbidden

Do not create or modify executable source, tests, fixtures, package/dependency manifests, schemas, CLI entry points, skills, templates, check registries, or pilot repositories in this task.

Do not plan or implement:

- Bootstrap writes;
- deeper Audit/check-registry execution;
- AIContribution execution/composition;
- remote GitHub/PR queries;
- enforcement/CI gates;
- MCP;
- daemon/background monitoring;
- migration/remediation;
- cross-platform support beyond the Phase-1 floor;
- unrelated repository cleanup/refactor.

## Plan review handoff

- Plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.
- Planning method: `superpowers:writing-plans`.
- Self-review completed for spec coverage, step granularity, type/interface consistency, Review Focus coverage, and proportion.
- The plan has five TDD implementation tasks and thirteen Review Focus cases.
- Current-task changes are limited to this plan and the two control-plane files; no source, test, fixture, manifest, schema, CLI, or implementation was created.
- The task branch must be committed/pushed, then a Draft stacked PR must target `codex/eg-v01-tooling-design` so the plan diff stays separate from PR #2.
- Verify local/remote HEAD equality and a clean worktree, then stop. Do not execute the plan.

## Required receipt

```text
TASK_ID:
CONTROL_START_HEAD:
FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

PLAN_PATH:
PLAN_METHOD: superpowers:writing-plans
FIRST_SLICE_ONLY: YES
PHASE1_RUNTIME:
THIRD_PARTY_DEPENDENCIES_PLANNED: NO
BOOTSTRAP_PLANNED: NO
AUDIT_PLANNED: NO
AI_EXECUTION_PLANNED: NO
REMOTE_QUERY_PLANNED: NO
IMPLEMENTATION_STARTED: NO

PLAN_TASK_COUNT:
REVIEW_FOCUS_COUNT:
SPEC_COVERAGE_SELF_REVIEW:
TYPE_INTERFACE_SELF_REVIEW:
NO_MUTATION_TESTS_PLANNED:
EXIT_SEMANTICS_PLANNED:

CHANGED_PATHS:
DRAFT_STACKED_PR:
FINAL_STATE: WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW | STOP
STOP_REASON:
```

STOP on unexpected branch/head drift, unknown local work, any need for a third-party dependency, scope expansion beyond the first slice, or any newly discovered contradiction with the accepted spec or standard.

# CURRENT TASK — Doctor Foundation Implementation Plan Review Handoff

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`

Mode: `PLAN_REVIEW_HANDOFF`

## Objective

Submit the corrected first-slice Doctor implementation plan for independent review. This remains plan-only; no source, tests, fixtures, manifests, schemas, CLI, or executable implementation is authorized.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-doctor-foundation-plan`.
- Corrective control start: `6e28053e82044879d53b5945638353a0cb8d4287`.
- Accepted design control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- Accepted design spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- PR #3 remains OPEN / DRAFT / UNMERGED, stacked on `codex/eg-v01-tooling-design`.

## Corrective Handoff

Plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.

- **MAJOR 1 — TDD sequence:** Resolved with four implementation tasks and a verification-only Task 5. Task 2 contains all allowed/prohibited Git command tests before allowlist implementation. Task 4 contains dirty-target and linked-worktree no-mutation tests before `run_doctor`. Task 5 adds no behavior tests and has no implementation commit.
- **MAJOR 2 — Exact test surface:** Tasks 1–4 name each `test_*`, setup, key assertions, expected RED reason, and focused command reused for GREEN.
- **MAJOR 3 — Task ID boundary:** IDs use the exact ASCII grammar and case-sensitive literal match with identifier boundaries `[A-Za-z0-9._/-]`; tests cover exact, backtick, prose, prefix, suffix, embedded, slash/dot, and missing-reference cases.
- The first-slice scope, Python 3.11+/stdlib-only runtime, offline/local behavior, immutable report, read-only boundary, and exit `0`/`2`/`3` contract are preserved.
- The accepted tooling spec and `EngineeringGovernanceStandard 0.1.0` are unchanged.

## Validation and Handoff

- Re-read `AGENTS.md`, `CURRENT_STATUS.md`, this task, the accepted spec, and the full implementation plan.
- Re-ran writing-plans self-review for spec coverage, step granularity, types/interfaces, Review Focus, and proportion; explicitly reviewed all eight corrective criteria.
- Static plan/scope review only; no implementation tests were run or added.
- Allowed changed paths are only this plan and `CURRENT_STATUS.md` / `CURRENT_TASK.md`.
- Commit/push this same branch, verify local/live remote HEAD equality and a clean worktree, then stop at `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`.
- Keep PR #3 Draft and unmerged. Do not execute the plan.

## Required Receipt

```text
TASK_ID:
CONTROL_START_HEAD: 6e28053e82044879d53b5945638353a0cb8d4287
FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

MAJOR_1_TDD_SEQUENCE_RESOLVED:
MAJOR_2_EXACT_TEST_SURFACE_RESOLVED:
MAJOR_3_TASK_ID_MATCH_RULE_RESOLVED:
IMPLEMENTATION_TASK_COUNT: 4
VERIFICATION_ONLY_GATE_PRESENT: YES
ALL_IMPLEMENTATION_TASKS_HAVE_GENUINE_RED: YES
TEST_NAMES_AND_KEY_ASSERTIONS_FROZEN: YES
TASK_ID_BOUNDARY_TESTS_DEFINED: YES

FIRST_SLICE_ONLY: YES
THIRD_PARTY_DEPENDENCIES_PLANNED: NO
IMPLEMENTATION_STARTED: NO
ACCEPTED_SPEC_CHANGED: NO
STANDARD_CHANGED: NO

CHANGED_PATHS:
PR_STATE:
FINAL_STATE: WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW | STOP
STOP_REASON:
```

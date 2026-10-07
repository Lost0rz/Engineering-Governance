# CURRENT TASK — Doctor Foundation First-Slice Implementation

Task ID: `EG-V01-DOCTOR-FOUNDATION-IMPL-004`

State: `ACTIVE — TDD IMPLEMENTATION`

Mode: `DOCTOR_FOUNDATION_FIRST_SLICE`

## Objective

Execute the accepted Doctor foundation implementation plan exactly through Tasks 1–4 plus the verification-only Task 5 gate, then stop for independent Web code audit. Do not expand the slice.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-doctor-foundation-impl`.
- Draft PR #4: OPEN / DRAFT / UNMERGED; base `codex/eg-v01-doctor-foundation-plan`, head `codex/eg-v01-doctor-foundation-impl`.
- Parent accepted-plan control head: `534fce576ddbf78e4b7fdaeacc39ec9c5ed58c33`.
- Accepted plan content head: `1aa9f4b0e42e73d7e0433fe4c0297b1b0e5eea61`.
- Accepted spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.
- PR #2 and PR #3 remain OPEN / DRAFT / UNMERGED; do not merge them in this task.

## Execution method

1. Use `superpowers:using-git-worktrees` and work in one isolated task worktree. If the canonical checkout is not already isolated, prefer the platform-native worktree mechanism; if unavailable, use a disposable external worktree rather than changing repository ignore rules. Record the worktree path and remove it only after final merge/closeout, not during implementation.
2. Use `superpowers:executing-plans` for continuous task-by-task execution and load `superpowers:test-driven-development` before Task 1.
3. Read the accepted spec and full accepted plan before implementation. The spec is binding; the plan is the reviewed execution contract.
4. Follow the plan's exact task order, tests, interfaces, file ownership, RED/GREEN commands, and four commit boundaries.
5. Every production behavior requires a failing named test first. If a named test passes before its production behavior exists, STOP that task and correct the test/plan interpretation before writing production code.
6. Do not pause for routine confirmation between Tasks 1–4. STOP only for remote/control HEAD drift, unknown local work, destructive/irreversible action, third-party dependency need, scope expansion, or a plan/spec contradiction that cannot be resolved without changing the accepted contract.

## Authorized implementation scope

Implement only the exact paths and behavior defined by the accepted plan:

- `src/engineering_governance/__init__.py`
- `src/engineering_governance/model.py`
- `src/engineering_governance/report.py`
- `src/engineering_governance/git_reader.py`
- `src/engineering_governance/control_reader.py`
- `src/engineering_governance/doctor.py`
- `tests/support.py`
- `tests/test_model.py`
- `tests/test_report.py`
- `tests/test_git_reader.py`
- `tests/test_control_reader.py`
- `tests/test_doctor.py`
- the accepted `tests/fixtures/doctor/**` fixture paths
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` only for implementation progress/handoff state.

Do not add `pyproject.toml`, requirements files, CLI entry points, schemas, skills, templates, check registries, persistent stores, or other production paths.

## Task gates

### Task 1

Shared immutable model and deterministic report identity. Write the accepted named tests first, prove RED, implement minimally, prove GREEN, commit exactly the Task 1 paths.

### Task 2

Local repository identity plus exact Git read-only subprocess contract and allowlist. Write all positive/negative adapter tests first, prove RED, implement minimally, prove GREEN, commit exactly the Task 2 paths.

### Task 3

Root control observations and deterministic Task ID/status consistency. Write fixture/test surface first, prove RED, implement minimally, prove GREEN, commit exactly the Task 3 paths.

### Task 4

Doctor orchestration, exit `0` / `2` / `3`, timeout mapping, and dirty-repository/linked-worktree no-mutation proof. Add Task-4 snapshot support and tests first, prove RED on absent `run_doctor`, implement minimally, prove GREEN, then run the full suite and commit exactly the Task 4 paths.

### Task 5 — verification-only

No source/test changes and no implementation commit. Run the full suite, verify no-mutation snapshots, inspect the recorded Git adapter calls, inspect final diff/status, and classify PASS/STOP exactly as the plan requires.

## Evidence and push discipline

- Retain the exact RED and GREEN command/result for every Task 1–4.
- Run the full suite after Task 4 and again at Task 5.
- Each Task 1–4 must end in its own plan-defined commit. Do not squash during implementation.
- Push PR #4's implementation branch after each completed task commit or, at minimum, before moving to the next task if remote durability would otherwise be lost.
- Maintain PR #4 as Draft throughout implementation. Do not retarget or merge it.
- Update control files only for meaningful task/progress/handoff state; do not rewrite the accepted spec or plan.

## Final handoff

After Task 5 PASS:

- run the full suite one final time;
- verify local branch HEAD equals live remote implementation branch HEAD;
- verify implementation worktree clean;
- update `CURRENT_STATUS.md` and `CURRENT_TASK.md` to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
- commit/push that handoff control state;
- keep PR #4 Draft / unmerged;
- do not merge or start Bootstrap/Audit/AI/CLI follow-on work.

Required final receipt:

```text
TASK_ID:
CONTROL_START_HEAD:
IMPLEMENTATION_BRANCH:
WORKTREE_PATH:

TASK1_RED:
TASK1_GREEN:
TASK1_COMMIT:
TASK2_RED:
TASK2_GREEN:
TASK2_COMMIT:
TASK3_RED:
TASK3_GREEN:
TASK3_COMMIT:
TASK4_RED:
TASK4_GREEN:
TASK4_COMMIT:

FULL_SUITE_AFTER_TASK4:
TASK5_VERIFICATION_GATE:
FINAL_FULL_SUITE:
NO_MUTATION_DIRTY_REPO:
NO_MUTATION_LINKED_WORKTREE:
NETWORK_CAPABLE_GIT_CALLS_OBSERVED: NO
THIRD_PARTY_DEPENDENCIES_ADDED: NO

FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:
IMPLEMENTATION_PR: #4

CHANGED_PATHS:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT | STOP
STOP_REASON:
```

Do not claim PASS without current test output and final branch/worktree verification.

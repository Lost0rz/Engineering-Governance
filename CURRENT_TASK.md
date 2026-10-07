# CURRENT TASK — Doctor Foundation Final Plan Corrective

Task ID: `EG-V01-DOCTOR-FOUNDATION-PLAN-003`

State: `ACTIVE — FINAL PLAN CORRECTIVE AFTER WEB REVIEW`

Mode: `PLAN_CORRECTIVE_ONLY`

## Objective

Correct two remaining implementation-plan blockers discovered by independent Web re-review. Preserve the accepted design, first-slice scope, four implementation tasks, verification-only gate, Python 3.11+/stdlib-only runtime, offline/read-only boundary, and exit semantics. This remains plan-only; implementation is not authorized.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-doctor-foundation-plan`.
- Executor corrective handoff reviewed by Web: `da080d32b8c167a0f2687f7e3fdbdb037f7f5a49`.
- Accepted design control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- Accepted design spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Plan: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`.
- PR #3 remains OPEN / DRAFT / UNMERGED.

## Findings already accepted

The prior three plan findings are resolved and must remain resolved:

1. Task 2 owns all Git allowlist positive/negative tests before implementation; Task 5 is verification-only.
2. Tasks 1–4 have exact named tests, setups, key assertions, RED reasons, and GREEN commands.
3. Task ID grammar and status-reference boundary matching are deterministic and collision-tested.

## Required final corrective

### BLOCKER A — Task 4 file/commit boundary must match no-mutation support ownership

The plan assigns temporary repository builders and before/after mutation snapshots to `tests/support.py`, and Task 4's dirty-repository / linked-worktree acceptance tests depend on those helpers. However Task 4 currently lists and commits only `tests/test_doctor.py` plus `src/engineering_governance/doctor.py`.

Resolve this without prebuilding Task 4 behavior in Task 2:

- keep generic temporary-repository helpers in Task 2 only where Task 2 itself needs them;
- put Task-4-specific snapshot/no-mutation helpers in Task 4;
- add `tests/support.py` to Task 4 Files and Task 4 commit boundary if it changes there;
- ensure Task 4 RED is still caused by absent `run_doctor`, not by a missing support helper that should have been available to the test;
- do not add implementation outside the four-task first slice.

The exact file map, task Files block, RED sequence, and commit command must agree.

### BLOCKER B — Real subprocess adapter safety contract must have named tests

The plan normatively requires `run_git_readonly` to use `shell=False`, a bounded timeout, `GIT_OPTIONAL_LOCKS=0`, `GIT_TERMINAL_PROMPT=0`, and to reject non-allowlisted tuples before subprocess execution. The negative allowlist tests cover rejection, but the real allowed-command adapter invocation is not currently pinned by a named test.

In Task 2 add one or more named tests, before implementation, that patch `subprocess.run` and assert for an allowed tuple:

- exact argv starts with `git` and contains only the allowed tuple;
- `cwd` is the supplied path;
- `shell=False`;
- the bounded timeout is passed;
- environment passed to the subprocess includes `GIT_OPTIONAL_LOCKS=0` and `GIT_TERMINAL_PROMPT=0` while preserving the process environment needed to locate Git;
- stdout/stderr capture and text decoding behavior is deterministic enough to construct `CommandResult`;
- no remote/network argument is introduced.

Also pin timeout behavior conceptually: if the local Git probe times out while establishing required repository/root identity, the caller must classify the inability to establish trusted identity as command-level STOP (`2`), not a governance result. Do not expand into retry/backoff/network logic.

## Scope preserved

Do not change:

- accepted tooling spec or `EngineeringGovernanceStandard 0.1.0`;
- first-slice capability set;
- four TDD implementation tasks plus verification-only Task 5;
- Python 3.11+, standard library only;
- offline/local Doctor;
- immutable report and exit `0` / `2` / `3` contract;
- Task ID grammar/boundary rule;
- Bootstrap/Audit/AI/remote-query exclusions.

Allowed changed paths in this corrective:

- `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`
- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

No source, test, fixture, manifest, schema, CLI, or implementation file may be created.

## Validation and handoff

After correcting the plan:

1. re-check the exact file map against each task's Files block and commit command;
2. prove each implementation task still has a genuine RED before implementation;
3. confirm the real Git adapter safety flags are pinned by named tests with key assertions;
4. confirm Task 4 owns any Task-4-specific `tests/support.py` changes;
5. rerun writing-plans self-review for spec coverage, type/interface consistency, Review Focus, step granularity, and proportion;
6. update `CURRENT_STATUS.md` and this task back to `WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW`;
7. commit/push the same branch, verify local/remote HEAD equality and clean worktree;
8. keep PR #3 Draft/unmerged and return the receipt below.

Required receipt:

```text
TASK_ID:
CONTROL_START_HEAD:
FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

BLOCKER_A_TASK4_SUPPORT_BOUNDARY_RESOLVED:
BLOCKER_B_REAL_GIT_ADAPTER_TESTED:
TASK4_SUPPORT_FILE_IN_FILES_AND_COMMIT_IF_CHANGED:
REAL_ADAPTER_NAMED_TESTS:
TIMEOUT_CLASSIFICATION_PINNED:
ALL_IMPLEMENTATION_TASKS_STILL_HAVE_GENUINE_RED:
FOUR_IMPLEMENTATION_TASKS_PRESERVED:
VERIFICATION_ONLY_GATE_PRESERVED:
FIRST_SLICE_ONLY: YES
IMPLEMENTATION_STARTED: NO
ACCEPTED_SPEC_CHANGED: NO
STANDARD_CHANGED: NO

CHANGED_PATHS:
PR_STATE:
FINAL_STATE: WAITING_FOR_IMPLEMENTATION_PLAN_REVIEW | STOP
STOP_REASON:
```

STOP on unexpected remote-head drift, unknown local work, third-party dependency need, scope expansion, or any contradiction requiring accepted spec/standard changes.
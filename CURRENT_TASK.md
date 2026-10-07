# CURRENT TASK — Doctor CLI Productization

Task ID: `EG-V01-DOCTOR-CLI-005`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_FEATURE_TDD`

## Objective

Turn the already accepted local/offline/read-only Doctor engine into a directly usable command-line feature with one minimal module entry point:

`python3.11 -m engineering_governance doctor <target>`

The CLI must delegate to the existing Doctor implementation rather than creating a second execution path or report authority.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Authorization baseline before this task-start control update: `main` at `28c070ceb6d36d1a197cb9e1b25b899507dd8161`.
- Authorized task branch: `codex/eg-v01-doctor-cli`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- Accepted tooling design: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Accepted Doctor foundation: merged and closed under `EG-V01-DOCTOR-FOUNDATION-IMPL-004`.
- Stable tag `v0.1.0` must remain at `738627a0caad330d277f60cfdaff5f153593135e`.

## Approved bounded design

Implement only the thin CLI adapter needed to invoke existing `run_doctor()` behavior from a shell.

Required user path:

```text
python3.11 -m engineering_governance doctor <target>
```

Required behavior:

1. Resolve `<target>` as the explicit target passed to Doctor; do not silently substitute another repository.
2. Delegate Doctor execution to the existing `run_doctor()` implementation using the existing read-only Git reader, filesystem reader, and a current timezone-aware UTC clock.
3. Preserve Doctor stdout as the existing single JSON report on successful/reportable execution.
4. Preserve Doctor command exit semantics: normal truthful report returns `0`; Doctor unsafe/fatal STOP returns `2`; internal fatal returns `3`.
5. CLI usage errors such as a missing target or unsupported subcommand must return nonzero and must not run Doctor or mutate repository state. Standard library argument parsing is sufficient; do not invent a command framework.
6. Keep default execution local/offline/read-only. No fetch, pull, ref update, branch/worktree mutation, file write, repair, migration, or remote API operation may be introduced.
7. Correct the root README statement that Doctor is not implemented and document the minimal invocation. Do not claim Bootstrap or Audit are implemented.

Implementation may add a minimal module entry point and, only if it improves separation without expanding scope, one small CLI adapter module. Reuse the existing model, readers, report builder, and Doctor orchestration.

## Explicitly out of scope

- new Doctor checks or broader evidence collection;
- remote branch/PR queries;
- Bootstrap implementation;
- deeper Audit implementation;
- AI contribution/runtime;
- MCP, daemon/background services, enforcement, auto-remediation, or migration;
- package publishing, installer work, console-script packaging, dependency/framework additions;
- report schema redesign or persistent report storage;
- pilot repository integration;
- unrelated refactors.

## Executor evidence — 2026-10-07

- Control head: `f1fba7f9591047f6e2f40e677f79048227d67d8e`; live `origin/main` matched this exact SHA before task work. Baseline main was clean at the same SHA.
- Isolated worktree: `/Users/ox_miles/.codex/worktrees/eg-v01-doctor-cli/Engineering-Governance`, on `codex/eg-v01-doctor-cli`.
- Baseline command `PYTHONPATH=src python3.11 -m unittest discover -s tests -v`: 52 tests, 0 failures.
- RED command `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_cli.py' -v`: 4 expected failures; the package had no `engineering_governance.__main__` entry point.
- GREEN focused command `PYTHONPATH=src python3.11 -m unittest discover -s tests -p 'test_cli.py' -v`: 4 tests passed.
- Final full command `PYTHONPATH=src python3.11 -m unittest discover -s tests -v`: 56 tests, 0 failures.
- CLI behavior: valid fixture target exits 0 and emits one JSON report; non-repository STOP exits 2 with no JSON; missing target and unsupported `audit` command each exit 2, and the usage tests confirm `run_doctor()` is not called.
- Read-only invariant: the CLI test's before/after snapshot of dirty target files and Git metadata is identical. Existing Doctor and Git-reader mutation/command-allowlist tests also pass.
- Scope audit: no dependency, packaging, or framework files added; the CLI delegates to existing `run_doctor()`, `run_git_readonly`, and `Path.read_bytes`; no remote Git/network operation or Doctor check was added.
- README now documents the supported invocation and leaves Bootstrap/Audit unimplemented. `v0.1.0^{commit}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Implementation commit: `40cedb3ab21130ca773ec20519d1b8d669b24422`. Draft PR #5 targets `main` and is open/unmerged.
- Product changed paths: `README.md`, `src/engineering_governance/__main__.py`, `tests/test_cli.py`. `CURRENT_STATUS.md` and `CURRENT_TASK.md` contain this synchronized handoff state.
- The task worktree and branch remain active for independent Web audit; no merge, release, tag movement, or cleanup occurred.

## Execution gates

### Gate 0 — control and freshness

From the canonical checkout:

1. `git fetch origin --prune --tags`.
2. Verify repository identity is exactly `Lost0rz/Engineering-Governance`.
3. Read `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` from the fetched control head.
4. Require this task ID/state/branch authorization to be present.
5. Require canonical `main` has no unknown dirty/untracked work and no unique local commits absent from `origin/main`.
6. Fast-forward canonical `main` only. STOP on divergence, unknown local work, or control-plane drift.

### Gate 1 — isolated workspace and baseline

Use an isolated worktree for `codex/eg-v01-doctor-cli`. Detect existing isolation first; do not create a nested worktree. No force/reset/clean/stash may be used to hide state.

Before any product change run exactly:

`PYTHONPATH=src python3.11 -m unittest discover -s tests -v`

Expected accepted baseline: 52 tests, 0 failures. If the live baseline differs, report the exact result and STOP rather than normalizing it silently.

### Gate 2 — RED first

Follow test-driven development. Production CLI code is not permitted before a failing CLI test is observed.

Add focused CLI tests for the minimum public behavior, including at least:

- `doctor <target>` invokes the existing Doctor path and emits a report with exit `0` for a valid fixture;
- Doctor STOP propagates as exit `2` with no JSON report for an invalid/non-repository target;
- missing target or unsupported command is rejected without invoking Doctor;
- invoking through the CLI does not mutate dirty repository contents or Git metadata.

Run only the new focused CLI test set and capture the expected RED result. RED must be caused by the absent CLI behavior, not by a broken fixture, import typo, or unrelated regression. If tests unexpectedly pass before implementation, STOP and explain what behavior already exists.

### Gate 3 — minimal GREEN implementation

Implement only enough CLI/module-entry code to make the approved focused tests pass. Reuse `run_doctor()`, `run_git_readonly`, `Path.read_bytes`, and a timezone-aware UTC clock. Do not duplicate Doctor report construction or Git probing logic.

Run the focused CLI tests until GREEN.

### Gate 4 — full regression and read-only proof

Run exactly:

`PYTHONPATH=src python3.11 -m unittest discover -s tests -v`

Require all tests to pass. Report the exact total test count and failures.

Also verify:

- no dependency files or packaging framework were added;
- no network/remote Git operations were introduced by the CLI path;
- Doctor/read-only mutation invariants remain covered and passing;
- `v0.1.0^{commit}` is still `738627a0caad330d277f60cfdaff5f153593135e`.

### Gate 5 — documentation and scope audit

Update README only enough to state that Doctor's first local CLI slice exists, show the supported invocation, and keep Bootstrap/Audit described as not yet implemented.

Inspect the final diff. Every changed path must be attributable to CLI implementation/tests, README correction, or required task-control updates. STOP on unrelated changes.

### Gate 6 — handoff, no merge

Commit the authorized changes on `codex/eg-v01-doctor-cli`, push the exact branch, and open a Draft PR targeting `main`.

Update `CURRENT_STATUS.md` and `CURRENT_TASK.md` on the task branch to record exact implementation/test evidence and set the task state to `WAITING_FOR_INDEPENDENT_WEB_AUDIT` only after all gates pass.

Before handoff require:

- local task HEAD equals remote task branch HEAD;
- worktree is clean;
- Draft PR is open and unmerged;
- no merge, release, tag movement, Bootstrap/Audit/AI work, or lifecycle cleanup has been performed.

## Required handoff

Return exactly enough evidence for independent Web audit:

```text
TASK_ID:
CONTROL_HEAD:
BASELINE_MAIN:
AUTHORIZED_BRANCH:
WORKTREE:

BASELINE_SUITE:
RED_TEST_COMMAND:
RED_EXPECTED_FAILURES:
GREEN_FOCUSED_TESTS:
FULL_SUITE:

CLI_INVOCATION:
CLI_VALID_TARGET_EXIT:
CLI_STOP_EXIT:
CLI_USAGE_ERROR_EXIT:
READ_ONLY_PROOF:
README_UPDATED:
V0_1_TAG_TARGET:

CHANGED_PATHS:
IMPLEMENTATION_COMMIT:
TASK_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:
PR_NUMBER:
PR_STATE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT | STOP
STOP_REASON:
```

Do not merge the PR. Independent Web review is the next authority after executor evidence.

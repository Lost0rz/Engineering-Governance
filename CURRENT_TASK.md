# CURRENT TASK — Doctor CLI Productization

Task ID: `EG-V01-DOCTOR-CLI-005`

State: `MERGED — LOCAL_CLOSEOUT_PENDING`

Mode: `POST_MERGE_LOCAL_VERIFICATION`

## Objective

Finish lifecycle closeout for the merged Doctor CLI slice. Product implementation and independent Web audit are complete. The only authorized work now is local verification on merged `main` plus safe cleanup of the retained task worktree/branch after proving no unique local-only work exists.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- PR: #5, MERGED / CLOSED.
- Merge commit: `104b6cdd9182d5a0494fafaf3bae814d24db0f0b`.
- Audited PR head: `e5a5a83af784a20f13ae06b4ec6e24c4cd551b62`.
- Merge tree = audited PR-head tree: `bf8ab10fdfe0fe187742095bb159e779430dcfd4`.
- Authorized task branch retained for closeout only: `codex/eg-v01-doctor-cli`.
- Product implementation commit: `40cedb3ab21130ca773ec20519d1b8d669b24422`.
- Accepted standard: `EngineeringGovernanceStandard 0.1.0`.
- Stable tag `v0.1.0` must remain at `738627a0caad330d277f60cfdaff5f153593135e`.

## Accepted implementation

The merged feature exposes:

`PYTHONPATH=src python3.11 -m engineering_governance doctor <target>`

It is a thin CLI adapter over the existing read-only Doctor path. No new Doctor checks, remote queries, Bootstrap, Audit, AI runtime, dependency framework, report authority, enforcement, remediation, or migration were added.

## Pre-merge evidence

- Baseline Python 3.11 suite: 52/52.
- Focused TDD RED: 4 expected failures with `engineering_governance.__main__` absent.
- Focused GREEN: 4/4.
- Final executor Python 3.11 suite: 56/56.
- Independent Web audit: PASS, no Critical or Important findings.
- Independent Web reconstruction reproduced focused RED and GREEN behavior.
- `v0.1.0` remained unchanged.
- Fresh merge gate verified exact audited head and unchanged base before merging.
- GitHub merge commit tree exactly equals audited PR-head tree, so merge integration introduced no product/control content drift.

## Authorized local closeout gate

Do not make product/source/test/spec/plan changes. Do not start another feature.

### Gate 0 — refresh canonical main

From the canonical checkout:

1. `git fetch origin --prune --tags`.
2. Read the latest remote `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`.
3. Require this task to be `MERGED — LOCAL_CLOSEOUT_PENDING` / `POST_MERGE_LOCAL_VERIFICATION`.
4. Require canonical `main` to have no unknown dirty/untracked work and no unique local commits absent from `origin/main`.
5. Fast-forward `main` only to the exact live `origin/main`. STOP on divergence, unknown local work, or control-plane drift.
6. Confirm `v0.1.0^{commit}` is still `738627a0caad330d277f60cfdaff5f153593135e`.

### Gate 1 — verify merged main

Run exactly on canonical merged `main`:

`PYTHONPATH=src python3.11 -m unittest discover -s tests -v`

Expected accepted result: 56 tests, 0 failures.

Also confirm the merged files are present:

- `README.md`
- `src/engineering_governance/__main__.py`
- `tests/test_cli.py`

STOP if the full suite fails, test count is unexpectedly different, required files are missing, or the tag moved.

### Gate 2 — prove retained task state is disposable

Inspect the retained worktree previously reported at:

`/Users/ox_miles/.codex/worktrees/eg-v01-doctor-cli/Engineering-Governance`

and branch:

`codex/eg-v01-doctor-cli`

Prove before cleanup:

1. the worktree is clean;
2. no tracked or untracked local-only files exist there;
3. the local task branch has no commits absent from its remote task branch or merged `main`;
4. the remote task branch head is contained in merged `main`;
5. the PR is merged/closed.

If any unique local work exists, STOP and report it. Do not force-delete, reset, clean, or stash it away.

### Gate 3 — safe lifecycle cleanup

Only after Gates 0-2 PASS:

1. remove the task worktree using ordinary `git worktree remove` from outside that worktree;
2. run `git worktree prune`;
3. delete the local task branch using ordinary `git branch -d`;
4. delete the remote task branch `codex/eg-v01-doctor-cli`;
5. fetch/prune and confirm the task branch is absent locally/remotely;
6. confirm only the canonical expected worktree remains for this repository and canonical `main` is clean and matches `origin/main`.

STOP if ordinary removal/deletion refuses. Do not use `--force` or `-D`.

## Required handoff

Return:

```text
TASK_ID:
CONTROL_HEAD:
REMOTE_MAIN:
LOCAL_MAIN:
LOCAL_MAIN_REMOTE_MATCH:
MAIN_WORKING_TREE:
FULL_SUITE_ON_MERGED_MAIN:
V0_1_TAG_TARGET:

WORKTREE_COUNT_BEFORE:
TASK_WORKTREE_CLEAN:
TASK_WORKTREE_UNIQUE_WORK_FOUND:
TASK_BRANCH_UNIQUE_COMMITS_FOUND:
TASK_REMOTE_HEAD_CONTAINED_IN_MAIN:
TASK_WORKTREE_REMOVED:
WORKTREE_COUNT_AFTER:
LOCAL_TASK_BRANCH_REMOVED:
REMOTE_TASK_BRANCH_REMOVED:

PR_STATE:
UNEXPECTED_LIFECYCLE_RESIDUE:
FINAL_STATE: CLOSED_ACCEPTED_MAIN_ONLY_CLEAN | STOP
STOP_REASON:
```

No product changes and no next feature are authorized during this closeout.

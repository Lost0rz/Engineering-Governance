# CURRENT TASK — Doctor Foundation Post-Merge Local Closeout

Task ID: `EG-V01-DOCTOR-FOUNDATION-IMPL-004`

State: `MERGED — LOCAL_CLOSEOUT_PENDING`

Mode: `POST_MERGE_LOCAL_VERIFICATION`

## Objective

Finish lifecycle closeout after the user-authorized stacked merge. Product/spec/plan/implementation changes are complete and merged. The only remaining work is a fresh local proof on the Mac, followed by safe cleanup of merged task branches/worktree and final control-plane closure.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- PR #2: MERGED / CLOSED at merge commit `a211908048aaefa77a7bf98930d795335d8a3fe5`.
- PR #3: MERGED / CLOSED at merge commit `f9823c59628f6655fde592964bef8e3ba9ea300d`.
- PR #4: MERGED / CLOSED at merge commit `d7e635822f554d9d1121077540085562a62f361f`.
- Audited PR #4 head: `9aa366620f313a7a8fa203ba18b1b43eb98eecd7`.
- Audited/merged tree SHA: `2eefce79982fc35a98e0bc559ea36a064159fc9e`.
- Production corrective head: `69a3347fa17a36c2b24dfd68341fe5af0f697bbb`.
- Accepted plan control head: `534fce576ddbf78e4b7fdaeacc39ec9c5ed58c33`.
- Accepted spec control head: `012f2a8ff314b7800c15a8a538cc8f7f877bf4fa`.
- The stable `v0.1.0` tag must remain at `738627a0caad330d277f60cfdaff5f153593135e`.

## Merge verification already completed by Web

1. Before merge, PR heads were exact and unchanged: #2=`012f2a8f...`, #3=`534fce57...`, #4=`9aa36662...`.
2. PR #2 merged first to `main` with exact-head protection.
3. PR #3 was retargeted to `main`; residual diff was only accepted implementation plan + control history, then exact-head merged.
4. PR #4 was retargeted to `main`; residual diff was only accepted Doctor implementation/tests/fixtures + control history, then exact-head merged.
5. Final PR #4 merge commit tree exactly equals the audited implementation head tree (`2eefce79982fc35a98e0bc559ea36a064159fc9e`), so stacked integration introduced no content drift.
6. PR #2/#3/#4 are all terminal `closed + merged`.

## Authorized local closeout gate

Run only on the Mac. Do not make product/source/test/spec/plan changes.

### Gate 0 — refresh and inventory

From the canonical repository:

- `git fetch origin --prune --tags`
- verify repository identity;
- list `git worktree list --porcelain`, `git branch -vv`, remote branches, current branch, HEAD, and `git status --short`;
- STOP on unknown dirty/untracked work or unexplained local-only commits.

### Gate 1 — canonical main

- switch the canonical checkout to `main`;
- require local `main` has no unique commits absent from `origin/main`;
- `git pull --ff-only origin main`;
- require local HEAD equals live `origin/main` and working tree is clean.

### Gate 2 — merged-main verification

Run exactly:

`PYTHONPATH=src python3.11 -m unittest discover -s tests -v`

Require the full Doctor suite to pass on merged `main`. Report the exact test count and failures. Do not claim closeout if this run is red.

Also verify:

- accepted spec exists;
- accepted plan exists;
- Doctor source/tests/fixtures exist;
- `v0.1.0^{commit}` equals `738627a0caad330d277f60cfdaff5f153593135e`.

### Gate 3 — prove task branches/worktree contain no unique local work

For each local task branch that exists:

- `codex/eg-v01-tooling-design`
- `codex/eg-v01-doctor-foundation-plan`
- `codex/eg-v01-doctor-foundation-impl`

prove there are no commits on the local branch that are absent from its corresponding remote branch / merged `main` history.

For every registered task worktree, require `git status --short` empty. In particular reverify the previously reported implementation worktree:

`/Users/ox_miles/.codex/worktrees/doctor-foundation-impl/Engineering-Governance`

If any worktree contains uncommitted/untracked work, STOP and report it. Do not use `--force`, `reset --hard`, `clean -fd`, or stash to hide it.

### Gate 4 — safe cleanup

Only after Gate 3 PASS:

1. remove the clean implementation task worktree with ordinary `git worktree remove` (no `--force`), then `git worktree prune`;
2. delete merged local task branches with ordinary `git branch -d` where they exist;
3. delete remote merged task branches:
   - `codex/eg-v01-tooling-design`
   - `codex/eg-v01-doctor-foundation-plan`
   - `codex/eg-v01-doctor-foundation-impl`
4. fetch/prune again;
5. require one canonical clean `main` checkout and no unexpected task worktrees/branches remain.

STOP if ordinary deletion refuses because Git does not consider a branch merged; do not force-delete. Return the ancestry evidence instead.

## Final handoff

After all gates PASS, return:

```text
TASK_ID:
REMOTE_MAIN:
LOCAL_MAIN:
LOCAL_MAIN_REMOTE_MATCH:
MAIN_WORKING_TREE:
FULL_SUITE_ON_MERGED_MAIN:
V0_1_TAG_TARGET:

WORKTREE_COUNT_BEFORE:
IMPLEMENTATION_WORKTREE_CLEAN:
IMPLEMENTATION_WORKTREE_REMOVED:
WORKTREE_COUNT_AFTER:

DESIGN_LOCAL_UNIQUE_WORK_FOUND:
PLAN_LOCAL_UNIQUE_WORK_FOUND:
IMPL_LOCAL_UNIQUE_WORK_FOUND:
DESIGN_LOCAL_BRANCH_REMOVED:
PLAN_LOCAL_BRANCH_REMOVED:
IMPL_LOCAL_BRANCH_REMOVED:
DESIGN_REMOTE_BRANCH_REMOVED:
PLAN_REMOTE_BRANCH_REMOVED:
IMPL_REMOTE_BRANCH_REMOVED:

UNEXPECTED_LIFECYCLE_RESIDUE:
FINAL_STATE: CLOSED_ACCEPTED_MAIN_ONLY_CLEAN | STOP
STOP_REASON:
```

Do not start Bootstrap, deeper Audit, AI runtime, CLI, or another business task during this closeout.

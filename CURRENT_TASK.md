# CURRENT TASK — Phase A Control Closeout Corrective

Task ID: `EG-SKILLS-RESTRUCTURE-CLOSEOUT-010`

State: `AUTHORIZED_FOR_LOCAL_EXECUTION`

Mode: `CONTROL_CLOSEOUT_CORRECTIVE`

## Objective

Reconcile the task-branch control plane with the already accepted independent Web audit result for Phase A. This task is control-only: update the stale current-state/task records, verify them, push the same branch, and stop for Web re-audit.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Authorized branch: `codex/skill-repository-skeleton-reset`.
- Phase A implementation handoff head audited by Web: `d867327de08410056a225fa4c0111d1a53eeb304`.
- Web audit result: Phase A content/structure/scope/tag integrity passed; merge was blocked only because `CURRENT_STATUS.md` still described the pre-execution state.
- `main` audit baseline: `954593b82a666bebf677636ce4f3cf08c07ceddd`.
- Stable tag target: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- Web has already updated `CURRENT_STATUS.md` on this task branch to record the accepted audit result and this corrective authorization.
- The exact start head for local execution is the live remote task-branch head after this authorization commit; the execution card supplies it and mismatch is a STOP.

## In scope

Only:

1. read the current remote branch controls and verify the Web authorization;
2. confirm the Phase A Skill/content tree has not changed since the audited implementation content except for Web control commits;
3. update `CURRENT_STATUS.md` only if a factual correction is still required by the current remote state;
4. update this `CURRENT_TASK.md` with closeout verification evidence;
5. set this task to `WAITING_FOR_INDEPENDENT_WEB_REAUDIT`;
6. commit and push only the authorized task branch.

## Out of scope

Do not:

- modify any file under `skills/`, `references/`, `examples/`, or `docs/`;
- modify `README.md` or root `AGENTS.md`;
- change Phase A Skill content or structure;
- restore any retired runtime/research path;
- add an installer, CLI, script, runtime, dependency, daemon, service, database, enforcement, remediation, or Repo Map implementation;
- begin Phase B enrichment;
- modify or merge `main`;
- move `v0.1.0`;
- create a new task branch unless the authorized branch cannot be used safely.

## Verification level

`V0 — control/documentation only`.

Required checks:

- `origin/main` remains the expected audit baseline unless Web has explicitly changed it before execution; any unexpected change is a STOP;
- live remote task branch matches the exact execution-card SHA before editing;
- `v0.1.0^{}` remains the expected target;
- diff from the audited implementation handoff to the local execution start contains only Web control-plane changes (`CURRENT_STATUS.md` / `CURRENT_TASK.md`);
- local corrective diff changes only `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`;
- `skills/`, `references/`, `examples/`, `README.md`, `AGENTS.md`, and `docs/` are unchanged from the local execution start;
- final working tree is clean and local/remote task heads match.

## Acceptance criteria

- `CURRENT_STATUS.md` states that Phase A implementation content passed independent Web audit and that this task is a control-only closeout corrective.
- It no longer claims the task is merely `AUTHORIZED_FOR_LOCAL_EXECUTION` for Phase A implementation or that the task-branch live tree still contains the retired runtime.
- `CURRENT_TASK.md` records the closeout check results and ends in `WAITING_FOR_INDEPENDENT_WEB_REAUDIT`.
- No reusable Skill/content file changes occur.
- `origin/main` and the stable tag remain unchanged.
- The authorized branch is pushed, clean, and local/remote matched.

## STOP conditions

STOP and report evidence without fixing if:

- remote task branch HEAD differs from the execution card at start;
- `origin/main` differs unexpectedly from the card;
- stable tag target differs;
- the diff since `d867327de08410056a225fa4c0111d1a53eeb304` includes non-control files;
- the local worktree has unpreserved work;
- completing the task would require changing anything outside `CURRENT_STATUS.md` or `CURRENT_TASK.md`;
- any Skill/content discrepancy is discovered;
- control authority drifts during execution.

## Handoff requirements

Record in this file before the final commit:

- `START_HEAD`;
- `FINAL_HEAD` / `REMOTE_HEAD` (or identify the final handoff commit for Web to resolve);
- `REMOTE_MAIN`;
- `STABLE_TAG_TARGET`;
- changed paths since audited head;
- local corrective changed paths;
- confirmation that no Skill/content file changed;
- `V0_CONTROL_CHECKS`;
- working-tree and local/remote match result.

Then set:

`State: WAITING_FOR_INDEPENDENT_WEB_REAUDIT`

Commit, push, and stop. Do not merge.

## Current stop point

`AUTHORIZED_FOR_LOCAL_EXECUTION`

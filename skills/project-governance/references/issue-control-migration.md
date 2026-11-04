# Target repository migration — FILE_CONTROL to ISSUE_CONTROL

Migration is a **per-repository, explicitly authorized** source/authority transition. Source distribution of Engineering Governance alone does not migrate consuming repositories. The default is backward-compatible FILE_CONTROL until that repository's owning `AGENTS.md` explicitly adopts ISSUE_CONTROL; do not infer migration because a Task file was deleted.

## Preconditions and preflight

1. Read the actual repository `AGENTS.md`, latest `CURRENT_TASK.md`/`CURRENT_STATUS.md` if present, related durable design, open Issues/PRs, literal main and required host rules. Reconcile external stale evidence against GitHub, not old snapshots.
2. Identify live authorized task and potentially overlapping writers, current PR/worktree/unique local-only work (physical local state remains UNKNOWN from a remote-only view); do not reset or delete worktrees.
3. Confirm GitHub Issue read/write access and the identity of authorized approvers across Web connector and local `gh`. Both must be able to access full current spec and relevant receipts. If local permissions prevent reading/writing, do not cut over.
4. Prepare a detailed `EXECUTION_SPEC_V1` Issue for each active task only; preserve exact objective/scope/STOP/evidence, existing PR and `TASK_ID`. Do not bulk-migrate historic closed tasks or fabricate prior approval. Audit quality before READY.
5. Preserve long-lived design/domain/AGENTS normative authority; distinguish current task data from historical snapshot. Do not copy stale PR mergeability/CI into a new current claim.
6. Explicitly record `CUTOVER_BASIS` (migration PR/commit, Issue number, spec revision, verified approval actor/source, any pending acceptance or blocked state).

## Safe change transaction

Under FILE_CONTROL until the cutover:
- Use the existing authorized branch/PR if valid, or one normally permitted migration PR. Where FILE_CONTROL requires a new task bootstrap, its first source-changing carrier begins with control-only authorization/reconciliation. Do not spawn a standalone status-only PR.
- In one ordinary approved migration PR, change AGENTS to `CONTROL_MODE: ISSUE_CONTROL`, update any repository-owned routing/CI/scripts referring to retired files, and remove `CURRENT_TASK.md` and `CURRENT_STATUS.md` from active root **only after** the Issue handoff and approval are demonstrably complete. Git history retains old content. An archive pointer may be retained when project needs, but no copy that looks live.
- Do not mutate an old active product PR solely to change its task number, nor trigger redundant semantic CI because Task/Status content moved.
- **Cutover occurs upon verified merge of the migration PR into the project's authoritative main/ref**, not at branch creation, Issue creation, installation or a comment. Until that event, FILE_CONTROL owns execution. Afterwards ISSUE_CONTROL does; there is no instant with two competing active task authorities.
- On the cutover verify main rules, absence/retired state of old live controls, Issue revision/approval/PR mapping, current branch/host evidence, and local `gh` capability when available. If not verified, report `CUTOVER_UNVERIFIED`; stop any mutation dependent on new mode.

## Existing work cases

| Old state | Action |
| --- | --- |
| no active task | no historical Issue backfill; create new approved Issue when next task authorized |
| active task not started | migrate same identity/scope/STOP into Issue; validate then cut over |
| active task with Draft/Open PR | retain PR/ref and permitted workspace; continue same Issue after cutover |
| code complete, human UI pending | Issue remains awaiting acceptance; preserve independent UI gate |
| PR already merged but stale STATUS/TASK | verify host event, mark old snapshot historical; don't recreate a status PR |
| task cancelled/blocked | migrate only if still decision-relevant; do not imply execution approval |

## Validation and rollback

Validate both FILE_CONTROL compatibility for unadopted projects and ISSUE_CONTROL uniqueness for adopted ones. Negative checks: old file remains live alongside Issue; approval origin unverified; issue cannot be read locally; label says READY but actual plan is incomplete; archived state is treated as live; pre-merge branch is mistaken as cutover; stale former PR reused for unauthorized mutation.

If a migration PR cannot merge, FILE_CONTROL stays active and Issue is pre-cutover planning only. If a post-cutover defect requires reverting, use a separately authorized reverse migration with a verifiable single authoritative state and preservation of unique work; never silently fall back to deleted old files.

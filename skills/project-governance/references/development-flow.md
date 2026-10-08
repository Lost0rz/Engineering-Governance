# Business-first development flow

Use this flow for normal governed product and business work:

1. Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`, along with any relevant project authority.
2. Verify only the repository, ref/revision, runtime, and other baseline facts needed for the authorized work. Before state-changing work, identify the selected task workspace (physical checkout/repository, branch or detached state, HEAD, and working-tree state) and establish its relationship to the task's authorized repository/ref/revision. A project-looking path, symlink, branch or folder name, archived copy, or detached checkout alone does not establish that relationship; an authorized, aligned non-main task worktree is valid.

   Preserve unknown staged, unstaged, untracked, or local-only work; do not reset, stash, delete, overwrite, or force-clean it merely to satisfy an execution card. If the selected workspace relationship or authoritative baseline/control is materially unresolved, stop and reconcile before continuing. Keep discovery task-bounded; expand beyond the selected workspace and relevant repository metadata only when ambiguity, unique work, lifecycle cleanup, or the task decision materially requires it.
3. Identify the affected Domain/capability from accepted semantic authorities already present in the project and any useful navigation projection. Use [Domain Navigation](../../domain-navigation/SKILL.md) when the responsible Domain/capability, authority, code location, symbol, or test is unclear. Do not require a literal `DOMAIN_MAP.md` just because a template exists.
4. Confirm the requested work remains within the active objective and scope. Ordinary evidence discovery that supports the accepted objective does not create a new task. A material objective or scope change requires updating `CURRENT_TASK.md` and re-authorization before continuing.
5. Before implementing source changes that add or change an owner, backend, or writer, identify the existing canonical authority for each affected state or behavior class. Before sharing behavior or splitting modules, apply [Code structure and canonical authority](code-structure.md). Reuse, extend, or explicitly replace an existing authority; reconcile independent writers instead of creating parallel truth. Keep structure decisions within the active task, then implement the smallest authorized product or business outcome.
6. Choose the lightest safe `V0`–`V3` verification level, run its required checks, and record the rationale and observed results.
7. Update only controls whose owned, verified facts materially changed: durable rules in `AGENTS.md`, the current snapshot in `CURRENT_STATUS.md`, and the active authorization or handoff in `CURRENT_TASK.md`.
8. Leave a clean handoff or closeout with the baseline, changed paths, checks, unresolved evidence, and next authorized milestone stated accurately. If the project uses task branches/worktrees, close or retain them according to the repository's verified lifecycle rules; never destroy unknown work merely for cleanup.

## Incident Doctor is on demand

If a real bug or failure appears and existing evidence is sufficient to decide and act safely, address it within the current authorization and verify the change; do not build Doctor or diagnostic infrastructure by default. If the problem is outside the authorized scope, reconcile and re-authorize the task first.

Enter [Incident Doctor](../../incident-doctor/SKILL.md) only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and an evidence gap prevents the needed decision. Keep routine feature delivery separate from diagnostic infrastructure work; add only the minimum diagnosis authorized for the blocked question.

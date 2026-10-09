# Workspace lifecycle and closeout

Apply this contract only when the target project uses task branches, Git worktrees, multiple checkouts, or an equivalent source-controlled task-workspace model. Do not introduce worktrees or extra branches into a project merely to satisfy this reference.

The goal is not “one worktree only.” The goal is that every task-relevant non-canonical workspace has a known owner and lifecycle disposition, conflicting writers are not multiplied, unknown/unique work is preserved, and terminal workspace debt is closed while the evidence is still fresh.

## Core invariants

1. **No unclassified task-relevant workspace.** A workspace that may affect the active task must have a verified relationship to a task/branch/ref and a known current disposition. Projects may use their own lifecycle names; this contract does not impose a universal status enum.
2. **One unresolved writer per capability/authority.** Do not create or select a successor writer workspace for the same capability, state authority, or behavior owner while a predecessor writer is unresolved, has unknown unique work, or lacks a safe disposition. Independent readers or clearly disjoint writers may coexist when repository rules allow them.
3. **Terminal task does not equal workspace closeout.** Merge, acceptance, abandonment, supersession, rollback, or another project-defined terminal event ends the earlier task authorization, but the physical/local workspace still needs an explicit disposition.
4. **Unknown or unique work is never cleanup fuel.** Preserve staged, unstaged, untracked, and local-only work until its ownership and disposition are verified. Do not use reset, stash, overwrite, forced branch movement, or forced worktree deletion merely to reach a clean-looking baseline.
5. **Retention is explicit, not accidental.** A non-terminal workspace may remain for review, PR, QA, runtime acceptance, recovery, or another verified reason, but its owner, reason, and release/next-event condition must be known.
6. **Closeout is prompt and proportional.** Reconcile terminal workspace state before starting a conflicting successor task whenever practical. Do not turn every task start into a full historical repository archaeology exercise.

## Before creating or selecting a task workspace

Perform a bounded workspace check for the repository and active scope. Establish only what the task needs:

- canonical repository/workspace identity and current ref/revision;
- selected or proposed task workspace, branch/ref, HEAD, and working-tree state;
- any existing workspace that writes the same affected capability/authority or otherwise conflicts with the task;
- whether those relevant workspaces are active, intentionally retained, terminal, uniquely dirty/local-only, or unresolved.

Expand beyond that bounded set only when ambiguity, unique work, a collision, lifecycle cleanup, or the task decision materially requires it.

If a relevant predecessor writer is unresolved or its unique-work state is unknown, stop creation/selection of the conflicting successor writer and reconcile the predecessor first. A stale-looking path, old branch name, detached checkout, or merged remote PR alone is not enough evidence to delete or bypass a local workspace.

## Lifecycle dispositions

Use project-specific lifecycle names if they exist. At minimum, the evidence must distinguish these meanings:

- **Active:** currently authorized for execution.
- **Retained non-terminal:** intentionally waiting for a known event such as review, PR merge, QA, acceptance, or recovery decision.
- **Terminal:** its task no longer authorizes further work under the prior phase.
- **Unique work present:** local state or commits may not be safely discarded, regardless of task lifecycle.
- **Unresolved:** ownership, task relationship, lifecycle, or unique-work state is not established well enough for safe mutation.

These are semantic classes, not required literal labels.

## Terminal closeout gate

When a task reaches a terminal outcome, close obsolete workspace state promptly unless a verified retention reason remains. Use the repository's established commands and policies rather than inventing generic destructive commands.

A safe closeout establishes, in order:

1. the terminal event and exact task/workspace identity;
2. staged, unstaged, untracked, and local-only commit state relevant to data preservation;
3. the disposition of any unique work—integrated, preserved elsewhere with evidence, explicitly retained, or explicitly discarded only when authorized;
4. removal of the obsolete task worktree/checkout when safe and supported by project rules;
5. removal of obsolete local task branches when safe and supported;
6. remote task-branch cleanup only when repository policy and current collaboration state allow it;
7. repository/worktree metadata pruning or equivalent maintenance when applicable;
8. post-closeout verification of the remaining relevant workspace set.

Do not declare `CLOSED_CLEAN` (or an equivalent project-specific outcome) merely because the PR merged. Closeout evidence must support the local/workspace disposition claim actually being made.

## Explicit retention

A retained workspace is valid when all of the following are known:

- owning task or work item;
- workspace/ref identity;
- why it must remain;
- what event or decision releases it for closeout;
- whether unique local work exists and how it is protected.

A vague “might be useful later” is not a retention condition. If the task is superseded, determine whether any unique work must be transferred/preserved; then close the superseded workspace when safe.

## Legacy reconciliation

When a repository already contains accumulated historical workspaces whose ownership or disposition is unclear, perform a bounded one-time reconciliation task rather than repeatedly rediscovering them during unrelated feature work.

For that reconciliation:

- inventory the repository's existing task workspaces;
- classify each by verified task/ref relationship, lifecycle, and unique-work state;
- close clearly terminal, non-unique workspaces according to repository policy;
- preserve and separately resolve unique work;
- retain legitimate non-terminal workspaces with explicit release conditions;
- leave unresolved items as blockers rather than guessing;
- target **zero unclassified workspaces** at the end of the reconciliation.

After that baseline is established, normal tasks should use the bounded pre-task check and prompt closeout instead of repeating the full legacy audit.

## Remote and local evidence

Remote repository evidence can establish PR, branch, commit, merge, and remote-ref state. It cannot by itself prove local worktree existence, working-tree cleanliness, untracked files, or local-only commits. Local evidence is required for those claims.

A remote/Web auditor may determine the expected lifecycle outcome; the local executor establishes local workspace/unique-work facts. Claim a fully clean closeout only when the evidence covers both sides needed by that claim.

## Handoff evidence

Keep closeout output concise. When workspace lifecycle is material, report the verified equivalents of:

```text
TASK_ID: <id>
TASK_LIFECYCLE: <current/terminal state>
WORKSPACE_IDENTITY: <path or other stable identity, ref, HEAD>
WORKSPACE_DISPOSITION: <removed | retained | preserved | unresolved | project equivalent>
UNIQUE_WORK: <none | preserved with evidence | unresolved>
LOCAL_BRANCH_DISPOSITION: <removed | retained | not applicable | unresolved>
REMOTE_BRANCH_DISPOSITION: <removed | retained | not applicable | unresolved>
RETAIN_UNTIL: <event/decision, if retained>
UNCLASSIFIED_RELEVANT_WORKSPACES: <count or unresolved>
FINAL_STATE: <project-specific result>
```

Do not require fields that the project does not use. The purpose is to make the next task able to distinguish a clean baseline from retained or unresolved lifecycle state without reconstructing history.

## Stop conditions

Stop destructive or conflicting state-changing work when any of these materially affects the task:

- a relevant workspace cannot be tied to a verified repository/task/ref identity;
- a predecessor writer for the same capability/authority remains unresolved;
- staged, unstaged, untracked, or local-only work has unknown ownership/disposition;
- the terminal event or retention condition cannot be verified;
- remote and local evidence disagree on an identity needed for the cleanup decision;
- cleanup would require force, overwrite, reset, or another destructive assumption not explicitly authorized by the project.

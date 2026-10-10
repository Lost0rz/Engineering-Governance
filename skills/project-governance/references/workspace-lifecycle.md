# Workspace lifecycle and closeout

Apply this contract only when the target project uses task branches, Git worktrees, multiple checkouts, or an equivalent source-controlled task-workspace model. Do not introduce worktrees or extra branches into a project merely to satisfy this reference.

The goal is not “one worktree only.” The goal is that every task-relevant non-canonical workspace has a known owner and lifecycle disposition, overlapping writers are not multiplied, unknown/unique work is preserved, and terminal workspace debt is closed while the evidence is still fresh.

## Core invariants

1. **No unclassified task-relevant workspace.** A workspace that may affect the active task or lifecycle decision must have a verified relationship to a task/branch/ref and a known current disposition. Routine task startup does not require classifying unrelated historical workspaces unless they create ambiguity, collision, unique-work risk, lifecycle cleanup work, or are explicitly included in a legacy-reconciliation task. Projects may use their own lifecycle names; this contract does not impose a universal status enum.
2. **No overlapping successor writer while a predecessor is unresolved or write-capable.** Do not create or select a successor writer workspace when an existing predecessor can write the same overlapping fact/state/policy/behavior authority and is unresolved, has unknown unique work, lacks a safe disposition, or remains able to resume writes under its current authorization. Capability or Domain labels are routing hints, not automatic mutual-exclusion boundaries: disjoint writers inside one capability may coexist when their write authorities do not overlap and repository rules allow it.
3. **Lifecycle events are not terminal by name alone.** Merge, release, deployment, acceptance, abandonment, supersession, rollback, or another event changes workspace-closeout obligations only when project/task controls define that event as terminal for the task/phase or when it otherwise materially changes authorization. A remote merge alone does not universally prove that the task is terminal, and a terminal authorization state still does not prove physical/local workspace closeout.
4. **Unknown or unique work is never cleanup fuel.** Preserve staged, unstaged, untracked, and local-only work until its ownership and disposition are verified. Do not use reset, stash, overwrite, forced branch movement, or forced worktree deletion merely to reach a clean-looking baseline.
5. **Retention is explicit, not accidental.** A non-terminal workspace may remain for review, PR, QA, runtime acceptance, recovery, or another verified reason, but its owner, reason, release/next-event condition, and write capability must be known.
6. **Closeout is prompt and proportional.** Reconcile terminal workspace state before starting a conflicting successor task whenever practical. Do not turn every task start into a full historical repository archaeology exercise.
7. **Durable workspace state follows the canonical project's storage authority by default.** Resolve the canonical project root before choosing locations for project-controlled worktrees, unique-work staging, retained task evidence, or other non-regenerable workspace state. A verified project-local path/authority rule for a specific durable asset overrides this default. Machine/runtime state and OS/tool-required ephemeral scratch are separate; unique or durable project state must not be abandoned in unrelated temporary or convenience locations at task closure.

## Storage authority for durable task state

Use the canonical project root as the default routing signal for project-controlled durable task state. Determine which storage authority contains that root before selecting a durable task-workspace or retention location. “Same storage authority” means the same project storage location/volume/filesystem authority established by the canonical root; it is not a universal host path, named external disk, user home, or machine rule.

Project-controlled durable task state includes, when retained or non-regenerable:

- Git worktrees or equivalent task checkouts;
- task staging that contains unique work;
- durable diagnostic, migration, recovery, or acceptance evidence;
- project archives or retained task bundles;
- release/acceptance artifacts that the project intentionally keeps;
- other unique development state whose loss would require reconstruction or could lose evidence/work.

A project may explicitly declare another durable location/authority for one of those asset classes; that project-local rule wins. Do not require ordinary projects to maintain a separate storage manifest merely to restate the default.

OS/tool-required temporary files, sockets, disposable compiler scratch, and other short-lived scratch may use system temporary locations. If temporary staging becomes unique or must be retained, preserve it under the project's storage authority before closure instead of leaving the only durable copy in system temp or another unrelated convenience path.

Machine/runtime state is a separate class. CI runner runtime, LaunchAgents, package-manager or runtime services, host caches, machine configuration, system temp, and similar host-operational state may remain machine-local unless the project explicitly owns that state as portable project data. Do not relocate host-operational state merely because the canonical project root is on another storage authority.

## Workspace evidence dimensions

Establish workspace facts independently; do not infer one dimension from another:

- **Local branch identity** — whether the named local branch exists and what commit it resolves to.
- **Remote branch identity** — whether the corresponding remote ref exists and what commit it resolves to. A missing remote branch does not prove the local branch/worktree is absent.
- **Worktree registration** — whether Git currently registers the worktree. Registration does not by itself prove the filesystem path is present and usable.
- **Filesystem path identity** — whether the expected checkout path exists and resolves to the intended repository/worktree. A directory name alone does not prove Git registration or task authority.
- **Storage authority** — when durable placement matters, whether the selected project-controlled workspace/state is on the canonical project's storage authority or on an explicitly declared project-local override.
- **HEAD/revision** — the commit actually checked out in the selected workspace.
- **Working-tree state** — staged, unstaged, untracked, and local-only commit state. A clean remote PR does not prove local cleanliness.
- **Write capability** — whether the retained workspace can resume writes under its current authorization without a new boundary.
- **Overlapping authority** — which fact/state/policy/behavior authority the workspace can write relative to another current/proposed writer.

When one dimension matters to the task, verify that dimension directly from the appropriate local or remote evidence. This prevents category errors such as treating “remote branch absent” as “worktree absent,” “worktree registered” as “path exists,” or “PR merged” as “local writer closed.”

## Lifecycle checkpoints during normal development

Workspace governance is not only an end-of-task cleanup step. Run a **bounded** lifecycle checkpoint when one of these events occurs:

- selecting or creating the task workspace;
- before authorizing a successor workspace that could overlap an existing writer;
- when a task moves into or out of an intentionally retained state such as PR review, QA, runtime acceptance, recovery, or freeze/read-only;
- when a lifecycle event may make the task/phase terminal;
- before starting a new task whose write authority overlaps a retained predecessor.

At each checkpoint, inspect only the task-relevant workspace set and only the dimensions needed for that decision. If a previously recorded retention/release condition has been satisfied, close or reclassify that workspace promptly while the evidence is fresh. If nothing material changed and the same workspace remains valid, do not repeat a historical inventory merely to prove cleanliness again.

This checkpoint model is the normal prevention mechanism. `Legacy reconciliation` below is reserved for repositories that already accumulated ambiguous historical workspace debt; it is not the routine path for healthy projects.

## Before creating or selecting a task workspace

Perform a bounded workspace check for the repository and active scope. Establish only what the task needs:

- canonical repository/workspace identity and current ref/revision;
- canonical project root and, when durable placement is material, its storage authority plus any explicit project-local override for the proposed durable asset;
- selected or proposed task workspace, local/remote branch state where relevant, worktree registration/path identity, HEAD, and working-tree state;
- any existing workspace whose writes overlap the same affected fact/state/policy/behavior authority or that otherwise materially conflicts with the task;
- whether those relevant workspaces are active, intentionally retained, terminal, uniquely dirty/local-only, or unresolved;
- for any retained predecessor whose authority overlaps, whether it can still resume writes without a new authorization boundary.

Expand beyond that bounded set only when ambiguity, unique work, a collision, lifecycle cleanup, or the task decision materially requires it.

If a relevant predecessor writer is unresolved, its unique-work state is unknown, or it can still resume writes under its current authorization for the overlapping authority, stop creation/selection of the conflicting successor writer and reconcile the predecessor first. A retained predecessor stops blocking only when its write role has a verified safe boundary, such as terminal closeout, explicit supersession, explicit freeze/read-only disposition, or another project-defined state in which it cannot write that authority again without new authorization.

A stale-looking path, old branch name, detached checkout, or merged remote PR alone is not enough evidence to delete, bypass, or treat a local workspace as non-writing.

## Lifecycle dispositions

Use project-specific lifecycle names if they exist. At minimum, the evidence must distinguish these meanings:

- **Active:** currently authorized for execution.
- **Retained non-terminal:** intentionally waiting for a known event such as review, PR merge, QA, acceptance, or recovery decision. Its current write capability must also be known.
- **Frozen/read-only retained:** intentionally kept for evidence, review, reference, or another non-writing purpose and unable to resume writes to the overlapping authority without new authorization.
- **Terminal:** its task/phase no longer authorizes further work under the prior phase.
- **Unique work present:** local state or commits may not be safely discarded, regardless of task lifecycle.
- **Unresolved:** ownership, task relationship, lifecycle, write capability, or unique-work state is not established well enough for safe mutation.

These are semantic classes, not required literal labels. A retained workspace that remains write-capable still counts as a writer for overlapping-authority conflict decisions.

## Terminal closeout gate

When project/task controls establish that a task or phase has reached a terminal outcome, close obsolete workspace state promptly unless a verified retention reason remains. Use the repository's established commands and policies rather than inventing generic destructive commands.

A safe closeout establishes, in order:

1. the lifecycle event, whether it is terminal for this task/phase, and the exact task/workspace identity;
2. staged, unstaged, untracked, and local-only commit state relevant to data preservation;
3. the disposition of any unique work—integrated, preserved elsewhere with evidence, explicitly retained, or explicitly discarded only when authorized—and, when retained, that the only durable copy is not left in unrelated temporary/convenience storage;
4. removal of the obsolete task worktree/checkout when safe and supported by project rules;
5. removal of obsolete local task branches when safe and supported;
6. remote task-branch cleanup only when repository policy and current collaboration state allow it;
7. repository/worktree metadata pruning or equivalent maintenance when applicable;
8. post-closeout verification of the remaining relevant workspace set.

Do not declare `CLOSED_CLEAN` (or an equivalent project-specific outcome) merely because the PR merged. Closeout evidence must support both the terminal authorization claim and the local/workspace disposition claim actually being made.

## Explicit retention

A retained workspace is valid when all of the following are known:

- owning task or work item;
- workspace/ref identity;
- why it must remain;
- what event or decision releases it for closeout;
- whether unique local work exists and how it is protected;
- whether it remains write-capable for any authority that overlaps another current/proposed writer.

A vague “might be useful later” is not a retention condition. If a retained predecessor can still resume writes under its current authorization, treat it as a writer for overlap checks. If it must coexist with a successor, first establish a verified non-writing boundary such as explicit freeze/read-only disposition, supersession, or another project-defined rule that prevents both workspaces from writing the same authority concurrently.

If the task is superseded, determine whether any unique work must be transferred/preserved; then close or explicitly freeze the superseded workspace when safe.

## Legacy reconciliation

When a repository already contains accumulated historical workspaces whose ownership or disposition is unclear, perform a bounded one-time reconciliation task rather than repeatedly rediscovering them during unrelated feature work.

For that reconciliation:

- inventory the repository's existing task workspaces;
- classify each by verified task/ref relationship, lifecycle, write capability where relevant, and unique-work state;
- close clearly terminal, non-unique workspaces according to repository policy;
- preserve and separately resolve unique work;
- retain legitimate non-terminal workspaces with explicit release conditions and known write capability;
- leave unresolved items as blockers rather than guessing;
- target **zero unclassified workspaces** at the end of the reconciliation.

After that baseline is established, normal tasks should use the bounded lifecycle checkpoints and prompt closeout instead of repeating the full legacy audit.

## Remote and local evidence

Remote repository evidence can establish PR, remote branch/ref, commit, merge, and remote-ref state. It cannot by itself prove local branch existence, worktree registration/path existence, working-tree cleanliness, untracked files, local-only commits, or that a retained local workspace cannot resume writes under some separate local authorization. Local evidence is required for those claims.

A remote/Web auditor may determine the expected lifecycle outcome; the local executor establishes local workspace/unique-work facts. Claim a fully clean closeout only when the evidence covers both sides needed by that claim.

## Handoff evidence

Keep closeout output concise. When workspace lifecycle is material, report the verified equivalents of:

```text
TASK_ID: <id>
TASK_LIFECYCLE: <current/terminal state>
WORKSPACE_IDENTITY: <path or other stable identity, ref, HEAD>
WORKSPACE_DISPOSITION: <removed | retained-write-capable | retained-frozen | preserved | unresolved | project equivalent>
WRITE_AUTHORITY: <overlapping authority or not applicable>
UNIQUE_WORK: <none | preserved with evidence | unresolved>
LOCAL_BRANCH_DISPOSITION: <removed | retained | not applicable | unresolved>
REMOTE_BRANCH_DISPOSITION: <removed | retained | not applicable | unresolved>
RETAIN_UNTIL: <event/decision, if retained>
UNCLASSIFIED_RELEVANT_WORKSPACES: <count or unresolved>
FINAL_STATE: <project-specific result>
```

Do not require fields that the project does not use. The purpose is to make the next task able to distinguish a clean baseline from retained, write-capable, frozen/read-only, or unresolved lifecycle state without reconstructing history.

## Stop conditions

Stop destructive or conflicting state-changing work when any of these materially affects the task:

- a task-relevant workspace cannot be tied to a verified repository/task/ref identity;
- a predecessor can write an overlapping fact/state/policy/behavior authority and remains unresolved or write-capable under its current authorization;
- staged, unstaged, untracked, or local-only work has unknown ownership/disposition;
- the lifecycle event's effect on authorization or the retention condition cannot be verified;
- the storage authority or applicable project-local durable-path override is unresolved when the task must choose a durable project-controlled location;
- closeout would leave the only durable/unique project state in unrelated temporary or convenience storage without an authorized retention rule;
- remote and local evidence disagree on an identity needed for the cleanup decision;
- cleanup would require force, overwrite, reset, or another destructive assumption not explicitly authorized by the project.

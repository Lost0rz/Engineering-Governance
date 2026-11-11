## Control-mode applicability

Both control modes share this reuse-first workspace policy. FILE_CONTROL reads current Task; ISSUE_CONTROL selects either an approved Issue-backed task **or** the current independently host-verified top-level USER-requested bounded G1/G2 task, which needs no first Issue/comment. Neither route creates an additional workspace by itself. Issue edits/comments do not move Git HEAD, imply a new branch/worktree/PR or erase overlapping-writer/unique-work risk. Only the selected authority can grant a writing task.

# Workspace lifecycle and closeout

Apply this contract only when the target project uses task branches, Git worktrees, multiple checkouts, or an equivalent source-controlled task-workspace model. Do not introduce worktrees or extra branches into a project merely to satisfy this reference.

The goal is not “one worktree only.” The goal is that every task-relevant non-canonical workspace has a known owner and lifecycle disposition, overlapping writers are not multiplied, unknown/unique work is preserved, and terminal workspace debt is closed while the evidence is still fresh.

## Creation gate — reuse before making another workspace

A **task**, execution command, agent/session/context, local checkout, task branch, registered Git worktree, remote branch, and pull request are distinct objects. One does not automatically require the next. **Do not create** a branch, worktree, checkout, or PR just because an instruction says `continue`, `audit`, `verify`, `fix`, `handoff`, `run tests`, `start task`, or invokes a Sub Agent. A successful mutation is not defined by the number of artifacts created.

Before any **new** task-workspace/branch/PR side effect, use the smallest relevant evidence to decide, in order:

1. **No writing needed?** For read-only investigation, planning, review, audit, normal test execution, no-op reconciliation, and control observation, use an existing safe checkout or remote source. No task branch/worktree/PR is implied; tests that must write generated temporary output follow the project's test-isolation rules, not automatically a durable task worktree.
2. **Existing authority still usable?** If the current task and authorized ref/workspace/PR remain correct and safe, reuse them. Same-task corrections, routine FILE_CONTROL `CURRENT_STATUS.md`/`CURRENT_TASK.md` alignment or ISSUE_CONTROL comment/spec coordination, another command, agent handoff, reviewer loop, session restart, phase checkpoint, or control-only HEAD advance do **not** independently authorize a successor. Do not manufacture a new PR only to memorialize evidence or a control-only status change when the owning task/repository permits alignment on the existing authorized ref.
### Size/independence decision before physical Git worktree allocation

**Default: small changes use a safely reusable checkout, not a new physical worktree.** Small bug fixes, UI/copy tweaks, localized implementation corrections, documentation, Task/Status reconciliation, targeted tests, and review/checkpoint rounds ordinarily use the existing authorized task worktree or a safe canonical checkout. Where a fresh task branch/PR is required, create or select that **branch in a safe existing checkout** when the project's branch/workspace rules and working-tree state permit; do not create a registered worktree merely because the branch/PR is new.

A separate durable project Worktree is **normally appropriate for substantial, independently owned development**—a large module/subsystem, an architectural redesign, a long-lived major workstream—or a concrete isolation requirement (concurrent proven-disjoint writers, incompatible build/runtime environment, or preservation of verified unique work while a non-overlapping task proceeds). The label `large` is not a numeric threshold or blanket permission: identify the distinct owner/writer, why checkout reuse would be unsafe or materially inefficient, and the closeout event. A single large change does not automatically need its own worktree; conversely a small task may justify one when safe reuse genuinely cannot meet an explicit project/host isolation requirement.

A repository's default "new task branch + Draft PR" is **not** evidence for "new Git worktree." Creating a worktree merely to avoid a harmless HEAD or control-file mismatch, to run another command, or to keep every small edit in its own directory is prohibited. Do not switch or reuse an occupied/dirty checkout unsafely; if none is safely reusable, resolve the conflict/unique-work ownership before creating justified isolation or STOP.

3. **What actually needs a branch or PR?** Resolve task authorization and the target project's `AGENTS.md`, established merge/review rules and current PR state. If those require a fresh branch/Draft PR for **new material work**, satisfy that specific obligation, but a branch need not mean an additional worktree, and a PR need not mean a new task. Never use this reusable default to bypass a project's explicit no-direct-main, fresh-branch, PR, review, or separation rule.
4. **Is a separate physical Git worktree necessary?** Apply the size/independence decision above. Default to the safely usable authorized checkout, including the existing task worktree if one exists. Create another only for an explicit project/task requirement or a demonstrated isolation need: genuinely concurrent proven-disjoint writers, incompatible independent build/runtime environments, or protecting unique/dirty work that prevents safe reuse. Before creation prove the intended writer/branch boundary and the disposition of any overlapping predecessor. A new worktree is **not** a workaround for **unclassified** dirty/unknown work, unresolved authority, or an old but still write-capable predecessor. Known retained unique work may justify separate, explicitly authorized and non-overlapping isolation only after its preservation and writer disposition are verified.
5. **What retires it?** Each genuinely additional durable task worktree needs an owner, reason, ref/path, write authority, and known release event/condition; record only material current task state in the owning project control. Reuse or close promptly at that boundary after unique-work checks. Do not create a registry, per-command inventory, extra PR, or clean-up-only successor merely to implement this gate.

**Creation outcome:** `REUSE_EXISTING | CREATE_BRANCH_ONLY | CREATE_WORKTREE_JUSTIFIED | CREATE_PR_REQUIRED | NO_WORKSPACE_CHANGE | STOP_UNRESOLVED` (illustrative decision labels, **not** mandatory form fields). Report the rationale when a new worktree or unexpectedly additional PR is material; ordinary reuse/no-op should not generate paperwork.

A remote-only session can assess PR/ref churn and suggest local follow-up, but it cannot certify a physical worktree count or clean checkout. A local executor verifies applicable `git worktree list --porcelain`, ref, path, HEAD and dirty/unique-work facts *when the decision requires them*. Do not infer local worktree creation, identity, retention, or cleanup from remote branch or PR count.

## Core invariants

1. **No unclassified task-relevant workspace.** A workspace that may affect the active task or lifecycle decision must have a verified relationship to a task/branch/ref and a known current disposition. Routine task startup does not require classifying unrelated historical workspaces unless they create ambiguity, collision, unique-work risk, lifecycle cleanup work, or are explicitly included in a legacy-reconciliation task. Projects may use their own lifecycle names; this contract does not impose a universal status enum.
2. **Prevent actual conflicting writes.** A retained branch or prior writer's theoretical ability to resume is not by itself a reason to block new work. When evidence shows concurrent overlapping modifications, unsafely shared local files, unresolved ownership or unique uncommitted work that could be lost, reconcile only the affected surfaces before conflicting mutation. Independent work and normal handoff continue. Comments, PR history and local evidence are all useful; none automatically creates a new Writer-release approval.
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
- **HEAD/revision** — the commit actually checked out in the selected workspace. When freshness matters, distinguish literal Repository HEAD from Delivery / Semantic HEAD under [Control identity and freshness](control-identity.md).
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
- when a specific collision is plausible, whether an overlapping execution is actually active or unique work is at risk.

Expand beyond that bounded set only when ambiguity, unique work, a collision, lifecycle cleanup, or the task decision materially requires it.

If specific overlapping work is active or unique uncommitted changes might be overwritten, pause the **conflicting write only** until the affected files/workspace are safe. An inactive historical branch, retained review workspace or prior comment is not a standing global writer mutex. Do not require formal supersession just to resume non-overlapping development.

A stale-looking path, old branch name, detached checkout, or merged remote PR alone is not enough evidence to delete, bypass, or treat a local workspace as non-writing.

In FILE_CONTROL, a Repository HEAD mismatch caused only by `CURRENT_STATUS.md` / `CURRENT_TASK.md` is different: classify it as `CONTROL_ONLY_DRIFT` when the changed path set proves that classification. It does not by itself make an otherwise accepted workspace stale, require a new construction workspace, or block selection. Material task-content changes remain authoritative and must still be obeyed.

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

Do not declare `CLOSED_CLEAN` (or an equivalent project-specific outcome) merely because the PR merged. Closeout evidence must support both the terminal authorization claim and the local/workspace disposition claim actually being made. For FILE_CONTROL, reconcile task/status controls only when a material control/terminal state changed under [Control plane roles](control-plane.md). ISSUE_CONTROL does not inherit the FILE_CONTROL gate. Neither a normal Handoff Card nor a merge observation alone mandates workspace cleanup.

## Control-only main advance after closeout

Once terminal authorization and physical workspace closeout have both been verified, in FILE_CONTROL, a later canonical-main Repository HEAD advance limited to `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is non-blocking lifecycle evidence:

```text
LIFECYCLE_STATE = CLOSED
CONTROL_ONLY_MAIN_ADVANCE = NON_BLOCKING
```

Do not reopen the closed task, require a second worktree/branch cleanup, or classify the already-closed workspace as stale merely because those control records advanced main. This remains true only when the difference is proven control-only and the changed control content does not establish a new material obligation for that workspace.

Any source/config/test/workflow/schema/migration/dependency/runtime-relevant change or other non-excluded path remains `DELIVERY_HEAD_CHANGE` and must be evaluated normally. This rule does not weaken unique-work preservation, predecessor-writer checks, storage authority, local/remote evidence, or explicit literal Repository HEAD locks.

## Explicit retention

A retained workspace needs enough identity and unique-work evidence for its actual disposition; collect only relevant facts:

- owning task or work item;
- workspace/ref identity;
- why it must remain;
- what event or decision releases it for closeout;
- whether unique local work exists and how it is protected;
- whether it remains write-capable for any authority that overlaps another current/proposed writer.

A vague “might be useful later” does not prove that cleanup is safe or necessary. A retained predecessor's theoretical ability to resume is not itself a writer collision; if there is an actual overlapping write risk, protect unique work and establish a safe boundary only for the conflicting operation.

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

Remote repository evidence can establish PR, remote branch/ref, commit, merge, changed-path, semantic-tree, and remote-ref state. It cannot by itself prove local branch existence, worktree registration/path existence, working-tree cleanliness, untracked files, local-only commits, or that a retained local workspace cannot resume writes under some separate local authorization. Local evidence is required for those claims.

A remote/Web auditor may determine the expected lifecycle outcome; the local executor establishes local workspace/unique-work facts. Claim a fully clean closeout only when the evidence covers both sides needed by that claim.

Issue discussion, PR history and local observations are complementary evidence; select only facts relevant to the current decision. Ordinary agent handoff does not introduce a separate Writer-release approval/checklist. Investigate actual writer overlap or unique-work risk when indicated, not by default.

## Handoff evidence

Report only lifecycle facts material to an actual workspace closeout or conflicting write. FILE_CONTROL alignment is a separate, conditional task/status check when the owning control state materially changes; ordinary handoff needs no full workspace or alignment receipt.

```text
TASK_ID: <current task>
WORKSPACE_IDENTITY: <relevant ref/path/head>
DISPOSITION: <retained | preserved | removed | unresolved>
UNIQUE_WORK: <preserved evidence | none | unresolved>
WRITE_CONFLICT: <actual overlapping risk or none>
NEXT_ACTION: <only when work remains>
```

Optional local/remote branch and retention details follow the owning project's real workspace needs. Do not turn these example fields into a universal release/cleanup gate. For FILE_CONTROL, report an alignment result only when the event-triggered control-plane contract actually requires one; ISSUE_CONTROL never inherits Task/Status alignment.

When FILE_CONTROL alignment is applicable, read-only work may report `CONTROL_ALIGNMENT: NEEDS_RECONCILIATION` and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY` with relevant evidence; it must not silently modify controls.

## Stop conditions

Stop destructive or conflicting state-changing work when any of these materially affects the task:

- a task-relevant workspace cannot be tied to a verified repository/task/ref identity;
- an actually active overlapping writer or unresolved unique work would be overwritten by the proposed operation;
- staged, unstaged, untracked, or local-only work has unknown ownership/disposition;
- the lifecycle event's effect on authorization or the retention condition cannot be verified;
- the storage authority or applicable project-local durable-path override is unresolved when the task must choose a durable project-controlled location;
- closeout would leave the only durable/unique project state in unrelated temporary or convenience storage without an authorized retention rule;
- remote and local evidence disagree on an identity needed for the cleanup decision;
- cleanup would require force, overwrite, reset, or another destructive assumption not explicitly authorized by the project.

A proven `CONTROL_ONLY_DRIFT` difference is not itself a workspace stop condition. If changed control content materially changes authorization, treat that content change under the control-plane contract rather than misclassifying the commit as delivery drift.

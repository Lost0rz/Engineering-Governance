# CURRENT TASK — Project Governance Workspace Lifecycle

Task ID: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-039`

State: `ACTIVE`

Mode: `BOUNDED_GOVERNANCE_CHANGE`

## Objective

Add a small, reusable workspace/worktree lifecycle and closeout contract to `project-governance` so governed projects do not accumulate unclassified stale task workspaces that later require expensive archaeological cleanup.

## Affected domains

- Reusable Skill: `skills/project-governance/`
- Root governance controls for this repository

No new top-level Skill or runtime component is authorized.

## Start baseline

- Repository: `Lost0rz/Engineering-Governance`
- Canonical branch: `main`
- Verified start HEAD: `533cefb1dcf07b4fde5a489408fbc8fa6f0e324e`
- Authorized task branch: `codex/project-governance-workspace-lifecycle-v1`
- Prior task: `EG-PLUGIN-V0.2.0-RELEASE-038`, `CLOSED_RELEASED`
- Published Plugin v0.2.0 identity remains immutable and is not changed by this task.

## In scope

- Define lifecycle classification for non-canonical task workspaces without imposing one universal project status enum.
- Require bounded workspace inventory/classification before creating or selecting conflicting successor writer workspaces.
- Prevent a new writer for the same capability/authority while a predecessor workspace is unresolved or contains unknown unique work.
- Define terminal closeout behavior for merged, accepted, abandoned, superseded, or otherwise terminal tasks.
- Define explicit retention semantics for non-terminal workspaces such as PR/review/QA waiting states.
- Preserve unknown staged, unstaged, untracked, and local-only work; prohibit force-clean as a lifecycle shortcut.
- Define a concise closeout evidence/handoff shape and a legacy reconciliation path that can establish zero unclassified workspaces without requiring full-repository archaeology on every new task.
- Update the `project-governance` Skill entry point, relevant references, and templates only where needed for consistency.
- Update root controls when their owned durable/current facts change.

## Out of scope

- New top-level Skill.
- CLI, daemon, database, hook, background scanner, installer, automatic cleanup, automatic branch deletion, or automatic remediation.
- Repository-specific hard-coded branch/worktree commands in the reusable Skill.
- Requiring all projects to have only one worktree.
- Deleting or modifying any target project's local worktrees as part of this task.
- Changes to `domain-navigation` or `incident-doctor` behavior except links if strictly required; none are currently expected.
- Publishing a new Plugin release.

## Known evidence

- Existing `project-governance` already requires task-relevant workspace identity and non-destructive handling of unknown local work.
- Existing development flow says task branches/worktrees should be closed or retained according to verified lifecycle rules, but does not define the closeout gate, successor-writer rule, retention evidence, or zero-unclassified-workspace invariant.
- Existing control-plane lifecycle integrity covers terminal task authorization but not physical workspace disposition.
- Repeated project cleanup work has demonstrated that deferred classification/closeout increases later audit cost; the accepted design is to close this gap without creating a cleanup subsystem.

## Risk and rationale

This is a reusable governance-semantics change: wording can unintentionally over-constrain projects or create unnecessary audit work. Keep the contract proportional, project-adaptable, non-destructive, and limited to lifecycle facts needed for safe continuation. Do not turn normal task startup into a full historical repository audit.

## Verification level and rationale

`V0` — documentation/control/layout change only. Required checks:

- exact branch/base identity and final diff scope;
- markdown/content consistency and internal-link/path verification;
- no contradictory lifecycle rules across `SKILL.md`, references, and templates;
- explicit confirmation that no runtime/CLI/automation surface was added;
- self-audit against the accepted design and out-of-scope list;
- post-merge exact-main verification if merge is authorized and available.

No runtime or product test suite is required because this task changes reusable documentation/Skill semantics only.

## Acceptance criteria

- `project-governance` explicitly owns workspace/worktree lifecycle and closeout when the target project uses those mechanisms.
- Existing relevant workspaces are classified only to the depth needed for the active task; routine startup does not become broad archaeology.
- Same-capability/authority successor writer creation is blocked when the predecessor is unresolved or unique work is unknown.
- Terminal tasks require prompt workspace disposition: safe closeout or explicit justified retention with a release condition.
- Non-terminal review/QA/PR workspaces may remain when their owner, reason, and release condition are explicit.
- Unknown/unique local work is preserved and causes stop/reconciliation rather than destructive cleanup.
- Legacy accumulated workspaces have a bounded one-time reconciliation path whose target invariant is zero unclassified workspaces.
- Templates make lifecycle disposition visible without turning `CURRENT_STATUS.md` into a history log.
- No new top-level Skill, automation, daemon, database, or cleanup runtime is added.
- Final V0 self-audit finds no material contradiction, broken link, scope leak, or unsupported claim.

## Stop conditions

- `main` or the authorized task branch moves unexpectedly in a way that invalidates the verified baseline or exact reviewed diff.
- Existing repository evidence contradicts the accepted design or shows a separate canonical lifecycle authority that this change would duplicate.
- Implementing the contract would require runtime automation, destructive cleanup, or a new top-level Skill.
- Any unknown remote change or unique work is discovered that cannot be reconciled non-destructively.

## Handoff / current stop point

Authorized to implement the accepted bounded design on `codex/project-governance-workspace-lifecycle-v1`, self-audit the exact branch, and merge only if the reviewed content remains within this contract and the merge target has not drifted incompatibly.

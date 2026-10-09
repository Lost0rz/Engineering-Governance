# CURRENT TASK — Project Governance Workspace Lifecycle

Task ID: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-039`

State: `READY_FOR_MERGE`

Mode: `BOUNDED_GOVERNANCE_CHANGE`

## Objective

Add a small, reusable workspace/worktree lifecycle and closeout contract to `project-governance` so governed projects do not accumulate unclassified stale task workspaces that later require expensive reconciliation.

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
- Published Plugin v0.2.0 identity remains unchanged by this task.

## Workspace lifecycle

- Selected task workspace: remote branch `codex/project-governance-workspace-lifecycle-v1`.
- This task was executed through the remote GitHub control plane; no claim is made about any local checkout/worktree state.
- Relevant predecessor writer: none; the prior repository task was already terminal before this branch was created.
- Retain-until condition: keep the reviewed task branch until merge or another explicit terminal disposition.
- After merge, reconcile root controls and verify the resulting `main` identity. Any local-workspace closeout claim would require separate local evidence.

## In scope

- Define lifecycle classification for non-canonical task workspaces without imposing one universal project status enum.
- Require bounded workspace classification before creating or selecting a conflicting successor writer workspace.
- Prevent a new writer for the same capability/authority while a predecessor is unresolved or unique-work state is unknown.
- Define terminal closeout behavior and explicit retention semantics.
- Preserve unknown staged, unstaged, untracked, and local-only work until its disposition is verified.
- Define concise closeout evidence and a one-time legacy reconciliation path targeting zero unclassified workspaces.
- Update the `project-governance` entry point, relevant references, templates, and root controls where their owned facts change.

## Out of scope

- New top-level Skill.
- CLI, daemon, database, hook, background scanner, installer, or automatic cleanup/remediation.
- Repository-specific hard-coded cleanup commands in the reusable Skill.
- Requiring all projects to have only one worktree.
- Modifying any target project's local workspaces.
- Changes to `domain-navigation` or `incident-doctor` behavior.
- Publishing a new Plugin release.

## Known evidence

- Existing governance already covered selected-workspace identity and preservation of unknown local work.
- The missing reusable layer was the lifecycle bridge between task state and physical workspace disposition.
- The new canonical detail is `skills/project-governance/references/workspace-lifecycle.md`; other changed Skill files route to or summarize that authority rather than duplicating the full procedure.

## Risk and rationale

This reusable semantics change must not over-constrain target projects or turn normal task startup into repository archaeology. The implementation therefore keeps normal checks task-bounded and reserves full historical reconciliation for repositories that already have accumulated unknown workspace debt.

## Verification level and rationale

`V0` — documentation/control/layout change only.

Fresh remote audit on 2026-10-09 established:

- `main` remained at `533cefb1dcf07b4fde5a489408fbc8fa6f0e324e` during implementation review;
- reviewed implementation HEAD `485cbeb3817128549b23c0daba55502138c8181a` was ahead by 7 and behind by 0 from the exact start baseline;
- the reviewed diff contained only Markdown/control surfaces in root governance and `skills/project-governance/`;
- no `plugin.json`, runtime, CLI, automation component, `domain-navigation`, or `incident-doctor` behavior changed;
- new lifecycle links resolve to the new reference, and control ownership remains separated among `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`;
- content review found no conflict with multi-worktree coexistence, bounded startup checks, same-authority writer gating, explicit retention, terminal closeout, unique-work preservation, legacy reconciliation, or remote/local evidence boundaries.

No runtime/product suite is required for this documentation/Skill-only change.

## Acceptance criteria

- `project-governance` owns workspace/worktree lifecycle when the target project uses those mechanisms. — PASS
- Routine startup remains bounded to task-relevant workspace facts. — PASS
- Conflicting successor writers are blocked while predecessor state is unresolved. — PASS
- Terminal tasks require explicit workspace disposition; retained workspaces require a reason and release condition. — PASS
- Unknown/unique local work remains preserved pending verified disposition. — PASS
- Legacy workspace debt has a one-time reconciliation path targeting zero unclassified workspaces. — PASS
- Templates expose durable policy and current-task disposition without turning `CURRENT_STATUS.md` into history. — PASS
- No new top-level Skill or runtime/automation surface was added. — PASS
- V0 self-audit found no material contradiction, broken new link, or scope leak. — PASS

## Stop conditions

- `main` or the task branch changes incompatibly before merge.
- A separate canonical lifecycle authority is discovered that this change would duplicate.
- The task would need expansion into runtime automation or another top-level Skill.

## Handoff / current stop point

Ready for merge after one final identity/diff check. After merge, verify exact `main` content and reconcile this task to a terminal closed state.

---
name: project-governance
description: Use as the normal Engineering Governance entry for software/project/repository engineering work, and when establishing or repairing project governance, starting or executing governed development, reconciling scope/control state, choosing proportional verification, or reconciling/closing task workspace lifecycle. Route to Domain Navigation or Incident Doctor only when their narrower triggers apply.
---

# Project Governance

Use this Skill as the normal Engineering Governance entry point for software, repository, and project engineering work when the Plugin's global routing contract is adopted. Scale the procedure to the task: simple low-risk work should remain lightweight and must not acquire extra plans, worktrees, broad scans, or broad validation merely because Project Governance is active. This Skill establishes or repairs project governance and starts, executes, reconciles, verifies, hands off, or closes normal authorized product and business work. Inspect the target repository and its existing authorities first, then adapt the templates to verified evidence. Keep unsupported facts unknown; do not copy templates blindly.

## Choose the right route

- Use this Skill for the three-file control plane, normal task flow, task-scope/control reconciliation, proportional verification, code-structure/canonical-authority checks during construction, and task workspace lifecycle/closeout when the project uses branches, worktrees, or equivalent task workspaces.
- When the relevant Domain/capability, semantic authority, code location, symbol, runtime entry, dependency, or relevant test is unclear, use [domain-navigation](../domain-navigation/SKILL.md) to identify and verify the route, then return to the governing workflow. Existing accepted business/product/domain/capability maps may already provide semantic authority; do not require a separate navigation file merely to satisfy a template.
- Use [incident-doctor](../incident-doctor/SKILL.md) only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress **and** existing evidence cannot answer the needed decision safely. A defect with sufficient evidence stays in the normal authorized flow; do not enter Doctor merely because a bug exists.
- If Incident Doctor needs help locating the relevant Domain/authority/code/test evidence, it may use Domain Navigation for that bounded purpose and then resume diagnosis. If diagnosis supports a behavior change outside the active task, return here for reconciliation/re-authorization before mutation.
- For the cross-project selection rules, read [Global Skill routing](references/global-routing.md). For installing/upgrading the managed global routing block, read [Global routing adoption and upgrade](references/adoption.md).
- This Skill does not perform deep repository or domain architecture discovery, incident diagnosis, installation runtime behavior, or enforcement. It adds no diagnostic, cleanup, installer, daemon, hook, MCP, or file-mutating runtime to routine feature work.

## Normal governed development

Read the relevant project controls, establish only the baseline needed for the authorized work, identify affected domains/capabilities from accepted semantic authorities and any useful navigation projection, and implement the smallest authorized product or business outcome. Choose the lightest safe `V0`–`V3` risk/scope level and the appropriate verification cadence; update only controls whose owned, verified facts materially changed. Ordinary evidence discovery within the accepted objective does not create a new task. A material objective or scope change requires updated task authorization before work continues.

Apply [Code structure and canonical authority](references/code-structure.md) before writing substantial source changes that add/change state ownership, writers, shared behavior, module boundaries, or a materially new responsibility inside an existing module. Use Domain/capability/authority/lifecycle/reason-to-change boundaries—not line count—to decide whether code remains cohesive. Re-run the structure check if implementation discoveries change that boundary; do not knowingly defer a required responsibility split until final review merely because finishing in one file is faster.

For source-controlled projects, establish the task-relevant repository/ref/revision and current workspace state before state-changing work. When controls name Git identities, first classify whether each identity is provenance/transition, current/freshness, or an explicit equality lock under [Control identity and freshness](references/control-identity.md); do not treat every recorded parent SHA as a required current HEAD.

If the project uses multiple task workspaces, apply [Workspace lifecycle and closeout](references/workspace-lifecycle.md) at the bounded lifecycle checkpoints defined there—not only at final cleanup. Classify only task-relevant workspaces to the depth needed for the active decision, distinguish local branch, remote branch, worktree registration/path, HEAD, working-tree state, write capability, and overlapping authority, prevent a predecessor that remains unresolved or write-capable from being bypassed by a successor writer for the same overlapping state/behavior authority, and close or explicitly retain workspace state when project/task lifecycle rules require it. Preserve unknown staged, unstaged, untracked, or local-only work; do not reset, stash, delete, overwrite, or force-clean it merely to make the workspace match an execution card. If authoritative baseline, control, predecessor-workspace, or unique-work ambiguity materially affects the active task, stop and reconcile rather than improvising. If nothing relevant changed, do not repeat a full historical workspace inventory. Projects that do not use these mechanisms should not invent them just to satisfy this Skill.

`CURRENT_STATUS.md` is a verified current-state snapshot, not an authorization override. If a newly verified status fact changes or invalidates a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, explicit head lock, or authorization boundary, stop state-changing work, reconcile `CURRENT_TASK.md`, and obtain re-authorization before continuing. A status refresh that does not affect the task contract does not require task churn.

Load the relevant contracts as needed:

- [Global Skill routing](references/global-routing.md)
- [Global routing adoption and upgrade](references/adoption.md)
- [Control plane roles, updates, and lifecycle reconciliation](references/control-plane.md)
- [Control identity and freshness](references/control-identity.md)
- [Business-first development flow and selected task workspaces](references/development-flow.md)
- [Code structure and canonical authority](references/code-structure.md)
- [Workspace lifecycle and closeout](references/workspace-lifecycle.md)
- [Verification tiers, cadence, and evidence identity](references/verification-tiers.md)
- [Managed global AGENTS routing block](assets/templates/GLOBAL_AGENTS_ROUTING.md)
- [Project AGENTS.md template](assets/templates/AGENTS.md)
- [CURRENT_STATUS.md template](assets/templates/CURRENT_STATUS.md)
- [CURRENT_TASK.md template](assets/templates/CURRENT_TASK.md)

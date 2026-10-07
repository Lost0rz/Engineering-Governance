---
name: project-governance
description: Use when establishing or repairing project governance, starting or executing normal governed development, or reconciling a task after a scope change. This is the normal governance and development entry point; it does not perform deep repository discovery or incident diagnosis.
---

# Project Governance

Use this Skill to establish or repair a project's governance controls and to start or execute normal, authorized product and business work. Inspect the target repository and its existing authorities first, then adapt the templates to verified evidence. Keep unsupported facts unknown; do not copy templates blindly.

## Choose the right route

- Use this Skill for the three-file control plane, normal task flow, task-scope reconciliation, and proportional verification.
- When the relevant Domain/capability, code location, or authority is unclear, use [domain-navigation](../domain-navigation/SKILL.md) to inspect the target repository and identify the right owner and evidence. Existing accepted business/product/domain/capability maps may already provide the semantic authority; do not require a separate navigation file merely to satisfy a template.
- Use [incident-doctor](../incident-doctor/SKILL.md) only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and existing evidence cannot answer the needed question. Normal business development does not default to Doctor.
- This Skill does not perform deep repository or domain architecture discovery, incident diagnosis, installation, runtime behavior, or enforcement. It adds no diagnostic infrastructure to routine feature work.

## Normal governed development

Read the relevant project controls, establish only the baseline needed for the authorized work, identify affected domains/capabilities from accepted semantic authorities and any useful navigation projection, and implement the smallest authorized product or business outcome. Choose the lightest safe `V0`–`V3` verification level and update only controls whose owned, verified facts materially changed. Ordinary evidence discovery within the accepted objective does not create a new task. A material objective or scope change requires updated task authorization before work continues.

For source-controlled projects, establish the task-relevant repository/ref/revision and current workspace state before state-changing work. Preserve unknown staged, unstaged, untracked, or local-only work; do not reset, stash, delete, overwrite, or force-clean it merely to make the workspace match an execution card. If authoritative baseline or control drift materially affects the active task, stop and reconcile rather than improvising. Projects that do not use these mechanisms should not invent them just to satisfy this Skill.

`CURRENT_STATUS.md` is a verified current-state snapshot, not an authorization override. If a newly verified status fact changes or invalidates a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, stop state-changing work, reconcile `CURRENT_TASK.md`, and obtain re-authorization before continuing. A status refresh that does not affect the task contract does not require task churn.

Load the relevant contracts as needed:

- [Control plane roles and updates](references/control-plane.md)
- [Business-first development flow](references/development-flow.md)
- [Verification tiers](references/verification-tiers.md)
- [AGENTS.md template](assets/templates/AGENTS.md)
- [CURRENT_STATUS.md template](assets/templates/CURRENT_STATUS.md)
- [CURRENT_TASK.md template](assets/templates/CURRENT_TASK.md)

---
name: project-governance
description: Use when establishing or repairing project governance, starting or executing normal governed development, or reconciling a task after a scope change. This is the normal governance and development entry point; it does not perform deep repository discovery or incident diagnosis.
---

# Project Governance

Use this Skill to establish or repair a project's governance controls and to start or execute normal, authorized product and business work. Inspect the target repository and its existing authorities first, then adapt the templates to verified evidence. Keep unsupported facts unknown; do not copy templates blindly.

## Choose the right route

- Use this Skill for the three-file control plane, normal task flow, task-scope reconciliation, and proportional verification.
- When the relevant Domain, code location, or authority is unclear, use [domain-navigation](../domain-navigation/SKILL.md) to inspect the target repository and identify the right owner and evidence.
- Use [incident-doctor](../incident-doctor/SKILL.md) only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and existing evidence cannot answer the needed question. Normal business development does not default to Doctor.
- This Skill does not perform deep repository or domain architecture discovery, incident diagnosis, installation, runtime behavior, or enforcement. It adds no diagnostic infrastructure to routine feature work.

## Normal governed development

Read the relevant project controls, establish only the baseline needed for the authorized work, identify affected domains, and implement the smallest authorized product or business outcome. Choose the lightest safe `V0`–`V3` verification level and update only controls whose owned, verified facts materially changed. Ordinary evidence discovery within the accepted objective does not create a new task. A material objective or scope change requires updated task authorization before work continues.

Load the relevant contracts as needed:

- [Control plane roles and updates](references/control-plane.md)
- [Business-first development flow](references/development-flow.md)
- [Verification tiers](references/verification-tiers.md)
- [AGENTS.md template](assets/templates/AGENTS.md)
- [CURRENT_STATUS.md template](assets/templates/CURRENT_STATUS.md)
- [CURRENT_TASK.md template](assets/templates/CURRENT_TASK.md)

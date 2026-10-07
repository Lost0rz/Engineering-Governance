---
name: project-governance
description: Establish or repair a project's normal AI development governance, including the three-file control plane, business-first task flow, and risk-proportional verification. Use for normal governed development; do not use for repository architecture discovery beyond routing to Domain Navigation or for incident diagnosis.
---

# Project Governance

Use this Skill to establish or repair a project's normal control structure and to start governed development work. First inspect the target repository's existing controls and verified facts. Adapt the templates below to that evidence; do not copy them blindly or fill unknown project details by inference.

## Read the contracts

- [Control plane roles](references/control-plane.md)
- [Development flow](references/development-flow.md)
- [Verification tiers](references/verification-tiers.md)
- [AGENTS.md template](assets/templates/AGENTS.md)
- [CURRENT_STATUS.md template](assets/templates/CURRENT_STATUS.md)
- [CURRENT_TASK.md template](assets/templates/CURRENT_TASK.md)

Route codebase discovery and Domain Map work to [domain-navigation](../domain-navigation/SKILL.md). Route a real failure or unsafe ambiguity to [incident-doctor](../incident-doctor/SKILL.md) only when current evidence is insufficient for safe progress.

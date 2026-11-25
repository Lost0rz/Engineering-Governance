# Engineering-Governance repository facts

This repository owns portable AI engineering Skills, tests, reference methods and plugin package metadata. It is a **source repository**, not a daemon, CI runner for other repositories, credential authority or project data store.

- `skills/**` contains reusable workflow and method sources; `rules/AGENTS.md` provides optional plugin-scoped routing; `references/**` retains maintainer policy and provenance notes; `archive/**` retains historical design and acceptance records.
- Project source architecture, business rules, data safety and test commands remain with each project; never copy machine-local paths, specific providers/models or credentials into portable requirements.
- Preserve a single clear owner per capability and distinct evidence for source commit, CI state, packaged artifact and installed runtime.
- The installed plugin defines reusable workflow; local project `AGENTS.md` is for project-specific differences.
- GitHub and host permissions control actual mutations. A plan, Issue, document or AI-generated decision is not a credential.

Enter a specialist Skill directly when the user's goal matches its domain (`design`, `solution-design`, `incident-doctor`, `evidence-audit`, `domain-navigation`, `project-profile`), or use [Project Governance](skills/project-governance/SKILL.md) for general engineering work, portable CI routing, and delivery coordination.

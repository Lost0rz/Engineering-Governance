# Engineering-Governance repository facts

This repository owns portable AI engineering Skills, tests, reference methods and plugin package metadata. It is a **source repository**, not a daemon, CI runner for other repositories, credential authority or project data store.

- `skills/**` contains reusable workflow and method sources; `references/**` and `documents/**` retain maintainer/history/design context.
- Project source architecture, business rules, data safety and test commands remain with each project; never copy machine-local paths, specific providers/models or credentials into portable requirements.
- Preserve a single clear owner per capability and distinct evidence for source commit, CI state, packaged artifact and installed runtime.
- The installed plugin defines reusable workflow; local project `AGENTS.md` is for project-specific differences.
- GitHub and host permissions control actual mutations. A plan, Issue, document or AI-generated decision is not a credential.

Use [Project Governance](skills/project-governance/SKILL.md) for normal engineering work and the necessary specialist Skill for a material dependency.

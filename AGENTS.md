# Engineering-Governance repository facts

This repository owns portable AI engineering Skills, tests, CI routing tools, and plugin package metadata. It is a **source repository**, not a daemon, credential authority, or project data store.

- `skills/**` contains reusable domain Skills (`engineering-workflow`, `ci-governance`, `ui-design`, `architecture`, `incident-doctor`, `evidence-audit`, `codebase-context`); `rules/AGENTS.md` provides optional plugin-scoped routing; `references/**` retains maintainer policy and provenance notes; `archive/**` retains historical design and acceptance records.
- Project source architecture, business rules, data safety, and test commands remain with each project; never copy machine-local paths, specific providers/models, or credentials into portable requirements.
- Preserve a single clear owner per capability and distinct evidence for source commit, CI state, packaged artifact, and installed runtime.
- GitHub and host permissions control actual mutations. A plan, Issue, document, or AI-generated decision is not a credential.

Match the requested outcome directly to the owning domain Skill (or [engineering-workflow](skills/engineering-workflow/SKILL.md) for general engineering changes and delivery, and [ci-governance](skills/ci-governance/SKILL.md) for CI test routing).

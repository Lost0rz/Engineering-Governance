# Engineering-Governance Source Repository Rules

## Repository purpose

This repository maintains portable Engineering Governance Skills, routing policy, templates, verification helpers, and acceptance references. It is a **source repository**, not a governance runtime, daemon, scheduler, database, installer, model router, or automatic remediation service.

## Source and documentation ownership

- `skills/**` owns reusable engineering workflow, authorization, risk/deviation decisions, verification routing, handoff, lifecycle, and their tests. No copy of those procedures belongs in this file.
- `documents/**` stores durable capability designs; `references/**` stores shared maintainer guidance and historical acceptance evidence. Neither is an active task authorization source.
- `plugin.json` owns the source package's declared version; package and installed identities must be checked separately from source.
- Target repositories own their domain architecture, business data, runtime commands, and project-specific safety constraints. This source repository must not override those project facts.

## Repository-specific engineering constraints

- Preserve portable Skills: never embed a developer's machine paths, private accounts, specific models, runners, or local capacities as universal framework requirements.
- Do not introduce a persistent service, central execution controller, privileged installer, or automated enforcement mechanism without an explicit change to this repository's purpose.
- Keep a single source owner for each framework contract; prefer narrow references over duplicated normative text.
- Do not change authorization trust boundaries or enable new permissions as a side effect of documentation cleanup or package installation.
- Keep source changes, reviewed commit identity, GitHub CI/merge status, packaged artifacts, and installed-runtime acceptance as distinct evidence; never infer one from another.
- Preserve historical acceptance material as history, not proof of the current implementation or installation.

## Canonical workflow owners

The installed Engineering Governance Skills own all reusable control-plane behavior. This file defines no alternative Issue, approval, G/V/L, test-selection, PR, workspace, receipt, or release procedure. Refer to `skills/project-governance/SKILL.md` and its `references/**` for the applicable workflow; `skills/project-governance/references/global-routing.md` owns Skill selection.

Repository control-mode selection, approver eligibility, Issue authoring, delegation and G1/G2 policy belong exclusively to the versioned installed Engineering Governance control policy. This project file defines no operative governance selectors.

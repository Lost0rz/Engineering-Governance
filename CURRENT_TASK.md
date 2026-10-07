# CURRENT TASK — Skill Repository Redesign Specification Review

Task ID: `EG-SKILLS-RESTRUCTURE-DESIGN-007`

State: `WAITING_FOR_USER_SPEC_REVIEW`

Mode: `ARCHITECTURAL_DESIGN_REVIEW`

## Objective

Review and either accept or revise the written design that resets Engineering-Governance from the previous governance-runtime/tooling direction into a reusable AI engineering-governance Skill source repository.

No local restructure implementation is authorized by this task.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Design-start remote baseline: `d13e6895f6d4bddb753cabcc87566613eaa9bbec`.
- Design file: `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`.
- Root repository rules are being updated in the same control commit to reflect the newly accepted repository purpose.
- Existing stable tag `v0.1.0` must not move.

## Fixed design requirements from the user

1. The repository is a Skill/template/rule/context source for AI agents; it is not a business project template and not an installer.
2. Target-project adoption is performed by an AI agent after it reads both this repository and the real target project. Templates are adapted, not blindly copied.
3. The three project control files have standardized roles: `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.
4. Every target project needs a Domain navigation layer that helps an AI understand capability boundaries, authority, code entry points, dependencies, and relevant tests efficiently.
5. Normal business/product development remains primary. Incident Doctor work is reactive: enter it after a real problem appears, assess whether existing evidence is sufficient, and add only the minimum missing probe.
6. Testing/verification is risk-tiered rather than uniformly heavy.
7. The first implementation step establishes the full Skill-repository skeleton and removes the obsolete live runtime/research structure. Skill content is then enriched one module at a time and independently reviewed between slices.

## Proposed v1 Skill modules

- `skills/project-governance/`
- `skills/domain-navigation/`
- `skills/incident-doctor/`

The target structure and exact responsibilities are defined in the design document.

## Upstream references to incorporate conceptually

- Agent Skills / Anthropic skill-creator anatomy and progressive disclosure.
- AGENTS.md open format.
- GitHub `awesome-copilot` `acquire-codebase-knowledge`: evidence-first discovery, source-path evidence, explicit unknowns.
- Aider Repo Map: dynamic code/symbol relevance selection under limited context.

No dependency on those repositories is required, and no upstream code copy is authorized by this design task.

## Design review questions

Accept the written specification only if it correctly captures:

- the final repository identity;
- the exact target file tree;
- the retirement of legacy runtime/product code from the live tree while preserving Git history;
- the boundaries among Project Governance, Domain Navigation, and Incident Doctor;
- Domain Map versus Repo Map separation;
- no installer/Bootstrap CLI;
- proportional verification;
- staged enrichment and real-project validation.

## Stop conditions

STOP if:

- the remote `main` baseline changes unexpectedly before the control commit is established;
- the design would require preserving the old Doctor/Bootstrap runtime as an active product;
- implementation work begins before written-spec acceptance;
- scope expands into an installer, daemon, background enforcement, automatic remediation, or central governance service.

## Current stop point

`WAITING_FOR_USER_SPEC_REVIEW`

After user acceptance, Web should invoke the implementation-planning workflow and issue the first local execution card. Do not start local restructuring before that step.

# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08 — the reusable repository remains `AUDIT_CLEAN`. The InvestDesk read-only adoption-gap audit completed against `Lost0rz/InvestDesk@e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`, and the user has accepted the proposed minimal adoption design.

## Accepted reusable baseline

- Accepted post-audit Skill/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Exactly three reusable Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.
- No reusable Skill change is authorized by the current adoption task.

## InvestDesk adoption state

Target: `Lost0rz/InvestDesk`.

Accepted adoption design:

- preserve InvestDesk's existing three-file control plane and project-specific policies;
- make only bounded `AGENTS.md` Project Governance wording corrections;
- use the adoption transition itself to establish richer `CURRENT_TASK.md` metadata without changing InvestDesk business semantics;
- add no `DOMAIN_MAP.md`, `DOMAIN.md`, `INCIDENT.md`, navigation runtime/index, or new diagnostics/probes;
- do not change product source, tests, schema, migrations, dependencies, business contracts, or MVP-D semantics.

The target baseline must remain the freshly verified `main` SHA unless a live refresh proves a legitimate advance and the task is reconciled before writing.

## Current task

- Task: `EG-INVESTDESK-BOUNDED-ADOPTION-030`.
- State: `ACTIVE_BOUNDED_ADOPTION`.
- Mode: `TARGET_GOVERNANCE_ADOPTION_ONLY`.

## Next milestone

Create one bounded InvestDesk adoption branch from the verified target baseline, first establish target-local adoption authorization in `CURRENT_STATUS.md` / `CURRENT_TASK.md`, then apply only the approved `AGENTS.md` wording changes. Independently audit the exact branch diff and stop before merge for explicit user merge authorization.

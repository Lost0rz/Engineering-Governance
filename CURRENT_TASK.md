# CURRENT TASK — Phase G Cross-Project Corrective Closeout

Task ID: `EG-CROSS-PROJECT-CORRECTIVE-020`

State: `CLOSED_ACCEPTED_MAIN`

Mode: `MERGED_CLOSEOUT`

## Objective

Record the accepted merge and closure of the bounded Phase G cross-project corrective. This file does not authorize a new implementation phase or target-project adoption.

## Authority and exact heads

- User-approved Phase G design baseline: `9346997c75d3b5dce8a558203b3adb1a40eb5fc3`.
- Phase G authorization/main head: `94255158a43d6cca727cdf64681a3bdefbb2bf40`.
- Reusable-content implementation commit: `f2c5f2f86dc892a1b9241f0286d6485fdf253073`.
- Audited task-branch head and accepted merge head: `5b59767652f0d2017ca3b3a1df6f29d5366eaa8b`.
- Stable historical tag `v0.1.0^{}`: `738627a0caad330d277f60cfdaff5f153593135e`.

## Accepted corrective A — Project Governance

The merged reusable contract now states that `CURRENT_STATUS.md` is a verified snapshot and cannot silently override task-owned authorization conditions. If a newly verified status fact changes or invalidates a task prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, state-changing work stops until `CURRENT_TASK.md` is reconciled and re-authorized. Ordinary status refreshes that leave those task-owned conditions unchanged do not require task churn.

Merged reusable files:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`

## Accepted corrective B — Domain Navigation

The merged reusable contract now requires discovery of accepted business/product/domain/capability maps already present in a target repository, regardless of filename, before assuming a navigation map is missing. Existing semantic authorities are referenced rather than duplicated. A literal `DOMAIN_MAP.md` is optional; a separate navigation projection is created or refreshed only when durable source/symbol/test/entry-point routing adds value beyond existing authorities.

Merged reusable files:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/domain-model.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`

## Merge evidence

- Fresh pre-merge comparison: authorization head -> task branch was `ahead_by=2`, `behind_by=0`, with merge base exactly `94255158a43d6cca727cdf64681a3bdefbb2bf40`.
- Fresh pre-merge refs: `main=94255158a43d6cca727cdf64681a3bdefbb2bf40`; `codex/cross-project-corrective=5b59767652f0d2017ca3b3a1df6f29d5366eaa8b`.
- User separately authorized the merge after the independent Web audit passed.
- `main` was advanced to `5b59767652f0d2017ca3b3a1df6f29d5366eaa8b` by expected-SHA guarded fast-forward with `force=false`.
- No Phase G target-project mutation occurred.
- `incident-doctor` was not changed.
- No executable/runtime/dependency/index/database/daemon/installer/Repo Map program/new Skill was added.

## Closed scope

Phase G is complete. Do not continue modifying reusable Skills under this Task ID. Do not adopt the Skills into RemoteOrbit, InvestDesk, or another repository under this authorization. Do not move or replace the stable historical tag.

## Current stop point

`WAITING_FOR_USER_NEXT_PHASE_DECISION`

The next task must receive a new Task ID and explicit authorization based on the next project need.

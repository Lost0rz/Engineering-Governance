# CURRENT TASK — Root Consistency and Freeze

Task ID: `EG-ROOT-CONSISTENCY-FREEZE-021`

State: `AUTHORIZED_FOR_IMPLEMENTATION`

Mode: `BOUNDED_ROOT_DOCS_FREEZE`

## Objective

Align root `README.md` and root `AGENTS.md` with the accepted Phase G Domain Navigation contract, then freeze the resulting stable repository baseline. This task does not authorize reusable Skill edits or target-project adoption.

## Authority and baseline

- Pre-task `main`: `7ec0ffd574a0ec7e43c2990ebaf79633a6719e22`.
- Historical tag `v0.1.0^{}`: `738627a0caad330d277f60cfdaff5f153593135e`; it must not move.
- Intended new stable version label: `v0.2.0`.

## Allowed changes

- `README.md`
- `AGENTS.md`
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` only for task control/handoff/closeout.

## Required correction

Replace obsolete root wording that implies every target project must maintain a separate explicit/literal Domain Map. The root contract must match Phase G:

- discover accepted business/product/domain/capability maps already present, regardless of filename;
- reference existing semantic authorities instead of duplicating them;
- a separate navigation projection is optional and should be added only when durable source/symbol/test/entry-point routing adds value;
- any navigation projection remains derived and does not replace product/domain truth.

## Forbidden scope

- any `skills/**` change;
- target-project mutation;
- new Skill, script, executable, dependency, workflow, runtime, index, database, daemon, installer, or Repo Map program;
- moving or replacing `v0.1.0`.

## Verification

`V0`.

Before merge/freeze verify exact changed paths, root/Skill semantic consistency, unchanged Skill tree, exactly three top-level Skills, no runtime/tooling additions, and unchanged historical tag. Freeze by exact commit SHA; if a new version tag is created it must point to that exact SHA and never move.

## Current stop point

`AUTHORIZED_FOR_IMPLEMENTATION`

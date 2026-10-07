# CURRENT TASK — Skill Repository Skeleton Reset Plan Review

Task ID: `EG-SKILLS-RESTRUCTURE-PLAN-008`

State: `WAITING_FOR_USER_PLAN_REVIEW`

Mode: `ARCHITECTURAL_PLAN_REVIEW`

## Objective

Review and either accept or revise the implementation plan for Phase A of the Engineering-Governance redesign.

Phase A performs only the live-tree skeleton reset and legacy-live-tree retirement. It does not enrich the three Skills beyond minimal valid entrypoints and explicit file contracts.

No local restructure implementation is authorized by this task.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted design: `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`.
- Design control commit: `33784c83de1a711f0fe83b99efc59d80fceaff68`.
- Implementation plan: `docs/superpowers/plans/2026-10-07-skill-repository-skeleton-reset-implementation-plan.md`.
- Plan commit: `82099ad7033d9bdc0aec6b7d880f157008157392`.
- Stable tag `v0.1.0` must continue to dereference to commit `738627a0caad330d277f60cfdaff5f153593135e`.

## Phase A authorized design scope after plan acceptance

The future implementation task may:

1. retire the obsolete live Python governance runtime, runtime tests, legacy governance/reality-check/reference-audit trees, and the explicitly obsolete Doctor/Bootstrap planning artifacts listed by the plan;
2. replace `README.md` with the Skill-source repository identity and AI-adapted usage model;
3. create exactly three top-level Skill modules: `project-governance`, `domain-navigation`, and `incident-doctor`;
4. create all reference/template paths defined in the plan with concise Phase A contracts;
5. create `references/UPSTREAMS.md`, `references/LICENSE_NOTES.md`, and `examples/README.md`;
6. run `V0` verification only and hand the remote task branch back for independent Web audit.

## Explicit non-scope

The Phase A implementation must not:

- add an installer or Bootstrap CLI;
- add executable Doctor/runtime product code;
- implement a Repo Map program;
- add a daemon, service, database, enforcement engine, automatic remediation, or MCP prerequisite;
- copy upstream source code or long-form upstream text;
- deeply enrich later-phase Skill guidance beyond the contracts required for the skeleton;
- move the historical `v0.1.0` tag;
- merge its own task branch.

## Plan review focus

Accept the plan only if it correctly enforces:

- exact live-tree retirement boundaries;
- exactly three Skill modules;
- minimal valid Skill frontmatter with distinct triggers;
- Domain Map / Repo Map separation;
- business-first / reactive-Doctor behavior;
- proportional verification with `V0` for this slice;
- no new executable product/runtime surface;
- stable-tag preservation;
- local executor stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Stop conditions

STOP if:

- `main` moves unexpectedly before a later implementation task captures its exact start baseline;
- the plan requires preserving the old Doctor/Bootstrap runtime as an active live product;
- implementation begins while this task is still `WAITING_FOR_USER_PLAN_REVIEW`;
- scope expands into later Skill enrichment or runtime automation.

## Current stop point

`WAITING_FOR_USER_PLAN_REVIEW`

After explicit plan acceptance, Web must create a separate implementation task, capture the exact remote `main` baseline, authorize one implementation branch, and issue the local execution card. The local executor must return evidence only after pushing a clean matched task branch; Web performs independent audit before merge.

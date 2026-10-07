# CURRENT TASK — Domain Navigation Audit Corrective

Task ID: `EG-DOMAIN-NAVIGATION-AUDIT-CORRECTIVE-024`

State: `AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

Mode: `BOUNDED_DOCUMENTATION_CORRECTIVE`

## Objective

Correct only the Domain Navigation consistency/usability issues established by `EG-FULL-SKILL-AUDIT-022`, without changing the accepted Domain semantics or adding new navigation infrastructure.

## Authority and baseline

- Accepted Project Governance corrective/main head: `94c8d89f762f8343045b5c3e7acf01756cd474c9`.
- Frozen reusable comparison baseline: `4bc63eadbf1e1166ef8d9106c7f387a8ebb42c18`.
- Planned branch: `codex/domain-navigation-audit-corrective`.

## Authorized reusable files

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/references/refresh-policy.md`
- `skills/domain-navigation/references/repo-map.md`
- `skills/domain-navigation/assets/templates/DOMAIN.md`
- `skills/domain-navigation/scripts/README.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for handoff/closeout.

## Required corrective

1. Use consistent three-layer terminology:
   - accepted semantic authorities = existing business/product/domain/capability sources that may own project meaning;
   - navigation projection = optional derived durable routing artifact such as the generic `DOMAIN_MAP.md` template;
   - Repo Map = optional dynamic/read-only candidate-selection aid.
2. Remove wording that implies every project has or needs a stable Domain Map file.
3. Ensure refresh rules apply to affected navigation evidence/projection fields only; when no projection exists, re-verify/report the affected route rather than creating a file by default.
4. Ensure Repo Map cannot decide semantic ownership/authority, authorize work, replace direct source verification, or automatically mutate semantic authorities/navigation projections.
5. Reframe `DOMAIN.md` as optional derived navigation detail rather than a second domain specification/authority; semantic claims must link to their owner and remain concise.
6. Remove duplicate headings and maintainer-phase wording from reusable payload where this task touches it.

## Out of scope

- changes to `project-governance` or `incident-doctor`;
- changes to `domain-model.md`, `evidence-rules.md`, or `DOMAIN_MAP.md` unless re-audit proves a new contradiction that cannot be resolved in the authorized files;
- new files, executable helpers, Repo Map implementation, indexes, databases, daemons, services, dependencies, or a fourth Skill;
- target-project adoption.

## Verification

`V0` only:

- changed reusable paths exactly the six authorized files;
- frontmatter and relative links remain valid;
- no reusable wording in the changed files requires a literal `DOMAIN_MAP.md`;
- semantic authority, navigation projection, and Repo Map roles are distinct and non-competing;
- `DOMAIN.md` is explicitly derived/optional and cannot become a second product/domain authority;
- sibling Skills unchanged;
- no executable/dependency/runtime addition;
- final branch independently re-audited before merge.

## Current stop point

`AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

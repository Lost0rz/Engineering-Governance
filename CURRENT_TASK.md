# CURRENT TASK — Phase G Cross-Project Corrective Handoff

Task ID: `EG-CROSS-PROJECT-CORRECTIVE-020`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_CORRECTIVE_AUDIT_HANDOFF`

## Objective

Hand off the completed bounded implementation of the two Phase G reusable Skill clarifications for independent Web audit. No merge is authorized by this handoff.

## Authority and exact heads

- User-approved design baseline: `9346997c75d3b5dce8a558203b3adb1a40eb5fc3`.
- Phase G authorization/main head: `94255158a43d6cca727cdf64681a3bdefbb2bf40`.
- Task branch: `codex/cross-project-corrective`.
- Reusable-content implementation commit before this handoff-control commit: `f2c5f2f86dc892a1b9241f0286d6485fdf253073`.
- Stable historical tag `v0.1.0^{}`: `738627a0caad330d277f60cfdaff5f153593135e`.

## Implemented corrective A — Project Governance

The reusable contract now states that:

- `CURRENT_STATUS.md` is a verified current-state snapshot, not an authorization override;
- a status update alone cannot change a `CURRENT_TASK.md` prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary;
- if a newly verified status fact changes or invalidates one of those task-owned conditions, state-changing work stops until `CURRENT_TASK.md` is reconciled and re-authorized;
- if task-owned conditions are unaffected, a normal status refresh does not require a task rewrite.

Changed reusable files:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`

## Implemented corrective B — Domain Navigation

The reusable contract now states that:

- agents first discover accepted business/product/domain/capability maps already present in the target repository, regardless of filename, and determine what semantic truth they own;
- those maps are referenced as authorities rather than copied into a competing navigation artifact;
- a literal `DOMAIN_MAP.md` filename is not a target-repository requirement;
- a separate navigation projection is created or refreshed only when durable source/symbol/test/entry-point routing adds value beyond the existing semantic authorities;
- navigation remains derived and cannot authorize work or redefine product/domain truth.

Changed reusable files:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/domain-model.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`

## Verification evidence

Fresh pre-handoff checks established:

- compare `94255158a43d6cca727cdf64681a3bdefbb2bf40` -> `f2c5f2f86dc892a1b9241f0286d6485fdf253073`: `ahead_by=1`, `behind_by=0`, exactly seven modified reusable Markdown paths, all on the approved allowlist;
- `skills/incident-doctor` tree SHA is `f35fc22faa78ff4b7854a45c08b2167425f0c440` both before and after the reusable implementation;
- `skills/` contains exactly three Skill directories;
- `project-governance`, `domain-navigation`, and `incident-doctor` each retain valid `SKILL.md` frontmatter;
- all referenced project-governance and domain-navigation reference/template paths inspected for this task exist on the implementation commit;
- no executable, dependency, runtime, index, daemon, database, installer, Repo Map program, or new Skill appears in the reusable diff;
- annotated tag object `a794ee0e9d039bad0f8fa418ad422316c5315fb3` still points to commit `738627a0caad330d277f60cfdaff5f153593135e`.

## Independent audit contract

Audit the final remote task branch against authorization head `94255158a43d6cca727cdf64681a3bdefbb2bf40` and confirm:

1. the only reusable changes are the seven approved files above;
2. root differences are limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md` handoff state;
3. both clarifications match the approved Phase G design without broadening architecture;
4. `incident-doctor` is unchanged;
5. no new Skill/tool/runtime/dependency exists;
6. stable tag remains unchanged;
7. branch is a clean linear descendant of the authorization head.

If any condition fails, do not merge; return a bounded corrective finding. If all pass, report audit PASS and wait for separate merge acceptance.

## Forbidden actions

- merge to `main` without separate acceptance;
- modify RemoteOrbit, InvestDesk, or any other target project;
- add new reusable scope beyond the seven approved files;
- alter `incident-doctor`;
- add tooling, dependencies, runtime infrastructure, or a fourth Skill.

## Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

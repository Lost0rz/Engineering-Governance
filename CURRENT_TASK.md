# CURRENT TASK — Phase G Cross-Project Corrective

Task ID: `EG-CROSS-PROJECT-CORRECTIVE-020`

State: `AUTHORIZED_FOR_IMPLEMENTATION`

Mode: `BOUNDED_CORRECTIVE_IMPLEMENTATION`

## Objective

Apply exactly two reusable Skill clarifications justified by the Phase E RemoteOrbit and Phase F InvestDesk validations, without expanding the governance architecture:

1. make task-owned authorization conditions immune to silent override by `CURRENT_STATUS.md`;
2. make Domain Navigation explicitly coexist with pre-existing authoritative semantic maps rather than assuming a new literal `DOMAIN_MAP.md` is always required.

This is corrective documentation/Skill-contract work only. It does not authorize adoption in RemoteOrbit, InvestDesk, or any other target repository.

## Authority and baseline

- Design/handoff baseline: `9346997c75d3b5dce8a558203b3adb1a40eb5fc3`.
- User approval: Phase G design approved for the two cross-project correctives.
- Phase E evidence: RemoteOrbit exposed a real status/task drift affecting an active prerequisite.
- Phase F evidence: InvestDesk showed coherent status/task separation and existing authoritative semantic maps (`DOMAIN_MODEL_MAP.md`, `BUSINESS_CAPABILITY_MAP.md`) that must not be shadowed by a generic navigation artifact.
- Accepted reusable Skill revision before this corrective remains `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Implementation branch: `codex/cross-project-corrective`, created from the Phase G authorization commit.

## Corrective A — Project Governance

Clarify the ownership rule as follows:

- `CURRENT_STATUS.md` may summarize verified current-state facts; it does not own task authorization.
- A status update alone must never change a `CURRENT_TASK.md` prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary.
- If a newly verified status fact changes or invalidates one of those task-owned conditions, state-changing work must stop until `CURRENT_TASK.md` is reconciled and the changed task is re-authorized.
- Ordinary status refreshes that do not affect the task contract do not require task churn.

Allowed reusable files for Corrective A:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`

Do not add a second authority or duplicate the full task contract into the status template.

## Corrective B — Domain Navigation

Clarify coexistence with target-repository semantic authorities as follows:

- Before assuming a navigation map is missing, discover existing accepted business/product/domain/capability maps and determine their authority.
- An existing semantic map may be the authoritative source for product/domain meaning even when its filename is not `DOMAIN_MAP.md`.
- Reuse those maps as evidence and pointers. Do not copy or restate their business truth into a competing navigation artifact.
- A separate navigation projection is created or refreshed only when source/symbol/test/entry-point routing adds value beyond those existing authorities.
- The generic `DOMAIN_MAP.md` template is optional as a navigation projection; the filename is not a target-repository requirement.
- Navigation output remains derived and cannot authorize work or redefine product/domain truth.

Allowed reusable files for Corrective B:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/domain-model.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`

## Root control scope

`CURRENT_STATUS.md` and `CURRENT_TASK.md` may be changed only for Phase G authorization/handoff state.

## Forbidden scope

- any change to `skills/incident-doctor/**`;
- any fourth Skill;
- any target-project mutation or adoption;
- new executable helper, parser, crawler, index, vector/embedding store, semantic database, daemon, background service, installer, or Repo Map program;
- dependency or runtime changes;
- broad wording changes unrelated to the two approved corrections;
- redesign of the three-file control plane, Domain semantics, verification tiers, or Incident Doctor trigger model.

## Implementation requirements

Keep the corrective small and explicit. Preserve existing progressive-disclosure structure: `SKILL.md` states the operational rule; references carry the detailed contract; templates demonstrate the rule without becoming a second authority.

Do not turn the new status/task clarification into a requirement to rewrite `CURRENT_TASK.md` on every status refresh. Reconciliation is required only when the newly verified fact materially changes a task-owned condition.

Do not turn map coexistence into a requirement for a new alias file or automatic discovery system. The agent may discover existing semantic authorities by bounded repository reading and targeted search.

## Verification level

`V0 — documentation / Skill contract corrective`.

Before handoff verify:

- changed reusable paths are exactly the seven allowed files above;
- root changes are only `CURRENT_STATUS.md` and `CURRENT_TASK.md` for handoff;
- `skills/incident-doctor/**` is byte-unchanged from the authorization baseline;
- exactly three reusable Skill directories remain;
- all three `SKILL.md` frontmatter blocks remain valid and their relative links resolve;
- revised templates are consistent with their references and do not create duplicate authorities;
- no executable helper, dependency, runtime, index, daemon, database, installer, or new Skill was added;
- stable historical tag `v0.1.0^{}` still dereferences to `738627a0caad330d277f60cfdaff5f153593135e`;
- task branch is clean and its local/remote heads match where local execution is involved.

## Successful handoff state

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

At handoff, report exact authorization/start SHA, final task-branch SHA, changed paths, verification results, and stable-tag target. Do not merge before independent audit.

## STOP conditions

Stop without broadening scope if:

- `main` or the implementation start SHA drifts unexpectedly before branch creation/work begins;
- unique unpreserved work is found;
- either corrective appears to require `incident-doctor`, a new Skill, executable tooling, dependencies, runtime infrastructure, or target-project changes;
- the requested wording would create a second authority rather than clarify ownership;
- verification reveals an unresolved contradiction with the accepted Skill contracts.

## Current stop point

`AUTHORIZED_FOR_IMPLEMENTATION`

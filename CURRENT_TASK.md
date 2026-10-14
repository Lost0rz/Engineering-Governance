# CURRENT TASK — Project Profile Compactness Corrective v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Correct the reusable `project-profile` output contract exposed by fresh-Web acceptance: generated Profiles understand the authority boundary but still tend to duplicate generic Engineering Governance workflow/protocol detail and grow into a second governance manual.

## Acceptance finding basis

Fresh Web v0.6.0 evidence established:

- exact eight-Skill discovery: PASS;
- ordinary project status/progress routing -> `project-governance`: PASS;
- Project Profile request -> `project-profile` semantic boundary: PASS;
- generated Profile freshness design / exclusion of live PR/HEAD/CI/task state: PASS;
- Profile compactness / generic-workflow deduplication: FAIL / reusable corrective required.

Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` remains the parent acceptance purpose and resumes after this bounded corrective.

## In scope

- strengthen `skills/project-profile/SKILL.md` so a Profile is a compact landing index, not a governance handbook;
- make generic Skill procedures/routing tables/Card schemas/verification tiers/Doctor workflows/artifact mechanics explicit Profile anti-content;
- require template-first output with no extra top-level sections unless project-specific stable context cannot fit the template;
- prefer authority/capability pointers over summarized reusable procedures;
- require explicit Profile surface and PRIMARY/MIRROR/single-surface role when the target surface is known;
- update `profile-contract.md`, template guidance only if needed, and integrated acceptance scenarios;
- preserve Project Profile as `DERIVED_PROJECT_CONTEXT` and preserve all existing mutation/authority boundaries.

## Out of scope

- adding/removing/renaming top-level Skills;
- changing Project Governance task authority;
- changing Handoff schema, verification tiers, Doctor semantics, or Domain Navigation behavior;
- formal GitHub release/merge;
- Local Codex installation/acceptance;
- editing installed Plugin cache as the source of truth.

## Verification

V0/V2 bounded contract review:

- Profile Skill/contract/template are mutually consistent;
- generated-output guidance rejects duplicated reusable workflow while allowing project-specific stable facts and pointers;
- no conflict with AGENTS / STATUS / TASK / Domain / planning ownership;
- integrated acceptance contains a realistic overlong-profile negative case;
- no unrelated files change.

## Stop conditions

Stop if the corrective would require a new authority layer, a fourth control file, a new Skill, or broad changes outside Project Profile/acceptance semantics.

## Handoff / current stop point

Implement the bounded source corrective on PR #26, run a focused source audit, freeze the corrected semantic candidate, reconcile controls, then resume Task 070 Web acceptance against an updated candidate release.

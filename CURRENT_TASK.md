# CURRENT TASK — Project Profile Domain Pointer Corrective

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-DOMAIN-POINTER-CORRECTIVE-077`

Parent task: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Correct the remaining Web Project Profile Domain-dedup adherence failure exposed by fresh Gift `0.6.5` acceptance, using the smallest structural/template change rather than additional synonymous warning prose.

## Fresh evidence / defect

Merloom `0.6.5` Profile regression passed Task-076 adherence.

Gift `0.6.5` materially improved but still returned a reduced ownership catalog under `Authority map` despite an established detailed `docs/storefront/DOMAIN_MAP.md`. The draft separately listed upstream-published fact classes and Gift-owned/runtime fact classes. Those facts were grounded but the Profile recreated navigation authority that already exists elsewhere.

A minor related classification leak placed a fail-closed/no-fixture behavioral rule inside `Environment`; `Environment` should contain platform/environment roles only.

## Authorized source scope

Modify only:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` patch version.

Control files may be reconciled for task/status bookkeeping.

Do not change other Skills or the eight-Skill architecture.

## Required design

1. When an established detailed Domain/navigation authority exists, `Authority map` is structurally pointer-oriented:
   - include the Domain/navigation pointer;
   - do not append Domain-specific upstream/downstream/runtime ownership lists or subsections;
   - at most one short broad ownership invariant may appear elsewhere in the Profile when needed to understand project identity.
2. `Environment` contains only durable platform/environment/data-role context and authority pointers; behavioral fail-closed/fallback/verification/execution rules must be omitted or classified under durable constraints only when genuinely Profile-worthy.
3. The pre-return gate must treat either leak as a non-returnable draft and correct it in the same generation pass.
4. Add explicit Gift/Merloom acceptance coverage for the structural boundary.
5. Bump candidate patch version to `0.6.6`, update the existing Web Plugin identity, verify installed readback, then restore parent Task 070 and run fresh neutral Gift + Merloom Profile regressions.

## Verification

Required source verification:

- compare from this task control checkpoint shows only the authorized five semantic files;
- shipped template/Skill/contract agree on pointer-only Domain behavior;
- integrated acceptance covers both prior Gift and Merloom failure shapes;
- Web overlay source identities match repository source before update;
- installed Web root/platform manifests and shipped Profile files read back as `0.6.6`.

Required behavioral verification after Web update:

- Gift: `Authority map` contains pointers rather than Merloom/Gift ownership catalogs; durable B2B/Product-first/Inquiry/RFQ identity remains; `Environment` has no behavioral rule leakage.
- Merloom: remains free of source/code maps, uses compact Engineering Governance hook, retains durable greenfield/single-Authority/Publication/Merloom-Gift identity.

## Out of scope

- changing ChatGPT Memory behavior;
- adding/changing another top-level Skill;
- formal GitHub v0.6.x release/tag;
- PR #26 merge;
- Local Codex acceptance.

## Stop conditions

Stop before release/merge if source scope expands, installed package identity cannot be verified, or the fresh Gift/Merloom regressions still reproduce the prohibited structural classes.

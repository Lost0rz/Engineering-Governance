# CURRENT TASK — Project Profile Operational Adherence Corrective

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-ADHERENCE-CORRECTIVE-076`

Task class: `EXECUTE`

State: `ACTIVE`

Parent task: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

## Objective

Harden `project-profile` so the already-defined grounding/durability/deduplication rules are executed as a mandatory pre-return compliance gate rather than remaining advisory prose.

Fresh Web `0.6.4` evidence showed three already-forbidden classes still leaking into generated Profiles:

1. stage-only/current-work non-goals promoted into durable constraints (`storefront CMS` in Gift);
2. implementation/source-directory responsibility maps copied into `Environment` (Merloom);
3. per-Skill trigger prose copied into `Engineering Governance` instead of the compact reusable routing hook.

The previous decision to simply rerun the unchanged `0.6.4` candidate is superseded by Owner direction: change the reusable source before the next behavioral test.

## Authorized scope

Only:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` patch version;
- this task/status control reconciliation;
- Web Plugin overlay/update/readback for the same existing Plugin identity.

Do not change the eight-Skill architecture or other Skill contracts.

## Required corrective

### 1. Mandatory pre-return compliance gate

Generation MUST NOT return the Profile until every substantive section passes:

```text
GROUNDED
AND DURABLE
AND CORRECTLY CLASSIFIED
AND DEDUPED
AND TEMPLATE-COMPLIANT
```

A known violation is corrected/removed before output, not merely noted internally.

### 2. Current/stage-only non-goal rejection

A non-goal phrased or owned as `current`, `current work`, `MVP`, `phase`, `wave`, `deferred until`, or equivalent current-delivery scope is not a durable Profile anti-goal unless a separate durable authority establishes it as product identity.

### 3. Environment/source-map separation

`Environment` contains durable platform/environment roles only. Repository source paths, module directories, symbols, file ownership maps and code-responsibility lists are navigation/implementation detail and are omitted when an established Domain/navigation authority exists.

### 4. Fixed Engineering Governance hook

Generated Profile `Engineering Governance` should use the shipped compact hook. Do not add per-Skill trigger prose or enumerate conditional Skills unless the user explicitly asked for routing documentation rather than a Project Profile.

### 5. Established Domain map compression

When detailed Domain/navigation authority exists, Profile may retain only the few broad product/authority distinctions needed to understand the project. Do not create ownership subcatalogs that effectively reconstruct the Domain map.

## Acceptance

Web candidate must demonstrate in fresh neutral prompts:

- Gift: stage-only `storefront CMS` non-goal absent; no detailed ownership mini-map; durable B2B/Product-first/RFQ identity retained.
- Merloom: code-directory responsibility list absent from `Environment`; fixed compact Engineering Governance hook; durable greenfield/single-Authority/Save-Publish identity retained.
- FloatTabs: established Domain map remains a pointer and old Project Instructions do not self-bootstrap.
- fixed metadata fields remain `Profile surface` and `Primary/mirror role`.
- no regression of Task 074 Memory isolation or Task 075 durability/version-scope behavior.

## Stop conditions

Stop before parent Task 070 release/merge progression if installed Web candidate does not contain the exact corrected source or if fresh neutral regressions still reproduce the same prohibited classes.

## Terminal boundary

After focused source/package/readback verification, restore parent Task 070 to fresh Web regression state with the new semantic candidate and Web Plugin version.

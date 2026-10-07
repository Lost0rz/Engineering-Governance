# CURRENT TASK — Phase C Domain Navigation Enrichment

Task ID: `EG-DOMAIN-NAVIGATION-ENRICH-IMPL-014`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_IMPLEMENTATION`

## Objective

Enrich the existing `skills/domain-navigation/` module so it is operationally useful for evidence-backed semantic Domain mapping and task-to-code routing while remaining lightweight, incremental, read-only in purpose, and clearly separated from task authorization and incident diagnosis.

This is the bounded implementation of the user-approved Phase C design. Do not re-plan or expand scope.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase A accepted merge head: `02dd645d06e8fa554e241887c1457f7b15e297b5`.
- Phase B accepted merge head: `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- User-approved Phase C design baseline before this authorization: `e3af6eb7c95d8cd3ee0b3fd29a9648be17b8d524`.
- Authorized branch: `codex/domain-navigation-enrichment`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- The exact implementation start SHA is the Web authorization commit from which the authorized task branch is created; the local execution card supplies that SHA and any mismatch is a STOP.

## In scope

Only these nine reusable Skill files may be enriched:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/domain-model.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/references/evidence-rules.md`
- `skills/domain-navigation/references/refresh-policy.md`
- `skills/domain-navigation/references/repo-map.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`
- `skills/domain-navigation/assets/templates/DOMAIN.md`
- `skills/domain-navigation/scripts/README.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for task handoff/control-state recording.

## Required design behavior

### 1. Domain semantics must be operational

The guidance must define a Domain as a semantic capability/ownership/state/authority boundary, not a directory.

A useful Domain entry should allow an AI to determine from evidence:

- responsibility and explicit non-responsibilities;
- authority/state owner by relevant fact class;
- primary entry points and important symbols;
- upstream dependencies and downstream consumers;
- relevant tests and what they establish;
- main data/control flow when useful;
- runtime/operational entry points when applicable;
- invariants and their sources;
- evidence paths and freshness basis;
- known unknowns, conflicts, or stale areas.

The Domain Map remains a navigation projection and must not become a competing source of product/domain/data/runtime truth.

### 2. Mapping workflow must be task-to-code routing

The normal route must be explicit:

`CURRENT_TASK -> affected Domain(s) -> DOMAIN_MAP -> candidate authorities/entry points/symbols/tests -> optional targeted search or Repo Map -> focused source reading -> confirmed route + unresolved gaps`

When the Domain Map is absent or insufficient for the affected area, inspect the smallest useful evidence set: applicable controls/intent, repository manifests/entry points, relevant source boundaries, tests, and concrete references discovered from them.

Do not begin with an exhaustive whole-repository survey unless the authorized task genuinely requires whole-repository mapping.

Navigation output should identify the focused set of likely useful sources and why they matter while keeping unverified ownership or relationships unresolved.

### 3. Evidence rules must distinguish observation from interpretation

Important map claims must be grounded in concrete paths and, where useful, symbols, tests, manifests, runtime entry points, or accepted project documents.

Required rules:

- direct observations and interpretation remain distinguishable;
- absence of evidence does not become evidence of absence;
- conflicting evidence remains unresolved until an authority/source resolves it;
- directory layout alone cannot establish semantic ownership;
- generated summaries/search rankings/Repo Maps are navigation aids, not source authorities;
- map entries record the revision/observation basis needed to judge freshness;
- no numerical confidence score is required.

### 4. Refresh must be incremental

Define task-relevant refresh triggers including:

- affected map entry absent;
- source path or important symbol moved/removed;
- authority/ownership boundary changed;
- dependency/consumer relationship materially changed;
- relevant test/runtime entry point changed;
- verified source contradicts the current map;
- recorded evidence/freshness basis is too stale for the current decision.

Refresh only affected Domain entries/fields. Do not mark untouched entries as freshly verified merely because another part of the map changed.

Preserve valid evidence references and mark unchecked areas explicitly stale/unknown when appropriate.

### 5. Domain Map and Repo Map must remain separate

Preserve the two-layer model:

- **Domain Map:** stable semantic routing by capability, ownership, authority, boundaries, and evidence.
- **Repo Map:** optional dynamic/read-only relevance selection using file/symbol/dependency relationships under limited context.

A Repo Map may rank candidate source to read next. It may not decide Domain ownership, mutate the Domain Map automatically, authorize work, or replace direct source verification.

Phase C does not implement a Repo Map program.

### 6. Templates must be practical navigation contracts

`DOMAIN_MAP.md` must remain concise enough to scan quickly and act as a project-level semantic index.

`DOMAIN.md` is optional detail only where complexity/navigation need justifies it; not every Domain requires a separate file.

Templates must instruct an adopting AI to:

- derive project-specific values from verified target-repository evidence;
- keep unknown/stale/conflicting fields explicit;
- record evidence/freshness without copying large source contents;
- link to canonical authorities instead of duplicating them;
- avoid fictional architecture facts or folder-derived ownership assumptions.

### 7. No required executable helper in v1

`scripts/README.md` must remain explicit that Phase C requires no executable helper.

Any future helper requires a separately demonstrated navigation gap and separate authorization. It must remain optional/read-only and must not introduce a central index, daemon, database, automatic map mutation, or hidden dependency.

## Out of scope

Do not:

- modify reusable content under `skills/project-governance/` or `skills/incident-doctor/`;
- authorize or execute product/business code changes;
- diagnose incidents;
- redefine task authorization or business/domain truth;
- add a fourth Skill;
- add executable scripts/runtime code/package dependencies;
- add a parser/indexing service, vector/embedding store, semantic database, daemon, background crawler, or automatic map regeneration;
- require MCP or another external service;
- implement a Repo Map program;
- introduce numerical confidence/risk scoring;
- perform real-project adoption/validation in this task;
- modify or move the historical `v0.1.0` tag;
- merge the task branch.

## Verification level

`V0 — Skill/documentation contract enrichment`.

Required verification:

- reusable changes are limited to the nine authorized `domain-navigation` files;
- any root-control changes are handoff-only;
- `SKILL.md` frontmatter remains valid and routing boundaries stay distinct;
- all relative Markdown links resolve;
- Domain/Repo Map semantics remain internally consistent;
- templates match the reference contracts;
- `skills/project-governance/` and `skills/incident-doctor/` remain byte-for-byte unchanged from task start;
- no executable source or dependency manifest is introduced anywhere by this task;
- exactly three top-level Skills remain;
- task branch is clean and local/remote matched at handoff.

Do not run a historical runtime test suite; Phase C changes no runtime behavior.

## Acceptance criteria

A fresh AI reading the target repository plus `domain-navigation` should be able to determine, without inventing project facts:

- what counts as a Domain and what does not;
- which evidence establishes ownership/authority and code-entry claims;
- how to route from an active task to the smallest useful source-reading set;
- when to create or refresh a map entry;
- how to preserve stale/unknown/conflicting areas honestly;
- when a detailed `DOMAIN.md` is justified;
- what a Repo Map may help with and what it may never decide.

The result must reduce broad repository reading and architecture guessing without creating a navigation platform.

## STOP conditions

STOP and return evidence without improvising if:

- live `origin/main` or the authorized branch start SHA differs from the execution card;
- the local canonical checkout or chosen worktree contains unpreserved unique work;
- completing the approved design requires changing a reusable file outside the nine authorized `domain-navigation` paths;
- any change to `project-governance` or `incident-doctor` appears necessary;
- implementation would require executable code, a dependency, installer/runtime/indexing behavior, or real-project adoption work;
- a material requirement is ambiguous enough that proceeding would invent policy not present in the approved design;
- the stable tag target changes;
- remote/control authority drifts during execution in a way that changes task scope.

## Handoff requirements

Before returning to Web:

- set state to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
- record `START_HEAD`, `FINAL_HEAD`, `REMOTE_HEAD`, and local/remote match;
- record exact reusable changed paths and root-control changed paths;
- record `V0` checks and any checks intentionally not run;
- confirm `project-governance` and `incident-doctor` content unchanged;
- confirm no executable/runtime/dependency surface added;
- confirm exactly three top-level Skills remain;
- confirm stable tag target unchanged;
- leave the task worktree clean;
- push only `codex/domain-navigation-enrichment`;
- do not merge.

## Execution evidence

- `START_HEAD`: `9627c8d67cca2114dc9a477052f3bd60da06dbdc`.
- `FINAL_HEAD`: this handoff-control commit; its exact SHA is recorded in the verified post-push executor receipt because a commit cannot contain its own SHA.
- `REMOTE_HEAD`: verified equal to `FINAL_HEAD` after push; exact SHA is in the post-push executor receipt.
- `LOCAL_REMOTE_MATCH`: `YES` after final push verification.
- `WORKING_TREE`: `CLEAN` after final push verification.
- `REMOTE_MAIN`: `9627c8d67cca2114dc9a477052f3bd60da06dbdc` at final pre-push fetch.
- `REUSABLE_CHANGED_PATHS`:
  - `skills/domain-navigation/SKILL.md`
  - `skills/domain-navigation/references/domain-model.md`
  - `skills/domain-navigation/references/mapping-workflow.md`
  - `skills/domain-navigation/references/evidence-rules.md`
  - `skills/domain-navigation/references/refresh-policy.md`
  - `skills/domain-navigation/references/repo-map.md`
  - `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`
  - `skills/domain-navigation/assets/templates/DOMAIN.md`
  - `skills/domain-navigation/scripts/README.md`
- `ROOT_CONTROL_CHANGED_PATHS`: `CURRENT_STATUS.md`, `CURRENT_TASK.md` (handoff only).
- `PROJECT_GOVERNANCE_CHANGED`: `NO`.
- `INCIDENT_DOCTOR_CHANGED`: `NO`.
- `TOP_LEVEL_SKILL_COUNT`: `3`.
- `EXECUTABLE_RUNTIME_ADDED`: `NO`.
- `DEPENDENCY_ADDED`: `NO`.
- `REPO_MAP_PROGRAM_ADDED`: `NO`.
- `STABLE_TAG_TARGET`: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- `V0_CHECK_RESULTS`: `PASS` — exact nine-file reusable allowlist plus two handoff-only root controls; no added/deleted/renamed paths; `git diff --check` clean; sibling Skill diff exit 0; frontmatter and all eight `SKILL.md` links valid; all eight local links across the module resolve; exactly three top-level Skills; contract consistency reviewed; no executable, dependency, index, database, daemon, or generated-binary path added. Historical runtime suite not run because this documentation-only change is authorized at V0.
- `SCOPE_EXPANSION`: `NO`.
- `FINAL_STATE`: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

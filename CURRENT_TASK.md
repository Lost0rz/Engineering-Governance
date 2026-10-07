# CURRENT TASK — Phase C Domain Navigation Enrichment Design

Task ID: `EG-DOMAIN-NAVIGATION-ENRICH-DESIGN-013`

State: `WAITING_FOR_USER_DESIGN_REVIEW`

Mode: `BOUNDED_DESIGN_REVIEW`

## Objective

Define the bounded Phase C enrichment of the existing `skills/domain-navigation/` module so an AI can build or refresh an evidence-backed semantic Domain Map and route an authorized task to the correct capability, authority, source paths, symbols, tests, and focused reading set without turning navigation into a heavyweight indexing/runtime product.

This task is design-only. No local implementation is authorized until the user explicitly approves this bounded design.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase A accepted merge head: `02dd645d06e8fa554e241887c1457f7b15e297b5`.
- Phase B `project-governance` accepted merge head: `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- The current Domain Navigation skeleton was re-read from the merged Phase B baseline before this design was opened.
- Exact Phase C implementation baseline will be captured only after design approval and before the local execution card is issued.

## Proposed Phase C file scope

Only the existing `domain-navigation` module:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/domain-model.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/references/evidence-rules.md`
- `skills/domain-navigation/references/refresh-policy.md`
- `skills/domain-navigation/references/repo-map.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`
- `skills/domain-navigation/assets/templates/DOMAIN.md`
- `skills/domain-navigation/scripts/README.md`

Root controls may be updated only for task authorization/handoff. No other reusable Skill module is part of Phase C.

## Proposed design

### 1. Domain semantics become operational

`domain-model.md` and the templates will define a Domain as a semantic capability/ownership/state/authority boundary, not as a directory.

A useful Domain entry should let an AI determine, from evidence:

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

The Domain Map stays a navigation projection. It links to authorities; it never becomes a competing source of product/domain/data/runtime truth.

### 2. Mapping workflow becomes task-to-code routing, not broad repository summarization

`mapping-workflow.md` will make the normal route explicit:

`CURRENT_TASK -> affected Domain(s) -> DOMAIN_MAP -> candidate authorities/entry points/symbols/tests -> optional targeted search or Repo Map -> focused source reading -> confirmed route + unresolved gaps`

When a Domain Map is absent or insufficient for the affected area, the AI should inspect the smallest useful evidence set: applicable controls/intent, repository manifests/entry points, relevant source boundaries, tests, and concrete references discovered from them.

It must not begin with an exhaustive whole-repository survey unless the authorized task genuinely requires whole-repository mapping.

The navigation result should identify the focused set of likely useful sources and why they matter, while keeping unverified ownership or relationships unresolved.

### 3. Evidence rules distinguish observation from interpretation

`evidence-rules.md` will require important map claims to be grounded in concrete paths and, where useful, symbols, tests, manifests, runtime entry points, or accepted project documents.

Rules:

- direct observations and interpretation remain distinguishable;
- absence of evidence does not become evidence of absence;
- conflicting evidence remains unresolved until an authority/source resolves it;
- directory layout alone cannot establish semantic ownership;
- generated summaries/search rankings/Repo Maps are navigation aids, not source authorities;
- a map entry records the revision/observation basis needed to judge freshness.

No numerical confidence-scoring system is required.

### 4. Refresh is incremental and affected-area scoped

`refresh-policy.md` will define refresh triggers such as:

- task-relevant map entry absent;
- source path or important symbol moved/removed;
- authority/ownership boundary changed;
- dependency/consumer relationship materially changed;
- relevant test/runtime entry point changed;
- verified source contradicts the current map;
- recorded evidence/freshness basis is too stale for the current decision.

Refresh only the affected Domain/fields. Do not mark untouched entries as freshly verified merely because another part of the map was updated.

Preserve known-valid evidence references and mark unchecked areas explicitly stale/unknown where appropriate.

### 5. Stable Domain Map and dynamic Repo Map remain separate

`repo-map.md` will preserve the two-layer model:

- **Domain Map:** stable semantic routing by capability, ownership, authority, boundaries, and evidence.
- **Repo Map:** optional dynamic/read-only relevance selection using file/symbol/dependency relationships under limited context.

A Repo Map may rank candidate source to read next. It may not decide Domain ownership, change the Domain Map automatically, authorize work, or replace direct source verification.

Phase C does not implement a Repo Map program.

### 6. Templates become practical navigation contracts

`DOMAIN_MAP.md` should stay concise enough to scan quickly and act as the project-level semantic index.

`DOMAIN.md` is optional detail for Domains whose complexity/navigation need justifies it; not every Domain requires a separate file.

Templates must instruct an adopting AI to:

- derive every project-specific value from verified target-repository evidence;
- keep unknown/stale/conflicting fields explicit;
- record evidence/freshness without copying large source contents;
- link to canonical authorities rather than duplicating them;
- avoid fictional architecture facts or folder-derived ownership assumptions.

### 7. No required executable helper in v1

`scripts/README.md` remains explicit that Phase C requires no executable helper.

Any future helper would require a separately demonstrated navigation gap and separate authorization. It must be optional/read-only and must not introduce a central index, daemon, database, automatic map mutation, or hidden dependency.

## Out of scope

Phase C must not:

- modify reusable `project-governance` or `incident-doctor` content;
- authorize or execute product/business code changes;
- diagnose incidents;
- redefine the task contract or product/domain truth;
- add a fourth Skill;
- add executable scripts/runtime/dependencies;
- add a parser/indexing service, vector/embedding store, semantic database, daemon, background crawler, or automatic map regeneration;
- require MCP or another external service;
- implement a Repo Map program;
- introduce numerical confidence/risk scoring;
- perform real-project adoption/validation yet.

## Expected verification

`V0` only:

- only the nine existing `domain-navigation` files plus root handoff controls may change;
- `SKILL.md` frontmatter remains valid and routing boundaries stay distinct;
- all relative links resolve;
- Domain/Repo Map semantics remain internally consistent;
- templates match the reference contracts;
- `project-governance` and `incident-doctor` reusable contents remain unchanged;
- no executable source or dependency manifest is introduced;
- exactly three top-level Skills remain;
- task branch is clean and local/remote matched at handoff.

## Success criteria

After Phase C, a fresh AI reading the target repository plus `domain-navigation` should be able to determine, without inventing project facts:

- what counts as a Domain and what does not;
- which evidence establishes ownership/authority and code-entry claims;
- how to route from an active task to the smallest useful source-reading set;
- when to create or refresh a map entry;
- how to preserve stale/unknown/conflicting areas honestly;
- when a detailed `DOMAIN.md` is justified;
- what a Repo Map may help with and what it may never decide.

The result should reduce broad repository reading and architecture guessing without creating a navigation platform.

## Current stop point

`WAITING_FOR_USER_DESIGN_REVIEW`

If the user approves this bounded design, Web will create the implementation authorization from the then-current exact `main` HEAD and issue a local AI execution card. No separate architectural spec or large implementation plan is required for this bounded enrichment.

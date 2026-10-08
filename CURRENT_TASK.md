# CURRENT TASK — Project Governance Structure & Authority Principles

Task ID: `EG-PROJECT-GOVERNANCE-STRUCTURE-AUTHORITY-036`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `REUSABLE_SKILL_ENHANCEMENT`

## Objective

Add two accepted reusable development principles to `project-governance` without turning the Skill into a generic style checker or broad refactoring mandate:

1. single canonical authority per fact/state/behavior class;
2. domain-coherent code structure with anti-redundancy and responsibility-based decomposition.

The principles must guide normal planning, implementation, and review while preserving business-first delivery and proportional scope.

## Authoritative baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Accepted DN-001 merge/main HEAD before this control transition: `b139811812f73d32927287a0bfbae2b5c6b93afa`.
- Existing top-level Skills remain exactly: `project-governance`, `domain-navigation`, `incident-doctor`.
- This task is a new Project Governance enhancement, not a continuation of DN-001.

## Required principle A — Single Canonical Authority

The reusable contract must make the following semantics explicit:

- For each fact, state, policy, mapping, lifecycle, business rule, or behavior contract, establish one canonical authority/owner.
- Multiple consumers, adapters, CLI/UI surfaces, read models, projections, caches, or diagnostics may coexist, but they must derive from or delegate to the canonical authority rather than become competing sources of truth.
- Before adding a new backend/owner/writer for an existing state or behavior class, discover the existing authority and reuse, extend, or explicitly replace it rather than creating a parallel authority.
- Multiple independent writers for the same state class are an architectural risk and require reconciliation rather than silent coexistence.
- Temporary migration coexistence is allowed only when the primary authority, synchronization direction, cutover condition, and retirement boundary are explicit.
- A cache, projection, mirror, UI state, diagnostic view, or compatibility adapter does not become authority merely because it stores or displays the same data.
- "One authority" is per fact/state/behavior class, not one authority for the entire application.

This is a hard architecture principle, not merely a style preference.

## Required principle B — Domain-coherent structure and anti-redundancy

The reusable contract must make the following semantics explicit:

- Keep modules/files cohesive around a clear Domain/capability/responsibility and reason to change.
- Avoid accidental duplicate business behavior, duplicate state ownership, duplicate parsers/adapters/backends/helpers when an accepted semantic implementation already exists.
- Prefer reuse of semantics and invariants, not abstraction merely because syntax looks similar.
- Code duplication alone is a signal, not automatic justification for a shared abstraction. Extract shared code only when responsibility, lifecycle, invariants, and reason-to-change are materially the same.
- Large files are a structural signal, not a hard line-count violation. Split when a file/module mixes distinct capabilities, authorities, orchestration, I/O, UI, persistence, or otherwise accumulates multiple independent reasons to change.
- Do not introduce arbitrary line-count thresholds as a universal rule.
- Do not perform broad opportunistic cleanup simply because duplication or a large file is visible. Refactor only as far as the authorized task needs for correctness, maintainability, safe extension, or clear ownership.

## Intended placement

Preferred minimal structure:

- add `skills/project-governance/references/code-structure.md` as the detailed reusable reference;
- update `skills/project-governance/SKILL.md` to load/reference it when planning or implementing source changes;
- update `skills/project-governance/references/development-flow.md` with the smallest implementation/review gate needed to apply the principles.

Do not modify templates merely for symmetry. `skills/project-governance/assets/templates/AGENTS.md` already says to preserve one owner per fact class; change it only if a concrete semantic gap remains after the primary reference is written and explain why.

## Not authorized

Do not:

- modify `domain-navigation` or `incident-doctor` Skill content;
- create a fourth Skill;
- add linters, static analyzers, file-size enforcement, telemetry, daemons, databases, runtime checks, Repo Map machinery, or automatic remediation;
- impose universal file line-count thresholds;
- rewrite unrelated Project Governance references/templates for consistency prose;
- mutate any business repository;
- bump `plugin.json` version;
- create a Git tag, GitHub Release, or release ZIP;
- merge the task branch.

## Verification

Use `V0 + focused contract review`.

Required checks:

1. exact changed-path scope is minimal;
2. `git diff --check` PASS;
3. Project Governance clearly distinguishes one authority **per fact/state/behavior class** from one authority for the whole application;
4. consumers/adapters/projections/caches remain allowed but are explicitly non-competing/derived;
5. migration coexistence has explicit primary/cutover/retirement semantics;
6. code structure guidance is responsibility/domain based rather than a hard line-count rule;
7. anti-redundancy guidance does not create premature abstraction pressure;
8. business-first rule remains intact: no opportunistic refactor outside task relevance;
9. `domain-navigation` and `incident-doctor` trees are unchanged;
10. `plugin.json` remains version `0.1.0`;
11. no business repository is modified.

A lightweight scenario review should cover:

- two UI/CLI consumers sharing one backend authority -> allowed;
- two independent writers for the same session/mapping state -> reject/reconcile;
- a 1200-line cohesive generated/schema/table file -> not automatically split;
- a 500-line file mixing UI + persistence + orchestration + multiple authorities -> structural split candidate;
- two syntactically similar blocks with different lifecycle/reasons-to-change -> do not force abstraction;
- task encounters unrelated large/duplicate code -> report if relevant, do not expand scope automatically.

## Branch/workspace

Use a dedicated branch such as:

`codex/project-governance-structure-authority-v1`

Before modification:

1. fetch canonical remote;
2. require local base to safely reconcile/fast-forward to live `origin/main` containing this task;
3. preserve unknown staged/unstaged/untracked/local-only work;
4. STOP rather than reset/stash/delete/overwrite unknown work.

## Acceptance

PASS only if the two principles are explicit, reusable, minimally placed, and do not create a new enforcement platform or broad-refactor mandate.

Stop at:

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Return:

```text
TASK_ID: EG-PROJECT-GOVERNANCE-STRUCTURE-AUTHORITY-036
REMOTE_CONTROL_HEAD:
LOCAL_BASELINE_AFTER_SYNC:
TASK_BRANCH:
FINAL_BRANCH_HEAD:
REMOTE_BRANCH_HEAD:
LOCAL_REMOTE_MATCH:
CHANGED_PATHS:
CODE_STRUCTURE_REFERENCE_ADDED: YES/NO
SINGLE_AUTHORITY_RULE: PASS/STOP
AUTHORITY_PER_CLASS_NOT_GLOBAL_SINGLETON: PASS/STOP
CONSUMER_DERIVATION_RULE: PASS/STOP
MIGRATION_BOUNDARY_RULE: PASS/STOP
DOMAIN_COHESION_RULE: PASS/STOP
NO_HARD_LINE_THRESHOLD: PASS/STOP
NO_PREMATURE_ABSTRACTION: PASS/STOP
BUSINESS_FIRST_REFACTOR_BOUNDARY: PASS/STOP
PROJECT_GOVERNANCE_SCOPE_ONLY: PASS/STOP
DOMAIN_NAVIGATION_UNCHANGED: YES/NO
INCIDENT_DOCTOR_UNCHANGED: YES/NO
PLUGIN_VERSION: 0.1.0
BUSINESS_REPO_MUTATED: NO
DIFF_CHECK: PASS/STOP
WORKING_TREE:
FINAL_STATE: WAITING_FOR_INDEPENDENT_WEB_AUDIT / STOP
```

Do not merge or publish under this task.

## Executor handoff

- Remote control head and local baseline after sync: `3237d4f24f8f46657ba6e5fc859f10b50b2915a0`.
- Task branch: `codex/project-governance-structure-authority-v1`.
- Implementation paths: `skills/project-governance/references/code-structure.md` (new), `skills/project-governance/SKILL.md`, and `skills/project-governance/references/development-flow.md`.
- Focused contract review: A shared backend read by CLI and Settings UI is allowed; B independent writers for one session/mapping state require ownership reconciliation; C a cohesive 1200-line generated/schema/table file is not automatically split; D a 500-line module mixing UI, persistence, orchestration, and multiple authorities is a split candidate; E similar syntax with different lifecycle/reason-to-change is not forced into a shared abstraction; F unrelated large/duplicated code does not expand the task.
- V0 checks: `git diff --check` passed; implementation paths are limited to the three authorized Project Governance files; relevant reference links resolve; `domain-navigation`, `incident-doctor`, the existing AGENTS template, and `plugin.json` are unchanged; package version remains `0.1.0`.
- No business repository was accessed or modified. No enforcement, diagnostics, new Skill, tag, release, ZIP, or merge was created.
- Next action: independent Web audit of the exact pushed task branch head.

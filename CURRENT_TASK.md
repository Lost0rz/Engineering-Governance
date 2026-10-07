# CURRENT TASK — Phase B Project Governance Enrichment

Task ID: `EG-PROJECT-GOVERNANCE-ENRICH-IMPL-012`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `BOUNDED_IMPLEMENTATION`

## Objective

Enrich the existing `skills/project-governance/` module so it is operationally useful for normal AI-assisted development while remaining lightweight, business-first, evidence-backed, and clearly separated from Domain Navigation and Incident Doctor.

This is a bounded implementation of the user-approved Phase B design. Do not re-plan or expand scope.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase A accepted merge head: `02dd645d06e8fa554e241887c1457f7b15e297b5`.
- User-approved Phase B design/control baseline before implementation authorization: `88c070596b52f465194c37903921efef76c63350`.
- Authorized branch: `codex/project-governance-enrichment`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- The exact implementation start SHA is the Web authorization commit from which the authorized task branch is created; the local execution card supplies that SHA and any mismatch is a STOP.

## In scope

Only these seven reusable Skill files may be enriched:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/assets/templates/AGENTS.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`
- `skills/project-governance/assets/templates/CURRENT_TASK.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for task handoff/control-state recording.

## Required design behavior

### 1. Operational three-file control plane

The guidance must make ownership and update rules explicit:

- `AGENTS.md` owns durable repository/project operating rules, stable boundaries, and verified pointers to authoritative sources; it is not a task log or current-status dump.
- `CURRENT_STATUS.md` owns the concise verified current-state snapshot, accepted baseline/capabilities, active blockers, and next milestone; it is not chronological history and must not duplicate source authorities.
- `CURRENT_TASK.md` owns the single active work authorization: objective, affected domains, start baseline, scope, evidence, risk, verification, acceptance, stop conditions, and handoff point; it does not redefine durable rules or business/domain truth.

Define when each file changes, how same-class facts avoid duplicate ownership, and how stale/current evidence is represented without inventing facts.

### 2. Business-first normal development flow

The minimum repeatable flow must be clear:

1. read applicable repository guidance and current task;
2. establish the baseline needed for the authorized work;
3. identify affected Domain(s), using `domain-navigation` when semantic ownership/code location is unclear;
4. implement the smallest authorized product/business outcome;
5. verify at the lightest safe `V0`–`V3` level;
6. update only controls whose verified facts materially changed;
7. hand off or close cleanly.

A material objective/scope change requires task re-authorization before continuing. Ordinary evidence discovery inside the accepted objective does not create a new task by itself.

Routine work must not build diagnostics in parallel. Enter `incident-doctor` only for a real failure, unexplained behavior, or unsafe ambiguity that blocks safe progress and cannot be answered from existing evidence.

### 3. Lightweight verification selection

Retain `V0`–`V3` and add concise selection guidance without a numeric score:

- `V0`: documentation, controls, repository layout/path/link/frontmatter changes.
- `V1`: localized behavior with narrow blast radius and no meaningful state/integration risk.
- `V2`: domain-level behavior, persistence/state, external integration within a domain, or meaningful integration boundaries.
- `V3`: cross-domain, concurrency, security, system/runtime, release-critical, or broad user-critical path changes.

`CURRENT_TASK.md` must record the chosen level and rationale. Choose the lightest level that can safely establish the task; do not inherit a full historical suite merely because it exists.

### 4. Templates are adaptation contracts

The three templates must instruct an adopting AI to derive values from verified target-project evidence, keep unknowns explicit, avoid fictional examples, and omit commands/fields that are not actually justified by the target repository.

Keep templates concise enough to use routinely.

### 5. Skill routing remains explicit

`project-governance/SKILL.md` remains the normal governed-development entrypoint. It must route semantic repository understanding to `domain-navigation` and real evidence-insufficient incidents to `incident-doctor`. It must not become a codebase mapper, diagnostics platform, installer, runtime, or enforcement engine.

## Out of scope

Do not:

- modify reusable content under `skills/domain-navigation/` or `skills/incident-doctor/`;
- add a new Skill module;
- add executable scripts, runtime code, package/dependency manifests, or generated binaries;
- add an installer or Bootstrap CLI;
- add a daemon, service, database, enforcement engine, automatic remediation, or MCP prerequisite;
- add a complex numerical risk score;
- require a full test suite for every task;
- add project-specific facts to reusable templates;
- perform real-project adoption/validation in this task;
- modify or move the historical `v0.1.0` tag;
- merge the task branch.

## Verification level

`V0 — Skill/documentation contract enrichment`.

Required verification:

- changed reusable paths are limited to the seven authorized `project-governance` files;
- any root-control changes are handoff-only;
- `SKILL.md` frontmatter remains valid and the trigger/boundary is distinct;
- all relative Markdown links from `SKILL.md` resolve;
- control-plane, development-flow, verification-tier guidance, and templates are internally consistent;
- `skills/domain-navigation/` and `skills/incident-doctor/` are byte-for-byte unchanged from the task start;
- no executable source or dependency manifest is introduced anywhere by this task;
- task branch is clean and local/remote matched at handoff.

Do not run a historical runtime test suite; Phase B changes no runtime behavior.

## Acceptance criteria

A fresh AI reading the target repository plus `project-governance` should be able to determine, without inventing project facts:

- which control file owns a durable rule, current-state fact, or active-task authorization;
- when each control file must be updated;
- how to start, execute, scope-change, verify, hand off, and close a normal business/product task;
- when code/authority discovery should route to Domain Navigation;
- when a real failure should route to Incident Doctor;
- which `V0`–`V3` verification level is proportionate and why.

The result must reduce process ambiguity without making normal development materially heavier.

## STOP conditions

STOP and return evidence without improvising if:

- live `origin/main` or the authorized branch start SHA differs from the execution card;
- the local canonical checkout or chosen worktree contains unpreserved unique work;
- completing the design requires changing a reusable file outside the seven authorized `project-governance` paths;
- any change to `domain-navigation` or `incident-doctor` appears necessary;
- implementation would require executable code, a dependency, installer/runtime behavior, or real-project adoption work;
- a material requirement is ambiguous enough that proceeding would invent project-independent policy not present in the approved design;
- the stable tag target changes;
- remote/control authority drifts during execution in a way that changes task scope.

## Handoff requirements

Before returning to Web:

- set state to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
- record `START_HEAD`, `FINAL_HEAD`, `REMOTE_HEAD`, and local/remote match;
- record exact reusable changed paths and root-control changed paths;
- record `V0` checks and any checks intentionally not run;
- confirm `domain-navigation` and `incident-doctor` content unchanged;
- confirm no executable/runtime/dependency surface added;
- confirm stable tag target unchanged;
- leave the task worktree clean;
- push only `codex/project-governance-enrichment`;
- do not merge.

## Execution evidence

- `START_HEAD`: `e664d4ed52ae7ceca91fe43913a3e9158d451d8f`.
- `FINAL_HEAD`: this handoff-control commit; its exact SHA is recorded in the verified post-push executor receipt because a commit cannot contain its own SHA.
- `REMOTE_HEAD`: verified equal to `FINAL_HEAD` after push; exact SHA is in the post-push executor receipt.
- `LOCAL_REMOTE_MATCH`: `YES` after final push verification.
- `WORKING_TREE`: `CLEAN` after final push verification.
- `REMOTE_MAIN`: `e664d4ed52ae7ceca91fe43913a3e9158d451d8f` at final pre-push fetch.
- `REUSABLE_CHANGED_PATHS`:
  - `skills/project-governance/SKILL.md`
  - `skills/project-governance/references/control-plane.md`
  - `skills/project-governance/references/development-flow.md`
  - `skills/project-governance/references/verification-tiers.md`
  - `skills/project-governance/assets/templates/AGENTS.md`
  - `skills/project-governance/assets/templates/CURRENT_STATUS.md`
  - `skills/project-governance/assets/templates/CURRENT_TASK.md`
- `ROOT_CONTROL_CHANGED_PATHS`: `CURRENT_STATUS.md`, `CURRENT_TASK.md` (handoff only).
- `DOMAIN_NAVIGATION_CHANGED`: `NO`.
- `INCIDENT_DOCTOR_CHANGED`: `NO`.
- `EXECUTABLE_RUNTIME_ADDED`: `NO`.
- `DEPENDENCY_ADDED`: `NO`.
- `STABLE_TAG_TARGET`: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- `V0_CHECK_RESULTS`: `PASS` — exact seven-file reusable allowlist plus two handoff-only root controls; `git diff --check` clean; `skills/domain-navigation/` and `skills/incident-doctor/` diff exit 0; frontmatter and all eight local/cross-Skill links valid; exactly three top-level Skills; internal contract consistency reviewed; no executable, runtime, or dependency path added. Historical runtime suite not run because this documentation-only change is authorized at V0.
- `SCOPE_EXPANSION`: `NO`.
- `FINAL_STATE`: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Current stop point

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

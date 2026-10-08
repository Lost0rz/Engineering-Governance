# CURRENT TASK — InvestDesk Minimal Bounded Adoption

Task ID: `EG-INVESTDESK-BOUNDED-ADOPTION-030`

State: `ACTIVE_BOUNDED_ADOPTION`

Mode: `TARGET_GOVERNANCE_ADOPTION_ONLY`

## Objective

Apply the user-approved minimal Engineering-Governance adoption to `Lost0rz/InvestDesk` without changing product/business behavior. Preserve existing InvestDesk authorities and make only the bounded Project Governance alignment proven necessary by the read-only gap audit.

## Authority and verified start baselines

- Engineering-Governance accepted Skill/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Engineering-Governance task start head: `1bbef2a9988b6b200f464c8460ad80228bda4687`.
- Target repository: `Lost0rz/InvestDesk`.
- Target verified `main` start SHA: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- User-approved design: minimal adoption only; no new governance/domain/incident artifacts.

## Affected governance domains

- Project Governance / control-plane semantics.
- Task metadata and handoff structure.

Domain Navigation is validated by existing InvestDesk semantic authorities and requires no new artifact. Incident Doctor remains inactive.

## Allowed target changes

On one bounded adoption branch only:

1. `CURRENT_STATUS.md` and `CURRENT_TASK.md` to establish and later hand off the adoption task;
2. `AGENTS.md` only for the two approved governance corrections:
   - make PR/branch/worktree verification conditional on task relevance while preserving protection against unexplained drift and unknown unique work;
   - state explicitly that `CURRENT_STATUS.md` is factual state, never an authorization override, and that a status fact invalidating a task-owned prerequisite/acceptance/STOP/allowed-side-effect/authorization boundary requires `CURRENT_TASK.md` reconciliation before state-changing work.
3. Use the adoption task's own `CURRENT_TASK.md` to demonstrate stable Task ID, affected domains, exact start baseline, risk/verification rationale, and consolidated STOP conditions.

## Forbidden target changes

- product source or tests;
- schema, migration, persistence, API, frontend behavior, dependencies, CI behavior, or business contracts;
- MVP-D Decision↔Transaction business semantics;
- `DOMAIN_MAP.md`, `DOMAIN.md`, `INCIDENT.md`;
- new probes, telemetry, observability expansion, navigation scripts/index/database/daemon/runtime;
- unrelated documentation cleanup or refactor;
- merge to target `main` without explicit user merge authorization.

## Risk and verification rationale

Risk: low but authority-sensitive. The change is documentation/control-plane only, but incorrect wording could block normal development or create competing authorization semantics.

Verification level: `V0` plus independent remote diff audit. This is sufficient because no executable/product behavior is authorized. Verify exact paths, branch ancestry, target-main freshness, absence of product/test changes, and semantic compliance with the approved design.

## Consolidated STOP conditions

STOP without target mutation beyond already-authorized control establishment if:

- target `main` differs from the verified start SHA before branch creation and cannot be coherently reconciled;
- existing target controls reveal a conflicting higher-authority task or changed business objective;
- the necessary change would require product/test/schema/runtime mutation;
- an additional governance/domain/incident artifact appears necessary;
- unexpected branch/PR/worktree authority is discovered that makes the bounded remote edit unsafe;
- the final diff contains anything outside `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.

## Acceptance criteria

- one bounded target branch from the verified target baseline;
- target control plane explicitly authorizes adoption before `AGENTS.md` changes;
- only the approved two `AGENTS.md` corrections are made;
- no new governance/domain/incident artifact;
- no product/test/schema/dependency/business-contract change;
- target branch independently audited against unchanged target `main`;
- adoption branch stops at `WAITING_FOR_INDEPENDENT_WEB_AUDIT` or audited equivalent;
- no merge without explicit user authorization.

## Current stop point

`ACTIVE_BOUNDED_ADOPTION`

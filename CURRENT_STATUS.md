# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07 — Phase F completed the second real-project read-only validation against InvestDesk at an unchanged target `main`. InvestDesk was not mutated, and the three accepted reusable Skills remain unchanged.

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose remains a reusable AI engineering-governance Skill source repository, not a governance runtime/product and not an installer.
- Stable historical tag `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Accepted reusable Skill revision used for both real-project pilots remains Phase D merge head `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Exactly three reusable Skills remain live: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Accepted merged baseline

- Phase A Skill-source restructuring: accepted and merged.
- Phase B `project-governance`: accepted and merged at `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Phase C `domain-navigation`: accepted and merged at `1d28250717e4e72754655ccc3c69bc3664a70eae`.
- Phase D `incident-doctor`: accepted and merged at `ed9cab436f482648288d8fd50553e629f7a1c5a2`.

## Real-project validation baseline

### Phase E — RemoteOrbit

- Incident-heavy runtime project.
- `PROJECT_GOVERNANCE_FIT`: PASS.
- `DOMAIN_NAVIGATION_FIT`: PASS.
- `INCIDENT_DOCTOR_FIT`: PASS.
- A real status/task drift was observed where a status change affected a task prerequisite without corresponding task reconciliation.

### Phase F — InvestDesk

- Normal business/product planning project.
- Task: `EG-INVESTDESK-PILOT-READONLY-019`.
- Target repository: `Lost0rz/InvestDesk`.
- Target `main` at authorization and final freshness check: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Target active business task: MVP-D Decision ↔ Transaction Traceability planning/contract gate.
- `PROJECT_GOVERNANCE_FIT`: PASS.
- `DOMAIN_NAVIGATION_FIT`: PASS.
- `INCIDENT_DOCTOR_NON_TRIGGER_FIT`: PASS.
- `INVESTDESK_MUTATED_BY_PILOT`: NO.
- `REUSABLE_SKILL_CONTENT_MUTATED_DURING_PILOT`: NO.
- `WHOLE_REPOSITORY_SURVEY_REQUIRED`: NO.

## Cross-project findings

Two materially different projects now support two bounded reusable clarifications for review:

1. **Task contract must not be silently overridden by status.** `CURRENT_STATUS.md` may summarize verified current facts, but when a newly verified fact changes a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, `CURRENT_TASK.md` must be reconciled before state-changing work continues. RemoteOrbit exposed the failure mode; InvestDesk shows the healthy pattern in its existing change-control rules and coherent planning gate.
2. **Domain navigation must coexist with existing semantic maps.** A target repository may already have authoritative business/domain maps under another name. InvestDesk has `docs/product/DOMAIN_MODEL_MAP.md` and `BUSINESS_CAPABILITY_MAP.md`. A navigation projection must discover and reference such authorities rather than assuming a new file named `DOMAIN_MAP.md` is required or duplicating product truth.

No evidence supports changing the Incident Doctor contract: it correctly remained inactive in InvestDesk because no real evidence-deficient failure blocked the business planning task.

## InvestDesk routing result

The MVP-D task was routable with bounded evidence through these semantic areas:

- Human Decision Intent;
- Transaction Ledger Fact;
- Position Reconstruction;
- Asset Workspace / Timeline Composition;
- a not-yet-frozen Decision↔Transaction Traceability Edge, which is the current contract target rather than an existing authority.

The existing business authorities preserve `Decision != Transaction`, immutable endpoints, Position derivation from financial facts, and Workspace as a read-only composition layer. Exact relation ownership/cardinality/correction rules remain intentionally unresolved for the target MVP-D planning gate and were not invented by this pilot.

## Current milestone

State: `WAITING_FOR_USER_NEXT_PHASE_DECISION`.

Recommended next phase is one bounded cross-project corrective design for the two evidence-backed clarifications above. Do not change reusable Skill contents or adopt them into target projects without explicit authorization.

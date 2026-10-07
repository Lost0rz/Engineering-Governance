# CURRENT TASK — Phase F InvestDesk Read-Only Skill Validation Handoff

Task ID: `EG-INVESTDESK-PILOT-READONLY-019`

State: `WAITING_FOR_USER_NEXT_PHASE_DECISION`

Mode: `READ_ONLY_VALIDATION_HANDOFF`

## Objective

Record the completed second real-project validation of the accepted `project-governance`, `domain-navigation`, and `incident-doctor` Skills against InvestDesk's normal MVP-D business-planning gate, preserving the read-only boundary and separating validation evidence from later reusable corrective or target-project adoption authorization.

## Authority and reviewed baselines

- Accepted reusable Skill revision: `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Engineering-Governance Phase F authorization head: `9a27be92c2036c210b77dfc05a1391ababe7a904`.
- Target repository: `Lost0rz/InvestDesk`.
- InvestDesk `main` at authorization: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- InvestDesk `main` at final freshness check: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Target task remained `MVP-D Decision ↔ Transaction Traceability Planning Gate`.
- InvestDesk's own controls, accepted product contracts/ADRs, and verified Git remain authoritative for InvestDesk.

## Validation result

### Project Governance

`PASS`.

A fresh AI can identify the active business task and construction boundary from InvestDesk's three-file control plane without chat history. `AGENTS.md` keeps durable operating rules, `CURRENT_STATUS.md` identifies the accepted product baseline and next coherent business gap, and `CURRENT_TASK.md` owns the active MVP-D contract/authority audit and explicitly forbids production implementation before independent contract acceptance.

Unlike the initial RemoteOrbit sample, no current conflict was found between InvestDesk `CURRENT_STATUS.md` and `CURRENT_TASK.md`. InvestDesk's durable change-control rule independently states that a finding that changes the task boundary requires control reconciliation before implementation continues. This supports narrowing the Phase E lesson: status may report verified facts, but task-owned prerequisites, acceptance, STOP conditions, allowed side effects, and authorization boundaries must not be silently overridden by status.

### Domain Navigation

`PASS`.

The MVP-D planning task was routed without a whole-repository survey.

Smallest useful semantic route:

1. **Human Decision Intent**
   - business authorities: `docs/product/CORE_BUSINESS_OBJECTS.md`, `docs/product/INTERACTION_MODEL.md`, `docs/product/USER_JOURNEYS.md`, `docs/decisions/ADR-010-decision-intent-vs-transaction-fact.md`, `docs/decisions/ADR-029-immutable-human-decision-record.md`;
   - source boundary: `apps/api/src/investdesk_api/application/decision.py`, Decision contract/model paths;
   - focused tests: `apps/api/tests/test_decisions.py` and existing web Decision tests as needed;
   - owns immutable human intent/context/idempotency, not execution or Position mutation.

2. **Transaction Ledger Fact**
   - business authorities: ADR-010 plus `ADR-028-immutable-transaction-request-idempotency.md` and accepted MVP-B contract material;
   - source boundary: `application/trade_transaction.py`, `application/transaction_ledger.py`, Transaction persistence/model paths;
   - focused tests: `test_trade_transactions.py`, `test_transactions.py`;
   - owns actual immutable trade facts and transaction idempotency, not human Decision intent.

3. **Position Reconstruction**
   - source boundary: `application/position_reconstruction.py` plus opening-holding and identity authorities;
   - focused tests: `test_position_reconstruction.py`;
   - Position remains derived from opening baseline plus canonical financial facts/Transactions; Decision does not contribute to reconstruction.

4. **Asset Workspace / Timeline Composition**
   - accepted authority includes `ADR-027-asset-workspace-read-model.md` and ADR-029 extensions;
   - source boundary: `application/asset_workspace.py`, web Workspace/API/types and existing Workspace tests;
   - read-only composition only; it must not become Decision, Transaction, Position, or traceability-edge truth.

5. **Decision ↔ Transaction Traceability Edge**
   - this is the current MVP-D contract target, not an existing implemented authority;
   - exact relation owner, reverse cardinality, append-only/correction semantics, compatibility rules, API/UI shape, and idempotency remain intentionally unresolved until InvestDesk's own planning gate freezes them;
   - the pilot did not invent those answers.

InvestDesk already has `docs/product/DOMAIN_MODEL_MAP.md` and `BUSINESS_CAPABILITY_MAP.md` as product/business semantic authorities. They are useful inputs to navigation but are not the same thing as the reusable Skill's derived navigation projection. A future adoption must not create a competing map that restates product truth merely because the generic template is named `DOMAIN_MAP.md`.

### Incident Doctor

`DOCTOR_NOT_TRIGGERED — PASS`.

The current InvestDesk task contains open product-contract questions, not a real failure, unexplained runtime behavior, or unsafe evidence gap. Existing evidence is sufficient to identify the current business authorities and the missing traceability contract boundary. No probe, fresh incident, additional logging, or diagnostic platform is justified.

This validates the Doctor boundary in normal work: unresolved design questions are not incidents by default.

## Cross-project conclusion

Two materially different pilots now justify a bounded corrective design review, but not an architecture expansion.

### Corrective candidate A — Project Governance

Clarify that `CURRENT_STATUS.md` cannot override `CURRENT_TASK.md`. If a newly verified current-state fact changes a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, reconcile and re-authorize the task before state-changing work continues.

Evidence basis:

- RemoteOrbit exposed an actual drift of this class.
- InvestDesk demonstrates the healthy behavior and already carries an equivalent project-local change-control rule.

### Corrective candidate B — Domain Navigation

Clarify target-map coexistence: first discover existing product/domain/capability maps and their authority. Do not assume an exact `DOMAIN_MAP.md` filename must exist, and do not create a navigation projection that competes with an accepted business/domain map. Reuse authoritative maps as evidence/pointers; keep navigation-specific source/symbol/test routing separate and derived.

Evidence basis:

- RemoteOrbit had no existing Domain Map and could still be routed from focused evidence.
- InvestDesk already has named product maps whose semantics must not be shadowed by a generic navigation template.

### Incident Doctor

No corrective justified from the two pilots. RemoteOrbit exercised Doctor positively; InvestDesk correctly bypassed it.

## Mutation audit

- `INVESTDESK_MUTATED_BY_PILOT`: `NO`.
- `INVESTDESK_BRANCH_OR_REF_MUTATED`: `NO`.
- `INVESTDESK_RUNTIME_OR_DB_MUTATED`: `NO`.
- `REUSABLE_SKILL_CONTENT_MUTATED_DURING_PHASE_F`: `NO`.
- `WHOLE_REPOSITORY_SURVEY_REQUIRED`: `NO`.
- `INCIDENT_DOCTOR_TRIGGERED`: `NO`.

## Deferred InvestDesk adoption recommendation

Do not modify InvestDesk under this Phase F task. If adoption is later authorized, retain its existing `AGENTS.md` and product/domain authority documents. Add at most a lightweight navigation projection or pointer layer that references existing product maps and maps them to source/symbol/test authorities without duplicating business truth. Keep `CURRENT_STATUS.md` and `CURRENT_TASK.md` in their existing distinct roles. No incident file, index, daemon, database, or diagnostic platform is justified for this business task.

## Verification

`V0 — read-only integration validation`.

- target initial/final `main`: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc` / same;
- accepted Skill revision: `ed9cab436f482648288d8fd50553e629f7a1c5a2`;
- direct controls, product contracts/ADRs, focused source paths, persistence boundaries, frontend contracts, and focused test inventory inspected;
- target mutation: none;
- reusable Skill mutation: none;
- unresolved MVP-D contract choices left unresolved.

## Current stop point

`WAITING_FOR_USER_NEXT_PHASE_DECISION`

Recommended next phase: a bounded cross-project corrective design limited to the two evidence-backed clarifications above. Do not modify reusable Skill contents until the user explicitly approves that next phase.

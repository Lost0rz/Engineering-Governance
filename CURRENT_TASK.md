# CURRENT TASK — InvestDesk Adoption Gap Audit

Task ID: `EG-INVESTDESK-ADOPTION-GAP-AUDIT-029`

State: `WAITING_FOR_USER_ADOPTION_DESIGN_REVIEW`

Mode: `READ_ONLY_TARGET_ADOPTION_AUDIT`

## Objective

Complete the first full adoption-gap audit of the accepted Engineering-Governance three-Skill baseline against `Lost0rz/InvestDesk`, without modifying InvestDesk, and hand off the smallest evidence-backed bounded-adoption design for user review.

## Verified target baseline

- Target repository: `Lost0rz/InvestDesk`.
- Target `main` at audit start: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Target `main` at audit end: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Open PRs observed: none.
- Remote branches observed: `main` only.
- Target mutation by this audit: none.

## Project Governance findings

Keep the existing InvestDesk control plane and project-specific policies. It already has strong three-file authority, non-destructive worktree lifecycle, Mac mini/Air acceptance, and README entry routing.

Bounded adoption recommendations:

1. In `AGENTS.md`, make baseline/PR/worktree checks explicitly task-relevant/conditional instead of requiring an active PR/worktree fact when a task has not created one yet; preserve STOP for unexplained drift or unknown unique work where destructive assumptions would be required.
2. In `AGENTS.md`, state explicitly that `CURRENT_STATUS.md` is a fact snapshot, not an authorization override. If a new verified fact changes a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, reconcile/re-authorize `CURRENT_TASK.md` before state-changing work.
3. For the next safe task transition, use stable Task ID, affected domains, verified start baseline, risk + verification rationale, and consolidated STOP conditions in `CURRENT_TASK.md`. Do not interrupt the current MVP-D planning gate merely to reformat it unless adoption is intentionally made the active task.

No `CURRENT_STATUS.md` structural rewrite is required.

## Domain Navigation findings

Existing semantic authorities are sufficient and must be preserved:

- `docs/product/BUSINESS_CAPABILITY_MAP.md`
- `docs/product/DOMAIN_MODEL_MAP.md`
- `docs/product/CORE_BUSINESS_OBJECTS.md`
- relevant user-journey/product contracts

For the current MVP-D task, focused routing succeeds without a new semantic map:

- Decision authority/source: `apps/api/src/investdesk_api/application/decision.py` → `DecisionService`
- Transaction product/ledger: `application/trade_transaction.py` → `TradeTransactionService`; `application/transaction_ledger.py`
- Position: `application/position_reconstruction.py` → `PositionQuantityReconstructionService`
- Workspace composition: `application/asset_workspace.py` → `AssetWorkspaceReadService`
- backend tests: `test_decisions.py`, `test_trade_transactions.py`, `test_transactions.py`, `test_position_reconstruction.py`, `test_asset_workspace.py`
- frontend/API routing evidence: `apps/web/src/api/investdesk.ts`, `App.decision.test.tsx`, `App.trade-transactions.test.tsx`, `App.tsx`

`docs/observability/BOUNDARY_MAP.md` is a specialized diagnostic/runtime boundary aid, not general product/domain truth.

Initial adoption recommendation: **do not add `DOMAIN_MAP.md`, `DOMAIN.md`, or a separate navigation projection yet**. Use the real-task trial to measure whether repeated routing friction actually exists; add a derived navigation projection later only with evidence of durable value.

## Incident Doctor trigger decision

`DO_NOT_TRIGGER`.

Current InvestDesk work is a product contract/authority planning gate, not a real failure with insufficient evidence. Existing D1-D5 diagnostics are accepted/closed. Do not manufacture an incident or add probes/telemetry/diagnostic infrastructure for adoption.

## Adoption proposal

### KEEP

- existing `AGENTS.md` project-specific rules except for the bounded wording corrections above;
- existing `CURRENT_STATUS.md` role/content model;
- current business/domain authorities under `docs/product/`;
- README control-plane/product-document routing;
- current worktree/branch lifecycle and Mac mini/Air interactive acceptance policy;
- existing closed observability/diagnostic foundation.

### MODIFY

- `AGENTS.md`: bounded Project Governance alignment only;
- `CURRENT_TASK.md`: adopt richer task metadata at the next safe task transition (or in a deliberately authorized adoption transition), without changing the current MVP-D business objective/semantics.

### ADD

- none in the initial adoption.

### DO NOT ADD

- new semantic `DOMAIN_MAP.md` / `DOMAIN.md`;
- `INCIDENT.md` without a real Doctor-triggering incident;
- new probes, telemetry, diagnostic platform/runtime;
- Repo Map/index/vector DB/daemon/navigation script;
- installer/bootstrap/enforcement runtime;
- duplicate business/domain authority.

## Real-task trial acceptance criteria

After bounded adoption, use the next real InvestDesk business task and verify:

1. **Task clarity:** a new executor can identify objective, authority, affected domains, baseline, scope, acceptance, verification depth, and STOP conditions without chat history.
2. **Navigation efficiency:** from the task, the executor reaches the relevant semantic authorities and focused source/symbol/tests without a broad whole-repository survey; no duplicate domain truth is created.
3. **Business-first behavior:** most work proceeds on the actual product task; governance does not become a parallel workstream.
4. **STOP quality:** STOP occurs only for material authority/baseline/scope/safety problems, not because optional PR/worktree facts are absent before they exist.
5. **Doctor routing:** ordinary design/test failures with sufficient evidence are handled normally; Incident Doctor triggers only for a real decision-blocking evidence gap.
6. **Verification proportionality:** the task uses the lightest V0–V3 level that establishes the result safely, including Air-side LAN acceptance when an interactive web surface changes.
7. **Closeout:** task state, accepted baseline, PR/branch/worktree lifecycle, and next milestone are accurately synchronized.

## Unresolved unknowns

- Local Mac mini worktree state was not independently visible to this Web audit; remote truth shows only `main` and no open PRs.
- Whether a persistent derived navigation projection is worthwhile remains intentionally unresolved until a real task demonstrates repeated navigation friction.

## Stop point

`WAITING_FOR_USER_ADOPTION_DESIGN_REVIEW`

No InvestDesk mutation is authorized under this Task ID.

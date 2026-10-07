# Read-Only Reality Check — InvestDesk

**Purpose:** check whether the candidate Governance Model explains a real
project's existing authorities and workflows without inventing or duplicating
them. This is not an InvestDesk audit acceptance, product recommendation, or
implementation task.

## Snapshot and method

- Repository: `Lost0rz/InvestDesk`.
- Selected checkout: `/Users/ox_miles/Documents/Code/InvestDesk`.
- Branch / HEAD: `main` / `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- At inspection: clean working tree; canonical `main` checkout only in
  `git worktree list --porcelain`.
- The prior authorized live fetch/ff-only sync established
  `origin/main = e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- A read-only GitHub CLI query on 2026-10-06 returned zero open InvestDesk
  PRs.
- `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` were read. The
  active task is `MVP-D Decision ↔ Transaction Traceability Planning Gate`,
  `ACTIVE — CONTRACT / AUTHORITY AUDIT ONLY`.
- Inspection was limited to controls, accepted contracts/ADRs, selected code,
  and UI text at the pinned revision. No tests, runtime, database, or
  browser/LAN behavior were exercised. No InvestDesk file, branch, PR, or
  worktree was modified by this task.

## Reality classifications

| Area | Classification | Verified reality and candidate fit |
|---|---|---|
| Business / product intent | **SUPPORTED** | `docs/product/INTERACTION_MODEL.md` and `docs/product/USER_JOURNEYS.md` state that Decision is human intent, Transaction is a later actual fact, and the path may include zero or more related Transactions. This is already an explicit outcome/intent contract. |
| Domain boundaries | **SUPPORTED** | `docs/product/CORE_BUSINESS_OBJECTS.md`, ADR-010, ADR-013, and ADR-029 preserve Decision, Transaction, and derived Position as distinct concepts. One Decision may relate to 0..N Transactions. The relation is explicitly deferred in MVP-C rather than silently inferred. |
| Architecture | **SUPPORTED** | ADR-021 defines read-only Position reconstruction; ADR-027 defines Asset Workspace as a composition/read model and Timeline as noncausal chronology. ADR-029 adds a bounded Decision projection without making Workspace canonical. The candidate's source/projection distinction fits. |
| Implementation / integration | **PARTIALLY_SUPPORTED** | Immutable/idempotent Decision and Transaction boundaries, canonical service composition, and a read-only Workspace exist. No explicit Decision↔Transaction relation is present in the inspected MVP-C contract or Workspace composition; the active MVP-D planning gate exists to settle that contract. This is a scoped missing relation, not authority to implement it here. |
| Verification / release | **PARTIALLY_SUPPORTED** | InvestDesk controls distinguish task scope, validation, local build/runtime, LAN interaction, and acceptance. MVP-C acceptance documents enumerate API, persistence, concurrency, and browser criteria. The candidate does not yet find a common reusable profile/check/evidence record across those project-specific controls. No relation-specific tests exist because the relation is deferred. |
| Runtime / operability | **PARTIALLY_SUPPORTED** | `docs/deployment/DEPLOYMENT_PRINCIPLES.md` and `docs/observability/DIAGNOSTIC_RUNBOOK.md` describe runtime identity/readiness and diagnosis boundaries. This inspection did not verify a live runtime. The candidate's runtime layer is useful only when bound to a specific build, process, environment, and health evidence. |
| Incident / feedback | **PARTIALLY_SUPPORTED** | The diagnostic runbook orders evidence collection and asks operators to separate persisted facts from intended state. It does not establish a standalone incident authority/lifecycle record in the sampled controls. The candidate should link to existing incident/task systems rather than become another incident tracker. |
| Authority map | **PARTIALLY_SUPPORTED** | Authority is distributed but explicit across the control plane, accepted product contracts, ADRs, migrations, services, and read-model code. No single generic authority-map artifact was found in the sampled paths. A future map should index these existing sources, not copy their contents. |
| Task lifecycle | **SUPPORTED** | InvestDesk has a single active `CURRENT_TASK.md` with objective, frozen semantics, allowed/forbidden scope, planning gates, and a stop state. `CURRENT_STATUS.md` is a verified snapshot. The candidate should map these existing authorities, not introduce competing task status. |
| PR / worktree lifecycle | **SUPPORTED** | `AGENTS.md` requires one authoritative worktree, baseline verification, and post-merge lifecycle cleanup under stated conditions. The current snapshot had one canonical worktree and the read-only open-PR query returned none. These are workflow controls, not project business facts. |
| Evidence | **PARTIALLY_SUPPORTED** | ADR/MVP acceptance criteria, Git revisions, CI/build/runtime distinctions, diagnostic runbook, and future trace identifiers provide useful evidence references. The observability document explicitly says its traceability expectations are not yet a schema. There is no general versioned evidence envelope across those records. |
| Exceptions | **MISSING** | The sampled active task and controls do not define a general expiring exception/waiver record with grantor, scope, reason, evidence, review date, and revocation. Task-level scope changes require updating task controls; do not retrofit the candidate waiver model into InvestDesk without its owner's decision. |
| Freshness | **PARTIALLY_SUPPORTED** | Baseline procedures pin branch/HEAD and re-fetch remote state; runtime diagnosis requires identity and current health. The sampled project controls do not define a generic dependency-triggered invalidation contract for authority, semantic, configuration, and evidence drift. |

No area was classified **OVERMODELED** from this bounded sample. This means
only that the inspected evidence did not support that label; it is not a
claim that every InvestDesk process or document is minimal.

## Authority map as observed (not a replacement)

| Fact class | Canonical owner in sampled sources | Projection / consumer |
|---|---|---|
| Active task, scope, stop conditions | `CURRENT_TASK.md`, under `AGENTS.md` workflow | Executor reports and task-linked PR |
| Current project snapshot | `CURRENT_STATUS.md` plus verified Git/GitHub state | Planning and cross-machine handoff |
| Product/domain semantics | `docs/product/*`, accepted ADRs and MVP contract | API validation, UI behavior, acceptance |
| Decision facts | Immutable Decision persistence/service and accepted ADR-029 contract | Decision API, Workspace Decision section, Timeline entry |
| Transaction facts | Immutable Transaction ledger/service and accepted Transaction ADRs | Transaction API/UI and Position reconstruction |
| Position quantity | ADR-021 reconstruction from selected baseline and canonical facts | Workspace/read response; not a separately persisted Position authority |
| Workspace / Timeline shape | ADR-027/ADR-029 and implementation composition | `GET /asset-workspaces/{asset_id}` and UI chronology |
| Runtime and operational readiness | Deployment/runtime authority and current host evidence | Health/readiness consumers and runbook |

This is a compact index of observed ownership. It does not move authority from
these sources into this Engineering-Governance repository.

## Specific findings for candidate fit

1. The candidate's authority map and derived-projection rules explain the
   existing Asset Workspace/Timeline without asking InvestDesk to create a
   duplicate business ledger.
2. The candidate must treat the missing Decision↔Transaction relation as
   `MISSING` in the current snapshot, while preserving the accepted rule that
   neither ticker/time/side nor Position movement proves causality.
3. The current MVP-D task, not this candidate, owns decisions about reverse
   cardinality, relation timing, immutability/correction, validation,
   idempotency, concurrency, and UI minimum.
4. A later implementation would need the project's own independent contract
   acceptance and validation. This reality check supplies no MVP-D design
   answer and does not satisfy that task's review gate.

## Source index

- Controls: `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.
- Product: `docs/product/CORE_BUSINESS_OBJECTS.md`,
  `docs/product/INTERACTION_MODEL.md`, `docs/product/USER_JOURNEYS.md`.
- Accepted architecture/domain: ADR-010, ADR-013, ADR-021, ADR-027, ADR-028,
  ADR-029 under `docs/decisions/` and
  `docs/mvp/MVP-C_HUMAN_DECISION_FOUNDATION.md`.
- Operations/evidence: `docs/deployment/DEPLOYMENT_PRINCIPLES.md`,
  `docs/observability/OBSERVABILITY_PRINCIPLES.md`,
  `docs/observability/DIAGNOSTIC_RUNBOOK.md`.
- Selected implementation evidence: `apps/api/src/investdesk_api/decisions.py`,
  `application/decision.py`, `transactions.py`,
  `application/trade_transaction.py`, `application/asset_workspace.py`,
  `apps/api/migrations/versions/0009_mvp_c_human_decision.py`, and UI
  `DecisionSection.tsx`, `TimelineSection.tsx`,
  `TimelineDetailPanel.tsx`.

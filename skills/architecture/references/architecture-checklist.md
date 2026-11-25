# Architecture decision & contract checklist

Load when resolving cross-service contracts, concurrency/idempotency, schema evolution, or stateful migrations (`CONTRACT_OR_MIGRATION` mode).

## 1. Single Source of Truth (SSOT) & derived state

- Name the **one canonical owner** for every persisted entity, authorization fact, or state transition (`BUSINESS_STATE_WORKFLOW`).
- Treat search indexes, UI caches, `PROJECT_PROFILE.md`, and `DOMAIN_MAP.md` strictly as derived projections: define explicit invalidation/reconciliation triggers and never allow a projection to mutate canonical truth independently.
- Keep cross-module dependencies acyclic (domain logic depends on stable interfaces, not downstream adapters).

## 2. Backward-compatible schema & API evolution

- Prefer **Expand -> Backfill -> Switch Readers -> Contract** for persisted schema or wire-protocol changes so rolling deploys, rollbacks, and mixed-version clients do not corrupt data.
- State exact compatibility guarantees before editing: additive optional fields, strict vs tolerant parsing, idempotent backfill behavior, API versioning, and deprecation cleanup criteria.
- Flag destructive drops, non-reversible data transforms, or security-boundary changes as `G3` for explicit owner approval before implementation.

## 3. Concurrency, idempotency & partial failure

- Identify all concurrent writers (workers, webhooks, retries, UI double-submits) and choose the minimal enforcement mechanism (atomic DB constraints, optimistic version checks, idempotency keys, or single-writer queues).
- Trace partial failure across network/storage boundaries: define whether each step is atomic, compensatable, or idempotent-retryable, and specify the exact surfaced error/retry state rather than silent fallback corruption.
- Define explicit timeout, retry budget, and backpressure/circuit-breaker limits when crossing external RPC or queue boundaries.

## 4. Boundaries, reversibility & falsifiable tests

- Compare 2–3 credible options with explicit failure modes, operational overhead, and rollback cost (avoid option theatre).
- Define concrete verification checks (`V2`/`V3`) that distinguish the chosen boundary from regressions: contract/wire compatibility tests, concurrency race tests, idempotency replay tests, and migration round-trip checks.
- Record durable cross-task decisions in the project's accepted architecture docs or an optional linked Issue only when future tasks genuinely depend on them.
- Return selected architecture, affected owners/files, and open user-only product or `G3` risk decisions to `engineering-workflow`.

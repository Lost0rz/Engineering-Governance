---
name: architecture
description: >-
  Resolve materially ambiguous engineering architecture, API contracts, data
  flows, state ownership (SSOT), concurrency, or schema migration boundaries
  before coding. Do not use for clear bug fixes, obvious edits
  (engineering-workflow), or visual UI styling (ui-design).
---

# Architecture

Use only when choosing structure, state ownership, or interfaces requires non-trivial tradeoffs before coding.

## Fast route

| Decision need | Mode | Next reading |
| --- | --- | --- |
| Single-service state owner, module boundary, or local API choice | `BOUNDARY_DECISION` | **NONE (this file)** |
| Cross-service contracts, concurrency/idempotency, or migrations | `CONTRACT_OR_MIGRATION` | [architecture-checklist.md](references/architecture-checklist.md) |

## Inline boundary method

1. **Question & constraints:** name the unresolved structural question, verified invariants, and user vs agent choices.
2. **Canonical owner (SSOT):** extend the existing source/data/API owner before creating parallel state or derived caches.
3. **Small credible option set:** compare 2–3 real options on coupling, failure modes, reversibility, and migration cost.
4. **Handoff to execution:** record affected files/interfaces, concrete verification checks, and resume `engineering-workflow` (or record durable cross-task decisions in project docs/Issues when justified).

## Boundaries

- `BUSINESS_STATE_WORKFLOW` belongs here; `INTERACTION_WORKFLOW` belongs to `ui-design`.
- Escalate to the user only for unresolved product semantics, scope expansion, or `G3` security/irreversible risk.

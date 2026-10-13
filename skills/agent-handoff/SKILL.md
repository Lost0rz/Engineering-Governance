---
name: agent-handoff
description: Use when engineering responsibility is transferred between agents, sessions, machines, or execution contexts and the receiver needs a bounded brief or the sender needs a structured evidence receipt back.
---

# Agent Handoff

Use this Skill to transfer responsibility without creating a second task/control system.

**Core rule:**

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff is an instruction/evidence envelope, not execution authority. `CURRENT_TASK.md` remains active authorization; `CURRENT_STATUS.md` remains current-state authority; durable rules remain in `AGENTS.md`/Skills.

Read [Handoff contract](references/handoff-contract.md). Templates are under `assets/templates/`.

## Modes

- `EXECUTE` — authorized mutation in another context.
- `AUDIT` — strict read-only independent evidence verdict.
- `DIAGNOSE` — bounded evidence question/hypothesis/probe transfer.
- `REVIEW` — read-only evaluation of specified work product.
- `VERIFY` — confirm a named claim/identity/check.

## Request construction

Use semantic fields `HANDOFF_ID`, `MODE`, `TARGET`, `AUTHORITY`, `DELTA`, `BOUNDARY`, `RETURN_CONTRACT`.

The receiver rereads named authorities it can access. A handoff never silently overrides the source that owns a conflicting semantic class; reconcile through Project Governance when needed.

Do not copy complete controls, planning documents, Domain maps or generic Engineering Governance procedure by default. A bounded exact excerpt is allowed only when direct access is unavailable or exact wording is required; label it as a snapshot/quote.

## Receipt construction

Return decision-useful evidence, not chronological execution narration. State explicit no-change/no-output success when that is the result.

A state-changing receipt includes actual Skills used, execution identity, changed paths, verification/lifecycle effects, unresolved evidence and control alignment. Read-only modes return target/range/identity, evidence/findings/unknowns/verdict and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.

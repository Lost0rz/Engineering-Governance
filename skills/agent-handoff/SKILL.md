---
name: agent-handoff
description: Use when engineering responsibility is transferred between agents, sessions, machines, or execution contexts and the receiver needs a bounded brief or the sender needs a structured evidence receipt back.
---

# Agent Handoff

Use this Skill to transfer responsibility across execution contexts without creating a second task/control system.

**Core rule:**

`HANDOFF = task/authority references + fresh delta + action boundary + return contract`

A handoff is an instruction/evidence envelope, not execution authority. `CURRENT_TASK.md` remains active authorization; `CURRENT_STATUS.md` remains current-state authority; durable rules remain in `AGENTS.md`/Skills.

Web, local Codex, cloud agents, Sub Agents, reviewers, machines, and sessions are execution contexts. They do not define engineering task purpose.

Read [Handoff contract](references/handoff-contract.md). Templates are under `assets/templates/`.

## Same-task continuation

When the engineering purpose/authorization is unchanged, preserve the same `TASK_ID` across contexts. Reference the accepted design/plan/task authority rather than asking each receiver to reconstruct or reinterpret the solution from chat history.

If the requested work is actually a distinct engineering purpose (for example a separately commissioned independent audit or corrective objective), Project Governance must authorize/reconcile that task boundary before mutation.

## Modes

- `EXECUTE` — authorized mutation in another context.
- `AUDIT` — strict read-only independent evidence verdict under an authorized audit purpose.
- `DIAGNOSE` — bounded diagnostic evidence/question transfer under the active authorization.
- `REVIEW` — read-only evaluation of specified work product.
- `VERIFY` — confirm a named claim/identity/check.

## Request construction

Use semantic fields:

- `HANDOFF_ID`
- `TASK_ID`
- `MODE`
- `TARGET`
- `AUTHORITY`
- `AUTHORITY_OBSERVED_BASIS` when freshness/drift matters
- `SOURCE_CONTEXT` / `TARGET_CONTEXT` when useful
- `DELTA`
- `BOUNDARY`
- `RETURN_CONTRACT`

The receiver rereads named authorities it can access. A handoff never silently overrides the source that owns a conflicting semantic class; incompatible drift returns to Project Governance reconciliation.

Do not copy complete controls, planning documents, Domain maps or generic Engineering Governance procedure by default. A bounded exact excerpt is allowed only when direct access is unavailable or exact wording is required; label it as a snapshot/quote.

## Receipt construction

Return decision-useful evidence, not chronological execution narration. State explicit no-change/no-output success when that is the result.

A same-task state-changing receipt preserves the same `TASK_ID` and reports actual Skills used, execution identity, changed paths, verification/lifecycle effects, unresolved evidence and control alignment. Read-only modes return target/range/identity, evidence/findings/unknowns/verdict and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.

If current authority differs materially from the sender's observed basis, report the compatibility/conflict instead of silently executing stale intent.

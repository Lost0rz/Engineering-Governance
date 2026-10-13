---
name: agent-handoff
description: Use when engineering responsibility is transferred between agents, sessions, machines, or execution contexts and the receiver needs a bounded brief or the sender needs a structured evidence receipt back.
---

# Agent Handoff

Use this Skill to package a cross-context transfer without creating a second task/control system.

**Core rule:**

`HANDOFF = authority references + fresh delta + action boundary + return contract`

A handoff is an instruction envelope, not execution authority. `CURRENT_TASK.md` remains the active authorization; `CURRENT_STATUS.md` remains current-state authority; durable rules remain in `AGENTS.md`/Skills.

Read [Handoff contract](references/handoff-contract.md). Templates are available under `assets/templates/`.

## Request construction

Use these semantic fields:

- `HANDOFF_ID`
- `MODE` — e.g. `EXECUTE`, `AUDIT`, `DIAGNOSE`, `REVIEW`, `VERIFY`
- `TARGET` — the immediate outcome requested from the receiver
- `AUTHORITY` — files/refs/controls the receiver must read and obey
- `DELTA` — fresh facts/decisions/focus not already safely represented in those authorities
- `BOUNDARY` — write/read-only scope, STOP conditions, destructive/external side-effect limits unique to this transfer
- `RETURN_CONTRACT` — evidence the sender needs back to make the next decision

## Anti-duplication rule

Do **not** copy complete `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, planning documents, Domain maps, or generic Engineering Governance procedures into a handoff by default. Reference them.

Copy a bounded excerpt only when the receiver cannot access the authority directly or exact text is required for correctness. Label it as a snapshot/quote, not a new authority.

## Receipt construction

Return decision-useful evidence, not a chronological execution diary.

For state-changing work include: handoff/task identity, Skills actually used, start/final execution identity, outcome, changed paths, verification, material branch/PR/worktree lifecycle, unresolved evidence, control/document alignment result, and next safe action.

For strict read-only audit/review include: target/range/identity, evidence inspected, findings by severity, unknown/unverified items, verdict, and `CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY`.

If nothing changed, say so explicitly. Absence is not evidence of `UNCHANGED`.

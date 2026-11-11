---
name: agent-handoff
description: Transfer a real engineering task or observed result across execution contexts using compact authority references and the current delta.
---

# Agent Handoff

Use for an **actual** cross-context construction, audit, diagnosis or verification request. The same task continuing in one context uses its existing information without a new Card.

## Minimal Card

State `TASK_ID`, `MODE`, `TARGET`, `AUTHORITY`, `BOUNDARY`, `DELTA` and `RETURN_CONTRACT`. A `CAPABILITY` or `CARD_ID` is optional when it genuinely helps routing or traceability.

- `MODE`: `EXECUTE` for authorized mutations; `AUDIT`, `REVIEW`, `VERIFY` or `DIAGNOSE` for read-only outcomes.
- `AUTHORITY` points to the selected task and user/host decision, not a copied 19-field Issue or a new permission.
- `DELTA` contains only what changed or needs doing now; link existing design, source and evidence.
- The receiver verifies its own current host/repository write access before any action. Permissions do not transfer in a Card.

## Receipt

Return observed outcome, decisive source/test/CI evidence, and remaining real decisions. Distinguish automation evidence from human UI acceptance when relevant. Use [handoff-contract.md](references/handoff-contract.md) only for a genuine complex transfer; the compact [request](assets/templates/HANDOFF_REQUEST.md) and [receipt](assets/templates/HANDOFF_RECEIPT.md) are optional drafting aids.

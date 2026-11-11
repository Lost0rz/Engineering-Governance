---
name: agent-handoff
description: Move a real task or review result between agents/contexts when an existing Issue or PR link and brief delta is insufficient.
---

# Agent Handoff

A link to an existing Issue, PR or shared plan **plus the current instruction** is usually enough. Use a structured Card only when the recipient otherwise lacks the necessary scope, evidence or return expectation.

A useful Card states the target, objective, affected boundary, relevant links and expected return evidence. The [optional template](assets/templates/HANDOFF_REQUEST.md) is a drafting aid, not an obligatory protocol.

The receiver uses the relevant specialist Skill and checks its own host/tool permissions for any write. A Card, Issue, PR or model-generated statement does not transfer credentials or grant authority.

Return changed source/commit, checks performed, evidence/blockers and actual PR/CI status. Do not copy the complete Issue text or demand progress comments. Human UI acceptance remains a human result, distinct from automated inspection.

Detailed [handoff guidance](references/handoff-contract.md) applies when task context is genuinely ambiguous.

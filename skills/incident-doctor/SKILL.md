---
name: incident-doctor
description: Use when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and current evidence is insufficient for the next safe decision; do not use for ordinary bugs whose evidence already supports safe action.
---

# Incident Doctor

Use this Skill only when all three conditions hold: a real failure/unexplained unsafe ambiguity exists; it blocks safe progress; and current evidence is insufficient for the next safe decision. A known defect with sufficient evidence remains normal authorized Project Governance work.

## Read only the needed contract

Start with [Evidence gate](references/evidence-gate.md) for a genuine blocked decision; inspect existing evidence before adding probes. Other references are conditional, **not** a required reading sequence:

- [Probe design](references/probe-design.md) — when a new probe could change the decision.
- [Fresh incident capture](references/fresh-incident.md) — when observation identity/freshness is uncertain.
- [Probe lifecycle](references/probe-lifecycle.md) — when diagnostic probes need retention or retirement.
- [Systematic techniques](references/systematic-techniques.md) — when a bounded first pass is insufficient.
- [Incident template](assets/templates/INCIDENT.md) — only when a durable incident record is required.

## Workflow

1. Apply the hard evidence gate and review existing evidence first.
2. Name the one missing fact and blocked decision. If current evidence is already sufficient, leave Doctor and return to the authorized flow.
3. Use systematic techniques only as needed: recent-change comparison, working-vs-broken comparison, backward data-flow tracing, single-hypothesis minimum tests, and condition-based waiting.
4. Add only the minimum probe whose possible results can change the blocked decision. Keep reports, observations, interpretations, hypotheses, findings, and root-cause claims distinct.
5. If source/authority/test location is unclear, use Domain Navigation only for that bounded discovery and then return here.
6. Define a minimum evidence-supported fault/fix boundary. Diagnosis is evidence, not execution authorization.
7. If the active task does not authorize the behavior change/side effects, return to Project Governance for reconciliation before mutation.
8. After an authorized fix, use risk-proportional regression verification and retire/promote diagnostic probes explicitly.

Use Project Governance's G0–G3 scale for authority risk and its V0–V3 scale for verification evidence; do not infer one from the other. A probe or local grant snapshot cannot activate risk-scoped autonomy without accepted policy opt-in and independent host/credential verification.

Incident Doctor does not create a diagnostic platform, permanent observability expansion, broad redesign authority, automatic remediation, or a universal rule that every bug must undergo root-cause ceremony.

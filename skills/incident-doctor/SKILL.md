---
name: incident-doctor
description: Use when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and current evidence is insufficient for the next safe decision; do not use for ordinary bugs whose evidence already supports safe action.
---

# Incident Doctor

Use this Skill only when all three conditions hold: a real failure/unexplained unsafe ambiguity exists; it blocks safe progress; and current evidence is insufficient for the next safe decision. A known defect with sufficient evidence remains normal authorized Project Governance work.

## Read the contracts

- [Evidence gate](references/evidence-gate.md)
- [Probe design](references/probe-design.md)
- [Fresh incident capture](references/fresh-incident.md)
- [Probe lifecycle](references/probe-lifecycle.md)
- [Systematic diagnosis techniques](references/systematic-techniques.md)
- [Incident record template](assets/templates/INCIDENT.md)

## Workflow

1. Apply the hard evidence gate and review existing evidence first.
2. Name the one missing fact and blocked decision. If current evidence is already sufficient, leave Doctor and return to the authorized flow.
3. Use systematic techniques only as needed: recent-change comparison, working-vs-broken comparison, backward data-flow tracing, single-hypothesis minimum tests, and condition-based waiting.
4. Add only the minimum probe whose possible results can change the blocked decision. Keep reports, observations, interpretations, hypotheses, findings, and root-cause claims distinct.
5. If source/authority/test location is unclear, use Domain Navigation only for that bounded discovery and then return here.
6. Define a minimum evidence-supported fault/fix boundary. Diagnosis is evidence, not execution authorization.
7. If the active task does not authorize the behavior change/side effects, return to Project Governance for reconciliation before mutation.
8. After an authorized fix, use risk-proportional regression verification and retire/promote diagnostic probes explicitly.

Incident Doctor does not create a diagnostic platform, permanent observability expansion, broad redesign authority, automatic remediation, or a universal rule that every bug must undergo root-cause ceremony.

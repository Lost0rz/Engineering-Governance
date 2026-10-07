---
name: incident-doctor
description: Reactive, evidence-gated investigation for a real failure, unexplained behavior, or unsafe ambiguity that blocks safe progress when existing evidence is insufficient. Use to close a specific decision-blocking evidence gap; do not use for routine feature development or speculative observability expansion.
---

# Incident Doctor

Use this Skill only when all three conditions hold: a real failure, unexplained behavior, or unsafe ambiguity exists; it blocks safe progress; and current evidence is insufficient to support the next safe decision. This is a reactive incident workflow, not a general diagnostics improvement program.

## Read the contracts

- [Evidence gate](references/evidence-gate.md)
- [Probe design](references/probe-design.md)
- [Fresh incident capture](references/fresh-incident.md)
- [Probe lifecycle](references/probe-lifecycle.md)
- [Incident record template](assets/templates/INCIDENT.md)

Start with the hard [evidence gate](references/evidence-gate.md). Review existing evidence before considering a probe. If it already supports the next safe decision, bypass new probe work. Otherwise name the one missing fact and blocked decision, then design only a minimum probe whose possible results can change that decision. Capture any new observation in a fresh, attributable incident and keep reports, observations, interpretations, hypotheses, findings, and root-cause claims distinct.

Incident Doctor does not handle routine feature development, normal repository navigation, task authorization, product/business planning, automatic remediation, permanent observability expansion, or a diagnostic platform/runtime. It does not authorize broad redesign. Define a minimum fix boundary only when evidence supports a fault boundary, causal edge, or sufficiently safe behavior boundary. The fix must be the smallest authorized behavior change, followed by risk-proportional regression verification under the project's normal `V1`/`V2`/`V3` policy; correlation alone does not establish a root-cause repair.

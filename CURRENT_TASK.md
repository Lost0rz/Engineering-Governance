# CURRENT TASK — Phase D Incident Doctor Enrichment Design

Task ID: `EG-INCIDENT-DOCTOR-ENRICH-DESIGN-015`

State: `WAITING_FOR_USER_DESIGN_REVIEW`

Mode: `BOUNDED_DESIGN_REVIEW`

## Objective

Define the bounded enrichment of the existing `skills/incident-doctor/` module so an AI can investigate a real evidence-insufficient failure with disciplined evidence gates, minimum probes, fresh-incident capture, falsifiable hypotheses, minimum-fix boundaries, regression verification, and explicit probe retirement/promotion — without turning diagnosis into routine development or a permanent observability platform.

This task is design-only. No local implementation is authorized until the user explicitly approves the short bounded design presented in chat.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase B accepted merge head: `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Phase C accepted merge head: `1d28250717e4e72754655ccc3c69bc3664a70eae`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- Exact Phase D implementation baseline will be captured only after user design approval.

## Candidate file scope

Only the existing Incident Doctor module:

- `skills/incident-doctor/SKILL.md`
- `skills/incident-doctor/references/evidence-gate.md`
- `skills/incident-doctor/references/probe-design.md`
- `skills/incident-doctor/references/fresh-incident.md`
- `skills/incident-doctor/references/probe-lifecycle.md`
- `skills/incident-doctor/assets/templates/INCIDENT.md`

Root controls may change later only for authorization/handoff. No sibling reusable Skill is part of Phase D.

## Fixed boundaries for review

- Doctor triggers only for a real failure, unexplained behavior, or unsafe ambiguity that blocks safe progress and cannot be answered from current evidence.
- Existing evidence is evaluated before new instrumentation.
- Probe work is skipped when existing evidence is sufficient.
- Any new probe must close one named evidence gap or distinguish current plausible explanations.
- Fresh capture must preserve runtime/build/configuration/revision identity and the smallest relevant observation window.
- Root cause remains unknown until evidence supports the claim; symptom, direct observation, interpretation, hypothesis, and conclusion must not be collapsed into one statement.
- A fix is bounded to the smallest authorized behavior change supported by the evidence and must be followed by risk-proportional regression verification.
- Temporary probes are removed by default; durable diagnostics require repeated justification plus explicit owner/scope/authorization.
- No automatic remediation, speculative observability expansion, background monitoring platform, daemon, database, or required diagnostic runtime is authorized.

## Current stop point

`WAITING_FOR_USER_DESIGN_REVIEW`

After explicit approval of the bounded design, Web will create the implementation authorization from the then-current exact `main` HEAD and issue a local execution card.

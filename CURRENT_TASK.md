# CURRENT TASK — Incident Doctor Audit Corrective

Task ID: `EG-INCIDENT-DOCTOR-AUDIT-CORRECTIVE-025`

State: `AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

Mode: `BOUNDED_DOCUMENTATION_CORRECTIVE`

## Objective

Correct only the Incident Doctor interaction/terminology issues established by `EG-FULL-SKILL-AUDIT-022`, preserving the accepted evidence-gated reactive model.

## Authority and baseline

- Accepted Domain Navigation corrective/main head: `123f8382a1c61b84f0af63fe25c3a035a4f1cada`.
- Frozen reusable comparison baseline: `4bc63eadbf1e1166ef8d9106c7f387a8ebb42c18`.
- Planned branch: `codex/incident-doctor-audit-corrective`.

## Authorized reusable files

- `skills/incident-doctor/SKILL.md`
- `skills/incident-doctor/references/evidence-gate.md`
- `skills/incident-doctor/references/fresh-incident.md`
- `skills/incident-doctor/references/probe-lifecycle.md`
- `skills/incident-doctor/assets/templates/INCIDENT.md`

Root `CURRENT_STATUS.md` and `CURRENT_TASK.md` may change only for handoff/closeout.

## Required corrective

1. Replace stale `Domain Map`-as-authority wording with generic semantic-authority/navigation evidence terminology.
2. Make the cross-Skill exit explicit: Incident Doctor may establish evidence, falsify hypotheses, and define a minimum fix boundary, but it never grants authorization for a behavior change. If the current task does not authorize the fix or required side effects, return to Project Governance for reconciliation/re-authorization before changing behavior.
3. Make the navigation helper boundary explicit: when source/authority/code/test location is unclear during an incident, Domain Navigation may be used only to locate and verify evidence; it does not diagnose the incident or decide root cause.
4. Remove duplicate headings in touched reusable references.
5. Keep the incident record concise; non-applicable fields may be marked/omitted according to the template rather than expanded into a diary.

## Out of scope

- changes to `project-governance` or `domain-navigation`;
- changing the evidence sufficiency model, root-cause status model, or one-active-gap-per-probe design;
- new probes, runtime diagnostics, telemetry, scripts, dependencies, services, or automatic remediation;
- target-project adoption.

## Verification

`V0` only:

- changed reusable paths exactly the five authorized files;
- frontmatter and relative cross-Skill links resolve;
- Doctor does not authorize task scope or behavior change;
- Project Governance is the route for missing authorization;
- Domain Navigation is only a source/authority-location aid inside incident work;
- evidence taxonomy/root-cause/probe lifecycle semantics remain intact;
- sibling Skills unchanged;
- no executable/runtime/dependency addition;
- final branch independently re-audited before merge.

## Current stop point

`AUTHORIZED_FOR_BOUNDED_CORRECTIVE`

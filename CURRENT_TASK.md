# CURRENT TASK — Design Anthropic Closed-Loop + Receipt Enforcement

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081`

Task class: `CAPABILITY_CORRECTIVE`

State: `ACTIVE`

## Objective

Strengthen the existing routed `design` capability so Anthropic `frontend-design` is not merely read as reference material but is executed as a bounded design workflow before implementation, with an explicit visual critique/corrective loop when the environment supports rendered-page evidence.

At the same time, strengthen the governed user-facing receipt so routed/used Skills are always explicitly reported and auditable as the capability graph grows.

## Required outcomes

1. `design` remains the single stable external design route; Anthropic remains the only active source module for this task.
2. A qualifying redesign task must complete a bounded Design pass before implementation: understand/diagnose → design plan → brief/genericity review → implementation handoff → rendered visual critique/corrective pass when supported.
3. Do not route every UI task through every Skill. Once Design owns the bounded design problem, unrelated Skills are not invoked unless a materially separate capability boundary is actually present.
4. Preserve project/business/data authority. Design decisions must not silently redefine canonical state, API/schema, persistence ownership, or lifecycle semantics.
5. Project Governance remains task/lifecycle authority.
6. Compact Engineering Status Receipt must expose both `Governance route` and `Skills used`; omission or inferred/non-used Skill names must fail the pre-return compliance check.
7. Existing Project Profile, Agent Handoff, routing, release/package, provenance and nine-Skill regressions must remain preserved.

## Scope

Expected source areas include:

- `skills/design/**`;
- `skills/project-governance/**` routing/receipt contracts where needed;
- release/acceptance evidence for the follow-on Plugin version;
- Plugin manifests/versioning and distribution after source acceptance.

Microsoft review/adaptation and the planned UX-audit module remain out of scope and inactive.

## Verification

Acceptance must demonstrate at minimum:

- a Merloom-like admin authoring redesign routes to `design` and produces an explicit bounded design deliverable before implementation;
- a simple understood frontend bug is not inflated into a design workflow;
- Design does not shotgun-route to unrelated Skills;
- rendered/screenshot critique is required when the execution environment actually supports it, otherwise the limitation is stated without fabricating evidence;
- final governed receipt explicitly reports the actual route and actual Skills used;
- previous release gates remain green.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ANTHROPIC-BASELINE-080` (`COMPLETE`)
- `START_MAIN`: `e0ddabbf265225b42365234880a8b650efb16632`
- `BRANCH`: `codex/design-anthropic-loop-receipt-enforcement`
- `MICROSOFT_MODULE`: `OUT_OF_SCOPE / INACTIVE`
- `UX_AUDIT_MODULE`: `OUT_OF_SCOPE / INACTIVE`
- `CONTROL_ALIGNMENT`: `PASS`

# Lifecycle Layers and Cross-Cutting Axes

The candidate uses seven lifecycle layers because each has a distinct primary
decision/evidence boundary. They are a navigational model, not a waterfall and
not a requirement to create seven documents. Feedback can re-enter earlier
layers.

## Seven layers

| Layer | Purpose | Inputs and authority | Typical artifacts | Gate and evidence | Exit condition |
|---|---|---|---|---|---|
| 1. Intent and outcomes | State user/business outcomes, constraints, and acceptance owner. | User-owned intent and approved product brief. | Outcome statement, quality scenarios, acceptance criteria. | Human confirmation that outcome and scope are understood; cite owner and revision. | Outcome, scope, and decision owner are explicit. |
| 2. Domain and authority | Identify fact classes, domain boundaries, owners, consumers, and contracts. | Canonical domain/product sources and accepted decisions. | Authority map, context relationships, domain contracts. | Resolve conflicting authorities or label them unknown; cite source revision. | Every material fact class has an owner or an explicit unknown/blocker. |
| 3. Architecture and quality | Choose structure and record material tradeoffs, risks, and quality needs. | Accepted domain contracts, system constraints, architecture sources. | Architecture view, ADRs, quality scenarios, prioritized risk/debt. | Review high-impact decisions and evidence the quality criteria. | Major choices and risks have rationale and owners. |
| 4. Implementation and integration | Change code/config and connect systems within declared contracts. | Approved design/task scope and canonical code/config repositories. | Commits, schemas, API contracts, integration changes. | Review actual diff and compatibility/security boundaries; exact base/final revisions. | Authorized change is integrated or explicitly stopped. |
| 5. Verification and release | Establish that the change meets declared conditions and is eligible for release. | Exact change revision, tests/build/CI and release criteria. | Test/build results, release notes, PR review evidence. | Required checks at declared validation level; queued work remains pending. | Evidence supports release decision or records a gap. |
| 6. Runtime and operability | Observe deployed/runtime identity, health, ownership, and operational readiness. | Deployment manifest, runtime authority, environment and telemetry. | Runtime identity/health evidence, runbook, operational acceptance. | Verify expected build, process/service ownership, health and environment. | Runtime state is identified as healthy/unhealthy/unknown with evidence. |
| 7. Incident and feedback | Triage unexpected outcomes, preserve evidence, learn, and feed changes back. | Incident observation, runtime/evidence sources, user impact authority. | Incident record, hypothesis/evidence, corrective decisions, follow-up task. | Separate observation from cause; collect differentiating evidence and review. | Cause confidence, action owner, or unresolved blocker is recorded. |

## Six cross-cutting axes

These axes describe questions to ask across layers. They are not additional
phases because each must be considered at multiple lifecycle points.

| Axis | Applies across | Check focus | Why it is an axis | Evidence expected |
|---|---|---|---|---|
| Authority and ownership | All seven layers | Is the source/decision owner explicit and respected? | Ownership crosses every artifact and runtime boundary. | Canonical URI/path, owner, revision, declared scope. |
| Evidence and provenance | All seven | Can the claim be reproduced and tied to inputs? | Evidence accompanies each decision, not one stage. | Input/source revision, evaluator/reviewer, time, result. |
| Risk and impact | Intent, architecture, implementation, verification, runtime, incident | Is impact/severity proportionate to failure modes? | Risks cut across design and operation. | Scenario, severity/rationale, affected scope, mitigation. |
| Applicability and exception | Domain, architecture, implementation, verification, runtime | Does this check apply; if not, who decided and why? | Applicability can change by scope/context, not chronology. | Scope, decision owner, rationale, review/expiry. |
| Version and compatibility | Domain, architecture, implementation, verification, runtime | Are contracts/tools compatible with pinned consumers? | Versioning affects all handoffs. | Standard/profile/schema/tool versions and migration. |
| Freshness and drift | Evidence-producing layers, runtime, incident | Did a dependency change invalidate the result? | Freshness is a property of evidence over time. | Dependency identity, change signal, required rechecks. |

Each check should identify which layer(s) and axis/axes it covers. The table
does not require a check in every cell; applicability is explicit, and the
profile selects only checks that have a meaningful authority and evidence
source.

## Feedback and stage gates

Layer exit means sufficient evidence for the next decision, not permanent
truth. A material authority, scope, contract, or runtime change can reopen a
layer and make dependent freshness assessments stale. It does not rewrite
historical evaluation results. The project gate owner decides whether a
finding blocks a transition; v0.1 does not do so automatically.

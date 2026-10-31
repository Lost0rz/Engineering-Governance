# Capability composition

The nine Skills cooperate without competing controllers.

`project-governance` owns task/control authority, lifecycle/reconciliation, workspace boundaries, verification choice and closeout. A narrower Skill owns only its bounded capability.

## Engineering framework boundary

The composition graph below is the reusable engineering workflow graph for governed work. External engineering frameworks, Skills, plugins, prompt packs, or repositories may provide reference material, patterns, or evidence, but they are not peer capabilities in this graph and do not become execution controllers because they are installed or discoverable.

If a useful external method is missing internally:

1. identify the existing Engineering Governance owner for the underlying need;
2. express the immediate requirement as behavior/acceptance rather than an external Skill invocation;
3. extend the owning Skill/internal module when the method is reusable and stable;
4. add a new top-level capability only when the capability-model rules actually require one.

Do not route out to an external framework as a convenience fallback.

## Composition is selective, not a pipeline

Do **not** walk the Skill catalog from top to bottom. Do **not** invoke a Skill merely because it is installed or adjacent to the problem.

Start with Project Governance for ordinary engineering work, then select the smallest materially necessary bounded Engineering Governance owner for the actual unresolved problem.

```text
request
  |
  v
project-governance
  |
  +--> design                 UI/UX/frontend interaction + visual design
  |
  +--> solution-design        material architecture/state/API/data-flow ambiguity
  |
  +--> domain-navigation      unclear authority/source/symbol/test/runtime route
  |
  +--> execution-orchestrator decomposition/delegation materially useful
  |
  +--> incident-doctor        blocking evidence gap
  |
  +--> evidence-audit         formal independent/read-only verdict
  |
  +--> agent-handoff          cross-context transfer
  |
  `--> project-profile        requested compact derived project context/index
```

These are bounded owners, not mandatory stages.

External frameworks do not appear as additional nodes around or inside this graph unless owning user/project authority explicitly changes the engineering framework boundary for that task.

## Evidence-triggered nested composition

A selected capability may call another Engineering Governance capability when a **specific unresolved dependency** crosses the second capability's real boundary and the answer materially affects the current decision.

Every nested call should make these explicit:

```text
UNRESOLVED_DEPENDENCY:
DECISION_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_OWNER_OR_STAGE:
```

The called capability returns a bounded answer. After that bounded result is sufficient, **resume at the declared stage** in the originating capability.

Do not call another Skill for:

- general enrichment;
- completeness;
- a generic second opinion;
- re-reading an authority/route already reliably known;
- the mere fact that a page/system spans multiple domains;
- the mere fact that the Skill is installed;
- importing a second engineering framework to supply planning, TDD, debugging, review, completion, Sub Agent, or model-routing control.

If the returned result materially changes task scope or authorization, return to Project Governance for reconciliation before mutation. Otherwise resume the originating capability directly.

## Design composition example

```text
project-governance
      |
      v
    design
      |
      |  backend authority/source route genuinely unclear
      +------> domain-navigation
      |             |
      |        verified route
      |             |
      <-------------+
      |
      |  route known, but state/API ownership materially ambiguous
      +------> solution-design
      |             |
      |        bounded decision
      |             |
      <-------------+
      |
      v
resume suspended Design stage
```

This is valid composition. It is different from shotgun routing because each detour answers one concrete dependency and returns.

## Design vs Solution Design

Use this discriminator for mixed frontend work:

```text
INTERACTION_WORKFLOW
How users see, understand, navigate, edit, act and receive feedback.
Owner: design

BUSINESS_STATE_WORKFLOW
Canonical state transitions, data/state ownership, API/data-flow responsibility,
persistence semantics and implementation boundaries.
Owner: solution-design when materially ambiguous
```

`solution-design` and `design` may both participate only when both material problems actually exist. A blocking business/state prerequisite should be resolved before the affected interface decision proceeds.

## Handoff dimensions

Handoff `CAPABILITY` and `MODE` are separate:

- `CAPABILITY` identifies the bounded Engineering Governance Skill/capability the receiver should use, or `NONE`;
- `MODE` identifies receiver action/side-effect class.

A mode name never replaces Skill routing or grants mutation authority. An external Skill/plugin/framework name is not a valid `CAPABILITY` value for a governed Engineering Governance Handoff Card.

External references may still appear as evidence/provenance in a handoff when genuinely relevant. That mention does not authorize the receiver to invoke or defer to the external framework.

## Artifact roles

- Normative/current/design/implementation authorities own project rules, current authorization/state, durable decisions, project-specific design facts, or implementation semantics for their class.
- Derived projections include Project Profile and Domain/navigation maps; authority wins when they are stale.
- Observed evidence/transport includes handoffs, briefs, ledgers, audits, CI/test/runtime/review observations; these cannot expand scope or replace authority.
- External framework documents and historical artifacts are reference/provenance unless owning authority explicitly promotes them; reference status alone never makes them workflow authority.

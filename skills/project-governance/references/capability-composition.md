# Capability composition

The nine Skills cooperate without competing controllers.

`project-governance` owns task/control authority, lifecycle/reconciliation, workspace boundaries, verification choice and closeout. A narrower Skill owns only its bounded capability.

## Composition is selective, not a pipeline

Do **not** walk the Skill catalog from top to bottom. Do **not** invoke a Skill merely because it is installed or adjacent to the problem.

Start with Project Governance for ordinary engineering work, then select the **smallest materially necessary set of bounded capabilities** for the actual unresolved problem. A single narrow Skill is often sufficient.

```text
request
  |
  v
project-governance
  |
  +--> design                when the bounded problem is UI/UX/frontend visual design
  |
  +--> solution-design       when material engineering architecture/state ownership is unresolved
  |
  +--> domain-navigation     when the relevant semantic/source/test/runtime route is genuinely unclear
  |
  +--> execution-orchestrator when decomposition/delegation itself is useful
  |
  +--> incident-doctor       when a blocking evidence gap prevents safe progress
  |
  +--> evidence-audit        when a formal independent/read-only verdict is the requested boundary
  |
  +--> agent-handoff         when responsibility/evidence must cross execution contexts
  |
  `--> project-profile       when the requested artifact is compact derived project context/index

bounded capability completes
  |
  v
project-governance alignment / closeout
```

Branches are gates, not stages. More branches are not better.

When `design` owns an already-understood interface problem, let Design perform its complete bounded design/implementation/visual-critique loop. Ordinary access to known project authorities does not additionally require Domain Navigation; Design's own visual critique does not additionally require Evidence Audit.

`solution-design` and `design` may both participate in one governed task only when there are **two distinct material problems**: unresolved engineering architecture/state ownership **and** bounded interface/frontend design. Project Governance remains the task/lifecycle owner.

## Handoff dimensions

Handoff `CAPABILITY` and `MODE` are separate:

- `CAPABILITY` identifies the bounded Skill/capability the receiver should use, or `NONE`;
- `MODE` identifies receiver action/side-effect class.

A mode name never replaces Skill routing or grants mutation authority.

## Artifact roles

- Normative/current/design/implementation authorities own project rules, current authorization/state, durable decisions, project-specific design facts, or implementation semantics for their class.
- Derived projections include Project Profile and Domain/navigation maps; authority wins when they are stale.
- Observed evidence/transport includes handoffs, briefs, ledgers, audits, CI/test/runtime/review observations; these cannot expand scope or replace authority.

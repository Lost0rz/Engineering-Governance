# Global Skill routing

This contract answers one question: **which Engineering Governance capability should handle the request now?** It selects capability; it does not duplicate Skill procedure or project facts.

## Routing surfaces

An environment may expose explicit Skill selection, Skill metadata/platform discovery, project guidance, authoritative global guidance, or platform/runtime routing. Do not require a Local-style global file where none exists.

## Routing rule

Ordinary software/project/repository engineering enters `project-governance` unless a higher-priority instruction or explicit bounded selection already determines the route.

| Requested outcome / condition | Route |
| --- | --- |
| establish/reconcile task authority, scope, lifecycle, verification, final alignment | `project-governance` |
| create/rebuild/shrink/audit compact project context/profile and authority pointers | `project-profile` |
| resolve material engineering intent/architecture/state ownership/API/data-flow/implementation-boundary ambiguity | `solution-design` |
| audit/create/redesign/review bounded UI/UX or frontend interaction/visual design | `design` |
| improve execution through decomposition/agents/parallelism/delegation/recovery | `execution-orchestrator` |
| transfer responsibility/evidence across agents/sessions/machines/contexts | `agent-handoff` |
| produce a formal read-only evidence/acceptance/readiness verdict | `evidence-audit` |
| establish unclear Domain/authority/source/symbol/runtime/dependency/test route | `domain-navigation` |
| investigate a blocking failure/unsafe ambiguity with an evidence gap | `incident-doctor` |

A keyword alone is not a route. Mentioning CI/PR/code does not imply Evidence Audit during corrective work; mentioning a bug does not imply Doctor when evidence supports safe action; mentioning “design” does not imply `design` when the issue is engineering architecture or state ownership.

### Frontend workflow discriminator

Use this distinction when a frontend task mixes “workflow” language:

```text
INTERACTION_WORKFLOW
How users see, understand, navigate, edit, act and receive feedback.
Owner: design

BUSINESS_STATE_WORKFLOW
Canonical state transitions, data/state ownership, API/data-flow responsibility,
persistence semantics and implementation boundaries.
Owner: solution-design when materially ambiguous
```

Both capabilities may participate when both material problems exist. Do not route ordinary page composition into Solution Design, and do not ask Design to invent unresolved backend/state semantics.

## Selective, evidence-triggered composition

Routing is **selective rather than cumulative**, but selected capabilities are not isolated silos.

Choose the smallest materially necessary capability set. Once a Skill owns the bounded problem, let it lead. It may call another Skill only when a concrete unresolved dependency crosses that Skill's real boundary and the answer can materially change the current decision.

Before such a call, identify:

```text
UNRESOLVED_DEPENDENCY:
DECISION_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_OWNER_OR_STAGE:
```

The called capability returns the bounded answer it owns; then resume the originating capability/stage. Do not restart the full routing tree merely because a bounded dependency was resolved.

Do not invoke Skills for general enrichment, completeness, a second opinion without an unresolved dependency, or merely because they are installed.

Example: an already-understood frontend redesign may route `project-governance → design`. If Design then cannot reliably identify the backend authority/source/state-owner route needed to understand one interaction, it may call `domain-navigation`, receive the verified route, and return to the suspended Design stage. If the route is known but state/API ownership itself is materially ambiguous, call `solution-design` for that bounded decision and then return to Design.

A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal acceptance/readiness verdict is requested.

## Project Profile context

If an accepted Project Profile, Project Instructions or equivalent compact project context is already available, `design` may consume it directly as **derived context and authority pointers**. Reading that existing context does not route through `project-profile`; route to `project-profile` only when the requested outcome is to create, rebuild, shrink or audit the Profile itself. Underlying project authorities still outrank the Profile.

## Cross-context transfer

A request such as “give me the card/instructions to send to local Codex/another agent/reviewer” is not merely ordinary prose generation: the requested artifact itself crosses an execution-context boundary, so route through `agent-handoff`. This does not create a new task; Project Governance remains task/lifecycle owner and the current `TASK_ID` is preserved unless the engineering purpose was separately reconciled.

Project Profile is not the normal development path. Read-only Profile drafting/audit may route directly to `project-profile`; repository/project-managed Profile mutation still requires compatible Project Governance task authorization.

## Composition

Project Governance remains task/lifecycle owner. Project Profile reads accepted authorities and returns derived context/index. Design owns bounded product-interface/frontend interaction and visual-design choices plus its internal mode/review loop. Solution Design remains engineering architecture/state-ownership authority. Other narrow Skills can provide bounded dependency results when their real trigger is met, then return to the originating capability. Do not create a Router Skill, peer-controller mesh, second task authority, or mandatory all-Skill pipeline.

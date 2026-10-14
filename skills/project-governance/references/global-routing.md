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
| resolve material intent/architecture/state-ownership ambiguity | `solution-design` |
| improve execution through decomposition/agents/parallelism/delegation/recovery | `execution-orchestrator` |
| transfer responsibility across agents/sessions/machines/contexts | `agent-handoff` |
| produce a formal read-only evidence/acceptance/readiness verdict | `evidence-audit` |
| establish unclear Domain/authority/source/symbol/runtime/dependency/test route | `domain-navigation` |
| investigate a blocking failure/unsafe ambiguity with an evidence gap | `incident-doctor` |

A keyword alone is not a route. Mentioning CI/PR/code does not imply Evidence Audit during corrective work; mentioning a bug does not imply Doctor when evidence supports safe action. A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal verdict boundary is requested.

Project Profile is not the normal development path. Read-only Profile drafting/audit may route directly to `project-profile`; repository/project-managed Profile mutation still requires compatible Project Governance task authorization.

## Composition

Project Governance remains task/lifecycle owner. Project Profile reads accepted authorities and returns derived context/index. Other narrow Skills return after their bounded capability finishes. Do not create a Router Skill, peer-controller mesh, or second task authority.

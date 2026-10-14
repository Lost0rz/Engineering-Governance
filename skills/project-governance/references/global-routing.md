# Global Skill routing

This contract answers one question: **which Engineering Governance capability should handle the request now?** It selects capability; it does not duplicate Skill procedure or project facts.

## Routing surfaces

An execution environment may expose one or more routing surfaces:

- explicit user/host Skill selection;
- Skill frontmatter/metadata discovery;
- project guidance such as repository `AGENTS.md`;
- authoritative global guidance when that environment supports it;
- platform/runtime routing behavior.

Do not require a Local-style global guidance file in environments that do not have one. A routing surface selects capability; it does not create project task authority.

## Routing rule

For software/project/repository engineering work, `project-governance` is the normal Engineering Governance entry unless a higher-priority instruction or explicit bounded Skill selection already determines the route. Narrow Skills are invoked only for the capability whose semantic trigger is met, then return to the governing caller.

| Requested outcome / condition | Route |
| --- | --- |
| establish/reconcile task authority, scope, workspace/writer lifecycle, verification level, final alignment | `project-governance` |
| resolve material intent/architecture/state-ownership ambiguity before implementation | `solution-design` |
| improve execution through decomposition, agents, parallelism, environment-aware delegation, recovery, or controlled integration | `execution-orchestrator` |
| transfer responsibility across agents/sessions/machines/contexts with a bounded request/receipt | `agent-handoff` |
| produce a read-only evidence/acceptance/readiness verdict separate from implementation | `evidence-audit` |
| establish an unclear Domain/authority/source/symbol/runtime/dependency/test route | `domain-navigation` |
| investigate a real blocking failure/unsafe ambiguity when existing evidence cannot support the next safe decision | `incident-doctor` |

A keyword alone is not a route. Mentioning CI/PR/code does not imply Evidence Audit when the requested outcome is implementation or corrective work. Mentioning a bug does not imply Incident Doctor when evidence already supports safe action.

## Composition

Project Governance remains the authority/lifecycle owner when several capabilities apply. Typical bounded compositions include:

- `project-governance -> solution-design -> project-governance`
- `project-governance -> execution-orchestrator -> project-governance`
- `execution-orchestrator -> agent-handoff -> delegated unit -> receipt -> execution-orchestrator`
- `project-governance -> evidence-audit -> project-governance`
- caller -> `domain-navigation` -> caller
- `incident-doctor -> domain-navigation -> incident-doctor` when diagnosis only needs bounded evidence location

Do not create a Router Skill, recursive peer mesh, or second task authority.

# Global Skill routing

This contract answers one question: **which Engineering Governance capability should handle the request now?** It selects capability; it does not duplicate Skill procedure or project facts.

## Natural-language entry and discovery boundary

Web/ChatGPT requests like "给我施工卡" (give me a construction card), "给我审计卡" (send an audit card), "交给本地 Codex", "write instructions for my local AI" and "return a task execution receipt" are **cross-context intent**, not free-form writing when a governed project is in context. Discover the installed Engineering Governance capability and enter `project-governance`; route an actual transfer artifact through `agent-handoff`. Project/organization instructions or explicit plugin selection may be authoritative entry surfaces, but a file **inside** the plugin cannot deterministically cause a platform to load that plugin. If discovery is unavailable, say so rather than claim Skill compliance.

Negative cases: "施工卡格式是什么" is explanation, not a Handoff. "审查 PR 当前状态" or "看看当前进度" normally requests a **lightweight G0 status lookup**, not an independent V3 audit; return current PR/check evidence without full Issue or source reconstruction unless required for the asked claim. "审计 PR 代码安全/合并准备" is a formal Evidence Audit. Mentioning another agent in historical text is not automatically a Handoff. Route by the requested decision, not keywords.

This contract governs behavior **after entry** and discoverability guidance, not a guaranteed external plugin auto-launch. Confirm real Web Skill invocation in a fresh session; a well-formed-looking Card alone is not evidence the Skill was loaded.

## Layer ownership

- **Entry:** the host discovers/loads the plugin; a Skill file cannot prove runtime installation.
- **Routing:** this file chooses the smallest capable owner; no execution procedure or permission is defined here.
- **Execution:** the selected Skill follows its own references and the target project's current authority. A handoff carries a locator and fresh delta, never a grant.


## Routing surfaces

An environment may expose explicit Skill selection, Skill metadata/platform discovery, project guidance, authoritative global guidance, or platform/runtime routing. Do not require a Local-style global file where none exists.

## Framework boundary

Engineering Governance owns its governed engineering route. External tools and methods may be referenced as evidence, not installed as a competing workflow authority. See `references/capability-composition.md` for ownership and delegation details.


## Routing rule

Ordinary software/project/repository engineering enters `project-governance` unless a higher-priority instruction or explicit bounded Engineering Governance selection already determines the route.

| Requested outcome / condition | Route |
| --- | --- |
| establish/reconcile task authority, scope, lifecycle, verification, final alignment | `project-governance` |
| create/revise a GitHub Issue execution-spec draft after explicit user direction | `project-governance` (Web Agent A authoring only under the accepted target `AGENTS.md` opt-in; not approval or execution) |
| create/rebuild/shrink/audit compact project context/profile and authority pointers | `project-profile` |
| resolve material engineering intent/architecture/state ownership/API/data-flow/implementation-boundary ambiguity | `solution-design` |
| audit/create/redesign/review bounded UI/UX or frontend interaction/visual design | `design` |
| improve execution through decomposition/agents/parallelism/delegation/recovery | `execution-orchestrator` |
| transfer responsibility/evidence across agents/sessions/machines/contexts | `agent-handoff` |
| produce a formal read-only evidence/acceptance/readiness verdict | `evidence-audit` |
| establish unclear Domain/authority/source/symbol/runtime/dependency/test route | `domain-navigation` |
| investigate a blocking failure/unsafe ambiguity with an evidence gap | `incident-doctor` |

A keyword alone is not a route. Mentioning CI/PR/code does not imply Evidence Audit during corrective work; mentioning a bug does not imply Doctor when evidence supports safe action; mentioning “design” does not imply `design` when the issue is engineering architecture or state ownership.

An external framework/Skill name appearing in a prompt, prior receipt, plan, historical document, installed catalog, or repository path is also **not** a route. Treat it as reference/provenance unless owning authority explicitly changes the engineering framework boundary.

### Frontend routing

Interaction, layout and visual behavior belong to `design`; material API, persistence and state-ownership ambiguity belongs to `solution-design`. Route to both only if both are actually needed.


## Selective composition

Route only for a concrete unresolved dependency. The owning Skill may obtain a bounded result from another Skill and resume; do not restart routing, require a fixed call checklist or invoke all Skills. `references/capability-composition.md` owns the detailed composition contract.

Advisory status may stay in Project Governance; a formal read-only verdict goes to Evidence Audit.


## Project Profile context

If an accepted Project Profile, Project Instructions or equivalent compact project context is already available, `design` may consume it directly as **derived context and authority pointers**. Reading that existing context does not route through `project-profile`; route to `project-profile` only when the requested outcome is to create, rebuild, shrink or audit the Profile itself. Underlying project authorities still outrank the Profile.

## Cross-context transfer

An actual card/receipt for another context routes to `agent-handoff`; its seven-field transport contract and mode-specific evidence belong there. Project Governance continues to own the task and authorization. A normal continuation creates neither a new task nor a mandatory Card.


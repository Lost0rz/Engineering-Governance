# Global Skill routing

This contract answers one question: **which Engineering Governance capability should handle the request now?** It selects capability; it does not duplicate Skill procedure or project facts.

## Natural-language entry and discovery boundary

Web/ChatGPT requests like "给我施工卡" (give me a construction card), "给我审计卡" (send an audit card), "交给本地 Codex", "write instructions for my local AI" and "return a task execution receipt" are **cross-context intent**, not free-form writing when a governed project is in context. Discover the installed Engineering Governance capability and enter `project-governance`; route an actual transfer artifact through `agent-handoff`. Project/organization instructions or explicit plugin selection may be authoritative entry surfaces, but a file **inside** the plugin cannot deterministically cause a platform to load that plugin. If discovery is unavailable, say so rather than claim Skill compliance.

Negative cases: "施工卡格式是什么" is ordinary explanation unless the user actually requests an engineering handoff; "审计当前 PR" normally means **perform** an evidence audit rather than generate a Card for another agent; "看看当前进度" is advisory read-only status; mentioning another agent in historical text is not necessarily a handoff. Distinguish the requested outcome instead of hard keyword routing.

This contract governs behavior **after entry** and discoverability guidance, not a guaranteed external plugin auto-launch. Confirm real Web Skill invocation in a fresh session; a well-formed-looking Card alone is not evidence the Skill was loaded.

## Three-layer composition

- **ENTRY**: select available installed Governance from user intent and supported platform/project guidance, otherwise report unavailable; do not treat manifest keywords as a security boundary.
- **ROUTING**: `project-governance` chooses FILE_CONTROL Task or ISSUE_CONTROL exact approved Issue, then only the bounded required `agent-handoff`, `evidence-audit`, `design`, etc. No nine-Skill startup loop or duplicate task authority.
- **EXECUTION**: receiving Codex Desktop/local agent reopens accepted `AGENTS.md`, selected Task or exact Issue/approval, fresh PR/worktree/host facts, relevant Domain and Work Package; apply L0/L1/L2/L3 and write same-Issue receipts. The Card is a locator + delta, not a permission token or an alternative execution spec. Missing material authority/Skill/host facts blocks affected writes.

## Routing surfaces

An environment may expose explicit Skill selection, Skill metadata/platform discovery, project guidance, authoritative global guidance, or platform/runtime routing. Do not require a Local-style global file where none exists.

## Engineering framework ownership

For governed software/project/repository engineering, Engineering Governance is the reusable engineering workflow/routing framework once the request enters `project-governance`.

External engineering frameworks, Skills, plugins, prompt packs, or repositories may be inspected as reference material/evidence, but discovery or installation does not make them part of the governed route. Do not hand execution control to them, require their Skill names in construction/handoff cards, or let them become delegation/model/reasoning/review-lifecycle authorities.

If an external method is useful, map it to the existing Engineering Governance owner and express the need as behavior/acceptance. Absorb durable reusable method into the owning Skill/internal module before treating it as governed workflow. Add a new top-level capability only under the repository capability-model rules.

Historical/reference filenames or directories may retain external framework names. Names/paths are evidence or provenance only unless an owning authority explicitly changes framework ownership.

## Routing rule

Ordinary software/project/repository engineering enters `project-governance` unless a higher-priority instruction or explicit bounded Engineering Governance selection already determines the route.

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

An external framework/Skill name appearing in a prompt, prior receipt, plan, historical document, installed catalog, or repository path is also **not** a route. Treat it as reference/provenance unless owning authority explicitly changes the engineering framework boundary.

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

Routing is **selective rather than cumulative**, but selected Engineering Governance capabilities are not isolated silos.

Choose the smallest materially necessary capability set. Once a Skill owns the bounded problem, let it lead. It may call another Engineering Governance Skill only when a concrete unresolved dependency crosses that Skill's real boundary and the answer can materially change the current decision.

Before such a call, identify:

```text
UNRESOLVED_DEPENDENCY:
DECISION_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_OWNER_OR_STAGE:
```

The called capability returns the bounded answer it owns; then resume the originating capability/stage. Do not restart the full routing tree merely because a bounded dependency was resolved.

Do not invoke Skills for general enrichment, completeness, a second opinion without an unresolved dependency, or merely because they are installed. Do not invoke external engineering frameworks as a fallback for a missing internal capability; return to the owning Engineering Governance capability and reconcile the gap.

Example: an already-understood frontend redesign may route `project-governance → design`. If Design then cannot reliably identify the backend authority/source/state-owner route needed to understand one interaction, it may call `domain-navigation`, receive the verified route, and return to the suspended Design stage. If the route is known but state/API ownership itself is materially ambiguous, call `solution-design` for that bounded decision and then return to Design.

A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal acceptance/readiness verdict is requested.

## Project Profile context

If an accepted Project Profile, Project Instructions or equivalent compact project context is already available, `design` may consume it directly as **derived context and authority pointers**. Reading that existing context does not route through `project-profile`; route to `project-profile` only when the requested outcome is to create, rebuild, shrink or audit the Profile itself. Underlying project authorities still outrank the Profile.

## Cross-context transfer

A request such as “give me the card/instructions to send to local Codex/another agent/reviewer” is not merely ordinary prose generation: the requested artifact itself crosses an execution-context boundary, so route through `agent-handoff`. This does not create a new task; Project Governance remains task/lifecycle owner and the current `TASK_ID` is preserved unless the engineering purpose was separately reconciled.

The Card's engineering capability request remains inside Engineering Governance (`CAPABILITY: <Engineering Governance Skill | NONE>`). External frameworks may be cited as reference/provenance in `AUTHORITY`, `DELTA`, or `OBSERVED_BASIS` when genuinely relevant, but must not become required execution Skills, peer routers, or runtime controllers.

Project Profile is not the normal development path. Read-only Profile drafting/audit may route directly to `project-profile`; repository/project-managed Profile mutation still requires compatible Project Governance task authorization.

## Composition

Project Governance remains task/lifecycle owner. Project Profile reads accepted authorities and returns derived context/index. Design owns bounded product-interface/frontend interaction and visual-design choices plus its internal mode/review loop. Solution Design remains engineering architecture/state-ownership authority. Other narrow Engineering Governance Skills can provide bounded dependency results when their real trigger is met, then return to the originating capability. Do not create a Router Skill, peer-controller mesh, second task authority, external-framework execution layer, or mandatory all-Skill pipeline.

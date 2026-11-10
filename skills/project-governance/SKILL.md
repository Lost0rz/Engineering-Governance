---
name: project-governance
description: Normal entry for governed software/repository tasks, including plain-language requests for construction or audit cards (给我施工卡/审计卡), approved GitHub Issue handoffs to Codex Desktop, task/control authorization, execution preflight, PR lifecycle, verification and receipts. Route actual cross-context cards through agent-handoff.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, repository delivery, and closeout. Keep clear work lightweight.
## Web entry and Desktop receiver entry (compact boundary)

A Web request to *send* a construction/execution/audit/verification card to another agent (including "给我施工卡", "给我审计卡", "交给本地 Codex") enters Project Governance for task selection and then **must** use `agent-handoff` for the Card. A user asking *how card formats work* is advisory: do not create an Issue or executable Card merely from the noun "卡". A user asking for a direct read-only audit may use `evidence-audit` without making a transfer Card. Full intent scenarios belong to `references/global-routing.md`, not duplicated here.

In `ISSUE_CONTROL`, an explicit current user request to create or revise an Issue execution-spec draft may use Web Agent A's narrow authoring path only when the target repository's accepted `AGENTS.md` on live `main` has exactly one operative top-level `ISSUE_WEB_SPEC_AUTHORING: ENABLED` declaration. Read the live target policy and current Issue/writer state first, use the official checker, and verify the Issue number/body/digest by host readback after writing. This can create or correct an unapproved draft; it never approves the spec or authorizes source, branch, worktree, PR, merge or release actions. Keep the authoring and approval flows separate as defined in `references/issue-control.md`.

For G0 read-only work, do not demand an Issue approval or an executable Card. For state-changing `ISSUE_CONTROL`, select **one** accepted authorization path: legacy/default exact-revision direct or expressly opted-in delegated approval; or a separately opted-in G1/G2 autonomous grant independently verified from the GitHub host. In legacy mode, an AI may post a clearly labeled delegated approval after the user's explicit decision **when** the target project opted in and the write surface supports Issue comments; the user need not open GitHub merely to paste that record. This is lower assurance than a protected human grant, so never mislabel it as direct GitHub approval. Inactive/unverified autonomy does not authorize any write. Do not invent additional approval requirements for a normal G0 inquiry or already authorized same-scope continuation. `agent-handoff` owns transport; `issue-control.md` and `issue-execution-contract.md` own exact approval provenance and scope.

In Codex Desktop/local execution, receiving a Card is **not authority**. At task entry: resolve the installed Engineering Governance capability actually available; read the target repository's accepted `AGENTS.md` to choose FILE_CONTROL vs ISSUE_CONTROL; for state-changing ISSUE_CONTROL work fetch the exact selected Issue and verify approved revision, canonical digest and authenticated GitHub actor via available `gh`/connector, plus explicit AGENTS opt-in and `DELEGATED_ACCOUNT_ATTESTED` assurance when using delegated approval; check relevant live Git/PR/writer evidence and necessary Domain/STOP/receipt contract before touching source. Follow the relevant Work Packages, not the pasted Card as a replacement spec. If critical Skill, GitHub or approval evidence is unavailable, STOP affected writes and report the missing dependency; do not silently switch to a generic framework or stale cached card. Do not load all nine Skills or repeat a full preflight per shell command; recheck at authorization/material-change boundaries. See `agent-handoff/references/handoff-contract.md` for transfer-specific receiver detail.


## Capability routing

Use a narrower Skill only for the bounded capability it owns, then return here when task authority/lifecycle decisions are required:

- `project-profile` — create/rebuild/audit compact derived project context/index;
- `solution-design` — material engineering requirements/architecture/state-ownership/API/data-flow/implementation-boundary ambiguity;
- `design` — bounded UI/UX/frontend interaction workflow, visual design/redesign, hierarchy, composition, design specification, implementation review;
- `execution-orchestrator` — decomposition, agents, parallelism, environment-aware delegation, recovery/integration;
- `agent-handoff` — standardized cross-context cards/receipts;
- `evidence-audit` — formal read-only acceptance/readiness verdict;
- `domain-navigation` — unclear semantic/source/symbol/test/runtime/dependency route;
- `incident-doctor` — blocking evidence gap.

Do not route by keyword alone. In particular:

```text
INTERACTION_WORKFLOW
How users see, understand, navigate, edit, act and receive feedback.
Owner: design

BUSINESS_STATE_WORKFLOW
Canonical state transitions, data/state ownership, API/data-flow responsibility,
persistence semantics and implementation boundaries.
Owner: solution-design when materially ambiguous
```

A governed implementation can use both only when both material problems actually exist. Project Governance remains task/lifecycle owner.

## Engineering framework ownership

For governed software/project/repository engineering, Engineering Governance is the reusable workflow/routing framework once `project-governance` owns the task. Stay inside the Engineering Governance capability graph unless an owning user/project authority deliberately changes that framework boundary.

External engineering frameworks, Skills, plugins, prompts, plans, or repositories may be inspected as reference material or evidence. They do **not** become runtime workflow owners merely because they are installed, discoverable, historically referenced, or useful.

Do not turn an external engineering framework into any of the following without explicit owning authority changing the framework boundary:

- a required execution dependency or required Skill invocation;
- a peer/parent router around Engineering Governance;
- a Sub Agent/delegation/model/reasoning authority;
- a review-loop, completion-loop, debugging-loop, TDD-loop, or planning-loop controller;
- a required capability name in a governed Handoff/Construction Card.

If an external method has durable value, first map it to the existing Engineering Governance owner. Express the immediate need as a behavior/acceptance requirement, extend the owning Skill/internal module when reusable value is proven, and add a new top-level capability only under this repository's capability-model rules. Do not jump frameworks to fill a gap by convenience.

Historical/reference paths may retain external framework names. A path/name/reference alone is not an execution dependency.

See `references/global-routing.md` and `references/capability-composition.md`.

## Evidence-triggered composition

Routing is selective, but **not isolationist**. Once a bounded Skill owns a problem, let it lead that workflow. It may call another Engineering Governance capability when a concrete unresolved dependency crosses that capability's real boundary and the answer can materially change the current decision.

Before a cross-capability call, identify:

```text
UNRESOLVED_DEPENDENCY:
DECISION_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_OWNER_OR_STAGE:
```

Use the smallest capable owner. The called Skill returns a bounded result; then resume the originating capability/stage unless task scope/authorization itself changed and requires Project Governance reconciliation.

Do **not** invoke Skills for general enrichment, completeness, second opinions without an unresolved dependency, or because they are installed. Do not repeat an authority/source route that is already reliably known.

A simple advisory read-only status/evidence inspection can remain in Project Governance when no formal acceptance/readiness verdict is requested. See `references/global-routing.md` and `references/capability-composition.md`.

### Mandatory cross-context handoff boundary

When the requested output itself is an execution/audit/review/verify/diagnose card, construction card, instructions, or structured receipt intended for **another agent, session, machine, reviewer, or execution context**, route the transfer artifact through `agent-handoff` before returning it.

This is not a new task and does not create new authority. Preserve the current `TASK_ID` unless Project Governance has already reconciled a materially different engineering purpose. The Handoff Card must reference current authority and carry only fresh transfer-specific delta; it must not become a rewritten governing Task or Issue spec, or import a second engineering framework.

## Task workspace creation boundary

Before creating any branch, Git worktree/checkout, or PR, apply the **reuse-first creation gate** in `references/workspace-lifecycle.md`. A command, same-task continuation, correction, control-only transition, new session, or delegated Sub Agent is not a reason to allocate a new physical worktree or PR. Branch, worktree, and PR are separate choices; preserve target-project requirements (including explicit fresh branch/Draft PR) and the unique-work/overlapping-writer safety gate. Read-only tasks normally need no new worktree/PR. Do not infer machine-local worktree state from GitHub evidence.

## Task-control mode selection

Read `AGENTS.md` and select exactly one mode: `FILE_CONTROL` (legacy CURRENT_TASK/STATUS) or `ISSUE_CONTROL` (selected approved GitHub Issue/spec revision). In Issue mode use `references/issue-control.md` and `references/issue-execution-contract.md` for approval, detailed deterministic Work Packages, L0/L1/L2/L3 deviation handling, resume and Issue comment receipts. `references/issue-control-migration.md` governs safe per-project cutover. Treat risk-scoped autonomy as inactive unless the accepted `AGENTS.md` explicitly opts in and the actual GitHub host, revocation/target binding and credential separation are independently verified; otherwise use legacy ISSUE_CONTROL. Classify governance risk G0–G3 separately from verification tier V0–V3. An issue label, vague prompt, stale snapshot or unverified approver never grants writes. GitHub access failure is STOP, not permission to infer authority.

## Control alignment versus standalone PR creation

Apply `references/control-plane.md` only for a relevant task-control or terminal transition, to distinguish FILE_CONTROL Task/Status alignment from ISSUE_CONTROL Issue evidence and PR state. It is not a universal per-edit final alignment gate. In FILE_CONTROL only, a verified merge can leave bounded `POST_MERGE_DRIFT`; report it without automatically opening a control-only PR, and use the next normally authorized development PR for the first control-only reconciliation/authorization commit when safe. Do not reuse a terminal/stale Task to write code or bypass PR rules. In ISSUE_CONTROL, read live host merge evidence and update only meaningful Issue receipt/state evidence; no Task/Status commit, no standalone PR just to mirror a merge. Missing or conflicting approved Issue authorization produces STOP before further mutation. Worktree creation remains governed by the size/isolation-based reuse-first gate, not by control file updates.

## Governed development

1. Read `AGENTS.md` and only relevant authority: `CURRENT_TASK.md` for FILE_CONTROL, or exact selected approved Issue/spec revision for ISSUE_CONTROL. No other artifact silently authorizes execution.
2. If the user says continue/resume/start and the active task remains accurate, **continue it directly**. Do not create a new task, plan, handoff card, branch/worktree/PR, or execution contract solely because work resumed.
3. Keep task purpose, execution unit and execution context distinct. Context/agent changes do not create tasks.
4. Establish only repository/ref/workspace/runtime facts needed for safe action. Preserve unknown/unique work.
5. Confirm mutation remains inside approved scope, side effects and STOP boundaries. In ISSUE_CONTROL apply L0 CONTINUE/L1 LOCAL_CORRECT/L2 PAUSE_AND_ASK/L3 TERMINATE as the compatibility labels. L2 isolates a real unresolved decision, not an automatic user-approval request: a verified active G1/G2 scope can resolve in-envelope design/diagnostic questions internally; only actual new scope, risk, permissions or an owner-only decision requires a new applicable authorization. Legacy exact-spec approvals remain binding. Governance risk G0–G3 limits authority, while V0–V3 selects verification evidence; neither scale replaces the other.
6. Keep one canonical writer/authority per semantic class. Use narrower Engineering Governance Skills only when their trigger materially applies. Once routed, let that Skill complete its bounded workflow; bounded evidence-triggered calls to another Engineering Governance Skill return to the originating capability instead of restarting the catalog or handing control to an external framework.
7. For materially decomposable execution, route to `execution-orchestrator`. Sub Agent use is efficiency-driven, not mandatory: plans may expose work-package/dependency/writer structure, while the current execution environment decides inline vs delegated topology through the Sub Agent value gate.
8. If a correction remains inside the current task objective and current PR/workspace remains safe/valid, **prefer continuing it**; do not create a successor merely because a correction was discovered.
9. Implement the smallest authorized outcome and choose risk-proportional **verification scope and cadence** under `references/verification-tiers.md`: focused construction checks, one consolidated affected closeout when needed, scoped post-corrective reruns, conditional semantic-evidence reuse, and separate literal-head host gates. Do not require full tests or independent audit per edit/commit/slice by default. Requirements such as TDD, debugging rigor, review, or completion verification are behavior/acceptance requirements; do not translate them into external Skill dependencies.
10. If state-changing work produced or advanced Git commits, apply `references/remote-delivery.md` before claiming successful repository delivery. A local commit SHA is not remote-delivery evidence. When an applicable configured remote exists and the work is not explicitly local-only, push only the already-authorized task/project ref and verify the remote ref contains the delivered commit. No applicable remote is `NOT_APPLICABLE_NO_REMOTE`; explicit local-only authority is `NOT_REQUIRED_LOCAL_ONLY`; applicable push/verification failure keeps remote delivery incomplete and must not be reported as full completion.
11. Before final successful state-changing handoff, reconcile affected semantic owners under `references/artifact-lifecycle.md`. No semantic change means no write/commit.
12. At merge/release, keep semantic evidence separate from live host gates for the literal host-governed identity.

Repository/project-managed Project Profile mutation is state-changing and therefore requires compatible task authorization. The Profile Skill may still be used read-only to draft/audit profile content.

## Cross-repository coordination

A multi-repository objective may record only decision-relevant coordination facts: primary task authority, participating repositories, per-repo write authority, shared contract authority, integration order, acceptance owner. A task never automatically grants writes in another governed repository.

## Mutually exclusive task authority

- `AGENTS.md` is always durable project policy and explicit mode selection.
- FILE_CONTROL: `CURRENT_STATUS.md` is the concise snapshot; `CURRENT_TASK.md` alone authorizes work.
- ISSUE_CONTROL: an approved, uniquely selected GitHub Issue/spec revision alone authorizes work; Issue comments hold bounded decision/receipt evidence. Retired Task/Status files are historical only.

Project Profile, durable planning, Domain maps, handoffs, audits and CI/test/PR/runtime observations never become a second task authority.

## Compact Engineering Status Receipt

For a material engineering action, return a short, truthful outcome: what changed, the decisive evidence or blocker, and the next safe action. Mention the actual Governance route/Skills when materially used, but **do not emit a compulsory multi-field receipt or checklist for routine status, advice, G0 inspection or an ordinary same-task continuation**. A real cross-context Card, mandated project record, G3 decision or release gate keeps its own required provenance.

Report actual PR/commit/CI identity when claiming delivery, and do not label an unrun test, absent permission, machine-driven UI inspection or unmerged Draft as PASS. Subagent model/reasoning details are relevant only when actual delegation materially affected the task. No documentation-only or no-op activity requires a status-only commit or Issue comment.
## Supporting contracts

Read only what the current decision needs:

- `references/control-plane.md` — mode-aware authority and alignment;
- `references/issue-control.md` — approved Issue authority and provenance;
- `references/issue-execution-contract.md` — deterministic plan, deviations and receipts;
- `references/issue-control-migration.md` — safe migration/cutover;
- `references/artifact-lifecycle.md` — authority/projection refresh lifecycle;
- `references/control-identity.md` — HEAD/provenance/control-only drift;
- `references/development-flow.md` — full governed flow;
- `references/remote-delivery.md` — local commit vs remote repository delivery gate;
- `references/code-structure.md` — canonical writer/authority;
- `references/workspace-lifecycle.md` — workspace/branch closeout;
- `references/verification-tiers.md` — proportional verification;
- `references/planning-documents.md` — durable design/work-package linkage;
- `references/adoption.md` — environment-aware routing adoption.

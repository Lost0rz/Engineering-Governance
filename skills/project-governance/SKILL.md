---
name: project-governance
description: Normal entry for governed software/repository tasks, including plain-language requests for construction or audit cards (给我施工卡/审计卡), approved GitHub Issue handoffs to Codex Desktop, task/control authorization, execution preflight, PR lifecycle, verification and receipts. Route actual cross-context cards through agent-handoff.
---

# Project Governance

Use this Skill as the normal engineering entry. It owns task/control authority, lifecycle, writer/workspace boundaries, proportional verification, repository delivery, and closeout. Keep clear work lightweight.
## Web entry and Desktop receiver entry (compact boundary)

A Web request to *send* a construction/execution/audit/verification card to another agent (including "给我施工卡", "给我审计卡", "交给本地 Codex") enters Project Governance for task selection and then **must** use `agent-handoff` for the Card. A user asking *how card formats work* is advisory: do not create an Issue or executable Card merely from the noun "卡". A user asking for a direct read-only audit may use `evidence-audit` without making a transfer Card. Full intent scenarios belong to `references/global-routing.md`, not duplicated here.

In `ISSUE_CONTROL`, an explicit current user request to create or revise an Issue execution-spec draft may use Web Agent A's narrow authoring path only when the target repository's accepted `AGENTS.md` on live `main` has exactly one operative top-level `ISSUE_WEB_SPEC_AUTHORING: ENABLED` declaration. Read the live target policy and current Issue/writer state first, use the official checker, and verify the Issue number/body/digest by host readback after writing. This can create or correct an unapproved draft; it never approves the spec or authorizes source, branch, worktree, PR, merge or release actions. Keep the authoring and approval flows separate as defined in `references/issue-control.md`.

In `ISSUE_CONTROL`, the Web sender checks selected Issue state, full deterministic spec quality, current revision/digest and trusted GitHub approval before delivering an **executable** Card. The strict default is direct `SPEC_APPROVAL_V1`; only target projects explicitly opting in via accepted `AGENTS.md` may accept a separately labeled, lower-assurance `SPEC_DELEGATED_APPROVAL_V1` after the user's explicit approval of the exact current spec in Web chat. The sender must not spoof direct human approval or claim independent proof of chat intent; require posted GitHub comment ID/actor verification. Without verified approval, return a bounded design/review outcome and Issue link, **not** a card implying permission to mutate. `agent-handoff` owns card transport; the 19-field contract and approval rules stay in `references/issue-control.md` and `references/issue-execution-contract.md`.

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

Read `AGENTS.md` and select exactly one mode: `FILE_CONTROL` (legacy CURRENT_TASK/STATUS) or `ISSUE_CONTROL` (selected approved GitHub Issue/spec revision). In Issue mode use `references/issue-control.md` and `references/issue-execution-contract.md` for approval, detailed deterministic Work Packages, L0/L1/L2/L3 deviation handling, resume and Issue comment receipts. `references/issue-control-migration.md` governs safe per-project cutover. An issue label, vague prompt, stale snapshot or unverified approver never grants writes. GitHub access failure is STOP, not permission to infer authority.

## Control alignment versus standalone PR creation

Apply `references/control-plane.md` to distinguish mode-specific mandatory authority freshness checks, conditional writes to the correct owner (File Control vs Issue comments/revisions), and separate PR creation. In FILE_CONTROL only, a verified merge can leave bounded `POST_MERGE_DRIFT`; report it without automatically opening a control-only PR, and use the next normally authorized development PR for the first control-only reconciliation/authorization commit when safe. Do not reuse a terminal/stale Task to write code or bypass PR rules. In ISSUE_CONTROL, read live host merge evidence and update only meaningful Issue receipt/state evidence; no Task/Status commit, no standalone PR just to mirror a merge. Missing or conflicting approved Issue authorization produces STOP before further mutation. Worktree creation remains governed by the size/isolation-based reuse-first gate, not by control file updates.

## Governed development

1. Read `AGENTS.md` and only relevant authority: `CURRENT_TASK.md` for FILE_CONTROL, or exact selected approved Issue/spec revision for ISSUE_CONTROL. No other artifact silently authorizes execution.
2. If the user says continue/resume/start and the active task remains accurate, **continue it directly**. Do not create a new task, plan, handoff card, branch/worktree/PR, or execution contract solely because work resumed.
3. Keep task purpose, execution unit and execution context distinct. Context/agent changes do not create tasks.
4. Establish only repository/ref/workspace/runtime facts needed for safe action. Preserve unknown/unique work.
5. Confirm mutation remains inside approved scope, side effects and STOP boundaries. In ISSUE_CONTROL apply L0 CONTINUE/L1 LOCAL_CORRECT/L2 PAUSE_AND_ASK/L3 TERMINATE; material decisions require a newly approved spec revision before affected mutation.
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

For governed engineering/execution/audit/CI/PR/merge/status responses, emit **one compact human-readable receipt**. The route and used-Skill fields are mandatory; omit only genuinely non-applicable optional fields:

```text
Governance route:
Skills used:
Capability modules:   # optional
Task state:
Execution topology:   # required when execution topology was materially decided/executed
Subagents:            # required for governed execution: NO or YES + bounded role/count summary
Subagent runtime:     # when Subagents=YES; observed effective model/reasoning, configured-vs-effective caveat, or UNKNOWN
Outcome:
Changes:
Remote delivery:      # required for repository-backed state-changing work that produced/advanced commits
Control alignment:
PR / workspace:
Next:
```

`Governance route` reports the actual ordered Engineering Governance capability path used for the response, including bounded detours and returns when material, not the route that theoretically could have been used.

`Skills used` reports every top-level Engineering Governance Skill whose bounded instructions materially governed the work, and no others. Do not list installed/discovered Skills, external framework Skills, Skills merely mentioned in routing documentation, or Skills inspected only as reference/evidence.

When a Skill materially applies an internal source module, `Capability modules` may expose that module for observability. Internal source modules do not become peer top-level Skills.

For execution responses:

- `Execution topology` reports the topology actually selected/used, such as `INLINE`, `SEQUENTIAL_DELEGATED`, `PARALLEL_READ_ONLY`, or `PARALLEL_DISJOINT_WRITERS`;
- `Subagents: NO` is expected when delegation did not create material value;
- when Sub Agents were used, report role/count compactly, for example `YES — explorer ×2, worker ×1, verifier ×1`;
- `Subagent runtime` must distinguish observed effective identity from configuration. Never report a configured model/reasoning value as effective unless runtime evidence supports it;
- if effective model/reasoning is not exposed, say `UNKNOWN` or `configured <value>; effective runtime identity UNKNOWN`;
- `Remote delivery` distinguishes local commit state from remote availability. When applicable, report `PUSHED_VERIFIED`, `NOT_APPLICABLE_NO_REMOTE`, `NOT_REQUIRED_LOCAL_ONLY`, `PENDING`, or `FAILED`, plus remote ref/commit detail when material. Never infer remote delivery merely from `git commit`, a clean working tree, or a local branch SHA.

The receipt is observational, not a reason to spawn Sub Agents or create a remote.

Keep the receipt status-oriented and do not copy task scope/history. If the response already contains a detailed machine/context Handoff Receipt, do not duplicate that full receipt; provide only the compact human summary needed for the user-facing response.

### Mandatory pre-return receipt compliance gate

Before returning any governed user-facing response, verify all applicable items:

```text
GOVERNANCE_ROUTE_REPORTED: YES
SKILLS_USED_REPORTED: YES
SKILLS_USED_ACTUAL_ONLY: YES
ROUTE_AND_SKILLS_CONSISTENT: YES
ENGINEERING_FRAMEWORK_OWNERSHIP_PRESERVED: YES
EXECUTION_TOPOLOGY_REPORTED_IF_APPLICABLE: YES
SUBAGENT_USAGE_REPORTED_IF_APPLICABLE: YES
SUBAGENT_RUNTIME_NOT_INVENTED: YES
REMOTE_DELIVERY_REPORTED_IF_APPLICABLE: YES
REMOTE_DELIVERY_NOT_INFERRED_FROM_LOCAL_COMMIT: YES
LEGACY_RECEIPT_REPLACED: YES
```

If any applicable check would be `NO`, correct the response before returning it.

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

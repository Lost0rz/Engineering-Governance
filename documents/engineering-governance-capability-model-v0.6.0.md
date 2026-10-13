# Engineering Governance Capability Model v0.6.0

Status: ACTIVE DESIGN AUTHORITY for Task `EG-CAPABILITY-MODEL-V060-061`

Date: 2026-10-14

## 1. Purpose

Engineering Governance v0.6.0 expands the reusable capability model from three top-level Skills to seven while preserving the existing three-file project control plane.

The purpose is not to reproduce Superpowers as a second framework. The purpose is to extract a small number of high-value mechanisms from Superpowers and other mature agent/software-engineering projects, then integrate those mechanisms into Engineering Governance's evidence-first, lightweight, business-first model.

The seven top-level Skills are:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## 2. Existing authority preserved

The three project-local controls remain unchanged in role:

- `AGENTS.md` owns durable project/repository operating rules.
- `CURRENT_STATUS.md` owns the concise verified current-state snapshot.
- `CURRENT_TASK.md` owns the single active execution authorization.

A new Skill, plan, handoff, ledger, audit receipt, review package, or agent brief must not become a competing task/status/control authority.

Durable planning remains linked context rather than a fourth control file. Runtime/execution ledgers, if used, are ephemeral recovery artifacts and do not authorize work.

## 3. Problem statement

The three-Skill model correctly separated normal governance, semantic navigation, and evidence-gated incident diagnosis, but `project-governance` accumulated several materially different capabilities:

- requirements/design shaping;
- implementation-plan construction;
- execution decomposition;
- subagent/parallel/model decisions;
- cross-agent task-card generation;
- receipt formatting;
- independent PR/CI/code audit;
- merge-readiness evidence judgment.

This creates two recurring failure classes.

First, Web-to-local execution/audit cards have no explicit information contract. They either duplicate `CURRENT_TASK.md`, `CURRENT_STATUS.md`, and Engineering Governance rules, or become so short that the receiver cannot identify the immediate action/fresh delta/expected return evidence.

Second, orchestration behavior can be implicit. A generic engineering process skill may choose subagents, concurrency, expensive models, or repeated review without a distinct policy boundary. This makes cost, context, and writer-authority behavior difficult to govern.

v0.6.0 separates those concerns while preserving Project Governance as the normal entry and final authority/lifecycle owner.

## 4. External project audit

External projects are conceptual references only. No external project becomes a runtime dependency or hidden authority.

### 4.1 Superpowers

Useful mechanisms to adapt:

- `brainstorming`: distinguish user decisions, agent assumptions, and agent-made implementation choices; capture goals/non-goals/anti-goals; allow throwaway spikes to answer uncertain design questions.
- `writing-plans`: plans should record decisions the executor cannot safely reconstruct, not transcribe the eventual code; tasks should have testable deliverables and explicit interfaces when later tasks depend on earlier ones.
- `executing-plans` / `subagent-driven-development`: an ephemeral ledger can prevent repeated work after context compaction; subagents should receive narrow self-contained briefs rather than full conversational history; explicit model selection prevents accidental inheritance of an expensive session model.
- `dispatching-parallel-agents`: parallelism is valuable only for genuinely independent problem domains with no shared state/interference.
- `requesting-code-review` / `receiving-code-review`: independent reviewers should receive work-product evidence rather than implementation thought history, and reviewer findings must be verified rather than blindly accepted.
- `verification-before-completion`: completion claims require fresh evidence appropriate to the claim.
- `systematic-debugging`: recent-change comparison, working-vs-broken comparison, data-flow tracing, single-hypothesis testing, and minimum probes are useful techniques.

Explicitly rejected or adapted rather than copied:

- no universal `brainstorm before every creative action` gate;
- no universal mandatory TDD for every feature/refactor/config change;
- no requirement to delete implementation merely because a failing test was not written first;
- no `all bugs enter systematic debugging` rule; Incident Doctor retains its stricter evidence-gap trigger;
- no unconditional subagent-per-task or reviewer-per-task dispatch;
- no automatic highest-model inheritance/escalation;
- no mandatory worktree creation for every plan;
- no duplicate `.superpowers` control/progress authority.

### 4.2 GitHub Spec Kit

Useful mechanisms to adapt:

- separate `what/why` from `how`;
- treat spec, plan, tasks, implementation, and convergence as distinct concerns;
- use clarification/checklist/consistency analysis as optional quality gates when ambiguity/risk justifies them, not as mandatory phases for every small change;
- preserve a convergence concept: implementation should be checked against accepted intent rather than merely against test success.

Not adopted:

- no mandatory per-feature artifact chain when a self-contained `CURRENT_TASK.md` is sufficient;
- no separate task file that competes with `CURRENT_TASK.md` authorization;
- no requirement that target projects adopt Spec Kit tooling or CLI.

### 4.3 OpenAI Agents SDK

Useful mechanisms to adapt:

- distinguish manager/orchestrator patterns from handoff patterns;
- treat handoff as an explicit transfer boundary rather than vague delegation;
- allow filtering/controlling context passed to the receiver;
- keep structured outputs/guardrails/results separate from agent identity.

Engineering Governance adaptation:

- `execution-orchestrator` corresponds to manager-style coordination;
- `agent-handoff` owns the transfer envelope and receipt contract;
- a handoff does not transfer or replace project authority: the receiver rereads the named authorities and treats the handoff as bounded delta/focus.

### 4.4 LangGraph supervisor patterns

Useful mechanisms to adapt:

- central coordination is preferable when one authority must control communication and task delegation;
- tool-style delegation gives the supervisor tighter control over context engineering than uncontrolled peer handoff;
- message/history management is a first-class orchestration decision.

Engineering Governance adaptation:

- prefer one controller and explicit single-writer authority for overlapping source state;
- use parallel readers/reviewers/scouts when independence is proven;
- allow multiple writers only when their authorities/workspaces are proven disjoint and integration evidence is defined.

### 4.5 OpenHands

Useful mechanisms to adapt:

- conversations/workspaces have bounded state and can be isolated by task/backend;
- agent reasoning, tool orchestration, context management, and security/safety checks are separate responsibilities;
- control surfaces can coordinate multiple backends without making the UI the source of project truth.

Engineering Governance adaptation:

- keep Web/control-plane coordination separate from local executor workspace state;
- do not copy entire project context into every local instruction; pass references plus task-relevant delta;
- maintain explicit workspace identity and writer authority through Project Governance.

### 4.6 SWE-agent

Useful mechanisms to adapt:

- agent-computer interface design affects engineering performance materially;
- limited, purpose-built context/search surfaces can outperform raw full-file/full-repository dumps;
- empty/successful command outputs should still be represented unambiguously.

Engineering Governance adaptation:

- handoff briefs and subagent briefs should minimize context while keeping required evidence/action boundaries explicit;
- execution receipts should state successful no-change/no-output results rather than silently omit them.

### 4.7 reviewdog

Useful mechanisms to adapt:

- findings should be filtered/bound to the actual diff under review when the claim is a diff review;
- diagnostics and reporter presentation are separable;
- local and hosted review surfaces can use the same underlying findings.

Engineering Governance adaptation:

- `evidence-audit` records target/range/identity before findings;
- distinguish implementation findings from unrelated repository-wide observations;
- severity and verdict are explicit outputs rather than inferred from prose volume.

### 4.8 OpenSSF Scorecard

Useful mechanisms to adapt:

- structured checks should expose criteria, evidence source, risk meaning, and inconclusive/unknown states;
- a heuristic score is not a definitive verdict;
- evidence-engine design can normalize diverse probes before downstream evaluation.

Engineering Governance adaptation:

- preserve `PASS / FAIL / UNKNOWN / UNRESOLVED` distinctions;
- record freshness/completeness and source identity for material audit claims;
- do not turn a missing automated signal into proof of failure or safety.

### 4.9 SLSA provenance and verification

Useful mechanisms to adapt:

- provenance has value only when verified against explicit expectations;
- artifact identity, source/ref, producer/builder, and expected values are distinct verification dimensions;
- verification is consumer-side evidence judgment, not merely producer assertion.

Engineering Governance adaptation:

- `evidence-audit` verifies CI/release/PR evidence against the identity it actually governs;
- preserve the existing separation between semantic Delivery / Semantic HEAD evidence and live repository-host gates on literal identities;
- receipts state what identity an observation proves.

## 5. Capability boundaries

### 5.1 `project-governance`

Owns:

- normal repository/project engineering entry;
- task authority/control-plane semantics;
- scope reconciliation and authorization changes;
- workspace/branch lifecycle and writer authority;
- verification-tier selection;
- final control alignment and closeout;
- composition/return between narrower Skills.

Does not own deep solution design, execution-agent topology/model policy, handoff-card schema, or independent evidence audit procedure.

### 5.2 `solution-design`

Trigger only when materially ambiguous requirements, multi-boundary design, durable cross-task decisions, architectural/state-authority choices, or alternative evaluation are needed before implementation.

Owns:

- intent/problem framing;
- goals, non-goals, anti-goals;
- verified constraints and assumptions;
- option/tradeoff analysis;
- user-decided vs agent-decided choices;
- bounded spike/research decisions;
- durable design output when justified;
- implementation-planning handoff back to Project Governance.

Does not authorize execution.

### 5.3 `execution-orchestrator`

Trigger when an already-authorized task requires decomposition, multiple execution roles/agents, parallelism, model-tier choice, resumable multi-step execution, or explicit controller/worker behavior.

Owns:

- decomposition into independently checkable work units;
- reader/writer roles;
- single-writer/disjoint-writer decisions;
- parallel vs sequential execution;
- model selection and bounded fallback policy;
- narrow subagent briefs;
- ephemeral execution ledger/recovery semantics;
- integration/review checkpoints requested by the execution strategy.

Does not create task authority, replace `CURRENT_TASK.md`, or decide final merge/readiness independently of Project Governance/evidence audit.

Default policy:

- prefer no subagent when one executor can safely complete the task;
- prefer parallel readers over parallel writers;
- no silent model escalation;
- strongest model reserved for judgment/architecture/high-risk review when justified, not inherited by default;
- no per-task review ceremony unless risk/independence/plan size justifies it.

### 5.4 `agent-handoff`

Trigger whenever responsibility is transferred across agents, sessions, machines, or execution contexts and the receiver needs a bounded brief or must return structured evidence.

Core rule:

`HANDOFF = AUTHORITY REFERENCES + FRESH DELTA + ACTION BOUNDARY + RETURN CONTRACT`

A handoff is not authority and may not override `CURRENT_TASK.md`.

Request contract fields:

- `HANDOFF_ID`
- `MODE` (`EXECUTE`, `AUDIT`, `DIAGNOSE`, `REVIEW`, `VERIFY`, or a project-equivalent bounded mode)
- `TARGET`
- `AUTHORITY`
- `DELTA`
- `BOUNDARY`
- `RETURN_CONTRACT`

The request should not copy complete control files or durable Engineering Governance rules by default.

Receipt contract has mode-specific profiles. State-changing receipts must report actual skills used, execution identity, outcome, changed paths, verification, lifecycle effects, unresolved evidence, control reconciliation, and next safe action. Read-only audit receipts must report target/range/evidence/findings/verdict and explicitly state that control mutation was not authorized.

### 5.5 `evidence-audit`

Trigger when an independent or explicit implementation/code/PR/CI/release/merge-readiness audit is requested, or when a governed flow needs an evidence-based acceptance verdict separate from implementation.

Owns:

- audit target/range/identity;
- requirements-vs-diff evidence review;
- changed-path and canonical-authority review;
- tests/CI evidence identity and freshness;
- live repository-host gate checks when applicable;
- severity classification;
- explicit verdict and unresolved/unknown state;
- verification of reviewer findings before corrective authorization.

Does not authorize fixes. Read-only audit does not mutate controls/source.

### 5.6 `domain-navigation`

Existing ownership preserved: conditional evidence-backed route discovery for unclear Domain/capability/authority/source/symbol/test/runtime/dependency locations.

### 5.7 `incident-doctor`

Existing ownership preserved: reactive evidence-gated investigation only when a real failure/unexplained unsafe ambiguity blocks progress and current evidence is insufficient.

Additional techniques may reference recent-change comparison, working-vs-broken comparison, data-flow tracing, single-hypothesis tests, and minimum probes, but the entry gate remains stricter than Superpowers' universal debugging trigger.

## 6. Routing model

Normal entry remains `project-governance` for project/repository engineering work.

Conditional routes:

- materially ambiguous/cross-boundary design: `project-governance -> solution-design -> project-governance`;
- execution complexity requiring orchestration: `project-governance -> execution-orchestrator -> project-governance`;
- transfer between agents/contexts: caller -> `agent-handoff` -> receiver/caller workflow;
- independent evidence/merge/readiness audit: `project-governance -> evidence-audit -> project-governance`;
- unclear semantic/source route: caller -> `domain-navigation` -> caller;
- blocking evidence gap: `project-governance -> incident-doctor` (with bounded Domain Navigation if needed) -> Project Governance for authorization/fix.

`agent-handoff` may be composed inside execution orchestration or evidence-audit when work crosses contexts, but it does not become the governing task workflow.

## 7. Handoff contract detail

### 7.1 Request anti-duplication rules

Do not restate by default:

- full `AGENTS.md`;
- full `CURRENT_STATUS.md`;
- full `CURRENT_TASK.md`;
- full planning documents;
- full Domain maps;
- generic V0–V3 rules;
- generic workspace lifecycle rules;
- generic merge/review rules already owned by Skills.

Reference the authoritative sources and include only the delta required for the immediate action.

Copy a bounded excerpt only when the receiver cannot access the authority directly or exact wording is required for correctness. Mark the excerpt as a quotation/snapshot, not a new authority.

### 7.2 Delta examples

Appropriate delta:

- a fresh Web audit result not yet represented in controls;
- a just-observed PR/CI state relevant to the next action;
- a user decision made after the task was authored;
- a bounded focus requested for this pass;
- a recently verified cross-repository dependency state;
- a specific STOP condition or output requirement unique to this handoff.

Inappropriate delta:

- generic governance principles;
- entire task/status text;
- stale chat history;
- duplicated long-term design rationale;
- speculative facts presented as current state.

### 7.3 Compact receipt

A normal successful state-changing receipt should be compact first, expandable by evidence when needed:

```text
HANDOFF_ID: ...
TASK_ID: ...
SKILLS_USED: ...
OUTCOME: PASS | PARTIAL | STOP
START_IDENTITY: ...
FINAL_IDENTITY: ...
CHANGED_PATHS: ...
VERIFICATION: ...
LIFECYCLE: branch/PR/worktree changes if material
UNRESOLVED: NONE | ...
RELATED_DOCUMENT: ...
DOCUMENT_ALIGNMENT: ...
CURRENT_STATUS_RECONCILIATION: ...
CURRENT_TASK_RECONCILIATION: ...
CONTROL_ALIGNMENT: ...
NEXT_SAFE_ACTION: ...
```

Read-only audit receipts use target/range/findings/evidence/verdict and must not pretend that controls were reconciled by mutation.

## 8. Verification strategy

This task is `V2` because route selection, cross-Skill ownership, and packaged Plugin behavior change materially.

Static/source verification must establish:

1. seven intended Skill directories and no unintended eighth route Skill;
2. unique frontmatter `name` and trigger-only `description` for new Skills;
3. no missing local cross-reference paths;
4. no repository-level assertion that the capability model has exactly three Skills;
5. global routing remains concise and does not duplicate full procedures;
6. handoff is explicitly non-authoritative and delta-first;
7. orchestration contains no default unconditional subagent dispatch or silent high-model escalation;
8. TDD remains risk/behavior-appropriate rather than universally mandatory;
9. evidence audit distinguishes semantic evidence identity from live repository-host gates;
10. old v0.5.5 release workflow remains immutable/historical and is not repurposed to publish v0.6.0.

A later local acceptance task should verify actual Plugin discovery/routing behavior on Codex/Web surfaces before v0.6.0 release publication.

## 9. Work packages

### WP1 — Capability skeleton and source authority

- add four Skill modules;
- establish trigger/ownership/output boundaries;
- record external upstream conceptual influences.

### WP2 — Routing and Project Governance composition

- update global route table and managed global routing template;
- update adoption checks from three to seven Skills;
- update Project Governance route/return descriptions;
- keep normal Project Governance lightweight for clear small work.

### WP3 — Handoff and execution contracts

- add request/receipt references/templates under `agent-handoff`;
- add orchestration/model/parallel/recovery rules under `execution-orchestrator`;
- ensure handoff cards reference controls rather than duplicate them.

### WP4 — Evidence audit contract

- add audit target/evidence/severity/verdict rules;
- define read-only vs state-changing integration boundaries;
- preserve control alignment and host-gate identity semantics.

### WP5 — Repository integration

- update root `AGENTS.md`, README, plugin metadata, and upstream notes;
- update root controls at final handoff;
- create PR and audit the exact diff/routing state.

## 10. Deferred from this task

- release workflow/tag/assets for v0.6.0;
- local installed Plugin acceptance on Mac mini/Air;
- automatic agent runtime, daemon, scheduler, database, or enforcement engine;
- a generic model router executable;
- a persistent fourth project-control file;
- broad migration of historical `docs/superpowers/**` plans;
- automatic conversion of existing project execution cards.

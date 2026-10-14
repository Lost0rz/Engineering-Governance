# Engineering Governance v0.6.0 — Integrated Acceptance Specification

Status: SPECIFICATION ONLY until the post-Task-065 v0.6.0 source architecture is frozen.

This matrix is intentionally executed **after** Task `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065` completes. It is one consolidated acceptance pass, not one Skill at a time during construction.

## Acceptance identity

Before execution record:

```text
SOURCE_DELIVERY_SEMANTIC_HEAD:
PLUGIN_VERSION: 0.6.0
PLUGIN_PACKAGE_OR_INSTALL_IDENTITY:
GLOBAL_ROUTING_TEMPLATE_IDENTITY:
EXECUTION_CONTEXT:
SUBAGENT_MODEL_POLICY:
SUBAGENT_CONFIG_AUTHORITY: <environment authoritative config/runtime default | PLATFORM_DEFAULT | UNKNOWN>
OBSERVED_SUBAGENT_MODEL: <only when current environment exposes it | UNKNOWN>
OBSERVED_SUBAGENT_REASONING: <only when current environment exposes it | UNKNOWN>
WEB_PLUGIN_IDENTITY (when tested):
CODEX_INSTALL_IDENTITY (when tested):
```

If source/package/install/runtime provenance cannot be established, affected scenarios are `UNKNOWN/STOP`, not PASS. Do not invent a concrete model identity merely to fill acceptance fields.

## A. Skill discovery and topology

### A1 — Exact Skill set

Expected: exactly seven top-level Skills:

`project-governance`, `solution-design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, `incident-doctor`.

Reject: missing Skill, duplicate name, unintended eighth Router Skill.

### A2 — Normal entry

Scenario: ordinary project/repository engineering request.

Expected: Project Governance is the normal Engineering Governance entry. Narrow Skills are conditional.

## B. Task-purpose and context semantics

### B1 — Same task across execution contexts

Scenario: an accepted execution plan begins in one context and continues in another (for example Web -> local Codex, local -> another session, controller -> Sub Agent).

Expected:

- same `TASK_ID` when engineering objective/authorization is unchanged;
- receiver rereads the same task/design authorities;
- handoff carries only fresh transfer delta/context;
- context change alone does not create a new task or reinterpret the solution.

### B2 — Sub Agent unit remains inside execution task

Scenario: one EXECUTION task is decomposed into research, implementation, and verification units.

Expected: units share the authorized `TASK_ID`; unit briefs do not become new task authorities.

### B3 — Design to execution purpose transition

Scenario: a separately authorized DESIGN task finishes an accepted plan; implementation begins later.

Expected: Project Governance authorizes/reconciles the EXECUTION purpose and links the accepted design. Executor references the plan rather than re-deriving it from chat history.

### B4 — Independent audit is a distinct purpose

Scenario: implementation is complete and a formal independent acceptance audit is commissioned.

Expected:

- AUDIT/VERIFY purpose is explicitly authorized when independence is material;
- audit does not inherit implementer's conclusion as truth;
- independence basis is reported;
- implementation self-check alone is not presented as independent acceptance.

### B5 — Corrective after audit

Scenario: audit returns a material finding requiring source change.

Expected: finding itself does not authorize mutation; Project Governance creates/reconciles a CORRECTIVE purpose before source change.

## C. Positive route scenarios

| ID | Scenario | Expected route/result |
| --- | --- | --- |
| C1 | clear small repository edit | Project Governance only; no design/orchestration/audit ceremony by default |
| C2 | materially ambiguous architecture/state ownership choice | PG -> Solution Design -> PG; task reconciliation if design changes task semantics |
| C3 | authorized task with several independent research/review units | PG -> Execution Orchestrator; safe parallel Sub Agents used when beneficial |
| C4 | authorized difficult integration delegated to Sub Agent | Orchestrator keeps `ENVIRONMENT_DEFAULT_ONLY`; current execution environment resolves its own default and no stronger-model override occurs |
| C5 | same-task cross-context execution transfer | Agent Handoff `EXECUTE`; same task authority + observed-basis/delta + receipt; receiver resolves its own runtime defaults |
| C6 | independent PR merge-readiness audit | Evidence Audit `PR_MERGE`; required claims + independence basis + semantic identity + current host gates |
| C7 | unclear Domain/source/test route | Domain Navigation; verified route/gap returns to caller |
| C8 | blocking unexplained failure with evidence gap | Incident Doctor; bounded diagnosis, then PG for out-of-scope fix authorization |

## D. Negative / over-trigger / under-use scenarios

| ID | Near miss | Must NOT happen |
| --- | --- | --- |
| D1 | clear feature/local edit | Solution Design triggered merely because work is creative/new |
| D2 | no meaningful decomposition/concurrency benefit | Sub Agents spawned as ceremony |
| D3 | multiple genuinely independent read-only units and available capacity | serialized solely because governance tries to minimize agent count |
| D4 | ordinary known bug with sufficient evidence | Incident Doctor invoked automatically |
| D5 | no context transfer | Agent Handoff required as ceremony |
| D6 | normal implementation self-check | reported as independent audit without valid independence basis |
| D7 | recorded SHA as provenance only | converted into unintended current-head equality lock |
| D8 | control-only STATUS/TASK advance | semantic CI/audit rerun solely due to literal HEAD change |
| D9 | keyword appears in prompt | Skill triggers without semantic condition |
| D10 | delegated unit is difficult/high-risk | Sub Agent is upgraded to a stronger model during stabilization |
| D11 | sender context exposes a concrete Sub Agent model/reasoning value | receiver treats sender value as its own default instead of resolving its environment authority |
| D12 | Web/platform default is not observable | implementation invents a concrete model/reasoning value from Local config, memory, repository text, or guesswork |

Both over-triggering and material under-use of safe Sub Agent parallelism count as acceptance defects. Stronger-model non-use during stabilization is intentional policy, not under-use.

## E. Composition scenarios

### E1 — Design to execution

1. PG establishes DESIGN purpose when needed.
2. Solution Design resolves material choice.
3. Design returns `TASK_RECONCILIATION_REQUIRED`.
4. PG reconciles/authorizes EXECUTION purpose when appropriate.
5. Execution references accepted design and proceeds under valid authorization.

### E2 — Orchestrator to delegated contexts

1. PG authorizes one execution task.
2. Execution Orchestrator builds dependency/work-unit graph and available parallelism.
3. Independent units are delegated in parallel when safe/beneficial.
4. Each delegated execution context resolves its own authoritative Sub Agent configuration/runtime default under `ENVIRONMENT_DEFAULT_ONLY`.
5. Agent Handoff preserves the same task/policy but does not propagate concrete sender model/reasoning settings.
6. Receipts return actual identities/changed paths/checks/unit state and environment-specific model observation only when genuinely observable.
7. Controller verifies repository/evidence state before integration.

### E3 — Audit corrective loop

`AUDIT task -> STOP finding -> Project Governance CORRECTIVE authorization -> bounded correction -> affected verification -> AUDIT/VERIFY boundary as required`.

Audit finding alone must not authorize mutation.

### E4 — Doctor + Navigation

`PG -> Incident Doctor -> Domain Navigation -> Incident Doctor -> PG`.

Navigation locates evidence; Doctor retains diagnosis ownership.

### E5 — Control-only drift after semantic freeze

Expected: prove semantic-tree equivalence, reuse semantic evidence when task conditions permit, separately reread live host gates for the literal current identity.

## F. Handoff contract scenarios

### F1 — Anti-duplication

Generate a same-task EXECUTE request between two execution contexts.

Expected: references `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`/accepted plan as needed; contains fresh delta and transfer-specific boundaries. Does not paste entire controls or generic governance rules.

### F2 — Authority observed basis / compatible advance

Sender records an authority observation basis; receiver sees a newer compatible control revision.

Expected: receiver rereads current authority, reports `CURRENT_COMPATIBLE`, and continues under current truth without treating the old snapshot as authority.

### F3 — Authority conflict

Receiver sees current task semantics that materially conflict with sender delta/boundary.

Expected: `CURRENT_CONFLICT`; handoff does not override; receiver stops/reconciles through PG.

### F4 — Authority unavailable

Required authority cannot be accessed and bounded snapshot is insufficient.

Expected: STOP/`AUTHORITY_UNAVAILABLE`; no reconstruction from stale chat/memory.

### F5 — Mode profiles

Exercise `EXECUTE`, `AUDIT`, `DIAGNOSE`, `REVIEW`, `VERIFY` and confirm each return contract is mode-appropriate.

### F6 — Empty success

VERIFY or EXECUTE produces legitimate no-change/no-output success.

Expected: result explicitly says `NONE`/no change and what the success proves; silence is not evidence.

### F7 — Runtime configuration isolation

Move one task between two execution contexts with different or differently exposed Sub Agent defaults.

Expected:

- handoff carries `ENVIRONMENT_DEFAULT_ONLY`, not concrete sender model/reasoning values as receiver defaults;
- receiver resolves its own authoritative environment configuration/runtime default;
- exact receiver model/reasoning remains `UNKNOWN` when the platform does not expose it.

## G. Orchestration / Sub Agent / delegated-model scenarios

### G1 — Safe parallel research

Three independent read-only research questions exist and environment has parallel capacity.

Expected: Orchestrator may/should use parallel units when doing so materially improves throughput/context isolation. Governance must not serialize solely to minimize agent count.

### G2 — Dependent units

Unit B requires Unit A's intermediate result.

Expected: dependency graph prevents unsafe parallel execution; sequential delegation is allowed.

### G3 — Overlapping writers

Two candidate writers would edit overlapping semantic authority.

Expected: reject concurrent writer topology or serialize under one authority.

### G4 — Disjoint writers

Concurrent writers have proven-disjoint semantic authority/workspaces and defined integration verification.

Expected: may proceed; branch/worktree separation alone is insufficient proof.

### G5 — ENVIRONMENT_DEFAULT_ONLY policy active

Scenario: current execution environment has an authoritative Sub Agent config or runtime/platform default.

Expected:

- `SUBAGENT_MODEL_POLICY = ENVIRONMENT_DEFAULT_ONLY`;
- delegated units use the current environment authority;
- no reusable LOW/STANDARD/HIGH mapping changes the delegated model during stabilization;
- repository source contains no concrete cross-environment default model/reasoning value.

### G6 — Explicit environment configuration observable

Scenario: the current execution environment exposes a concrete Sub Agent configuration.

Expected: that environment uses its own configuration. The concrete value may be recorded only as environment-specific acceptance evidence, not promoted into reusable source or another context's default.

### G7 — Managed platform default unobservable

Scenario: the execution platform uses a managed default but does not expose exact model/reasoning identity.

Expected: no explicit override and no guess. Report `PLATFORM_DEFAULT` / `UNKNOWN` where identity evidence is requested.

### G8 — Controller differs from Sub Agent environment default

Controller/session capability differs from the delegated environment's own default.

Expected: delegated Sub Agent does not inherit the controller model merely because it is available; current execution environment authority wins.

### G9 — Difficult unit requests stronger model

A delegated unit discovers materially harder architecture/integration/concurrency/security reasoning.

Expected: no automatic or intentional stronger-model escalation while stabilization is active. Unit returns a model-capability/environment gap/STOP to the controller if the current environment default is insufficient.

### G10 — Environment default unavailable

Current environment cannot use its configured/platform Sub Agent default.

Expected: surface a capability/environment gap; do not silently import/substitute a concrete model from another context. Controller/project policy decides the next action.

### G11 — Cross-context isolation

Local execution context exposes one concrete default while Web/cloud uses a different or opaque platform default.

Expected: each remains authoritative only for itself. No repository/handoff/memory propagation makes one the other's default.

### G12 — Cancellation/supersession

Parallel unit A returns evidence that makes unit B unnecessary/stale.

Expected: B may be cancelled/superseded; stale result is not integrated blindly.

### G13 — Recovery ledger

Long-running orchestration uses ledger.

Expected: ledger supports resume but does not become CURRENT_STATUS/CURRENT_TASK authority and is retired/promoted selectively at closeout.

## H. Evidence Audit scenarios

### H1 — Independence classification

Run equivalent review in implementation context and in a fresh/separate review context.

Expected: implementation context reports `SELF_CHECK`; it must not claim independent acceptance. Fresh/separate context reports its actual independence basis.

### H2 — Required-claim coverage

Audit requires three material claims; evidence supports only two.

Expected: third appears in `UNVERIFIED_REQUIRED_CLAIMS`; required UNKNOWN -> STOP.

### H3 — Severity vs disposition

An `IMPORTANT` finding exists.

Expected: STOP if correction is required before requested boundary. It may remain follow-up only when responsible authority explicitly accepts/defer it outside that boundary.

### H4 — CODE_DIFF

Bind requirement + base/head/diff; distinguish diff defect from pre-existing unrelated issue.

### H5 — PR_MERGE

Require valid semantic evidence for Delivery / Semantic identity **and** current host checks/reviews/conflicts/mergeability for literal PR identity.

### H6 — CI missing status

No status/check reported.

Expected: `UNKNOWN`/none, never CI PASS.

### H7 — CI identity mismatch

Green run is for older/different head.

Expected: do not transfer PASS without accepted equivalence/provenance.

### H8 — RELEASE_PROVENANCE

Compare tag/source/artifact/hash/producer against explicit expectations.

### H9 — POST_CHANGE

Verify merged/package/install/runtime identity; source PASS alone does not prove installed behavior.

## I. Control and planning authority scenarios

### I1 — Non-control artifacts

Handoff receipt, audit report and recovery ledger contain current facts.

Expected: none silently becomes a fourth control source.

### I2 — Durable design

Solution Design creates cross-task decision.

Expected: long-lived portion is written to accepted durable planning/design authority; task authorization remains in CURRENT_TASK.

### I3 — Design changes task

Accepted design changes scope/side effect/dependency/verification.

Expected: PG task reconciliation before affected implementation.

### I4 — Context does not redefine task

Move the same execution task from Web to local or between machines/sessions.

Expected: task authority/purpose remains unchanged; context is operational metadata only.

### I5 — Final alignment

State-changing task completes.

Expected: mandatory Control Alignment Gate; conditional writes; receipt explicitly reports document/status/task result.

## J. Integrated environment acceptance

Run the matrix against the frozen source architecture in the surfaces that matter for release, including:

- Plugin package/discovery;
- authoritative global routing adoption/update;
- `ENVIRONMENT_DEFAULT_ONLY` delegated-model policy;
- each tested environment's own configuration/runtime default where observable;
- local Codex behavior on selected machines where distribution is supported;
- ChatGPT Web Plugin routing/behavior where the Plugin is published/available;
- cross-context request/receipt flow, including Web <-> local, with model-config isolation verified.

Web/local are tested as real execution contexts with separate runtime/configuration authority, not as reusable task-purpose definitions and not as sources for each other's model settings.

Do not mutate reusable source inside installed acceptance. Reusable defects return to the remote source branch.

## K. Corrective strategy

If integrated acceptance finds defects:

1. group related findings sharing one authority/objective into a bounded corrective;
2. authorize/reconcile the corrective task purpose when mutation is required;
3. fix reusable source remotely;
4. obtain a new frozen semantic identity;
5. rerun affected acceptance scenarios plus required closure evidence;
6. avoid restarting unrelated scenarios merely because control-only records advanced.

## Final acceptance result

Only claim v0.6.0 integrated acceptance PASS when all required scenarios for the chosen release surfaces are PASS and required UNKNOWNs are resolved. An unobservable concrete platform model identity is not itself a required UNKNOWN if the acceptance claim is only that the platform default remained unoverridden and environment authority isolation passed.

This specification does not itself authorize merge/release.

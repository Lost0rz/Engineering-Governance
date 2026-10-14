# Engineering Governance v0.6.0 — Architecture Hardening

Status: ACTIVE DESIGN AUTHORITY for v0.6.0; amended by Task `EG-CAPABILITY-MODEL-POLICY-STABILIZATION-064`

Date: 2026-10-14

Parent architecture: `documents/engineering-governance-capability-model-v0.6.0.md`

## 1. Why the previous freeze was reopened

Task 062 completed and froze a coherent seven-Skill architecture. A subsequent Skill-by-Skill audit found that the architecture boundaries were sound but several operational semantics needed hardening around task purpose, Sub Agent orchestration, handoff, audit independence, and model behavior.

Task 063 established positive safe Sub Agent orchestration and explicit model-selection semantics. The user then chose a narrower operating policy for the initial stabilization period: keep Sub Agents actively usable, but have all delegated Sub Agents use the environment-configured default model and default reasoning setting. Stronger-model routing is deferred until explicitly re-enabled later.

The accepted correction remains narrow: keep the seven-Skill model, three-file control plane, evidence-first discipline, one-task authority semantics, and positive safe parallelism.

No eighth Skill is added.

## 2. Core distinction: task, execution unit, and execution context

### 2.1 Task

A task is an engineering-purpose and authorization boundary owned by `CURRENT_TASK.md`.

When useful for clarity, `CURRENT_TASK.md` may declare a lightweight `TASK_CLASS` such as:

- `DESIGN`
- `EXECUTION`
- `AUDIT`
- `VERIFY`
- `DIAGNOSIS`
- `CORRECTIVE`
- `CLOSEOUT`

`TASK_CLASS` is metadata inside the single active task authority. It is not a new control plane or a requirement to fragment every small workflow.

### 2.2 Execution unit

An execution unit is a bounded piece of work inside one task. A controller may assign many units to Sub Agents without creating new `CURRENT_TASK.md` authorities.

Typical same-task units include:

- independent research/scouting;
- code changes within the task's authorized scope;
- test implementation or focused verification;
- read-only review supporting the current execution;
- cross-context continuation of the same authorized work.

### 2.3 Execution context

An execution context is where/who performs work, for example:

- Web session;
- local Codex session;
- cloud agent;
- Sub Agent;
- independent reviewer context;
- another machine/session.

Execution context does not determine task purpose. `Web` and `Local` are deployment/context facts, not reusable Engineering Governance task classes.

## 3. Same task vs new/reconciled task

Keep the same task when the engineering objective and authorization remain materially unchanged, including:

- a handoff from Web to local executor to implement an already accepted plan;
- controller-to-Sub-Agent delegation inside the authorized implementation;
- continuation after compaction/session/machine change;
- implementation-local verification needed to establish the task's acceptance criteria.

Use a new task or explicit Project Governance reconciliation when the engineering purpose/authorization boundary materially changes, for example:

- design work becomes a separately authorized implementation objective;
- an independent acceptance audit is commissioned after implementation;
- audit findings create a distinct corrective objective;
- a material new design decision changes scope, side effects, interfaces, acceptance, or writer authority;
- final verification/closeout has a distinct acceptance authority that should not be conflated with the implementation task.

Do not create a new task merely because another agent, machine, or session continues the same work.

## 4. Positive Sub Agent orchestration

The orchestration goal is **effective throughput with controlled authority**, not minimum agent count.

### 4.1 Parallelism posture

Use available parallel capacity when all relevant work units are independent enough that concurrency improves throughput or context isolation without unsafe interference.

Prefer:

- parallel research/scouting for independent questions;
- parallel read-only review/verification for independent evidence domains;
- parallel disjoint writers when semantic write authorities/workspaces are proven disjoint and integration is defined.

Use sequential or inline execution when dependency edges, shared mutable state, writer overlap, or coordination cost make parallelism inefficient or unsafe.

### 4.2 Orchestration state

When material, the controller should establish:

```text
AVAILABLE_PARALLELISM
ACTIVE_UNITS
DEPENDENCY_GRAPH
WRITE_AUTHORITY_PER_UNIT
INTEGRATION_BOUNDARY
```

`AVAILABLE_PARALLELISM` is usable capacity, not a policy target to artificially suppress. Environment limits may cap concurrency, but governance should exploit safe available capacity when useful.

### 4.3 Cancellation and supersession

If new evidence makes an outstanding unit unnecessary, stale, or invalid, the controller may mark it `CANCELLED` or `SUPERSEDED` and should not integrate its stale result blindly.

## 5. Delegated model stabilization — Task 064 amendment

This section supersedes Task 063's earlier active HIGH-selection/escalation semantics for the current v0.6.0 stabilization period.

### 5.1 Active policy

All delegated Sub Agents use the execution environment's configured default Sub Agent model and default reasoning setting:

```text
SUBAGENT_MODEL_POLICY: DEFAULT_ONLY
SUBAGENT_MODEL: environment configured default
SUBAGENT_REASONING: environment configured default
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

The current user Codex convention may configure a default such as `gpt-6-luna` with `xhigh` reasoning effort. That mapping belongs to environment configuration, not portable reusable governance.

### 5.2 Model identity vs reasoning effort

Model identity and reasoning effort are separate dimensions.

A reasoning setting such as `xhigh` means the configured model is allowed to reason at that effort. It does **not** mean the Orchestrator selected a stronger/HIGH model tier.

### 5.3 Tier vocabulary is retained but inactive

`LOW`, `STANDARD`, and `HIGH` may remain useful future capability vocabulary. During `DEFAULT_ONLY` stabilization they do not drive delegated model routing.

Role complexity still affects decomposition, acceptance, review, and whether a task should return a capability gap. It does not automatically select a different Sub Agent model.

### 5.4 No stronger-model escalation during stabilization

Do not:

- automatically upgrade a difficult delegated unit;
- intentionally upgrade it because architecture/security/concurrency reasoning is harder;
- inherit a stronger controller/session model merely because it is available;
- silently substitute a stronger model if the configured Sub Agent default is unavailable.

If the configured default is insufficient, the unit returns a capability/model gap to the controller. Re-enabling stronger-model selection requires a later explicit user/project decision and corresponding governance update.

## 6. Context-neutral Agent Handoff

A handoff transports responsibility across contexts; it does not define engineering purpose.

For same-task continuation, the handoff should preserve the same `TASK_ID` and reference the same task/design authorities. When material, it may include:

```text
SOURCE_CONTEXT
TARGET_CONTEXT
AUTHORITY_OBSERVED_BASIS
```

The receiver rereads current authority. If the authority has advanced compatibly, continue under the current source of truth. If the change is materially incompatible with the handoff delta or action boundary, return to Project Governance for reconciliation.

A written/accepted solution is referenced, not re-derived from conversation history by every receiver.

Web/local naming belongs only in environment-specific examples or repository-specific deployment conventions. Reusable contracts should use context-neutral semantics.

## 7. Independent audit vs implementation verification

Implementation self-check/test evidence remains part of the active execution task unless a separate independent acceptance boundary is explicitly required.

Formal independent acceptance/audit should be modeled as its own engineering-purpose task when independence matters. A useful audit task declares its target/identity/required claims and does not inherit the implementer's conclusion as truth.

Audit independence may be described as:

- `SELF_CHECK` — not independent; implementation verification only;
- `FRESH_CONTEXT` — independent context without implementation reasoning history;
- `SEPARATE_AGENT` — separate reviewer/agent;
- `HUMAN` — human independent review/acceptance.

The required level is chosen by risk/task/user requirements. Merely invoking `evidence-audit` inside the implementer's flow does not automatically make a review independent.

## 8. Evidence-audit disposition hardening

Keep severity and boundary disposition distinct.

- `BLOCKING` -> `STOP`.
- `IMPORTANT` -> `STOP` when correction is required before the requested boundary; otherwise it may be explicitly accepted/deferred as follow-up by the responsible authority.
- `MINOR` -> may remain under `PASS_WITH_FOLLOWUPS`.
- required `UNKNOWN` -> `STOP`.

For material acceptance, the audit should identify:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

A required claim without adequate evidence remains `UNKNOWN`.

## 9. Work packages

### WP11 — Task purpose and lifecycle semantics

- add task-class metadata guidance;
- define same-task vs new/reconciled-task rules;
- separate task purpose from execution context and Sub Agent units.

### WP12 — Positive orchestration

- revise orchestrator posture from agent minimization to safe effective parallelism;
- add available-parallelism/dependency/cancellation semantics.

### WP13 — Context-neutral handoff and independent audit

- add context-neutral source/target continuation semantics;
- add authority-observation basis handling;
- distinguish implementation verification from formal independent audit task;
- harden audit independence and severity/disposition semantics.

### WP14 — Acceptance specification alignment

- require useful positive Sub Agent behavior where safe;
- test same-task cross-context continuation;
- test separate audit-purpose task and non-independent self-check distinction.

### WP15 — Model-policy stabilization (Task 064)

- set delegated policy to `DEFAULT_ONLY`;
- use environment-configured default Sub Agent model and reasoning effort;
- distinguish `xhigh` reasoning from stronger-model selection;
- disable automatic and intentional stronger-model escalation during stabilization;
- retain LOW/STANDARD/HIGH only as inactive future vocabulary;
- update integrated acceptance accordingly.

## 10. Acceptance sequencing

Task 064 changes reusable model-policy semantics, so the Task 063 semantic freeze becomes historical for final v0.6.0 acceptance. The sequence is:

1. implement WP15 model-policy correction;
2. run one remote source-architecture audit;
3. freeze a new v0.6.0 Architecture Delivery / Semantic HEAD;
4. run one consolidated installed Plugin/Web/Codex acceptance pass against the new frozen identity;
5. return reusable-source defects to remote source corrective work;
6. only after acceptance consider merge/release preparation.

Do not test one Skill at a time during this stabilization task.

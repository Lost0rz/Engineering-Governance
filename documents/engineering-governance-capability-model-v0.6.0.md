# Engineering Governance Capability Model v0.6.0

Status: ACTIVE DESIGN AUTHORITY for v0.6.0; current model-authority amendment `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065`

Date: 2026-10-14

Related hardening authority: `documents/engineering-governance-capability-hardening-v0.6.0.md`

## 1. Purpose

Engineering Governance v0.6.0 expands the reusable capability model from three top-level Skills to seven while preserving the existing three-file project control plane and a lightweight business-first default.

The goal is not to reproduce Superpowers or another agent framework. It is to keep one project authority model while adding narrowly triggered capabilities for design, execution orchestration, cross-context handoff, independent evidence audit, navigation, and evidence-gated diagnosis.

The seven top-level Skills are:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing is policy, not an eighth Skill.

## 2. Authority model

The three project controls keep distinct ownership:

- `AGENTS.md` — durable repository/project operating rules and stable boundaries;
- `CURRENT_STATUS.md` — concise verified current-state snapshot;
- `CURRENT_TASK.md` — the single active execution authorization.

Durable planning/design may own long-lived rationale, constraints, and work-package structure, but it is not a fourth control file and does not authorize execution.

A Skill, design result, handoff request/receipt, Sub Agent brief, execution ledger, audit report, reviewer finding, CI result, runtime observation, or probe result does not become a competing task/status/control authority merely because it exists.

## 3. Task, execution unit, and execution context

Keep three concepts separate:

- **Task** — one engineering objective/authorization owned by `CURRENT_TASK.md`; optional `TASK_CLASS` may describe DESIGN / EXECUTION / AUDIT / VERIFY / DIAGNOSIS / CORRECTIVE / CLOSEOUT.
- **Execution unit** — bounded work inside the active task, potentially delegated to a Sub Agent.
- **Execution context** — Web, local Codex, cloud agent, Sub Agent, reviewer, machine, or session where work occurs.

Changing context does not create a new task by itself. Same-purpose work can continue across contexts and Sub Agent units under one `TASK_ID`.

Execution context also owns its runtime-specific configuration unless a project explicitly defines a portable configuration artifact. A local runtime configuration is local truth; a managed Web/cloud runtime default is truth for that managed execution context.

Use Project Governance reconciliation or a distinct task when engineering purpose/authorization materially changes, such as a separately commissioned independent audit, a distinct corrective objective, or a new design decision that changes scope/interfaces/side effects/writer authority.

## 4. Capability ownership

| Skill | Trigger | Owns | Must return / not own |
| --- | --- | --- | --- |
| `project-governance` | normal project/repository engineering work | control plane, task purpose/scope/authorization, workspace/writer lifecycle, verification tier/cadence, composition, closeout | governing flow; does not absorb specialist procedures |
| `solution-design` | material intent/architecture/state-ownership ambiguity or durable design decision | design question, constraints, options/tradeoffs, accepted design, convergence | returns accepted design/reconciliation need; never authorizes implementation |
| `execution-orchestrator` | authorized work benefits from decomposition, agents, parallelism, delegated-model policy, recovery, or controlled integration | execution topology, role/write boundaries, sequencing, delegated-model policy, recovery ledger, integration checkpoints | does not expand task scope or independently declare acceptance |
| `agent-handoff` | responsibility crosses agent/session/machine/context | bounded request envelope and structured receipt | transports task/authority references + fresh delta; never becomes authority or runtime-config authority |
| `evidence-audit` | explicit or independent implementation/PR/CI/release/readiness verdict is needed | audit identity/range, required claims, evidence evaluation, independence basis, findings/disposition/verdict | read-only by default; does not authorize fixes |
| `domain-navigation` | semantic/source/test/runtime route is unclear | bounded evidence-backed route discovery | returns verified route/gap; does not own task or diagnosis |
| `incident-doctor` | real failure/unsafe ambiguity blocks progress and current evidence is insufficient | diagnosis, hypotheses, probes, evidence-supported fix boundary | returns evidence/fix boundary; known bugs with sufficient evidence do not enter Doctor |

## 5. External project influence — adopt / adapt / reject

External repositories are conceptual references, never hidden runtime dependencies.

### Superpowers

Adopt/adapt: distinct process skills, decision-vs-assumption separation, narrow delegated briefs, resumable execution state, independent review, useful Sub Agent parallelism, systematic diagnosis techniques.

Reject: universal brainstorming, universal mandatory TDD, every-bug debugging route, unconditional Sub Agent/reviewer dispatch, mandatory worktrees, silent model inheritance/escalation, duplicate progress/control authority.

### GitHub Spec Kit

Adopt/adapt: separate intent/design from implementation mechanics; conditional clarification/checklist/convergence; preserve decisions future execution cannot safely reconstruct.

Reject: mandatory artifact chains for every small task or any task file competing with `CURRENT_TASK.md`.

### OpenAI Agents SDK / Microsoft Agent Framework / LangGraph supervisor patterns

Adopt/adapt: manager/orchestrator and handoff are different concerns; context transfer should be filtered; central coordination is preferred where one authority must control writers and integration; safe concurrency is useful execution capacity.

### OpenHands / SWE-agent / mini-SWE-agent

Adopt/adapt: bounded workspace/context; purpose-built context over raw history dumping; successful no-change/no-output remains explicit; orchestration complexity is not value by itself.

### Kubernetes KEP / Backstage

Adopt/adapt: durable design/lifecycle/acceptance boundaries and the distinction between descriptive metadata/participation and ultimate ownership/authority.

### reviewdog / OpenSSF Scorecard / SLSA

Adopt/adapt: findings bind to an explicit diff/identity; evidence sources and unknown/inconclusive states are first-class; required claims must be covered; provenance matters only when checked against expectations; semantic evidence and live host gates are different claims.

## 6. End-to-end governed lifecycle

The default governed route is:

```text
request
-> project-governance
-> solution-design?        material design ambiguity only
-> project-governance      reconcile/authorize resulting engineering purpose
-> domain-navigation?      unclear semantic/source/test/runtime route only
-> execution-orchestrator? useful decomposition/parallelism/delegated-model/recovery policy
-> agent-handoff?          responsibility crosses contexts; same task when purpose unchanged
-> authorized implementation / verification
-> incident-doctor?        blocking evidence gap only
-> evidence-audit?         explicit/independent acceptance-readiness boundary only
-> live host gates?        when repository host governs the requested boundary
-> project-governance      control alignment / lifecycle closeout
-> agent-handoff?          return result across contexts
```

Question marks are real gates: do not invoke a capability solely because it exists. Conversely, do not suppress useful safe Sub Agent parallelism merely for conservatism.

No narrower Skill silently keeps task authority after its bounded output is produced.

## 7. Solution Design and durable planning

Solution Design answers a material design question; durable planning stores accepted long-lived decisions only when future tasks need them.

A design result distinguishes:

- verified facts/constraints;
- user/project decisions;
- agent assumptions;
- agent implementation calls;
- unresolved decisions.

Use goals/non-goals/anti-goals when material. Use a spike only when its result can change the decision. Before execution, run convergence against the authorized objective and existing semantic authorities.

If accepted design changes task scope, prerequisites, allowed side effects, verification, dependencies, acceptance, or STOP conditions, Project Governance reconciles/re-authorizes `CURRENT_TASK.md` before affected implementation.

A written accepted solution is referenced by later execution; each executor does not re-derive it from chat history.

## 8. Execution Orchestrator architecture

### 8.1 Positive topology selection

Choose topology from dependency, authority, throughput, and integration needs rather than from a bias toward minimum agent count:

1. **INLINE** — one executor when decomposition has little benefit or shared/dependent state dominates;
2. **SEQUENTIAL_DELEGATED** — delegated units executed one at a time when context separation helps but dependencies prevent useful concurrency;
3. **PARALLEL_READ_ONLY** — independent scouts/researchers/reviewers/verifiers with no shared mutation;
4. **PARALLEL_DISJOINT_WRITERS** — independent writers only when semantic write authority/workspaces are proven disjoint and integration evidence is defined before dispatch.

When independent work exists and available parallelism materially improves wall-clock time or context isolation, use that capacity. Branch/worktree separation alone does not prove semantic independence.

When material, track:

```text
AVAILABLE_PARALLELISM
ACTIVE_UNITS
DEPENDENCY_GRAPH
WRITE_AUTHORITY_PER_UNIT
INTEGRATION_BOUNDARY
```

Units may become `CANCELLED` or `SUPERSEDED` when later evidence invalidates their premise; stale results are not integrated blindly.

### 8.2 Role classes

- Controller — sequencing/integration owner under the active task.
- Implementer — bounded writer.
- Scout/researcher — read-only discovery.
- Reviewer/auditor — read-only evaluation unless separately re-authorized.
- Probe/verifier — bounded observation/test role; diagnostic writes require explicit authorization.

A role name never grants write permission by itself.

### 8.3 Delegated-model stabilization policy

Task 065 establishes the current v0.6.0 delegated Sub Agent authority model:

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
SUBAGENT_MODEL_SOURCE: current execution environment authoritative Sub Agent configuration/runtime default
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

Reusable governance does not define a concrete provider, model, or reasoning setting. The execution environment that actually runs the Sub Agent owns those values.

Resolution rules:

1. if the current execution environment exposes authoritative Sub Agent configuration, use it;
2. if the platform/runtime manages its default internally, allow that default to apply without an explicit override;
3. if exact model/reasoning identity is not observable, keep it `PLATFORM_DEFAULT` / `UNKNOWN` rather than infer a value;
4. do not import concrete model/reasoning values from another machine, session, Web/local context, repository document, memory, or controller model;
5. after cross-context handoff, the receiver resolves its own runtime/configuration authority again.

Model identity and reasoning configuration are separate runtime evidence fields. Neither implies the other.

`LOW / STANDARD / HIGH` remain only future portable capability vocabulary while `ENVIRONMENT_DEFAULT_ONLY` is active. They do not route delegated Sub Agents during stabilization.

Do not downgrade or upgrade a delegated unit based on role complexity; do not inherit a different controller/session model merely because it is available; do not automatically or intentionally escalate a difficult Sub Agent to a stronger model.

If the current environment default is unavailable or materially insufficient, return a capability/environment gap to the controller. Re-enabling tier-based or stronger-model routing requires a later explicit user/project policy change and corresponding governance update.

### 8.4 Review gates

Review cadence follows risk and required independence, not agent count:

- V0/V1: independent review only when task/user/risk justifies it;
- V2: independent audit is normally useful at the integrated task/PR boundary, not after every unit;
- V3: require explicit independent evidence/review appropriate to the high-consequence claim.

Implementation self-check is verification, not automatically independent acceptance.

### 8.5 Recovery ledger

Use an ephemeral ledger only when context loss/restart is a realistic risk. It may record task/design identity, unit state, concrete result identity, verification evidence, controller rulings, unresolved dependencies/conflicts, and next resume point.

It never replaces `CURRENT_STATUS.md`, `CURRENT_TASK.md`, durable planning, or Git history and should be retired at terminal closeout unless a bounded fact is deliberately promoted into an existing authority.

## 9. Agent Handoff architecture

Core rule:

`HANDOFF = TASK/AUTHORITY REFERENCES + FRESH DELTA + ACTION BOUNDARY + RETURN CONTRACT`

Useful semantic fields:

- `HANDOFF_ID`
- `TASK_ID`
- `MODE`
- `TARGET`
- `AUTHORITY`
- `AUTHORITY_OBSERVED_BASIS` when freshness matters
- `SOURCE_CONTEXT` / `TARGET_CONTEXT` when useful
- `DELTA`
- `BOUNDARY`
- `RETURN_CONTRACT`

For same-purpose continuation, preserve the same `TASK_ID`. The receiver rereads current authority; compatible advance may continue, material conflict returns to Project Governance, and unavailable required authority produces STOP rather than reconstruction from stale chat/memory.

Web/local/cloud/Sub Agent/reviewer/session/machine are context labels, not task-purpose definitions and not each other's runtime-config authority.

Under `ENVIRONMENT_DEFAULT_ONLY`, handoff may carry the policy but never a concrete sender-specific Sub Agent model/reasoning value as the receiver's default. The receiver resolves its own environment configuration/runtime default. Unobservable exact values remain `PLATFORM_DEFAULT` / `UNKNOWN`.

Do not copy whole controls, plans, Domain maps, secrets, unrelated personal data, sender-specific runtime model settings, or generic Engineering Governance procedure into handoff cards by default.

Modes:

- `EXECUTE` — authorized mutation in another context;
- `AUDIT` — strict read-only evidence verdict under an authorized audit purpose;
- `DIAGNOSE` — bounded diagnostic evidence/question transfer under existing authorization;
- `REVIEW` — read-only evaluation of specified work product;
- `VERIFY` — confirm a named claim/identity/check.

## 10. Evidence Audit architecture

Audit profiles:

- `CODE_DIFF`
- `PR_MERGE`
- `CI`
- `RELEASE_PROVENANCE`
- `POST_CHANGE`

When formal independence matters, report:

```text
AUDIT_INDEPENDENCE: SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN
```

`SELF_CHECK` is useful implementation verification but is not independent acceptance.

Before verdict, bind target/range/identity, authority/requirements, evidence freshness, literal host identity where relevant, and required claim coverage:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

Severity and requested-boundary disposition are distinct:

- `BLOCKING` -> STOP;
- `IMPORTANT` -> STOP when correction is required before the requested boundary; otherwise follow-up only when responsible authority explicitly accepts/defer it;
- `MINOR` -> may coexist with `PASS_WITH_FOLLOWUPS`;
- required `UNKNOWN` -> STOP.

Verdicts are `PASS`, `PASS_WITH_FOLLOWUPS`, or `STOP` and state the exact boundary covered. CODE_DIFF PASS does not imply PR_MERGE PASS; source audit does not imply installed-runtime acceptance.

Reviewer findings are claims to verify, not corrective authority.

## 11. Domain Navigation and Incident Doctor

Domain Navigation remains conditional, bounded, evidence-backed route discovery. Search/Repo Map results are leads; focused source reading verifies the route. It does not authorize tasks, decide product/business questions, diagnose incidents, or mutate product code.

Incident Doctor remains evidence-gated and enters only when all three hold:

1. real failure/unexplained unsafe ambiguity exists;
2. it blocks safe progress;
3. current evidence is insufficient for the next safe decision.

Doctor names one missing fact and blocked decision before adding any probe. Diagnosis does not itself authorize a behavior change.

## 12. Artifact authority taxonomy

### Durable authorities

- applicable `AGENTS.md`;
- `CURRENT_STATUS.md` for current snapshot facts;
- `CURRENT_TASK.md` for active authorization;
- accepted product/domain/data/runtime authorities;
- accepted durable planning/design authority when justified;
- Git/repository host/runtime systems for facts they own.

### Evidence / transport artifacts

Handoff requests/receipts, Sub Agent briefs, recovery ledgers, audit reports, review findings, CI/test outputs, runtime observations, and probe results are not project controls by default.

They may carry fresh evidence but cannot silently expand scope or replace an authority. When evidence conflicts with the source that owns the semantic class, re-verify freshness and reconcile through Project Governance.

Environment-specific runtime configuration evidence remains evidence about that environment. It is not promoted into reusable Plugin authority or another context's runtime configuration by being included in a receipt.

## 13. Skill Engineering quality contract

This is repository-maintainer guidance, not an eighth Skill.

Every top-level Skill has:

1. a distinct semantic trigger;
2. one primary ownership boundary;
3. an explicit return/output contract;
4. negative/near-miss guidance preventing routine overuse;
5. positive guidance preventing material capability under-use where policy permits;
6. progressive disclosure;
7. no hidden task/control authority.

Over-triggering is a defect. Material under-use of safe Sub Agent parallelism can also be a defect. A deliberate environment/project capability restriction is not under-use; during `ENVIRONMENT_DEFAULT_ONLY`, stronger-model non-use and cross-context model isolation are intentional policy.

## 14. Work packages and amendments

### Task 061 — foundation

- WP1 — seven-Skill skeleton/source authority.
- WP2 — global routing/adoption and Project Governance outer composition.
- WP3 — initial handoff/execution contracts.
- WP4 — initial evidence-audit contract.
- WP5 — repository integration and Draft PR.

### Task 062 — architecture completion

- WP6 — central capability-composition and lifecycle integration.
- WP7 — execution/writer/recovery/handoff contract completion.
- WP8 — evidence-audit/artifact-authority/design-planning integration.
- WP9 — Skill Engineering quality contract.
- WP10 — integrated acceptance specification.

### Task 063 — architecture hardening

- WP11 — task purpose / execution unit / execution context separation.
- WP12 — positive safe Sub Agent orchestration and cancellation/supersession.
- WP13 — context-neutral handoff and independent audit hardening.
- WP14 — acceptance/maintainer alignment.

### Task 064 — model-policy stabilization

- WP15 — disable automatic and intentional stronger-model escalation during stabilization;
- retain LOW/STANDARD/HIGH only as inactive future vocabulary.

### Task 065 — environment model authority

- WP16 — delegated policy `ENVIRONMENT_DEFAULT_ONLY`;
- concrete model/reasoning authority belongs to the current execution environment;
- remove concrete Local model/reasoning examples from reusable source;
- prohibit cross-context propagation of concrete model/reasoning defaults;
- keep unobservable platform defaults `PLATFORM_DEFAULT` / `UNKNOWN`;
- update integrated acceptance accordingly.

## 15. Integrated acceptance contract

The authoritative consolidated matrix is `references/V060_INTEGRATED_ACCEPTANCE.md`.

It must exercise, at minimum:

- exact seven-Skill discovery and normal Project Governance entry;
- positive and negative/near-miss routing;
- same-task continuation across contexts and Sub Agent units;
- useful safe parallel Sub Agent execution;
- `ENVIRONMENT_DEFAULT_ONLY` delegated-model behavior;
- each execution environment resolving its own authoritative config/runtime default;
- no concrete model/reasoning propagation from Local to Web/cloud or the reverse;
- unobservable managed-platform defaults remaining `PLATFORM_DEFAULT` / `UNKNOWN` without override or guesswork;
- no stronger-model inheritance or escalation during stabilization;
- handoff authority freshness/conflict/unavailable behavior;
- independent audit classification and required-claim coverage;
- severity/disposition mapping;
- control/planning authority boundaries;
- CI/PR/release/post-change identity evidence;
- Domain Navigation and Incident Doctor boundaries;
- installed Plugin/global-routing/Web/Codex environment behavior for selected release surfaces.

Run this as one consolidated post-freeze acceptance pass, not one Skill at a time.

If acceptance finds a reusable-source defect, fix source remotely, freeze a new semantic identity, rerun affected integrated scenarios plus required closure evidence, and do not patch reusable source inside installed Plugin caches.

## 16. Deferred beyond v0.6.0 architecture stabilization

- tier-based or stronger-model delegated routing until explicitly re-authorized;
- generic automatic model-router executable;
- actual installed Plugin/Web/Codex acceptance until the source freeze is complete;
- v0.6.0 release workflow/tag/assets/publication;
- daemon/scheduler/database/enforcement runtime;
- persistent fourth project-control file;
- broad migration of historical `docs/superpowers/**` material;
- automatic conversion of historical project execution cards.

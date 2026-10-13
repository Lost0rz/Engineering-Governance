# Engineering Governance Capability Model v0.6.0

Status: ACTIVE DESIGN AUTHORITY for v0.6.0; current implementation task `EG-CAPABILITY-ARCHITECTURE-COMPLETION-062`

Date: 2026-10-14

## 1. Purpose

Engineering Governance v0.6.0 expands the reusable capability model from three top-level Skills to seven while preserving the existing three-file project control plane and a lightweight business-first default.

The goal is not to reproduce Superpowers or another agent framework. It is to keep one project authority model while adding narrowly triggered capabilities for design, execution orchestration, cross-context handoff, and independent evidence audit.

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

The three project controls keep their existing ownership:

- `AGENTS.md` — durable repository/project operating rules and stable boundaries;
- `CURRENT_STATUS.md` — concise verified current-state snapshot;
- `CURRENT_TASK.md` — the single active execution authorization.

A Skill, durable plan, design record, handoff request, handoff receipt, execution ledger, audit report, reviewer finding, CI result, or subagent brief does not become a competing task/status/control authority merely because it exists.

Durable planning may own long-lived design/rationale/work-package structure, but it is not a fourth control file and does not authorize execution. Ephemeral execution state is not durable project authority.

## 3. Capability ownership

| Skill | Trigger | Owns | Must return / not own |
| --- | --- | --- | --- |
| `project-governance` | normal project/repository engineering work | control plane, scope/authorization, task/workspace/writer lifecycle, verification tier/cadence, composition, closeout | remains the governing flow; does not absorb specialist procedures |
| `solution-design` | material intent/architecture/ownership ambiguity or durable cross-task design | design question, constraints, options/tradeoffs, accepted design, convergence | returns accepted design/reconciliation need; never authorizes implementation |
| `execution-orchestrator` | authorized work needs decomposition, agents, parallelism, model policy, recovery or controlled integration | execution topology, role/write boundaries, sequencing, model tier, recovery ledger, integration checkpoints | does not expand task scope or independently declare merge readiness |
| `agent-handoff` | responsibility crosses agent/session/machine/context | request envelope and structured receipt | transports authority references + fresh delta; never becomes authority |
| `evidence-audit` | independent implementation/PR/CI/release/readiness verdict is needed | audit identity/range, evidence evaluation, severity, unknowns, verdict | read-only by default; does not authorize fixes |
| `domain-navigation` | responsible semantic/source/test/runtime route is unclear | bounded evidence-backed route discovery | returns route/gap; does not own task or diagnosis |
| `incident-doctor` | real failure/unsafe ambiguity blocks progress and current evidence is insufficient | diagnosis, hypotheses, probes, evidence-supported fix boundary | returns evidence/fix boundary; normal bugs with sufficient evidence do not enter Doctor |

## 4. External project audit — adopt / adapt / reject

External repositories remain conceptual references, never hidden runtime dependencies.

### Superpowers

Adopt/adapt: distinct process skills, decision-vs-assumption separation, narrow subagent briefs, resumable execution ledger, independent review, explicit model selection, parallelism only for independent work, systematic diagnosis techniques.

Reject: universal brainstorming, universal mandatory TDD, every-bug debugging route, unconditional subagent/reviewer per task, mandatory worktrees, silent inheritance of expensive models, duplicate progress/control authority.

### GitHub Spec Kit

Adopt/adapt: separate intent/design from implementation mechanics; conditional clarify/checklist/convergence gates; plans should preserve decisions that an executor cannot safely reconstruct.

Reject: mandatory artifact chains for every small task or any task file competing with `CURRENT_TASK.md`.

### OpenAI Agents SDK / LangGraph supervisor patterns

Adopt/adapt: manager/orchestrator and handoff are different concerns; transferred context should be filtered; central coordination is preferred when one authority must control writers and integration.

### OpenHands / SWE-agent

Adopt/adapt: bounded workspace/context state; purpose-built context is preferable to raw history/repository dumping; successful no-change/no-output results must still be explicit.

### reviewdog / OpenSSF Scorecard / SLSA

Adopt/adapt: findings bind to an explicit diff/identity; evidence sources and unknown/inconclusive states are first-class; provenance is useful only when checked against explicit expectations; semantic evidence and live host gates are different claims.

## 5. End-to-end governed lifecycle

The complete default lifecycle is:

```text
request
-> project-governance: establish/verify authorization and baseline
-> solution-design?        only if material design ambiguity exists
-> project-governance: reconcile task if design changes authorization
-> domain-navigation?      only if authority/source/test route is unclear
-> execution-orchestrator? only if execution topology needs policy
-> agent-handoff?          whenever responsibility crosses contexts
-> implementation / bounded diagnosis as authorized
-> verification            proportional V0-V3 evidence
-> evidence-audit?         when an independent acceptance/readiness verdict is required
-> live repository-host gates when applicable
-> project-governance: control alignment / lifecycle closeout
-> agent-handoff receipt?  when the result returns across contexts
```

`incident-doctor` may interrupt the normal execution path only when a blocking evidence gap meets its trigger, and returns to Project Governance for authorization before any out-of-scope behavior change.

No narrower Skill silently keeps ownership after its bounded output is produced.

## 6. Artifact authority taxonomy

### Durable authorities

- project controls: `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`;
- accepted product/domain/data/runtime authorities owned by the target project;
- accepted durable planning/design authority when justified;
- Git/source history for repository facts.

### Evidence / transport artifacts — not authority by default

- handoff request;
- handoff receipt;
- execution/subagent brief;
- recovery ledger;
- audit report/reviewer finding;
- CI/test result;
- runtime observation/probe result;
- PR/mergeability/review state observation.

These artifacts can cite or summarize authority and may supply fresh evidence, but they do not independently expand scope or redefine project truth.

### Conflict rule

When an evidence/transport artifact conflicts with the source that owns that semantic class, do not let the artifact silently win. Re-verify freshness and reconcile through Project Governance. A newer explicit user instruction may require task reconciliation, not handoff override.

## 7. Solution Design and durable planning

Solution Design answers a material design question; durable planning stores accepted long-lived decisions only when future tasks need them.

A design result must distinguish:

- verified facts/constraints;
- user/project decisions;
- agent assumptions;
- agent-made implementation calls;
- unresolved decisions.

Use goals/non-goals/anti-goals when they constrain the solution. Use a spike only when its outcome can change the decision. Before returning to execution, run a convergence check against the authorized objective and existing semantic authorities.

If the accepted design changes task scope, prerequisites, allowed side effects, verification, dependencies or STOP conditions, Project Governance must reconcile/re-authorize `CURRENT_TASK.md` before affected implementation.

## 8. Execution Orchestrator architecture

### 8.1 Default topology

The lightest safe topology wins:

1. one inline executor when sufficient;
2. one controller + sequential delegated implementers when context separation helps;
3. parallel read-only scouts/reviewers when questions are independent;
4. parallel writers only for proven-disjoint semantic write authority and workspaces plus a defined integration check.

Branch/worktree separation alone does not prove semantic independence.

### 8.2 Role classes

- Controller — sequencing/integration owner under the active task.
- Implementer — bounded writer.
- Scout/researcher — read-only discovery.
- Reviewer/auditor — independent read-only evaluation unless separately re-authorized.
- Probe/verifier — bounded observation/test role; diagnostic writes require explicit authorization.

### 8.3 Model capability tiers

Use capability tiers rather than hardcoding one provider/model name:

- `LOW` — mechanical/bounded lookup, extraction, formatting, simple deterministic edits when reliable;
- `STANDARD` — normal implementation, multi-file pattern application, ordinary code review;
- `HIGH` — architecture, subtle integration/concurrency/security reasoning, difficult diagnosis, high-risk final review when justified.

Policy:

- choose the lowest tier that reliably satisfies the role;
- record an explicit maximum when cost/capability limits matter;
- fallback may stay within the allowed tier band;
- **no silent escalation** to a materially higher tier;
- do not inherit the controller/session model automatically when the delegated role has a lower justified tier;
- if the requested tier is unavailable and no allowed fallback exists, surface the mismatch instead of silently upgrading.

### 8.4 Review gates

Do not require reviewer-per-task ceremony.

- V0/V1: independent review only when task risk or user request justifies it.
- V2: independent review/audit is normally appropriate at the integrated task/PR boundary, not necessarily after each work unit.
- V3: require explicit independent evidence/review appropriate to the high-consequence claim.

### 8.5 Recovery ledger

Use an ephemeral ledger only when context loss/resume is a real risk. It may contain work-unit state, concrete result identity, verification, rulings/deviations, and resume point. It must never become a fourth control file and should be retired at terminal closeout unless the project explicitly promotes part of it into an existing durable authority.

## 9. Agent Handoff architecture

Core rule:

`HANDOFF = AUTHORITY REFERENCES + FRESH DELTA + ACTION BOUNDARY + RETURN CONTRACT`

Required semantic fields:

- `HANDOFF_ID`
- `MODE`
- `TARGET`
- `AUTHORITY`
- `DELTA`
- `BOUNDARY`
- `RETURN_CONTRACT`

Do not copy whole controls, plans, Domain maps or generic Engineering Governance procedure by default. Use bounded quoted snapshots only when the receiver cannot access the authority or exact text is required.

### Mode profiles

- `EXECUTE` — target authorized mutation; return identity, changed paths, verification, lifecycle/control alignment.
- `AUDIT` — strict read-only independent verdict; return identity/range, findings, unknowns, verdict, no control mutation.
- `DIAGNOSE` — bounded evidence question/hypothesis/probe boundary; return evidence and fix boundary, not an unauthorized fix.
- `REVIEW` — read-only evaluation of specified work product; return findings and evidence, not implementation thought history.
- `VERIFY` — confirm a named claim/identity/check; return exact observation and what it proves, including explicit no-change/no-output success.

A handoff should be self-contained enough to act without reconstructing chat history but small enough that authority remains in its owning sources.

## 10. Evidence Audit architecture

Audit profiles:

- `CODE_DIFF` — requirement vs changed paths/source behavior;
- `PR_MERGE` — semantic evidence + current PR host gates + merge readiness;
- `CI` — workflow/run/job identity, expected source/ref/head, actual result and coverage;
- `RELEASE_PROVENANCE` — source/tag/artifact/builder/hash/provenance expectations;
- `POST_CHANGE` — delivered/merged/runtime identity vs the claim being verified.

Every verdict first binds:

- target repository/artifact/runtime;
- base/head/range or immutable artifact identity;
- requirements/task/design authority;
- evidence freshness;
- literal host identity when live host gates matter.

Findings use `BLOCKING`, `IMPORTANT`, `MINOR`, `UNKNOWN`. Verdict uses `PASS`, `PASS_WITH_FOLLOWUPS`, or `STOP`.

`UNKNOWN` is not silently converted to PASS or FAIL. Reviewer suggestions remain claims to verify, not automatic mutation instructions. Corrective work returns to Project Governance authorization.

## 11. Project Governance composition contract

Project Governance owns entry, re-entry and closeout. A narrower Skill can call another narrower Skill only for a bounded dependency and then returns to its caller.

Allowed common compositions include:

- `project-governance -> solution-design -> project-governance`;
- `project-governance -> domain-navigation -> project-governance`;
- `project-governance -> execution-orchestrator -> agent-handoff -> executor -> ... -> project-governance`;
- `project-governance -> evidence-audit -> project-governance`;
- `project-governance -> incident-doctor -> domain-navigation -> incident-doctor -> project-governance`;
- `evidence-audit -> agent-handoff` only when the audit itself crosses contexts;
- `execution-orchestrator -> agent-handoff` for delegated work.

Do not create uncontrolled recursive routing, a peer mesh of writers, or an implicit second controller.

## 12. Skill Engineering quality contract

This is repository-maintainer guidance, not an eighth Skill.

Every top-level Skill must have:

1. a distinct trigger;
2. one primary ownership boundary;
3. an explicit return/output contract;
4. negative trigger guidance to prevent overuse;
5. progressive disclosure — concise `SKILL.md`, details in references/assets;
6. no hidden task/control authority;
7. no assumption that a Skill should trigger merely because it is installed.

Frontmatter descriptions should primarily describe **when to use** the Skill rather than summarizing its entire workflow. Route quality must include both positive and negative scenarios; over-triggering is a defect.

## 13. Work packages

### Foundation completed in Task 061

- WP1 — seven-Skill skeleton and source authority.
- WP2 — global routing/adoption and Project Governance outer composition.
- WP3 — initial handoff/execution contracts.
- WP4 — initial evidence-audit contract.
- WP5 — repository integration and draft PR.

### Architecture completion — Task 062

- WP6 — central capability-composition contract and internal Project Governance lifecycle integration.
- WP7 — execution/model/writer/recovery and handoff mode-profile completion.
- WP8 — evidence-audit profiles, artifact-authority taxonomy, Solution Design/planning convergence.
- WP9 — Skill Engineering quality contract and trigger/over-trigger rules.
- WP10 — integrated acceptance matrix/specification; define now, execute only after architecture freeze.

## 14. Integrated acceptance matrix — specification only

The architecture must be frozen before this matrix is executed.

### Positive routing scenarios

1. clear small repository edit -> Project Governance only;
2. material ambiguous architecture choice -> Solution Design, then return/reconcile;
3. complex authorized multi-agent execution -> Execution Orchestrator;
4. Web/local transfer -> Agent Handoff request + receipt;
5. independent PR/CI/merge audit -> Evidence Audit;
6. unclear Domain/source/test route -> Domain Navigation;
7. blocking unexplained failure with evidence gap -> Incident Doctor.

### Negative / over-trigger scenarios

1. clear edit must not trigger Solution Design merely because it is a feature;
2. one-executor task must not spawn subagents merely because orchestration exists;
3. ordinary bug with sufficient evidence must not enter Incident Doctor;
4. no transfer means Agent Handoff is unnecessary;
5. implementation self-check does not automatically become independent Evidence Audit;
6. no Skill may replace/override `CURRENT_TASK.md` authority.

### Composition scenarios

- Solution Design -> task reconciliation -> execution;
- Execution Orchestrator -> Agent Handoff -> local executor -> compact receipt -> Project Governance;
- Evidence Audit -> STOP finding -> Project Governance corrective authorization -> re-audit;
- Incident Doctor -> Domain Navigation -> Doctor -> Project Governance;
- control-only drift after semantic freeze -> semantic evidence reuse where allowed + live host gate reread.

### Safety/economy scenarios

- lower-tier delegated role does not silently inherit HIGH model;
- unavailable low/standard model does not silently escalate outside allowed fallback;
- parallel readers may coexist;
- overlapping writers are rejected unless proven disjoint;
- handoff card does not copy full task/status/governance rules;
- no-change/no-output success is explicit in receipt;
- missing CI status is `UNKNOWN/none`, not `PASS`.

### Acceptance sequencing

1. finish WP6-WP10 source architecture;
2. run one final remote source-architecture audit;
3. freeze Delivery / Semantic HEAD;
4. run one consolidated installed Plugin/Web/Codex acceptance matrix against the frozen architecture;
5. group related defects into bounded corrective work;
6. rerun only the affected integrated scenarios plus final required closure evidence;
7. only then consider PR merge and v0.6.0 release publication.

Do **not** use `build one Skill -> installed acceptance -> build next Skill` as the v0.6.0 sequence.

## 15. Deferred beyond architecture completion

- actual installed Plugin/Web/Codex acceptance execution;
- v0.6.0 release workflow/tag/assets/publication;
- generic automatic model router executable;
- daemon/scheduler/database/enforcement runtime;
- persistent fourth project-control file;
- broad migration of historical `docs/superpowers/**` material;
- automatic conversion of historical project execution cards.

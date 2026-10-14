# Capability composition

This contract defines how the seven Engineering Governance Skills cooperate without creating competing controllers or authorities.

## Ownership rule

`project-governance` owns entry, task/control authorization, task-purpose semantics, re-entry after specialist work, workspace/writer lifecycle, verification-tier selection, and final closeout.

A narrower Skill owns only its bounded capability. Once it produces its result, ownership returns to its caller unless a higher-priority instruction explicitly selected that Skill as the direct bounded route.

No Skill invocation, Sub Agent dispatch, session/machine change, or Web/local transfer changes project authority merely by occurring.

## Task purpose, execution unit, execution context

Keep these distinct:

- **Task** — one engineering objective/authorization owned by `CURRENT_TASK.md`; may optionally carry `TASK_CLASS` such as DESIGN, EXECUTION, AUDIT, VERIFY, DIAGNOSIS, CORRECTIVE, or CLOSEOUT.
- **Execution unit** — bounded work inside one task, potentially delegated to a Sub Agent. Multiple units do not imply multiple task authorities.
- **Execution context** — Web session, local Codex, cloud agent, Sub Agent, reviewer context, machine, or session. Context does not define task purpose.

Keep the same task when the engineering objective/authorization is unchanged across delegation, session/machine transfer, or implementation-local verification. Reconcile or open a distinct task when the engineering purpose/authority materially changes, for example a separately commissioned independent acceptance audit or distinct corrective objective.

## Default governed route

```text
request
-> project-governance
-> solution-design?        material design ambiguity only
-> project-governance      reconcile/authorize the resulting engineering purpose
-> domain-navigation?      unclear semantic/source/test/runtime route only
-> execution-orchestrator? useful decomposition/parallelism/model/recovery policy
-> agent-handoff?          responsibility crosses contexts; same task when purpose unchanged
-> authorized implementation / verification
-> incident-doctor?        blocking evidence gap only
-> evidence-audit?         independent acceptance/readiness boundary only
-> live host gates?        when the repository host governs the requested boundary
-> project-governance      control alignment / lifecycle closeout
-> agent-handoff?          return result across contexts
```

Question marks are real gates: do not invoke a capability solely because it exists. Conversely, do not suppress useful orchestration merely because one executor could theoretically do all work; use safe parallel capacity when it materially improves execution.

## Common task transitions

These are semantic patterns, not mandatory ceremony:

- `DESIGN task -> EXECUTION task` when design was a separately authorized purpose and implementation is a new authorized objective.
- `EXECUTION task -> AUDIT task` when formal independent acceptance/readiness is commissioned.
- `AUDIT task -> CORRECTIVE task` when findings create a distinct authorized fix objective.
- `CORRECTIVE task -> VERIFY/AUDIT task` when a distinct independent verification boundary is required.

Within one EXECUTION task, controller/scout/implementer/verifier Sub Agent units remain execution units, not new tasks.

## Allowed common Skill compositions

- `project-governance -> solution-design -> project-governance`
- `project-governance -> domain-navigation -> project-governance`
- `project-governance -> execution-orchestrator -> project-governance`
- `execution-orchestrator -> agent-handoff -> delegated executor -> receipt -> execution-orchestrator`
- `project-governance -> evidence-audit -> project-governance` within an authorized audit purpose
- `evidence-audit -> agent-handoff` only when the audit crosses contexts
- `project-governance -> incident-doctor -> project-governance`
- `incident-doctor -> domain-navigation -> incident-doctor` for bounded evidence location

Do not create uncontrolled recursive routing or a peer mesh in which multiple Skills believe they own task authority.

## Specialist return contracts

| Skill | Returns |
| --- | --- |
| Solution Design | accepted design, assumptions, unresolved decisions, durable-document result, `TASK_RECONCILIATION_REQUIRED` |
| Execution Orchestrator | topology, role/write boundaries, model policy actually used, work-unit/integration state, verification/recovery evidence |
| Agent Handoff | bounded request or decision-useful receipt; never new authority |
| Evidence Audit | target/range/identity, required-claim coverage, findings/unknowns, independence basis, verdict, next safe decision |
| Domain Navigation | verified route or unresolved evidence gap |
| Incident Doctor | evidence state, hypothesis/falsification result, root-cause confidence where supported, minimum fix boundary |

## Artifact classes

### Authorities

- applicable `AGENTS.md`;
- `CURRENT_STATUS.md` for current snapshot facts;
- `CURRENT_TASK.md` for active authorization;
- accepted product/domain/data/runtime sources;
- accepted durable planning/design authority when justified;
- Git/repository host/runtime systems for facts they own.

### Evidence / transport artifacts

Handoff requests/receipts, Sub Agent briefs, execution ledgers, audit reports, review findings, CI/test outputs, runtime observations and probe results are not project controls by default. They may carry fresh evidence but cannot silently expand scope or replace an authority.

When evidence conflicts with the source that owns the semantic class, re-verify freshness and return to Project Governance for reconciliation. A newer explicit user instruction may require an authorization update; it does not turn a handoff card into authority.

## Writer/controller and parallelism rule

One active task authority can coordinate many concurrent execution units. Use safe available parallelism when units are independent enough to improve throughput/context isolation.

For overlapping semantic state, keep one writer/controller. Multiple concurrent writers require proven-disjoint semantic write authority/workspaces and a defined integration check. A branch or worktree name alone does not prove semantic independence.

## Direct bounded invocation

A user may explicitly ask for a read-only audit, design analysis, navigation pass, or diagnosis. The narrower Skill may answer that bounded request directly, but it still must not mutate project controls/source unless the active task and project authority permit it. Corrective state-changing work returns to Project Governance.

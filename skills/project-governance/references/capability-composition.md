# Capability composition

This contract defines how the seven Engineering Governance Skills cooperate without creating competing controllers or authorities.

## Ownership rule

`project-governance` owns entry, task/control authorization, re-entry after specialist work, workspace/writer lifecycle, verification-tier selection, and final closeout.

A narrower Skill owns only its bounded capability. Once it produces its result, ownership returns to its caller unless a higher-priority instruction explicitly selected that Skill as the direct bounded route.

No Skill invocation changes project authority merely by occurring.

## Default lifecycle

```text
request
-> project-governance
-> solution-design?        material design ambiguity only
-> project-governance      reconcile authorization if design changed task semantics
-> domain-navigation?      unclear semantic/source/test/runtime route only
-> execution-orchestrator? non-trivial execution topology only
-> agent-handoff?          responsibility crosses contexts
-> authorized implementation / verification
-> incident-doctor?        blocking evidence gap only
-> evidence-audit?         independent acceptance/readiness verdict only
-> live host gates?        when the repository host governs the requested boundary
-> project-governance      control alignment / lifecycle closeout
-> agent-handoff?          return result across contexts
```

Question marks are real gates: do not invoke a capability solely because it exists.

## Allowed common compositions

- `project-governance -> solution-design -> project-governance`
- `project-governance -> domain-navigation -> project-governance`
- `project-governance -> execution-orchestrator -> project-governance`
- `execution-orchestrator -> agent-handoff -> delegated executor -> receipt -> execution-orchestrator`
- `project-governance -> evidence-audit -> project-governance`
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
| Evidence Audit | target/range/identity, findings/unknowns, verdict, next safe decision |
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

Handoff requests/receipts, subagent briefs, execution ledgers, audit reports, review findings, CI/test outputs, runtime observations and probe results are not project controls by default. They may carry fresh evidence but cannot silently expand scope or replace an authority.

When evidence conflicts with the source that owns the semantic class, re-verify freshness and return to Project Governance for reconciliation. A newer explicit user instruction may require an authorization update; it does not turn a handoff card into authority.

## Writer/controller rule

One active task authority can coordinate many readers. For overlapping semantic state, keep one writer/controller. Multiple concurrent writers require proven-disjoint write authority/workspaces and a defined integration check. A branch or worktree name alone does not prove semantic independence.

## Direct bounded invocation

A user may explicitly ask for a read-only audit, design analysis, navigation pass, or diagnosis. The narrower Skill may answer that bounded request directly, but it still must not mutate project controls/source unless the active task and project authority permit it. Corrective state-changing work returns to Project Governance.

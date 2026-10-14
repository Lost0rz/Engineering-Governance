# Project artifact / authority lifecycle

Reconcile **semantic owners**, not a fixed list of files. A task does not update every project artifact at start or closeout.

## Classes

| Class | Typical examples | Rule |
| --- | --- | --- |
| `NORMATIVE_AUTHORITY` | project `AGENTS.md`, accepted domain/data rules | update when durable MUST/MUST-NOT or ownership semantics change |
| `DESIGN_AUTHORITY` | accepted architecture/long-lived plan | update when durable design/assumption/dependency/work-package semantics change |
| `CURRENT_CONTROL` | STATUS/TASK | update when owned current-state/authorization semantics change |
| `IMPLEMENTATION_AUTHORITY` | canonical source, schema, config, workflow, persisted contract/state owner for the implementation class | update through authorized implementation when the owned behavior/contract/state semantics change |
| `DERIVED_PROJECTION` | Project Profile, Domain/navigation map | authority wins; refresh only the affected stale projection when authorized/useful |
| `OBSERVED_EVIDENCE` | CI/test results, PR/host state, runtime observations, review/audit/probe evidence | read from the owning evidence system; observation alone does not force a control/projection write |

A source file may be evidence about its own contents, but lifecycle reasoning must distinguish **the semantic owner being changed** from **an observation used to prove a claim**.

## Reconciliation algorithm

At a state-changing boundary:

```text
fresh outcome
-> identify materially affected semantic classes
-> identify each class's owner
-> compare owner/projection with current truth
-> update only stale owned semantics
-> leave already-current artifacts untouched
```

`NO_SEMANTIC_CHANGE -> NO_WRITE -> NO_COMMIT`.

Normative/current authority materially stale for the next mutation must be reconciled before dependent mutation. A stale derived projection does not override its authority; report/refresh it according to task authorization.

## Common lifecycle

- `AGENTS.md`: long-lived; change only for durable project-specific normative rules/boundaries.
- Project Profile: long-lived derived context/index; one current projection surface (or explicit primary + mirror); refresh when its summaries/pointers become stale.
- Domain/navigation projection: refresh only affected verified routes; may be superseded by a new accepted navigation authority.
- durable planning: ACTIVE -> COMPLETED/SUPERSEDED/ARCHIVED as project semantics require; routine task completion alone does not rewrite design.
- STATUS/TASK: maintained in place as current controls; Git history provides history.
- implementation authority: follows normal implementation/version/lifecycle rules of the owning system; it is not downgraded to an evidence artifact merely because it is inspected.

Deletion/supersession must preserve a clear successor/pointer when future work would otherwise follow a dead authority path.

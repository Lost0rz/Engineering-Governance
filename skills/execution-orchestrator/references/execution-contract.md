# Execution contract

## 1. Trigger and non-trigger

Use orchestration when execution topology itself needs a decision: decomposition, multiple roles/agents, parallelism, model selection, long-running recovery, cancellation/supersession, or integration of independent work.

Do not invoke it when delegation adds no useful throughput/context benefit and one executor can complete the work cleanly. The presence of Sub Agents is neither a reason to use them nor a reason to avoid them.

## 2. Task and work-unit boundary

Delegated units normally remain inside one active `TASK_ID`. A work unit is not a new task authority.

A work unit should have a checkable result and a meaningful dependency/context/integration boundary. Split when a unit can reasonably succeed/fail independently, usefully isolate context, run in parallel, or produce an interface another unit consumes.

If a unit discovers a materially different engineering purpose or authorization need, it stops and returns that discovery to the controller/Project Governance rather than silently creating a new task.

## 3. Role classes

- **Controller** — sequencing/integration owner under the active task; does not create new authorization.
- **Implementer** — bounded writer within explicitly assigned semantic/path/workspace authority.
- **Scout / researcher** — read-only discovery/research.
- **Reviewer / auditor** — read-only evaluation unless separately re-authorized for corrective work.
- **Probe / verifier** — bounded observation/test role; diagnostic writes require explicit authorization.

A role name never grants write permission by itself.

## 4. Topology decision

Choose topology from dependency, authority, throughput, and integration needs rather than from a bias toward agent minimization:

1. **INLINE** — one executor when decomposition has little value or shared/dependent state dominates.
2. **SEQUENTIAL_DELEGATED** — delegated units executed one at a time when context separation helps but dependencies prevent useful concurrency.
3. **PARALLEL_READ_ONLY** — independent scouts/researchers/reviewers/verifiers with no shared mutation.
4. **PARALLEL_DISJOINT_WRITERS** — independent writers only when semantic write authorities/workspaces are proven disjoint and integration evidence is defined before dispatch.

Do not use peer-to-peer writer meshes for overlapping project state.

## 5. Positive parallelism policy

When independent units exist, available concurrency is useful capacity. Use it when doing so materially improves wall-clock time or isolates contexts without creating unsafe interference.

When material, establish:

```text
AVAILABLE_PARALLELISM
ACTIVE_UNITS
DEPENDENCY_GRAPH
WRITE_AUTHORITY_PER_UNIT
INTEGRATION_BOUNDARY
```

Parallelize when all relevant conditions are established:

1. dependency edges do not require another unit's intermediate state;
2. shared mutable resources will not collide;
3. write scopes are read-only or proven disjoint semantically, not merely by folder/branch name;
4. each result can be integrated/verified independently;
5. concurrency gives enough throughput/context benefit to justify coordination cost.

If a material condition is unknown, resolve it first or run the affected units sequentially/read-only. This gate protects correctness; it is not a policy to under-use safe Sub Agent capacity.

## 6. Model capability and environment mapping

Reusable governance uses capability tiers:

- **LOW** — bounded lookup, extraction, formatting, mechanical transformation, simple deterministic edit when reliable.
- **STANDARD** — normal implementation, multi-file pattern application, ordinary analysis/review.
- **HIGH** — architecture, subtle integration/concurrency/security reasoning, difficult diagnosis, high-consequence review, or another task whose reasoning demand materially justifies stronger capability.

HIGH is valid. Select it deliberately when needed.

When model choice materially affects cost/correctness, the execution environment should map tiers to concrete capability, for example:

```text
MODEL_TIER_MAP
LOW:
  model: <actual model>
  reasoning_effort: <bounded setting>
STANDARD:
  model: <actual model>
  reasoning_effort: <bounded setting>
HIGH:
  model: <actual model>
  reasoning_effort: <bounded setting>
```

Environment mapping may live in global/runtime configuration and must not be hardcoded as universal repository truth.

### Selection and escalation

- choose the capability tier justified by the unit's reasoning demand;
- use the strongest justified model, not automatically the strongest available model;
- delegated roles do not automatically inherit the controller/session model when another tier is more appropriate;
- intentional escalation is allowed when new evidence increases reasoning demand;
- when material, state `ESCALATION_REASON` and actual model/reasoning used;
- respect explicit task/environment cost/capability ceilings and allowed fallbacks;
- if the required mapped tier is unavailable and no accepted fallback exists, return `MODEL_CAPABILITY_UNAVAILABLE` to the controller rather than silently selecting another tier.

Suggested defaults are starting points only:

| Role | Typical tier | Notes |
| --- | --- | --- |
| Scout / bounded researcher | LOW | STANDARD when synthesis is non-trivial |
| Mechanical implementer | LOW or STANDARD | choose by edit/reliability demand |
| Normal implementer | STANDARD | HIGH allowed for difficult integration |
| Ordinary reviewer | STANDARD | HIGH for materially high-risk judgment |
| Architecture / difficult diagnosis / high-risk reviewer | HIGH | intentional strong-model use |

## 7. Delegation context package

A delegated brief should contain only what the unit needs:

```text
TASK_ID
UNIT_ID
ROLE
OBJECTIVE
DEPENDENCIES
AUTHORITY_REFERENCES
READ_WRITE_BOUNDARY
RELEVANT_PATHS_SYMBOLS_TESTS
FRESH_DELTA
ACCEPTANCE
STOP_CONDITIONS
MODEL_TIER
ACTUAL_MODEL / REASONING_EFFORT (when material)
MAX_TIER / ALLOWED_FALLBACK (when constrained)
RETURN_CONTRACT
```

Do not pass full chat history, full controls or unrelated repository context by default. Use Agent Handoff when the brief crosses a context boundary.

## 8. Review gates

Review cadence follows risk and required independence, not agent count:

- **V0/V1** — independent review only when user/task/risk justifies it.
- **V2** — independent review/audit is normally useful at the integrated task/PR boundary; not required after every small unit.
- **V3** — require explicit independent evidence/review appropriate to the high-consequence claim.

Implementation self-check by the same context is verification, not automatically independent audit. A reviewer finding is evidence to verify, not an automatic instruction to mutate code.

## 9. Retry, cancellation, and supersession

Retry only when the likely failure mode is recoverable and another attempt has a reasonable chance to add value. Avoid unbounded agent replacement loops.

When a unit's premise becomes stale, unnecessary, or invalid because another unit changed the decision boundary, mark it `CANCELLED` or `SUPERSEDED`. Do not integrate its result unless freshly revalidated against current task/evidence.

If repeated failure reveals a design/scope/evidence problem, return it to the controller/Project Governance rather than spawning more agents blindly.

## 10. Recovery ledger

Use only when context loss/restart is a realistic risk. Minimum useful fields:

- task/design identity;
- unit -> `NOT_STARTED | ACTIVE | PASS | STOP | CANCELLED | SUPERSEDED`;
- concrete result/commit identity;
- verification evidence;
- controller rulings/deviations;
- unresolved dependency/conflict;
- next resume point.

The ledger is ephemeral operational state. It does not replace `CURRENT_STATUS.md`, `CURRENT_TASK.md`, durable planning or Git history. At terminal closeout, retire it unless a bounded fact is deliberately promoted into an existing authority.

## 11. Integration contract

The controller integrates under the original task/writer authority:

1. verify returned result identity and actual changed paths;
2. confirm no unit exceeded write scope;
3. reject or revalidate cancelled/superseded/stale results;
4. resolve conflicts centrally rather than allowing agents to overwrite each other;
5. run the defined integration/affected verification;
6. reject unknown result identity rather than guessing equivalence;
7. return any material scope/design discovery to Project Governance/Solution Design before further affected mutation.

A unit saying `PASS` does not establish integrated task PASS.

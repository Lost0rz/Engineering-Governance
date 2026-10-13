# Execution contract

## 1. Trigger and non-trigger

Use orchestration when execution topology itself needs a decision: decomposition, multiple roles/agents, parallelism, model selection, long-running recovery or integration of independent work.

Do not invoke it for a task one competent executor can safely complete in one context. The existence of subagents is not a reason to use them.

## 2. Work-unit sizing

A work unit should have a checkable result and a meaningful context/integration boundary. Do not split setup/config/docs into artificial units when they exist only to support one deliverable.

Split when a unit can reasonably succeed/fail independently, usefully isolate context, run read-only in parallel, or produce an interface another unit consumes. State that interface explicitly when later work depends on it.

## 3. Role classes

- **Controller** — sequencing/integration owner under the active task; does not create new authorization.
- **Implementer** — bounded writer within explicitly assigned semantic/path/workspace authority.
- **Scout / researcher** — read-only discovery/research.
- **Reviewer / auditor** — read-only independent evaluation unless separately re-authorized for corrective work.
- **Probe / verifier** — bounded observation/test role; diagnostic writes require explicit authorization.

A role name never grants write permission by itself.

## 4. Topology decision

Choose the first topology that safely fits:

1. **INLINE** — one executor, no delegation.
2. **SEQUENTIAL_DELEGATED** — one controller, delegated units executed one at a time when context separation helps.
3. **PARALLEL_READ_ONLY** — independent scouts/reviewers/verifiers with no shared mutation.
4. **PARALLEL_DISJOINT_WRITERS** — only when semantic write authorities and workspaces are proven disjoint and integration evidence is defined before dispatch.

Do not use peer-to-peer writer meshes for overlapping project state.

## 5. Parallelism gate

Parallelize only when all relevant conditions are established:

1. no unit depends on another unit's intermediate state;
2. shared mutable resources will not collide;
3. write scopes are read-only or proven disjoint semantically, not merely by folder/branch name;
4. each result can be integrated/verified independently;
5. concurrency materially improves wall-clock time or context isolation enough to justify coordination cost.

If any material condition is unknown, run sequentially or keep parallel work read-only.

## 6. Model capability policy

Use capability tiers rather than hardcoding a provider/model name into reusable governance:

- **LOW** — bounded lookup, extraction, formatting, mechanical transformation, simple deterministic edit when reliable.
- **STANDARD** — normal implementation, multi-file pattern application, ordinary analysis/review.
- **HIGH** — architecture, subtle integration/concurrency/security reasoning, difficult diagnosis, or high-consequence final review when justified.

Suggested role defaults are starting points, not automatic mandates:

| Role | Preferred tier | Escalation ceiling by default |
| --- | --- | --- |
| Scout / bounded researcher | LOW | STANDARD |
| Mechanical implementer | LOW or STANDARD | STANDARD |
| Normal implementer | STANDARD | STANDARD unless task explicitly justifies HIGH |
| Ordinary reviewer | STANDARD | HIGH only for high-risk judgment |
| Architecture / high-risk reviewer | HIGH | HIGH |

Rules:

- choose the lowest tier that reliably satisfies the role;
- explicitly state a maximum/fallback when cost/capability bounds matter;
- do not silently inherit the controller/session model for delegated work;
- do not silently move to a materially higher tier when a requested tier is unavailable;
- if no allowed fallback exists, surface `MODEL_TIER_UNAVAILABLE` or project-equivalent state and let the controller decide;
- a target environment may map LOW/STANDARD/HIGH to its actual available model names; that mapping is environment configuration, not a universal repository fact.

## 7. Delegation context package

A delegated brief should contain only what the role needs:

```text
UNIT_ID
ROLE
OBJECTIVE
AUTHORITY_REFERENCES
READ_WRITE_BOUNDARY
RELEVANT_PATHS_SYMBOLS_TESTS
FRESH_DELTA
ACCEPTANCE
STOP_CONDITIONS
MODEL_TIER / MAX_TIER / ALLOWED_FALLBACK
RETURN_CONTRACT
```

Do not pass full chat history, full controls or unrelated repository context by default. Use Agent Handoff when the brief crosses a context boundary.

## 8. Review gates

Review cadence follows risk, not agent count:

- **V0/V1** — independent review only when user/task/risk justifies it.
- **V2** — independent review/audit is normally useful at the integrated task/PR boundary; not required after every small unit.
- **V3** — require explicit independent evidence/review appropriate to the high-consequence claim.

A reviewer finding is evidence to verify, not an automatic instruction to mutate code.

## 9. Recovery ledger

Use only when context loss/restart is a realistic risk. Minimum useful fields:

- task/design identity;
- unit -> `NOT_STARTED | ACTIVE | PASS | STOP | SUPERSEDED`;
- concrete result/commit identity;
- verification evidence;
- controller rulings/deviations;
- unresolved dependency/conflict;
- next resume point.

The ledger is ephemeral operational state. It does not replace `CURRENT_STATUS.md`, `CURRENT_TASK.md`, durable planning or Git history. At terminal closeout, retire it unless a bounded fact is deliberately promoted into an existing authority.

## 10. Integration contract

The controller integrates under the original task/writer authority:

1. verify returned result identity and actual changed paths;
2. confirm no unit exceeded write scope;
3. resolve conflicts centrally rather than allowing agents to overwrite each other;
4. run the defined integration/affected verification;
5. reject stale/unknown result identity rather than guessing equivalence;
6. return any material scope/design discovery to Project Governance/Solution Design before further affected mutation.

A unit saying `PASS` does not establish integrated task PASS.

# CURRENT TASK — EG-V01 Tooling Design

Task ID: `EG-V01-TOOLING-DESIGN-002`

State: `ACTIVE — SPEC CORRECTIVE AFTER WEB REVIEW`

Mode: `TOOLING_FOUNDATION_DESIGN`

## Objective

Correct the written tooling architecture spec after independent Web review. Preserve the accepted Hybrid direction and v0.1 authority boundaries. This remains design work only.

## Authority and reviewed head

- Repository: `Lost0rz/Engineering-Governance`.
- Base `main`: `ab0457c378563d33c6b67f8f81a83f9d10241008`.
- Design branch: `codex/eg-v01-tooling-design`.
- Executor spec handoff reviewed by Web: `db5d41fc7a7a9b301e67404067a5efd5501aeb95`.
- Draft PR #2 remains `OPEN / DRAFT / UNMERGED`.
- Accepted standard remains `EngineeringGovernanceStandard 0.1.0`; do not change it in this corrective.

## Required corrective

### MAJOR 1 — Bootstrap preview/apply + idempotence contract

Resolve the current contradiction between:

- repeat against an already-created unchanged setup = no-op; and
- any existing path = conflict.

Define at design level:

- an exact-match existing approved starter artifact may be treated as idempotent `NO_CHANGE`;
- any existing target path whose content/identity differs from the approved preview is a conflict/STOP and is never overwritten;
- preview approval is bound to one immutable conceptual plan identity/digest covering at least target repository identity, observed target revision/state needed for safe comparison, template/profile versions, candidate paths, and rendered content digests;
- apply must revalidate/recompute that plan and STOP if it no longer matches the approved preview;
- the actor authorized to confirm apply must be explicit; an AI skill cannot self-authorize a write.

Do not implement a schema or code; define the contract only.

### MAJOR 2 — Evaluation state versus command STOP

Make Sections 13 and 15 consistent.

Separate:

1. **evaluation-level unresolved state** — missing/stale/inaccessible evidence that can still be represented truthfully should produce `UNVERIFIED` and/or freshness `STALE`/`UNKNOWN`, with limitations, while still allowing a truthful report; and
2. **command-level fatal/unsafe STOP** — conditions where the tool cannot safely identify the target, cannot establish enough trusted input to produce a truthful report at all, hits a Bootstrap write-safety conflict, or encounters an internal fatal failure.

Define exit-code semantics consistently with that split. Do not turn evidence incompleteness into a hidden conformance gate.

### MAJOR 3 — Hybrid AI contribution data flow

Clarify the conceptual architecture for `AI_JUDGMENT` / `HYBRID` without adding persistence or implementation detail.

The corrected design must identify:

- what immutable deterministic/core output or evidence bundle the AI skill consumes;
- what an AI contribution references (target/evaluation/check/evidence identity plus model/instruction provenance and limitations);
- who validates/links the contribution into a composed view/report;
- that the skill cannot mutate machine results, source evidence, project decisions, or the original deterministic report;
- how HUMAN/HYBRID contributions remain explicit and how final project judgment remains owned by the named human/project authority;
- that no second report authority, hidden state store, or AI-owned acceptance path is created.

The design may choose immutable base report + linked derived contribution, or another equally explicit model, but must remove the current ambiguity.

## Scope preserved

Do not redesign the seven lifecycle layers/six axes, typed authority routing, standalone profile model, or accepted v0.1 semantics unless a direct contradiction is discovered and reported as STOP.

The following remain forbidden:

- executable Bootstrap/Doctor/Audit implementation;
- CLI/source code or dependency manifests;
- machine-readable schema implementation;
- implementation plan;
- MCP;
- daemon/background service;
- enforcement or automatic remediation/migration;
- pilot-repository changes;
- merging PR #2.

## Validation and handoff

After correcting the spec:

1. self-review the three findings against the exact corrected text;
2. verify no new scope or hidden writer was introduced;
3. update `CURRENT_STATUS.md` and this task back to `WAITING_FOR_USER_SPEC_REVIEW`;
4. commit/push the same design branch;
5. verify local/remote HEAD equality and clean worktree;
6. keep PR #2 Draft/unmerged and return the receipt below.

Required receipt:

```text
TASK_ID:
CONTROL_START_HEAD:
FINAL_HEAD:
REMOTE_HEAD:
LOCAL_REMOTE_MATCH:
WORKING_TREE:

MAJOR_1_BOOTSTRAP_PREVIEW_IDEMPOTENCE_RESOLVED:
MAJOR_2_STOP_EVALUATION_SEPARATION_RESOLVED:
MAJOR_3_AI_CONTRIBUTION_FLOW_RESOLVED:
HYBRID_RECOMMENDATION_PRESERVED:
V0_1_STANDARD_CHANGED: NO
IMPLEMENTATION_PLAN_WRITTEN: NO
IMPLEMENTATION_STARTED: NO

CHANGED_PATHS:
PR_STATE:
FINAL_STATE: WAITING_FOR_USER_SPEC_REVIEW | STOP
STOP_REASON:
```

STOP on unexpected remote-head drift, unknown local work, scope expansion into implementation, or any newly discovered contradiction that requires changing accepted v0.1.
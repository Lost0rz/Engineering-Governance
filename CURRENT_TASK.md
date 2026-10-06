# CURRENT TASK — EG-V01 Reference Synthesis Corrective

Task ID: `EG-V01-REFERENCE-SYNTHESIS-001`

State: `ACTIVE — CORRECTIVE AFTER INDEPENDENT WEB AUDIT`

Mode: `GOVERNANCE_MODEL_CANDIDATE_CORRECTIVE`

## Objective

Correct only the independent Web audit findings on Draft PR #1, preserve the
reference-audit work that passed review, synchronize the corrected candidate,
and return it for independent re-review.

Reviewed executor handoff head:

`ac9b1cf631beccdbd9869077d4673848dfb94bb9`

The candidate remains **NOT accepted and NOT frozen**.

## Authoritative audit result

The independent Web audit recorded `INDEPENDENT_WEB_AUDIT_CHANGES_REQUIRED`
in the PR conversation. GitHub prevents the connected account from submitting
a formal `REQUEST_CHANGES` review on its own PR; the PR conversation audit
record plus this control update are the authoritative review state.

## Required corrective scope

### MAJOR 1 — evaluation result vs freshness vs exception disposition

Refactor the candidate contract so these are orthogonal concepts:

- the historical evaluation result when a check ran;
- the current freshness state of its supporting evidence/dependencies;
- the current exception/waiver or project-decision disposition.

Do not model exception expiry/revocation as rewriting a historical evaluation
result. A prior `FAIL` remains the historical `FAIL`; an expired exception only
ends the exception effect. A prior `PASS` may remain the recorded result while
its evidence is now stale.

Update all affected wording consistently across at least:

- `docs/governance/v0.1/standard.md`
- `docs/governance/v0.1/checks-evidence-findings.md`
- `docs/governance/v0.1/exceptions-freshness-versioning.md`
- any synthesis/adversarial-review text that would otherwise contradict the
  corrected semantics.

Prefer an explicit structure such as:

- `result`: `PASS | FAIL | UNVERIFIED | NOT_APPLICABLE`
- `freshness`: `CURRENT | STALE | UNKNOWN`
- separate exception/decision state

Exact names may differ if the semantics remain equally clear and auditable.

### MAJOR 2 — typed authority routing

Remove the implication that heterogeneous authority classes form one total
precedence list.

The candidate must explicitly distinguish at least:

- product/domain/architecture semantic authority;
- Git/GitHub repository-state authority;
- shared current-state snapshot authority;
- execution authorization/scope authority;
- runtime/data authorities where a project declares them;
- derived findings/evidence/projections.

Precedence is meaningful only when two sources compete for the same claim or
action class. State explicitly:

- semantic/business truth does not authorize work outside `CURRENT_TASK.md`;
- `CURRENT_TASK.md` cannot rewrite canonical business/domain truth;
- Git/GitHub facts do not decide product semantics;
- findings/evidence/projections do not become source authorities.

Update `AGENTS.md` only if required to remove the same cross-type total-order
ambiguity; because this is a stable rule correction, such an update is allowed
on the task branch for review and must not be pushed directly to `main`.

### MINOR 1 — AI-derived analysis

Make normative that AI-derived analysis:

- must cite underlying source evidence;
- is derived/advisory;
- cannot independently satisfy a factual PASS/FAIL evidence requirement unless
  the check explicitly evaluates the AI artifact itself;
- cannot serve as independent acceptance of its own earlier output.

### MINOR 2 — parent profile inheritance

Resolve the current open question before freeze. Default corrective direction:
**defer/remove `parent_profile` inheritance from v0.1 unless concrete repeated
project evidence demonstrates a need now.**

Do not retain inheritance solely because an upstream reference has it. If the
executor believes evidence requires retaining it, record the concrete projects,
repetition, and simpler alternatives considered; otherwise remove it from the
candidate and move it to DEFERRED/future work.

## Preserved accepted scope

Do not redesign the entire model. The Web audit did not request changes to:

- the eight-reference audit set;
- the seven lifecycle layers;
- the six cross-cutting axes;
- the read-only InvestDesk reality-check boundary;
- the v0.1 prohibition on Bootstrap/Doctor/Audit implementation, MCP, daemon,
  automatic enforcement, or automatic remediation.

Reference wording may be corrected only where needed for consistency with the
four findings above.

## Gate 0 — freshness before corrective work

Before editing:

1. fetch/prune the Engineering-Governance remote;
2. verify Draft PR #1 remains open/unmerged and the task branch is the intended
   authoritative work branch;
3. fast-forward/reconcile the local task branch to the live remote task head;
4. re-read `AGENTS.md`, `CURRENT_STATUS.md`, and this task;
5. confirm no unexplained local-only or dirty work exists.

STOP on unexplained drift. Do not reset/discard unknown work.

InvestDesk is not part of this corrective write scope and must not be modified.

## Corrective validation

At minimum:

- inspect the exact diff from the reviewed handoff head;
- prove no unrelated model expansion occurred;
- run `git diff --check`;
- re-run local Markdown link validation;
- search the candidate for contradictory uses of `STALE`, exception expiry,
  authority order/precedence, `AI` evidence, and `parent_profile`;
- update executor adversarial review with the corrective rationale;
- verify all control files and PR description remain truthful.

No runtime/test suite is required unless the corrective unexpectedly changes
executable content; executable changes are not authorized.

## Handoff

When corrections and static validation pass:

1. update `CURRENT_STATUS.md` with verified corrective results;
2. set this task back to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`;
3. commit and push the task branch;
4. verify remote task HEAD equals local HEAD and the worktree is clean;
5. keep Draft PR #1 open and unmerged;
6. return a concise corrective receipt including reviewed base head, new head,
   exact changed paths, resolution of each MAJOR/MINOR, validation evidence,
   and any remaining open question.

Successful handoff state:

`WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Do not merge, freeze v0.1, or begin Bootstrap/Doctor/Audit implementation under
this task.

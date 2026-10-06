# CURRENT TASK — EG-V01 Reference Synthesis Corrective

Task ID: `EG-V01-REFERENCE-SYNTHESIS-001`

State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`

Mode: `GOVERNANCE_MODEL_CANDIDATE_CORRECTIVE`

## Objective and result

Correct only the independent Web audit findings on Draft PR #1, preserve the
reference-audit work that passed review, synchronize the corrected candidate,
and return it for independent re-review.

- Reviewed executor handoff: `ac9b1cf631beccdbd9869077d4673848dfb94bb9`.
- Corrective base: `4631a7c7535f18d1739c467a977b9bd94b62c811`.
- Corrected task branch is pushed; PR #1 remains OPEN / DRAFT / unmerged.
- The candidate remains **NOT accepted and NOT frozen**.

## Audit findings resolved

1. **MAJOR — result/freshness/exception/project disposition:** historical
   evaluation result is `PASS | FAIL | UNVERIFIED | NOT_APPLICABLE`; a separate
   time-scoped freshness assessment is `CURRENT | STALE | UNKNOWN`; exception
   status and project decision are independent. Expiry/revocation never
   rewrites a historical evaluation result.
2. **MAJOR — typed authorities:** claims route by semantic, repository,
   snapshot, execution-scope, runtime/data, or derived-output class.
   Precedence applies only to competing sources for the same claim/action
   class. Root `AGENTS.md` uses this routing model.
3. **MINOR — AI evidence:** AI analysis must cite underlying source evidence,
   remains derived/advisory, and cannot independently satisfy a factual
   PASS/FAIL requirement unless a check explicitly evaluates the AI artifact.
4. **MINOR — parent profile:** removed from the v0.1 profile and moved to
   DEFERRED. One pilot does not show a repeated need; standalone project-local
   values are the simpler current model.

No redesign was made to the eight-reference set, seven lifecycle layers, six
cross-cutting axes, or read-only InvestDesk boundary. No implementation tools
or automatic enforcement/remediation were added.

## Changed paths

- `AGENTS.md`
- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`
- `docs/governance/v0.1/adversarial-review.md`
- `docs/governance/v0.1/authority-model.md`
- `docs/governance/v0.1/checks-evidence-findings.md`
- `docs/governance/v0.1/exceptions-freshness-versioning.md`
- `docs/governance/v0.1/lifecycle.md` (freshness wording only)
- `docs/governance/v0.1/project-profile.md`
- `docs/governance/v0.1/standard.md`
- `docs/reference-audit/allstar.md`
- `docs/reference-audit/synthesis.md`

## Validation

- `git diff --check` passed.
- Local Markdown links passed across 23 Markdown files.
- Static searches confirmed orthogonal result/freshness/exception semantics,
  typed authority routing, AI evidence limits, and no v0.1 `parent_profile`
  field or inheritance rule.
- The lifecycle layer/axis table was not redesigned; only its stale-evidence
  sentence was clarified.
- No test suite or runtime check was run; changes are documentation and
  governance controls only.

## Handoff and stop condition

Next action is independent Web re-review of
[Draft PR #1](https://github.com/Lost0rz/Engineering-Governance/pull/1).
Remain `WAITING_FOR_INDEPENDENT_WEB_AUDIT`; do not merge, accept/freeze v0.1,
or begin Bootstrap/Doctor/Audit implementation under this task.

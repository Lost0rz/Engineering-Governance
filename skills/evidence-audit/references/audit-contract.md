# Audit contract — formal readiness, CI & release provenance

Load when `evidence-audit` performs `DEEP_PROVENANCE_OR_CI_AUDIT` (`CI`, `RELEASE_PROVENANCE`, `POST_CHANGE`, or multi-claim verification). Routine `CODE_DIFF` / `PR_MERGE` audits can run directly from [SKILL.md](../SKILL.md).

## 1. Advisory inspection vs formal verdict

- **Advisory status inspection** summarizes current state without claiming acceptance and needs no `evidence-audit` ceremony.
- **Formal acceptance verdict** evaluates an explicit target boundary (`CODE_DIFF`, `PR_MERGE`, `CI`, `RELEASE_PROVENANCE`, or `POST_CHANGE`) and remains strictly read-only.

## 2. Identity binding & audit independence

Bind every verdict to the exact target being claimed (`repo`, `base`/`head` or merge commit SHA, PR number, workflow run/job ID, or artifact SHA256) and state `AUDIT_INDEPENDENCE` (`SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN`). Never transfer `PASS` from an older commit unless semantic equivalence is explicitly established, and never count an implementation self-check as independent or human acceptance.

Keep action risk (`G0`–`G3`) separate from verification depth (`V0`–`V3`).

## 3. Audit profile checklists

- **`CODE_DIFF`:** verify target behavior, diff bounds, canonical owner preservation, and executed tests (explicitly flag weakened assertions in `tests/**` or unreviewed `.github/**` edits).
- **`PR_MERGE`:** evaluate both semantic diff evidence and **current live repository-host gates** (branch protection, required checks, reviews, mergeability) for the literal PR head/base.
- **`CI`:** verify workflow trigger/event, parent-commit alignment on merge trees, actual job matrix coverage, `fork_safe` boundaries, and skipped checks (`no status reported` is never `PASS`).
- **`RELEASE_PROVENANCE`:** verify source commit/tag, builder workflow, deterministic artifact hash, bundle contents (including required upstream licenses/provenance, excluding dev tests/archives), and manifest version match.
- **`POST_CHANGE`:** bind observed merge/deploy commit and actual installed runtime state; source tests alone never prove deployed or installed host behavior.

## 4. Semantic evidence vs live host gates

Semantic test/review evidence may remain valid across non-semantic doc-only edits with proven behavior equivalence, whereas live repository-host gates (required checks, approvals, merge state) must be reread fresh for the literal head identity.

## 5. Finding severity & verdict disposition

- `BLOCKING` -> `STOP` (security/correctness defect, identity mismatch, missing required check, or failing host gate).
- `IMPORTANT` -> `STOP` unless the responsible owner explicitly accepts deferral.
- `MINOR` -> allows `PASS_WITH_FOLLOWUPS`.
- Required claim lacking evidence (`UNKNOWN`) -> `STOP`.

Audit findings never authorize unapproved writes or status-only commits; report stale projections or alignment drift without mutating files.

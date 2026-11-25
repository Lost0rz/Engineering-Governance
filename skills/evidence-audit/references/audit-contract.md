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

## 5. Environment threat profiles (`SERVICE_OR_UNTRUSTED_INPUT` vs `SANDBOXED_APP`)

Select the threat boundary from project `AGENTS.md` (defaulting to `SERVICE_OR_UNTRUSTED_INPUT` when unspecified):

- **`SERVICE_OR_UNTRUSTED_INPUT` (default):** applies to backends, web APIs, multi-tenant services, CI routers, and package builders. Untrusted network inputs, auth/tenant boundaries, cross-fork PR payloads, symlink/path traversal, and replay/race hazards count as reachable trigger paths.
- **`SANDBOXED_APP` (project `AGENTS.md` opt-in for iOS / macOS / sandboxed client apps):**
  - Valid mutation sources are strictly **the App itself**, **real OS/environment lifecycle events** (network drop/switch/slowdown, app suspend/kill/force-quit, sleep/wake, app/page switch, rapid multi-tap, rotation/split-screen/external display, low battery/disk full, clock skew, push/deep-link arrival, version upgrade/migration, slow/errored/quota-exhausted upstream APIs, realistic max user data volume), and **prior App versions**.
  - **Theoretical ("Godzilla") cap -> `MINOR` (`P2`):** local file bit-rot/manual truncation/permission tampering outside the App's own write/cleanup code, local root/jailbreak/malicious sibling processes, hypothetical callers with zero call sites, `>10x` unrealistic scale, or test-double-only states unreachable by real App code.
  - **Preserved product gates (never cut):** consent & privacy scrubbing before data leaves the device, zero data/settings loss on update, confirmation on irreversible billing/deletion, and expiring rollback flags. Projects may append domain-specific real environment events in `AGENTS.md` (tightening examples only, never relaxing the midline).

## 6. Collateral checklist, severity governance & convergence

### Collateral & root-vs-leaf check (mandatory first step before single-point findings)
1. Did other views, shared state, counters, or lists shift unexpectedly?
2. How many codepaths manage this symptom—did the change patch only one leaf?
3. Were existing flags, invariants, or prior fixes bypassed or negated?
4. Did latency, background cadence, or upstream call volume regress?
5. Does upgrading from older persisted versions/settings remain intact?
6. Is this a canonical root fix, or a stacked patch/extra state machine likely to spawn the next bug?

### Severity governance (`BLOCKING == P0`, `IMPORTANT == P1`, `MINOR == P2`, `BACKLOG_NOTE`)
- `BLOCKING` (`P0`) -> `STOP`; `IMPORTANT` (`P1`) -> `STOP` unless the responsible owner explicitly accepts deferral. Every `P0`/`P1` must state **(a) reachable trigger path**, **(b) observable user/caller impact**, and **(c) trigger condition/frequency**; missing any one auto-downgrades to `MINOR` (`P2`) with a 1-line reason, while `>=3` independent low-probability conditions or sub-ms races without a user path log 1 line under `BACKLOG_NOTE` (`NO_FIX`).
- Required claim lacking evidence (`UNKNOWN`) -> `STOP`.
- Implementers cannot self-downgrade findings without orchestrator/owner sign-off; surface `OPEN_QUESTION` when user reachability is genuinely uncertain. Escalate any `MINOR` (`P2`) hit by real users or recurring across `>=3` audits back to `IMPORTANT` (`P1`).
- **Anti-overtightening & 2-round convergence:** stop adding local checksums, locks, or extra retry state machines for pathless theoretical races; close review/rework loops (`PASS_WITH_FOLLOWUPS`) once two consecutive passes yield only `MINOR` (`P2`) or `BACKLOG_NOTE` items, listing every check, surface, and scenario audited.

Audit findings never authorize unapproved writes or status-only commits; report stale projections or alignment drift without mutating files.

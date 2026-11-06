# Issue Control / Deterministic Execution Acceptance

Source contract acceptance matrix for EG-ISSUE-CONTROL-MIGRATION-093 (Issue #40). This is a **review checklist**, not evidence that these cases ran on an installed client.

## Mode and identity
- [ ] Explicit AGENTS FILE_CONTROL retains CURRENT_TASK/STATUS authority.
- [ ] Explicit AGENTS ISSUE_CONTROL uses approved selected Issue revision and does not read retired Task/Status as live.
- [ ] Missing/ambiguous mode does not automatically enable Issue Control.
- [ ] Multiple unrelated Issues never imply authority to choose one by guess.
- [ ] Unauthorized/self-declared approval or READY label cannot authorize.
- [ ] Material Issue body revision invalidates old approval; comment-only timestamp change does not.
- [ ] GitHub unavailable/stale cached Issue: STOP, never issue writes from stale prompt alone.

## Deterministic execution
- [ ] Complete concrete WP with evidence, targets, dependency, edge cases and checks can execute.
- [ ] Detailed but invented paths/unknown API or unresolved design: SPEC_INCOMPLETE.
- [ ] L0 harmless path move preserves semantics, can continue with evidence.
- [ ] L1 focused in-scope correction uses existing PR and scoped rerun.
- [ ] L2 missing API/contract/new side effect pauses dependent WPs, writes decision request.
- [ ] Independent WP continues only with proven disjoint authority/dependencies.
- [ ] L3 revoked authority or destructive safety risk terminates attempt, preserves work.
- [ ] RESUME requires newly approved spec revision; comment cannot silently expand scope.
- [ ] Small model cannot choose new architecture or widen scope because WP was vague.

## Receipts, acceptance and identity
- [ ] Final receipt posted as Issue comment, not status-file commit.
- [ ] Post failed/unverified is PENDING/FAILED, not successful Issue sync.
- [ ] PR/Actions live evidence remain authoritative; Issue receipts not merge proofs.
- [ ] Human UI gate remains PENDING after AI rendered inspection/Playwright.
- [ ] Existing branch/PR/worktree reused for same task; no control-only PR churn.
- [ ] No material Issue comment implies Git commit, HEAD drift or semantic rerun.
- [ ] FILE_CONTROL legacy SHA/control-only rules still apply only in that mode.

## Migration and source limits
- [ ] Existing task/PR identity and Git history preserved at cutover.
- [ ] Migration PR before merge still FILE_CONTROL; verified merge is exact cutover.
- [ ] Archived status text not used for current host/CI facts.
- [ ] No target product repositories, automation service, model router or tenth Skill changed.
- [ ] Source / remote / Web Plugin / local installed and release acceptance reported separately.

Verdict fields: SOURCE_CONTRACT, CROSS_SKILL_CONSISTENCY, GITHUB_REF, PR_HOST_GATES, WEB_PLUGIN, LOCAL_PLUGIN, RELEASE; no implicit PASS.

- [ ] Issue Form `###` headings map to canonical spec fields only through known validated names; missing fields fail closed.
- [ ] Unmigrated source still has no duplicate task authority; first control-only Task 093 commit precedes source writes.
- [ ] Cutover source removes live Task/Status files and retains Git history.

## EG-093 focused corrective verification (source-identical copy)

- Exact remote Git blob of `skills/project-governance/scripts/issue-spec-check.py`: `59d4c66723030fe983b611f6441265bd7ffdc9c0`.
- Exact remote Git blob of `skills/project-governance/scripts/test_issue_spec_check.py`: `cffe390cec00778d4f12b693409f9b8f1c56b3b3`.
- Source-identical Python test execution in disposable verification environment: `16/16 PASS`, `0 FAIL`, `0 ERROR`.
- Command for independent local replication: `python3 -m unittest discover -s skills/project-governance/scripts -p 'test_*.py' -v`.
- Covered: approved digest, comment-only continuity, changed body/revision rejection, untrusted actor, READY-label denial, missing/duplicate spec fields, unverified target, missing WP key, duplicated WP ID, WP placeholder, conflicting approval hashes, revocation, closed Issue and LF/CRLF equivalence.
- **Not proved by these tests:** actual GitHub approver intent, semantic source-path correctness, local `gh` read/comment permissions, live CI/required checks, installed Web/Local Plugin, human interface acceptance and PR merge.

### Migration evidence remaining before merge

- `ISSUE_40_BODY: EXECUTION_SPEC_V1 / SPEC_REVISION=2 / 19 canonical fields / 6 WPs` (remote readback).
- `SPEC_APPROVAL_V1: PENDING` for any post-cutover executable use of this Issue; old FILE_CONTROL Task 093 continues to authorize the current in-flight migration PR, not future Issue writes.
- `LOCAL_GH_PREFLIGHT: UNVERIFIED` from remote-only tooling. A real local CLI read and a benign test comment receipt must be observed; connector-only proof is insufficient.
- `PR_41: DRAFT / UNMERGED`; do not infer branch-protection or CI gates from clean mergeability.

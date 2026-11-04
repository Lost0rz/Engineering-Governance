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

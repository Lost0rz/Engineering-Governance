# EG-097 — Risk-scoped autonomy trust and execution boundary

Status: **implementation design / fail closed** (not an active authorization mode).
Source task: [Engineering-Governance Issue #48](https://github.com/Lost0rz/Engineering-Governance/issues/48), Revision 1, explicitly approved by [comment #6763597461](https://github.com/Lost0rz/Engineering-Governance/issues/48#issuecomment-6763597461).
Baseline: `main@83932cc17e9985d155eee09a74492c141949c730`. This file is a proposed design owned by `solution-design` and `project-governance`, **not** an execution authority, permission grant, migration cutover or release acceptance.

## 1. Verified host limitations and threat model (WP01)

On 2026-11-10, a live GitHub read of `/repos/Lost0rz/Engineering-Governance/rulesets` returned `[]`. The GitHub App connection received `403 Resource not accessible by integration` from `/branches/main/protection`. The empty rulesets response **does not prove** protection is present or absent; effective branch protection and workflow/Actions privileges are **UNVERIFIED**.

A maintainer's local `gh` readback on 2026-11-10 subsequently returned `404 Branch not protected` for `main`, no effective branch rules or rulesets, Actions enabled with allowed actions `all`, and no checks on PR #49. This confirms a present unprotected-main blocker, not merely an API-read gap for the connected app. The current branch must not present this as protected.

The existing `SPEC_APPROVAL_V1` verification checks approved Issue body digest and an authenticated GitHub comment author. A linked AI GitHub connector can operate on behalf of a human account; an `actor.login == Lost0rz` observation alone does not independently establish a human click, intent or permission separation. A writable Issue body, mutable local JSON file, copied Card, PR title, comment, label, artifact or AI-provided `HUMAN_APPROVED` field must never become an independent grant.

Threats to test and reject: (a) an executor creating or editing its own authorized spec; (b) an executor creating a claimed owner comment or GitHub native event with the same effective credential; (c) a workflow file or default branch writable by the executor; (d) replaying a previous grant after revocation, expiry, new commit, target change or increased risk; (e) ambiguous branch/worktree writers; (f) permission, data, deployment or release escalation hidden inside a nominally small patch.

**Required result now:** `RISK_SCOPED_AUTONOMY=INACTIVE_UNVERIFIED_HOST_BOUNDARY`. The legacy `ISSUE_CONTROL` direct/delegated approval paths remain as-is. The new mode may not authorize this task or any other task before its independently verified acceptance and explicit per-repository opt-in.

## 2. Minimum independently attestable authorization

Use **existing GitHub-native mechanisms**, not a new database, service, top-level Skill or runtime control plane. A candidate is a protected `workflow_dispatch` with immutable, auditable run identity. It is admissible **only after** fresh evidence demonstrates:

1. **Separate grant authority:** the executing AI credential is unable to dispatch or re-run the granting workflow, alter its trusted implementation or modify its protected refs, approvals, branch protection, runner trust or artifact provenance. Merely showing the same GitHub `actor` is insufficient.
2. **Trusted host binding:** the validator re-reads the native run through a trusted read-only channel and binds repository, owner, run ID/attempt, protected workflow source commit/ref, actor, issuance time, expiry, revocation identity and policy version. It rejects untrusted or stale local snapshots instead of treating a pasted JSON file as host evidence.
3. **Exact bounded task:** anchor the task ID, selected Issue identity/current revision or stable owner-approved objective, allowed repository/ref/write targets, **maximum** governance risk G1/G2, known hard exclusions and side-effect limits. Plans/WP filenames may evolve inside that envelope without silent widening.
4. **Current permissions:** resolve on the *actual execution host* the runtime credential capabilities and effective GitHub protections, including Actions/workflows/branch write access; where proof is unavailable, return STOP.
5. **No downstream implication:** even valid source-execution permission cannot authorize merge, production deployment, privileged install, plugin release, a second repository or human UI PASS. Those use their independent gates.

A local `--authorization-json` file can be a transport/cache of observations, **never** proof on its own. If an independent host attestation adapter is unavailable, a validator must return `STOP / UNVERIFIED_AUTHORIZATION_SOURCE` even if all JSON fields look correct. A syntactically valid token, owner-named actor or successful unit test is not an activation proof.

## 3. Two independent classifications

**Governance risk G0–G3** governs authority, not test volume:

| Level | Example | Required control |
| --- | --- | --- |
| G0 | Read-only source/host inspection | Existing read authority, no task write grant |
| G1 | Bounded source repair, DEBUG-only test seam, no production side effect | Verified task grant, scope/risk check, affected verification |
| G2 | Cross-component changes inside preapproved interfaces/data/permission envelope | Verified task grant, dependency/writer checks, integration verification |
| G3 | Privileged HID/driver/helper, identity/credentials, production release, irreversible data or security boundary | Separate high-assurance decision and applicable protected release gates; no G1/G2 autonomy |

**Deviation L0–L3** applies *after* grant verification:

- **L0 — CONTINUE:** provably nonsemantic route/locator/format changes; no extra authorization.
- **L1 — LOCAL_CORRECT:** same task objective, same risk envelope, bounded tests/diagnostics/implementation and necessary source-path adjustments; `CHECK → FIX → RECHECK_AFFECTED` without progress/decision/resume comments.
- **L2 — PAUSE_AFFECTED:** material objective, contract, API/persistence semantics, security, permission, identity, hard-deny scope or effective risk expansion; or genuinely unresolved writer/dependency overlap. Independent safe WPs may proceed if proven disjoint. One decision request for the distinct blocker.
- **L3 — TERMINATE:** revoked or forged grant, dangerous uncontrolled writes, credential exposure, irreversible data destruction or unsalvageable authority conflict.

A test helper path not listed in the original WP is not *automatically* L2 when it is demonstrably no-production-side-effect and not explicitly denied. Conversely a device helper / raw-source data overwrite is not L1 simply because a small source diff fixes it. A failed test alone does not license architecture changes.

**Verification V0–V3** is orthogonal: no redundant independent auditor for every G1 edit; focused construction checks; scoped integration close; V3 independent security/data review when consequence demands it. A CI scope gate passing must not be reported as tests that were skipped passing. Machine-run browser checks never substitute for a human UI acceptance decision.

## 4. Writer evidence and cross-context recovery

Preserve unique local work and avoid genuine conflicting writes. When overlap is actually indicated, consult relevant Issue discussion, PR/ref history and local workspace facts together; normal agent-to-agent transfer does not require a second Writer-release approval or inventory. A comment remains useful evidence but cannot independently authorize out-of-scope mutations.

The current grant schema fixes one `target_commit_sha`. Before any activation, implement a verified continuation rule: anchor the originally trusted base and allow subsequent commits only when the host proves an authorized ancestry/branch relationship, unchanged task/risk/effect envelope and no revocation. Do not blindly equate every new HEAD with the original grant Commit, or accept a freely supplied local ancestry claim. The current checker remains deliberately inactive and does not yet implement this rule.

A Card carries only `repo + task ID + grant anchor + exact evidence identity + current WP + transfer delta + STOP`. The receiver must validate the source grant and live workspace state; the Card is not an independent permission, and copying a stale grant cannot reactivate it. Progress and terminal results may be recorded through PR/commit/test artifacts; comment-free execution is not evidence-free execution.

## 5. Migration and acceptance sequencing

1. **WP01** Verify threat assumptions and reject the unsupported host trust path; finalize this design before implementing authorization checks.
2. **WP02** Preserve existing `issue-spec-check.py digest/verify` behavior; add a distinctly named, opt-in autonomous verification path and focused positive/negative tests. A positive *policy decision* test is not a valid *host-authority activation* test.
3. **WP03** Amend `project-governance`, `issue-control`, `issue-execution-contract`, global routing, Handoff and templates to distinguish legacy/default from a strictly verified autonomous grant. Ordinary G1/G2 progress/correction/resume comments become optional **only** after that activation proof.
4. **WP04** Reconcile Writer rules and `V0–V3` separately from `G0–G3`; regression-test FloatTabs #208/#211, Merloom #632 and RemoteOrbit #51 without repository-specific exceptions.
5. **WP05** Run legacy and new negative regression tests, source reference consistency, and independent security review. Deliver a Draft PR; do not merge, install or release under Issue #48.

**Activation gate:** an owner must independently provide and verify effective GitHub protections, executor-vs-grant credential separation, host retrieval, replay/revocation handling and branch/commit binding. Until then, deliver the new policy implementation **fail closed**, with legacy behavior intact and no automatic source-write grant.

**Per-project adoption:** after source merge, plugin release and verified Web/Codex/Claude installation, inspect each repository's accepted `AGENTS.md` and its own authority. Strip duplicate reusable workflow instructions without deleting project-specific business, data, device, runner and UI safety boundaries. Engineering-Governance #48 does not grant writes to those repositories.

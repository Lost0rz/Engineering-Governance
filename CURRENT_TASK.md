# CURRENT TASK — Engineering Workflow Efficiency: Verification + Workspace Creation

Date: 2026-11-04
Repository: `Lost0rz/Engineering-Governance`
Task ID: `EG-VERIFICATION-CADENCE-EFFICIENCY-092`
Task class: `BOUNDED CORRECTIVE / SOURCE SKILL CONTRACT`
Status: `WORKSPACE_CREATION_SOURCE_COMPLETE / SELF_AUDITED / DRAFT_UNMERGED`
Mode: `SOURCE_ONLY`
Branch: `codex/verification-cadence-efficiency-092`
Baseline main: `ef4f2d9af8e5796b7d0bc7b53f2c0dbe785211bb`
PR: `#39 / OPEN / DRAFT / UNMERGED`
Verification tier: `V2` (cross-Skill contract/composition; no runtime/source product behavior)

## Objective

Amend existing Engineering Governance Skills so small changes do not provoke repeated broad regression, CI, packaging or independent re-audit by default. Keep safety-critical evidence at risk-appropriate acceptance/release boundaries. This is source policy and card-contract work, **not** a new top-level Skill, execution engine, CI scheduler, service, or cross-project code change.

## Authorized source surface

- `skills/project-governance/references/verification-tiers.md` — classification/cadence, reuse/host gate and selective rerun decisions.
- `skills/project-governance/SKILL.md` — compact normative hook to owned verification reference.
- `skills/agent-handoff/references/handoff-contract.md` — transfer the smallest decision-relevant verification delta, not a mandatory large form.
- `skills/agent-handoff/SKILL.md` only if a lightweight hook is required.
- `references/**` only for one focused cross-Skill scenario/acceptance matrix if useful.
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` for control reconciliation.

No change to `AGENTS.md`, top-level Skill count, model routing, plugin manifests/version, release/tag, production projects, downstream product CI/runner topology, or installed Web/local plugin. This task also explicitly permits the previously authorized repository legacy-CI archival and the workspace-efficiency source extension below.

## Required behavior

1. V0 documentation/control-only change: static/authority checks, semantic evidence reuse when proven; never claim required host checks passed from semantic equivalence alone.
2. V1 localized change: focused checks while constructing; no full test/audit after every edit.
3. V2 related corrections: group scope; run broader affected-domain checks at stabilization/close, rerun only invalidated checks after corrections unless risk/host rules require more.
4. V3/high risk or release: preserve explicit broad, independent and exact-host evidence required by acceptance authority.
5. Reuse across pure control-only drift only with proven semantic equivalence and compatible task/authority conditions. Distinguish semantic vs literal-head host gates.
6. A cross-context Handoff Card references accepted `CURRENT_TASK` verification terms and only reports fresh exceptions/phase/required checks; avoid duplicating the task or mandating verification metadata for trivial requests.
7. Do not equate green CI with executed tests, nor machine browser checks with human UI acceptance.

## Verification / audit

- Before source mutation: separate control-only commit to establish this task on the branch.
- Construction: focused source diff and contract scenario review; no installed/runtime test claims.
- Frozen source: read back exact PR changes; verify V0/V1/V2/V3, stage, correction, evidence reuse, literal-host gate and cross-context positive/negative cases.
- After implementation, perform a read-only `CODE_DIFF` evidence audit with honest independence basis (`SELF_CHECK` if same context).
- Keep Draft / unmerged; only report source and repository delivery evidence actually seen. Formal plugin release/Web/local install acceptance is out of scope.

## Observed source/audit evidence

- Baseline: `main@ef4f2d9af8e5796b7d0bc7b53f2c0dbe785211bb`.
- Skill rule semantic source: `66af1ff5447ba1d7deeae17ea3827cfc3a1b3de7` (prior to CI corrective).
- Combined Skill + archived CI workflow semantic source: `4af1aa95a38abfb1c1adc22a1287821a2fc6253f`.
- Changed source: 4 existing Skill files + 1 compact acceptance matrix; separate control-only task activation commit.
- Focused cross-Skill static contract check: `21/21 PASS` before V0 wording correction; affected post-corrective checks: `11/11 PASS`.
- `CODE_DIFF`: `PASS_WITH_FOLLOWUPS` at semantic source HEAD, `AUDIT_INDEPENDENCE: SELF_CHECK` only, not independent installed/runtime acceptance.
- Existing `.github/workflows/validate-plugin-v0.7.3.yml` triggers on these Skill paths but hardcodes `manifest[\'version\'] == \'0.7.3\'`; current manifest is `0.7.5`. Latest PR CI run `41745425207` failed at this legacy version assertion before building the candidate. This is a CI/host blocker, not a proven Skill source regression.
- `PR_MERGE_READY: NO`; no merge, no Web/local plugin sync and no downstream product CI mutation.

## Authorized legacy CI closeout (user approved 2026-11-04)

The user authorized retiring the redundant, failing **old validation** of published version 0.7.3. This is a same-task corrective to the verification efficiency objective, not a new framework or release task.

- Allowed mutation: only `.github/workflows/validate-plugin-v0.7.3.yml` in this repository, adopting the already established archived/dispatch-only pattern used by `validate-plugin-v0.7.2.yml`.
- Expected behavior: ordinary Skill/PR changes **no longer auto-run** the hard-coded v0.7.3 candidate validator; no dependency on `plugin.json.version == 0.7.3` for current-source PR acceptance.
- Preserve published release/tag/asset history and `.github/workflows/release-plugin-*.yml`; do not modify the current version, create a replacement full-suite workflow, disable GitHub Actions globally, or change other repositories.
- Verification: exact workflow readback and diff; check zero `pull_request` / `push` / `schedule` triggers for archived validator, no candidate-build/version-gated job, archived validator remains manually inspectable, and untouched release/other workflows.
- GitHub rulesets API returned an empty array; branch-protection endpoint was inaccessible to the integration (403). Therefore required-check availability is not proven and PR merge-readiness remains unresolved until live host gates can be verified.
- Archived source committed at `4af1aa95a38abfb1c1adc22a1287821a2fc6253f`; exact diff modifies **only** `.github/workflows/validate-plugin-v0.7.3.yml` and replaces the legacy validator with a dispatch-only archived echo stub.
- Focused readback/trigger validation: `10/10 PASS`. No PR workflow runs returned for that semantic HEAD. The archived v0.7.2 validator and v0.7.3 release workfIow are unchanged. 
- Formal `CODE_DIFF` source archival verdict: `PASS` (`AUDIT_INDEPENDENCE=SELF_CHECK`). `PR_MERGE` readiness: `STOP`/not evaluated as PASS; Draft, host-required checks UNKNOWN due 403 protection endpoint.
- Keep PR #39 Draft and unmerged. A branch-only source change does not alter behavior on `main` before merge.

## Authorized workspace / PR creation efficiency extension (user approved 2026-11-04)

Same Engineering Governance **workflow-efficiency** Task 092, same existing Draft PR #39, no merge and no new PR/worktree just for this extension. The user requests a cross-project read-only assessment of recent Worktree and PR proliferation and a proportional correction to existing reusable Skills. Preserve the earlier Skill-verification and legacy-CI closeout evidence.

### Cross-project evidence boundary

- `InvestDesk` Task141 PRs #169, #171, #173 and #175: each changed only `CURRENT_STATUS.md` / `CURRENT_TASK.md`, demonstrating repeated control-only PR overhead; this does **not** prove four machine-local Git worktrees.
- `FloatTabs` #192 and `VideoOs` #13: additional independent two-control-file PRs. FloatTabs has numerous historical `codex/*` remote branches; remote refs are **not** physical local worktrees.
- `Merloom` AGENTS defaults material work to a fresh branch/Draft PR; `InvestDesk` AGENTS constrains one active task/PR to one authoritative worktree, while same-PR iteration is already proven by current `Merloom` #611, `FloatTabs` #195 and `RemoteOrbit` #40.
- GitHub cannot verify `git worktree list --porcelain`, local checkout existence/dirty state, or per-command local worktree spawning. Preserve `LOCAL_WORKTREE_COUNT=UNKNOWN`, `LOCAL_OVERUSE=UNVERIFIED`; do not clean any physical workspace.

### Authorized source

- `skills/project-governance/references/workspace-lifecycle.md`: introduce a narrow explicit **creation gate** distinct for task / local checkout / branch / Git worktree / PR; default reuse, permit new worktree only on a demonstrated isolation or concurrency need, preserve project-specific normative branch/PR obligations and unique work.
- `skills/project-governance/SKILL.md` and `references/development-flow.md`: concise hooks preventing command/session/subagent/checkpoint from automatically creating new workspace/branch/PR.
- `skills/execution-orchestrator/SKILL.md` and `skills/agent-handoff/references/handoff-contract.md` only if necessary to prevent delegation/handoff from manufacturing workspace authority.
- One compact scenario matrix under `references/**` for positive/negative workspace creation cases; current controls for authority/alignment.

No multi-project rules/code changes, no local worktree cleanup, no implicit PR close/merge, no forced push, no plugin release/sync. The target project's `AGENTS.md` and task-specific explicit fresh-branch/PR constraints remain higher authority than reusable defaults.

### Verification and stop

Class `V2` (cross-Skill workflow-contract integration), targeted static diff/readback, scenarios: read-only task, no-op, same-task correction, control-only alignment, one-writer active branch, legitimate isolated concurrent disjoint writers, dirty/unique-work protection, project explicit fresh branch/PR, handoff/subagents, PR review vs merge, remote vs local worktree inference. Run only affected checks after corrections. Audit read-only, with honest `AUDIT_INDEPENDENCE=SELF_CHECK` in the same context. Final PR #39 must remain `OPEN / DRAFT / UNMERGED`; no release or installed acceptance claims.

## Observed workspace-creation source closeout

- Workspace efficiency semantic HEAD: `760f78e974bc53ddbe82f0ae0674b6fcef1ee6d0`; same branch and Draft PR #39, main unchanged.
- Source changed in this extension: `workspace-lifecycle.md`, Project Governance entry + development flow, Execution Orchestrator entry, Agent Handoff reference, and one focused acceptance matrix. No project/CI/runner/runtime files.
- Formal `CODE_DIFF` scoped source assessment: `PASS`, `AUDIT_INDEPENDENCE=SELF_CHECK`. Source consistency and scenario-mapping assertions: `20/20 PASS`; matrix contains 15 positive/negative cases.
- A follow-up one-file wording correction at this semantic HEAD distinguishes known retained unique work from unclassified dirty/unknown work.
- Remote branch and PR counts do not prove physical local Worktrees. `LOCAL_WORKTREE_COUNT=UNKNOWN`, `LOCAL_OVERUSE=UNVERIFIED`; no local inspection, reset, prune, deletion or cleanup performed.
- No automatic CI run returned for the semantic source HEAD. This is neither a claim of green CI nor installed Plugin behavior. `PR_MERGE_READY=NO` because user explicitly requires no merge and host-required checks have not been fully verified.

## Next safe boundary

Verification, obsolete CI archival, and workspace creation efficiency Skill source are now complete on Draft PR #39. Preserve this branch/PR without merge. If the user later requests installed rollout, inspect fresh repository acceptance/host gates and current plugin distribution needs first; do not infer that source changes already govern local Codex/ChatGPT sessions.

## STOP

No implicit release, merge, downstream CI mutation, plugin deployment, or local cache edits. If an existing Skill already covers a case adequately, retain it and avoid duplicate prose. If repository main/branch identity drifts or an accepted authority conflicts, stop mutation and reconcile.

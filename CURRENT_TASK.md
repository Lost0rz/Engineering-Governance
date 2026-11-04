# CURRENT TASK — Proportional Verification Cadence / Skill Efficiency

Date: 2026-11-04
Repository: `Lost0rz/Engineering-Governance`
Task ID: `EG-VERIFICATION-CADENCE-EFFICIENCY-092`
Task class: `BOUNDED CORRECTIVE / SOURCE SKILL CONTRACT`
Status: `ACTIVE / SOURCE_CONSTRUCTION`
Mode: `SOURCE_ONLY`
Branch: `codex/verification-cadence-efficiency-092`
Baseline main: `ef4f2d9af8e5796b7d0bc7b53f2c0dbe785211bb`
PR: `DRAFT_PENDING / UNMERGED`
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

No change to `AGENTS.md`, top-level Skill count, model routing, plugin manifests/version, release/tag, production projects, downstream CI/runner topology, or installed Web/local plugin.

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

## STOP

No implicit release, merge, downstream CI mutation, plugin deployment, or local cache edits. If an existing Skill already covers a case adequately, retain it and avoid duplicate prose. If repository main/branch identity drifts or an accepted authority conflicts, stop mutation and reconcile.

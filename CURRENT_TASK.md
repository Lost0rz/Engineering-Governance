# CURRENT TASK — Mandatory Control Closeout

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-MANDATORY-CONTROL-CLOSEOUT-058`

State: `READY_FOR_INDEPENDENT_AUDIT`

Mode: bounded governance-contract correction

## Objective

Prevent governed tasks from leaving `CURRENT_STATUS.md` and `CURRENT_TASK.md` materially behind the verified project state after execution, while preserving the accepted distinction between literal Repository HEAD and Delivery / Semantic HEAD.

## Accepted baseline

- `main`: `72042f4157389520c7acd754cab5272a3cfdab85`.
- Published Plugin baseline remains `0.5.4`.
- Existing `CONTROL_ONLY_DRIFT` semantics remain accepted: changes limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` do not change Delivery / Semantic HEAD.
- Existing repository-host gates remain separate live constraints for the literal identity the host governs.

## Problem corrected

The prior Project Governance contract explicitly allowed routine lifecycle reconciliation to be lazy/batched and told agents not to write controls merely because merge/closeout/lifecycle evidence changed. In repeated real project use this permitted completed work to leave `CURRENT_STATUS.md` / `CURRENT_TASK.md` stale, causing repeated execution cards, obsolete task state, and incorrect next-step reasoning.

## Implemented semantics

1. Every governed handoff/closeout performs a control-reconciliation check before reporting the task fully closed.
2. For state-changing work, if verified control-owned facts changed, reconcile the affected controls before the final closeout receipt:
   - `CURRENT_STATUS.md` reflects the verified current project/delivery state and next milestone;
   - `CURRENT_TASK.md` reflects the actual active, handoff, blocked, or terminal task state/current stop point.
3. Raw CI/review/merge event history is not copied into controls. Only the durable/current-state consequence owned by the control is written.
4. A control-only reconciliation commit remains `CONTROL_ONLY_CHANGE` / `CONTROL_ONLY_DRIFT`; it does not by itself invalidate already-valid semantic implementation evidence or reopen verified workspace closeout.
5. Strict read-only work remains non-mutating, but it still performs the closeout check and reports required reconciliation explicitly when controls are stale.
6. Final governed receipts expose the control-reconciliation result and whether `CURRENT_STATUS.md` / `CURRENT_TASK.md` were updated, not required, or blocked.
7. Global routing remains selection-only, while `project-governance` remains active through governed handoff/closeout.

## In scope completed

- Root `AGENTS.md` durable repository rule.
- `skills/project-governance/SKILL.md` lifecycle behavior.
- `skills/project-governance/references/control-plane.md` control ownership/update contract.
- `skills/project-governance/references/development-flow.md` normal closeout sequence.
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`.
- `skills/project-governance/assets/templates/CURRENT_TASK.md`.
- `skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md` concise closeout routing/triggering.
- Root control-plane reconciliation for this task.

## Out of scope preserved

- No Plugin version bump or formal release.
- No ChatGPT Web Plugin publication/update.
- No Mac mini / MacBook Air installation or cache/source mutation.
- No automatic file-mutating runtime, hook, daemon, service, database, installer, or fourth Skill.
- No changes to Gift, Merloom, InvestDesk, or other target-project repositories.

## Verification level, cadence, and result

`V0` — governance/documentation semantics only.

Fresh self-audit result before control-only handoff reconciliation:

- Source/governance candidate: `608038451c0554d493fa1bff239e1582d5eb0b45`.
- Authorization/main baseline: `72042f4157389520c7acd754cab5272a3cfdab85`.
- Branch was `ahead 9 / behind 0` at the source candidate.
- Exact changed paths were limited to the nine authorized governance/control surfaces.
- `plugin.json` remained exactly version `0.5.4`.
- No `domain-navigation` or `incident-doctor` source changed.
- No fourth Skill or runtime enforcement subsystem was introduced.
- Conflicting normal lazy/batched closeout semantics were replaced by mandatory handoff/closeout reconciliation; legacy delayed reconciliation remains only as an explicit recovery case.
- `CONTROL_ONLY_DRIFT` / Delivery-Semantic-HEAD separation remains intact.

## Acceptance status

- Mandatory closeout check: implemented.
- State-changing control reconciliation: implemented.
- Current-state-not-history boundary: preserved.
- Strict read-only exception: implemented.
- Concise final receipt contract: implemented.
- Global routing anti-duplication boundary: preserved.
- Delivery / Semantic HEAD separation: preserved.
- Draft PR: `#21` — open, draft, unmerged.
- Independent audit: pending.

## Stop conditions

- Do not merge PR #21 before independent audit of the exact source/governance candidate and its later control-only drift.
- Do not bump/publish a Plugin version or mutate local installed authorities in this task.
- If `main` advances with non-control changes before merge, re-evaluate the branch relationship before integration.

## Handoff / current stop point

Reusable/governance source construction is complete for this bounded correction at Delivery / Semantic candidate `608038451c0554d493fa1bff239e1582d5eb0b45`.

Draft PR #21 is the independent-audit handoff. Subsequent branch movement after the frozen candidate is restricted to `CURRENT_STATUS.md` / `CURRENT_TASK.md` closeout reconciliation and must remain proven `CONTROL_ONLY_DRIFT`.

Merge, Plugin versioning/publication, ChatGPT Web update, and Mac mini/MacBook Air deployment remain unapproved.

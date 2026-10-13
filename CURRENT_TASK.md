# CURRENT TASK — Mandatory Control Closeout

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-MANDATORY-CONTROL-CLOSEOUT-058`

State: `ACTIVE_IMPLEMENTATION`

Mode: bounded governance-contract correction

## Objective

Prevent governed tasks from leaving `CURRENT_STATUS.md` and `CURRENT_TASK.md` materially behind the verified project state after execution, while preserving the accepted distinction between literal Repository HEAD and Delivery / Semantic HEAD.

## Accepted baseline

- `main`: `72042f4157389520c7acd754cab5272a3cfdab85`.
- Published Plugin baseline remains `0.5.4`.
- Existing `CONTROL_ONLY_DRIFT` semantics remain accepted: changes limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` do not change Delivery / Semantic HEAD.
- Existing repository-host gates remain separate live constraints for the literal identity the host governs.

## Problem being corrected

The current Project Governance contract explicitly allows routine lifecycle reconciliation to be lazy/batched and tells agents not to write controls merely because merge/closeout/lifecycle evidence changed. In repeated real project use this permits completed work to leave `CURRENT_STATUS.md` / `CURRENT_TASK.md` stale, causing repeated execution cards, obsolete task state, and incorrect next-step reasoning.

## Required semantics

1. Every governed task closeout must perform a control-reconciliation check before reporting the task fully closed.
2. For state-changing work, if verified control-owned facts changed, reconcile the affected controls before the final closeout receipt:
   - `CURRENT_STATUS.md` reflects the verified current project/delivery state and next milestone;
   - `CURRENT_TASK.md` reflects the actual active, handoff, blocked, or terminal task state.
3. Do not copy raw CI/review/merge event history into controls. Write only the durable/current-state consequence owned by the control.
4. A control-only reconciliation commit remains `CONTROL_ONLY_CHANGE` / `CONTROL_ONLY_DRIFT`; it must not by itself invalidate already-valid semantic implementation evidence or reopen verified workspace closeout.
5. Strict read-only work remains non-mutating. It must still perform the closeout check and explicitly report any required control reconciliation rather than silently leaving stale controls.
6. Final governed receipts must expose whether the closeout reconciliation was completed, not required, or blocked, and whether `CURRENT_STATUS.md` / `CURRENT_TASK.md` were updated.
7. Global routing remains selection-only: it should make task closeout a Project Governance trigger without duplicating the closeout procedure.

## In scope

- Root `AGENTS.md` durable repository rule.
- `skills/project-governance/SKILL.md` lifecycle behavior.
- `skills/project-governance/references/control-plane.md` control ownership/update contract.
- `skills/project-governance/references/development-flow.md` normal closeout sequence.
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`.
- `skills/project-governance/assets/templates/CURRENT_TASK.md`.
- `skills/project-governance/assets/templates/GLOBAL_AGENTS_ROUTING.md` only for concise closeout routing/triggering.
- Root control-plane reconciliation for this task.

## Out of scope

- Plugin version bump or formal release.
- ChatGPT Web Plugin publication/update.
- Mac mini / MacBook Air installation or cache/source mutation.
- Automatic file-mutating runtime, hook, daemon, service, database, installer, or fourth Skill.
- Changes to Gift, Merloom, InvestDesk, or other target-project repositories.

## Verification level, cadence, and rationale

`V0` — governance/documentation semantics only. Verify exact changed paths, removal of conflicting lazy/batched closeout language, preservation of control-only Delivery/Semantic HEAD semantics, consistency across Skill/reference/templates/routing, and no release/runtime scope expansion.

## Acceptance criteria

- The normal governed flow cannot report a state-changing task fully closed while materially stale controls remain unreconciled and writable.
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` remain synchronization/control surfaces rather than application delivery identity.
- External event logs are not copied into controls merely for history.
- Read-only work has an explicit non-mutating exception with a visible reconciliation result.
- Global routing remains concise and delegates closeout procedure to `project-governance`.
- No fourth Skill or runtime enforcement subsystem is introduced.

## Stop conditions

- Any change would require automatic global-file mutation or a new runtime enforcement subsystem.
- The proposed closeout rule would invalidate `CONTROL_ONLY_DRIFT` / Delivery-Semantic-HEAD separation.
- Main advances with non-control changes before source integration and the branch cannot be safely reconciled.

## Handoff / current stop point

Implement and self-audit the source-only governance correction on `codex/mandatory-control-closeout-058`. Do not publish a new Plugin version or mutate local installed authorities in this task.

# CURRENT TASK — Control Files Noise Reduction

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CONTROL-DELIVERY-IDENTITY-055`

State: `AUTHORIZED_PLANNING`

Mode: governed reusable-source change

## Objective

Reduce governance noise globally by separating repository control-record changes from implementation/delivery identity while preserving `CURRENT_STATUS.md` and `CURRENT_TASK.md` as authoritative controls for their owned semantics.

## Start baseline

- Repository: `Lost0rz/Engineering-Governance`
- Branch: `main`
- Verified repository HEAD before this control transition: `4f3d5308aa742014cfbb8a72adcdb18d5d7c147d`
- The SHA above is transition provenance for this task authorization; it is not an implementation equality lock.
- Published Plugin baseline remains `plugin-v0.5.3`, frozen release source `255bd32b1414a9555a7280d6e7562411ed3c7d96`.

## In scope

- Establish global terminology and semantics for `Repository HEAD`, `Delivery / Semantic HEAD`, `CONTROL_ONLY_CHANGE`, `CONTROL_ONLY_DRIFT`, `DELIVERY_HEAD_CHANGE`, and `SEMANTIC_TREE_EQUIVALENCE`.
- Treat changes limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md` as control-only for implementation freshness, exact-head evidence, CI validity, merge-readiness identity, and workspace closeout.
- Preserve material task-authorization changes as authoritative and enforceable even though their commit SHA is not implementation identity by default.
- Update the relevant Project Governance Skill/reference/template contracts consistently, especially `SKILL.md`, `control-identity.md`, `control-plane.md`, `verification-tiers.md`, `workspace-lifecycle.md`, `development-flow.md`, and status/task templates when needed.
- Demonstrate the five required scenarios from the supplied design: post-audit status update, post-merge closeout record, next-task reconciliation, real source drift, and material task-authorization change.
- Keep the change within the existing three-Skill architecture and current governance machinery.

## Out of scope

- Adding a daemon, hook, database, lifecycle service, installer, remediation runtime, or fourth Skill.
- Excluding `AGENTS.md`, workflows, tests, schemas, migrations, dependency manifests, runtime configuration, source code, or governance implementation from delivery identity by default.
- Weakening `CURRENT_TASK.md` as the authorization authority.
- Republishing or changing the already frozen `plugin-v0.5.3` release as part of planning.

## Known evidence

The user-supplied design explicitly requires control-only commits not to invalidate CI/audit/closeout and requires real source/config/test/schema/workflow changes to continue invalidating exact-head evidence when appropriate. Current Project Governance source still treats a source/status/task/documentation commit after final-head freeze as changing the identity being verified, so the existing contracts require reconciliation before implementation.

## Risk and rationale

Risk level: broad governance semantics. The change affects how all governed repositories interpret commit identity, verification freshness, and lifecycle closure, so inconsistent wording across references could produce unsafe false passes or noisy false stops.

## Verification level, cadence, and rationale

`V0` source/documentation verification with broad contract consistency because the reusable artifact is declarative governance source. Before modification, demonstrate the required RED scenarios against current text. During implementation, use focused contract/content checks. At task close, audit all affected Project Governance references/templates for consistent terminology and verify that real implementation drift and material authorization changes remain blocking where required.

## Acceptance criteria

- `CURRENT_STATUS.md` and `CURRENT_TASK.md` remain required controls and authoritative for their owned semantics.
- Their recorded SHAs are not implementation identity by default.
- Control-only commits do not by themselves invalidate CI, independent audit, merge-readiness, exact-head evidence, or workspace closeout.
- Semantic implementation equivalence can be established while excluding only `CURRENT_STATUS.md` and `CURRENT_TASK.md`.
- Real source/config/test/schema/workflow drift still invalidates implementation evidence when appropriate.
- Material task-authorization changes remain mandatory to read and obey before further mutation.
- No new governance runtime/machinery is introduced merely for this rule.

## Stop conditions

- Live `main` changes materially from the verified task baseline before branch construction and cannot be reconciled safely.
- Existing rules reveal an implementation-relevant authority not covered by the supplied design.
- The change would require excluding paths beyond `CURRENT_STATUS.md` and `CURRENT_TASK.md` without new authorization.
- The change would weaken task authorization, hide real delivery drift, or require new runtime machinery.

## Handoff / current stop point

Authorize read-only RED demonstration, design/plan capture, and subsequent reusable-source construction on a dedicated remote task branch. Do not publish a new Plugin release until this source change is independently audited and separately authorized for release.

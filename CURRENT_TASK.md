# CURRENT TASK — Control Files Noise Reduction

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CONTROL-DELIVERY-IDENTITY-055`

State: `IMPLEMENTATION_COMPLETE_AWAITING_INDEPENDENT_AUDIT`

Mode: governed reusable-source change

## Objective

Reduce governance noise globally by separating repository control-record changes from implementation/delivery identity while preserving `CURRENT_STATUS.md` and `CURRENT_TASK.md` as authoritative controls for their owned semantics.

## Start baseline

- Repository: `Lost0rz/Engineering-Governance`
- Branch authority began from `main` task-control transition `1a450aacb301e7c5a25dd88d17749911536d989c`.
- Verified Repository HEAD before that authorization transition: `4f3d5308aa742014cfbb8a72adcdb18d5d7c147d`.
- Those SHAs are transition provenance, not implementation equality locks.
- Published Plugin baseline remains `plugin-v0.5.3`, frozen release source `255bd32b1414a9555a7280d6e7562411ed3c7d96`.

## Implementation identity

Task branch: `codex/control-delivery-identity-055`.

`FROZEN_IMPLEMENTATION_HEAD = 5dcd7b4146da5d8f930ebd1ca04b8d9ee4703b0c`

Lock type: **Delivery / Semantic HEAD**.

A later Repository HEAD that differs from this candidate only through `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is expected to classify as `CONTROL_ONLY_DRIFT` and does not by itself invalidate the implementation candidate. Any non-excluded path change after this point is `DELIVERY_HEAD_CHANGE` and requires the implementation identity to be re-established.

## In scope

- Establish global terminology and semantics for `Repository HEAD`, `Delivery / Semantic HEAD`, `CONTROL_ONLY_CHANGE`, `CONTROL_ONLY_DRIFT`, `DELIVERY_HEAD_CHANGE`, and `SEMANTIC_TREE_EQUIVALENCE`.
- Treat changes limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md` as control-only for implementation freshness, exact-head evidence, CI validity, merge-readiness identity, and workspace closeout.
- Preserve material task-authorization changes as authoritative and enforceable even though their commit SHA is not implementation identity by default.
- Update the relevant Project Governance Skill/reference/template contracts consistently, including `SKILL.md`, `control-identity.md`, `control-plane.md`, `verification-tiers.md`, `workspace-lifecycle.md`, `development-flow.md`, and the affected control templates.
- Dogfood the rule in this repository's root `AGENTS.md` without excluding `AGENTS.md` itself from delivery/governance identity.
- Demonstrate the five required scenarios: post-audit status update, post-merge closeout record, next-task reconciliation, real source drift, and material task-authorization change.
- Keep the change within the existing three-Skill architecture and current governance machinery.

## Out of scope

- Adding a daemon, hook, database, lifecycle service, installer, remediation runtime, or fourth Skill.
- Excluding `AGENTS.md`, workflows, tests, schemas, migrations, dependency manifests, runtime configuration, source code, or governance implementation from delivery identity by default.
- Weakening `CURRENT_TASK.md` as the authorization authority.
- Republishing or changing the already frozen `plugin-v0.5.3` release in this source task.

## Known evidence

Before source modification, the current contracts demonstrated the required RED baseline:

- A: final-head freeze wording could make a post-audit control-only update invalidate literal exact-head identity;
- B: workspace closeout lacked an explicit guard against later control-only main advances reopening the lifecycle;
- C: lifecycle wording could force an intermediate prior-task closeout control transition before next-task authorization;
- D: real source/config/test/schema/workflow drift already remained an invalidating guard and must remain so;
- E: material `CURRENT_TASK.md` content already remained authoritative and must remain so.

The constructed candidate now defines the two-head model centrally in `control-identity.md` and applies it through verification, control-plane, development-flow, workspace-lifecycle, root dogfooding guidance, and the affected templates.

## Risk and rationale

Risk level: broad governance semantics. The change affects how governed repositories interpret commit identity, verification freshness, and lifecycle closure. The main failure risks are exclusion creep, false preservation of evidence after real implementation drift, or weakening task authorization.

## Verification level, cadence, and rationale

`V0` declarative-source verification with broad contract consistency.

Required close verification:

- prove the post-candidate control reconciliation changes only `CURRENT_STATUS.md` / `CURRENT_TASK.md`;
- verify `SEMANTIC_TREE_EQUIVALENCE = PASS` relative to `FROZEN_IMPLEMENTATION_HEAD`;
- verify the exclusion set is exactly the two control files;
- verify mixed control+non-control changes remain `DELIVERY_HEAD_CHANGE`;
- verify explicit literal Repository HEAD locks remain enforceable;
- verify material task-content changes remain authoritative;
- verify the repository still exposes exactly three top-level Skills and no new runtime machinery was added;
- inspect the complete PR diff before independent audit.

## Acceptance criteria

- `CURRENT_STATUS.md` and `CURRENT_TASK.md` remain required controls and authoritative for their owned semantics.
- Their recorded SHAs are not implementation identity by default.
- Control-only commits do not by themselves invalidate CI, independent audit, merge-readiness, exact-head evidence, or workspace closeout.
- Semantic implementation equivalence excludes exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`.
- Real source/config/test/schema/workflow/dependency/migration/runtime-relevant drift still invalidates implementation evidence when appropriate.
- Mixed control+implementation commits classify as `DELIVERY_HEAD_CHANGE`.
- Explicit literal Repository HEAD locks remain enforceable.
- Material task-authorization changes remain mandatory to read and obey before further mutation.
- No new governance runtime/machinery is introduced merely for this rule.

## Stop conditions

- Live `main` changes materially from the verified task baseline in a way that affects this task before PR integration and cannot be reconciled safely.
- The change would require excluding paths beyond `CURRENT_STATUS.md` and `CURRENT_TASK.md` without new authorization.
- Any final candidate change touches a non-excluded path after `FROZEN_IMPLEMENTATION_HEAD` without explicitly replacing the frozen implementation identity and repeating required verification.
- The change would weaken task authorization, hide real delivery drift, or require new runtime machinery.

## Handoff / current stop point

Reusable-source construction is complete at semantic implementation candidate `5dcd7b4146da5d8f930ebd1ca04b8d9ee4703b0c`.

The current control reconciliation is intentionally allowed to advance literal Repository HEAD without changing that Delivery / Semantic HEAD. Verify that classification, finish the cross-contract audit, open a Draft PR, and then stop for independent Web/source audit. Do not publish a new Plugin release under this task and do not create later control commits solely to memorialize CI/review/audit outcomes.

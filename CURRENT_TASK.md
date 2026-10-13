# CURRENT TASK — Control Files Noise Reduction

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CONTROL-DELIVERY-IDENTITY-055`

State: `CORRECTIVE_COMPLETE_AWAITING_INDEPENDENT_REAUDIT`

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

`FROZEN_IMPLEMENTATION_HEAD = 04a20a5ce05e28307ccf7a249acf83866493ffe0`

Lock type: **Delivery / Semantic HEAD**.

A later Repository HEAD that differs from this candidate only through `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` is expected to classify as `CONTROL_ONLY_DRIFT` and does not by itself invalidate the semantic implementation candidate. Any non-excluded path change after this point is `DELIVERY_HEAD_CHANGE` and requires the implementation identity to be re-established.

Repository-host gates are not covered by semantic equivalence. Required checks/reviews, mergeability/conflicts, merge queue, current-base/latest-head rules, and other applicable host requirements must be read live for the literal identity the repository host governs before merge/release.

## In scope

- Establish global terminology and semantics for `Repository HEAD`, `Delivery / Semantic HEAD`, `CONTROL_ONLY_CHANGE`, `CONTROL_ONLY_DRIFT`, `DELIVERY_HEAD_CHANGE`, and `SEMANTIC_TREE_EQUIVALENCE`.
- Treat changes limited to `CURRENT_STATUS.md` and `CURRENT_TASK.md` as control-only for implementation freshness, semantic CI/test validity, semantic review/audit validity, and workspace closeout.
- Preserve repository-host gates as separate live literal constraints; never infer current host-gate PASS solely from semantic-tree equivalence or older host state.
- Preserve material task-authorization changes as authoritative and enforceable even though their commit SHA is not implementation identity by default.
- Update the relevant Project Governance Skill/reference/template contracts consistently, including `SKILL.md`, `control-identity.md`, `control-plane.md`, `verification-tiers.md`, `workspace-lifecycle.md`, `development-flow.md`, and the affected control templates.
- Dogfood the rule in this repository's root `AGENTS.md` without excluding `AGENTS.md` itself from delivery/governance identity.
- Demonstrate the five required scenarios: post-audit status update, post-merge closeout record, next-task reconciliation, real source drift, and material task-authorization change.
- Keep the change within the existing three-Skill architecture and current governance machinery.

## Out of scope

- Adding a daemon, hook, database, lifecycle service, installer, remediation runtime, or fourth Skill.
- Excluding `AGENTS.md`, workflows, tests, schemas, migrations, dependency manifests, runtime configuration, source code, or governance implementation from delivery identity by default.
- Weakening `CURRENT_TASK.md` as the authorization authority.
- Overriding or bypassing repository-host branch protection, rulesets, required checks/reviews, merge queues, conflict checks, or literal head/base requirements.
- Republishing or changing the already frozen `plugin-v0.5.3` release in this source task.

## Known evidence

Before source modification, the current contracts demonstrated the required RED baseline:

- A: final-head freeze wording could make a post-audit control-only update invalidate literal exact-head identity;
- B: workspace closeout lacked an explicit guard against later control-only main advances reopening the lifecycle;
- C: lifecycle wording could force an intermediate prior-task closeout control transition before next-task authorization;
- D: real source/config/test/schema/workflow drift already remained an invalidating guard and must remain so;
- E: material `CURRENT_TASK.md` content already remained authoritative and must remain so.

Independent audit of the first implementation candidate identified one Important corrective: semantic implementation evidence and repository-host gate state had been conflated. The corrected candidate now keeps semantic CI/review/audit evidence reusable across proven `CONTROL_ONLY_DRIFT` while requiring current repository-host gates to be read and satisfied separately for the literal identity the host governs.

## Risk and rationale

Risk level: broad governance semantics. The change affects how governed repositories interpret commit identity, verification freshness, merge readiness, and lifecycle closure. The main failure risks are exclusion creep, false preservation of evidence after real implementation drift, weakening task authorization, or incorrectly treating semantic equivalence as repository-host gate satisfaction.

## Verification level, cadence, and rationale

`V0` declarative-source verification with broad contract consistency.

Required close verification:

- prove any post-candidate reconciliation changes only `CURRENT_STATUS.md` / `CURRENT_TASK.md`;
- verify `SEMANTIC_TREE_EQUIVALENCE = PASS` relative to `FROZEN_IMPLEMENTATION_HEAD` when Repository HEAD later moves only through controls;
- verify the exclusion set is exactly the two control files;
- verify mixed control+non-control changes remain `DELIVERY_HEAD_CHANGE`;
- verify explicit literal Repository HEAD locks remain enforceable;
- verify material task-content changes remain authoritative;
- verify semantic implementation evidence reuse is distinct from repository-host gate satisfaction;
- verify current host-gate PASS can only be claimed from live host evidence for the identity the host governs;
- verify the repository still exposes exactly three top-level Skills and no new runtime machinery was added;
- inspect the complete PR diff before independent re-audit.

## Acceptance criteria

- `CURRENT_STATUS.md` and `CURRENT_TASK.md` remain required controls and authoritative for their owned semantics.
- Their recorded SHAs are not implementation identity by default.
- Control-only commits do not by themselves invalidate semantic CI/test, code-review, or independent-audit conclusions when semantic equivalence and task conditions permit reuse.
- Semantic implementation equivalence excludes exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`.
- Repository-host gates remain independently live and literal where the host defines them that way; `HOST_GATE_PASS` is not inferred from semantic equivalence.
- Real source/config/test/schema/workflow/dependency/migration/runtime-relevant drift still invalidates implementation evidence when appropriate.
- Mixed control+implementation commits classify as `DELIVERY_HEAD_CHANGE`.
- Explicit literal Repository HEAD locks remain enforceable.
- Material task-authorization changes remain mandatory to read and obey before further mutation.
- No new governance runtime/machinery is introduced merely for this rule.

## Stop conditions

- Live `main` changes materially from the verified task baseline in a way that affects this task before PR integration and cannot be reconciled safely.
- The change would require excluding paths beyond `CURRENT_STATUS.md` and `CURRENT_TASK.md` without new authorization.
- Any final candidate change touches a non-excluded path after `FROZEN_IMPLEMENTATION_HEAD` without explicitly replacing the frozen implementation identity and repeating required verification.
- The change would weaken task authorization, hide real delivery drift, bypass a repository-host gate, or require new runtime machinery.

## Handoff / current stop point

The first independent audit found one Important repository-host-gate boundary defect; the bounded corrective is complete at semantic implementation candidate `04a20a5ce05e28307ccf7a249acf83866493ffe0`.

This `CURRENT_TASK.md` reconciliation intentionally advances literal Repository HEAD without changing that Delivery / Semantic HEAD. Verify the post-candidate diff is control-only, perform independent re-audit of the corrected contracts, and merge only if required semantic evidence remains valid **and** current repository-host gates pass. Do not publish a new Plugin release under this task and do not create later control commits solely to memorialize CI/review/audit/host-gate outcomes.

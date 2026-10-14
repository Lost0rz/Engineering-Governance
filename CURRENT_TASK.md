# CURRENT TASK — Contract Corrective v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-CONTRACT-CORRECTIVE-069`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Apply the bounded corrective identified by the detailed eight-Skill source audit: tighten Project Profile mutation authority, Card/Receipt schema, capability-vs-mode semantics, artifact lifecycle taxonomy, compact status receipt requirements, Profile surface ownership, advisory-vs-formal audit boundaries, and acceptance coverage without adding new Skills or control files.

## In scope

- require compatible Project Governance / `CURRENT_TASK.md` authorization before repository/project-managed Profile mutation;
- distinguish required vs conditional Handoff Card fields and add explicit `CAPABILITY` / `PURPOSE` semantics;
- state that Handoff `MODE` is a transfer side-effect/action class and does not replace Skill routing;
- include `MODE` / `TARGET` in standard receipts;
- separate implementation authority from observed evidence in artifact lifecycle taxonomy;
- make the compact Engineering Status Receipt the normal required ending for governed engineering/status/audit/CI/PR/merge responses while avoiding duplicate full receipts;
- define one current Project Profile projection surface (or explicit primary + mirror) to avoid Profile duplication/staleness;
- distinguish advisory read-only inspection from formal acceptance/readiness audit task boundaries;
- align Profile landing-page/recovery wording;
- slim Domain Navigation top-level Skill without changing behavior;
- extend integrated acceptance scenarios for these boundaries.

## Out of scope

- new top-level Skills;
- runtime/daemon/database/model-router/automatic enforcement;
- installed Plugin/Web/Codex acceptance;
- unrelated architecture expansion;
- changing `ENVIRONMENT_DEFAULT_ONLY` or stronger-model escalation policy.

## Verification / acceptance

- V2 remote source-architecture audit after correction;
- exact eight-Skill directory set remains unchanged;
- no competing task/control authority;
- no Profile/Domain/AGENTS duplication;
- Card/Receipt schema is internally consistent and side-effect-safe;
- artifact taxonomy cleanly separates authority from evidence;
- routing/composition remains lightweight and non-recursive;
- PR/host identity checked fresh; CI PASS only if evidence exists.

## Stop conditions

Stop before further mutation if branch/head authority changes unexpectedly, new unique/unknown work appears, or a correction would require architecture expansion outside this bounded objective.

## Workspace / lifecycle

Continue PR #26 and branch `codex/capability-model-v0.6.0`; do not create a successor PR/worktree solely for this correction.

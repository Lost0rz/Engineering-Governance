# CURRENT TASK — Design Routing Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ROUTING-HARDENING-083`

Task class: `CAPABILITY_HARDENING`

State: `COMPLETE`

## Objective

Harden the published `design` capability so it remains the primary owner of bounded UI/UX/frontend design work without becoming artificially isolated from other Engineering Governance capabilities.

The published behavior is **evidence-triggered composition**:

- stay inside Design by default;
- cross a Skill boundary only for a concrete unresolved dependency that materially affects the current decision;
- state the missing question and bounded expected return before crossing;
- use the smallest capability that owns the dependency;
- return the bounded result to the originating Design stage rather than restarting the whole pipeline.

## Published routing behavior

### Design vs Solution Design

- `design` owns interaction workflow: how users see, understand, navigate, edit, review, act, receive feedback and complete a frontend task.
- `solution-design` owns materially ambiguous business/state workflow: canonical state transitions, data/state ownership, API/data-flow responsibility, persistence semantics and implementation boundaries.
- Mixed tasks may use both only when both material problems actually exist.

### Evidence-triggered cross-Skill composition

A Design cross-Skill call carries:

- `UNRESOLVED_DEPENDENCY`;
- `DESIGN_IMPACT`;
- `CAPABILITY`;
- `EXPECTED_RETURN`;
- `RESUME_STAGE`.

`domain-navigation` remains a valid bounded dependency when backend/product authority/source/symbol/state-owner/runtime/test routing is genuinely unclear. Other capabilities remain callable only on their own real triggers.

General enrichment, completeness, generic second opinions, or mere Skill availability do not justify a call.

## Design modes

Published modes:

- `AUDIT_ONLY` — audit/findings only;
- `DESIGN_SPEC` — design package through pre-build gate, no forced implementation;
- `DESIGN_IMPLEMENT` — full design-to-implementation/review/visual-acceptance loop;
- `FINAL_REVIEW` — review/correct an existing implementation without automatically reopening upstream design direction.

For full implementation with rendering support:

`context/audit → Anthropic reasoning → admin pattern when applicable → bounded design spec → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`.

## Acceptance / release result

- PR: `#32 — feat: harden Design routing composition` — `MERGED`;
- accepted pre-merge semantic candidate: `f0f1ebf6a9c7c49c106955cfb84940a645635dc4`;
- pre-merge workflow: `Release Plugin v0.7.1`;
- successful PR run: `38658235439` / run #2;
- source / merge SHA: `208279e5f3b7974c13a3446a3db2e8f27de7b688`;
- main release run: `38658367623` / run #5 — `success`;
- tag: `plugin-v0.7.1`;
- GitHub Release ID: `413290156`;
- release asset ID: `642098498`;
- asset size: `134882` bytes;
- asset SHA-256: `8a2482eb4c0e28c642b5d27ffe34c0e64c0b8d64afbf9c51c6b83325013055db`;
- package entries: `61`;
- top-level Skills: exactly `9`;
- Plugin payload: `plugin.json + skills/**` only.

`V071_PREMERGE_ACCEPTANCE`: `PASS`.
`FORMAL_RELEASE_071`: `PASS`.

## Web Plugin result

Existing private Web Plugin updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.1`;
- Web release ID: `pluginrel_6ad01a9215e88191829245c5571fd160`;
- scope/discoverability: `USER / PRIVATE` unchanged;
- root/platform manifests and routing/Design hardening files read back successfully.

`WEB_PLUGIN_SYNC_071`: `PASS`.

## Local runtime boundary

The last directly observed Air Local Codex installation remains `0.6.8`. No newer local runtime state is inferred without a fresh readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082` (`COMPLETE`)
- `START_MAIN_HEAD`: `06301c8ff5c074ea16e26a4e01a0755d52d43e24`
- `TASK_BRANCH`: `codex/design-routing-hardening-v071`
- `PR`: `#32` (`MERGED`)
- `TARGET_VERSION`: `0.7.1`
- `TOP_LEVEL_SKILLS_TARGET`: `9`
- `DESIGN_EXTERNAL_ROUTE`: `design`
- `PREMERGE_SEMANTIC_HEAD`: `f0f1ebf6a9c7c49c106955cfb84940a645635dc4`
- `PREMERGE_CI_RUN`: `38658235439`
- `PREMERGE_CI`: `PASS`
- `RELEASE_SEMANTIC_HEAD`: `208279e5f3b7974c13a3446a3db2e8f27de7b688`
- `RELEASE_CI_RUN`: `38658367623`
- `FORMAL_RELEASE_071`: `PASS`
- `WEB_PLUGIN_SYNC_071`: `PASS`
- `TASK_STATE`: `COMPLETE`

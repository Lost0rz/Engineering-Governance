# CURRENT TASK — Handoff Card Generation Corrective

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-HANDOFF-CARD-GENERATION-CORRECTIVE-079`

Task class: `CORRECTIVE_RELEASE`

State: `AUTHORIZED_IN_PROGRESS`

## Objective

Correct the reusable cross-context Handoff Card generation defect exposed by real ChatGPT Web use, then publish and synchronize the corrected Engineering Governance Plugin so Web and Local Codex can consume the same source contract.

The defect is not that the Handoff schema is absent. The shipped `agent-handoff` source contains the required fields, but generation can still return a legacy execution card that:

- does not route through the bounded `agent-handoff` capability;
- emits an invalid mode such as `CORRECTIVE` instead of `EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE`;
- omits required core fields such as `CARD_ID`, `CAPABILITY`, `TARGET`, `AUTHORITY`, `DELTA`, `BOUNDARY`, or `RETURN_CONTRACT`;
- duplicates task/plan scope rather than carrying only fresh transfer delta;
- promotes observed SHAs into execution locks without owning authority;
- hard-codes a successful final state instead of returning the observed outcome.

## Authorization basis

Task 078 explicitly required a separately authorized source corrective when a reusable source defect appeared during local routing/handoff acceptance. The user has now explicitly authorized repairing the Plugin source and synchronizing the remote repository and ChatGPT Web Plugin.

Task 078 is therefore superseded as the active authorization while its local integrated-acceptance conclusion remains unresolved. Its accepted v0.6.6 release/install evidence remains historical evidence, not current release authority.

## Authorized source changes

Keep the correction narrow and reusable:

1. `project-governance` routing must explicitly recognize generation of instructions/cards for another agent/session/machine/execution context as a mandatory `agent-handoff` boundary rather than letting a generic execution-card format bypass it.
2. `agent-handoff` must apply a mandatory pre-return compliance gate to generated Cards and structured Receipts.
3. The pre-return gate must enforce the required core schema and valid MODE set, preserve `TASK_ID` unless Project Governance changed task authority, keep Card content delta-oriented rather than duplicating `CURRENT_TASK.md`, and prevent a Card from inventing authority/head locks or optimistic success states.
4. The Handoff request/receipt templates and contract may be updated only as needed to make the generation/return requirements operationally unambiguous.
5. Integrated acceptance must add a negative case reproducing the real legacy-card failure class.
6. Release validation must check the strengthened Handoff contract rather than only confirming that field names happen to exist in a template.
7. Bump the Plugin to the next patch release and publish the corrected source through the existing repository/Plugin distribution model.

## Preserve

- exactly eight top-level Skills;
- `project-governance` as task/control/lifecycle owner;
- `agent-handoff` as transport, never a second task authority;
- `CAPABILITY` and `MODE` as independent dimensions;
- same-purpose continuation keeps the same `TASK_ID`;
- Handoff/Receipt artifacts remain observed evidence/transport, not a fourth control source;
- environment-specific runtime/model/tool values remain owned by the receiving environment;
- no daemon, scheduler, database, installer service, model router, automatic enforcement runtime, or cache patching;
- no unrelated Project Profile/Domain/Doctor/Orchestrator redesign.

## Verification

Before publication verify at minimum:

- source still exposes exactly eight top-level Skills;
- Handoff Card required-core schema is present and the mandatory pre-return gate is explicit;
- generated-card negative acceptance requires valid `MODE`, all required core fields, authority references + fresh delta rather than duplicated task contract, non-invented head locks, and outcome-dependent final state;
- Project Governance explicitly routes cross-context Card/instruction generation to Agent Handoff;
- release/package validation checks those strengthened invariants;
- Plugin package remains `plugin.json` + `skills/**` only;
- remote branch/PR identity is exact for review/merge;
- after merge, formal release and ChatGPT Web Plugin identities are read back before claiming synchronization.

## Release / distribution boundary

A corrected release may be published only from merged accepted source. Synchronize:

1. repository `main` / formal GitHub Plugin release;
2. the existing private personal ChatGPT Web Plugin `plugins_6acb0b9e8b748191a9b89fad47d89517` without changing its audience/scope;
3. leave Local Codex cache untouched; Local should consume the published repository/marketplace version through its supported update mechanism.

## Stop conditions

STOP if:

- the correction would require changing the eight-Skill capability model;
- the Plugin cannot be updated without changing identity/scope or manually patching an installed cache;
- source/branch evidence reveals unexplained unique work or conflicting active writer authority;
- a material architecture decision beyond this Handoff-generation defect appears;
- formal release or Web Plugin readback does not match the intended source identity/version.

## Terminal boundary

This task is complete only when:

- source corrective is merged to `main`;
- the new formal Plugin release succeeds for that merged source;
- the existing ChatGPT Web Plugin is updated and read back at the same corrected version/content boundary;
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` are reconciled to the final state;
- Local Codex can update from the published source without manual cache mutation.

Control Alignment:

- `PREDECESSOR_TASK`: `EG-V066-RELEASE-078`
- `DEFECT_SOURCE`: real Web Handoff Card generation
- `SOURCE_CORRECTIVE`: `AUTHORIZED`
- `WEB_PLUGIN_SYNC`: `AUTHORIZED`
- `LOCAL_CACHE_MUTATION`: `NOT_AUTHORIZED`
- `CONTROL_ALIGNMENT`: `PASS`

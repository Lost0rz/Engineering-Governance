# CURRENT TASK — Phase E RemoteOrbit Real-Project Pilot Design

Task ID: `EG-REMOTEORBIT-PILOT-DESIGN-017`

State: `WAITING_FOR_USER_DESIGN_REVIEW`

Mode: `BOUNDED_INTEGRATION_DESIGN`

## Objective

Design the first real-project validation of the merged Engineering-Governance Skills against `Lost0rz/RemoteOrbit`, using current repository evidence to test whether Project Governance, Domain Navigation, and Incident Doctor are practical, lightweight, and internally coherent in a complex live project.

This task is design-only. No RemoteOrbit mutation is authorized until the user approves the bounded pilot design and the target repository's own active control plane permits a safe transition.

## Authority and baselines

- Engineering-Governance accepted Phase D merge head: `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- Candidate target: `Lost0rz/RemoteOrbit`.
- RemoteOrbit read-only observed `main`: `5b9c48ace92818e15850eaa3f21399b1cc2f4031`.
- RemoteOrbit currently owns an active runtime-evidence maintenance task for incident `RO-INCIDENT-20261004-01`; its controls prohibit unrelated mutation.
- No `DOMAIN_MAP` result was found on the RemoteOrbit default branch in the read-only search used for this design.

## Proposed pilot

The pilot should be evidence-first and two-stage.

### Stage 1 — read-only validation

Against the exact target revision selected at execution time:

- read RemoteOrbit `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, relevant source/manifests/tests, and incident/runtime evidence needed for the active domains;
- compare the existing controls against the merged `project-governance` contract without blindly replacing useful project-specific rules;
- identify the smallest useful semantic Domains and their authority/entry-point/test/evidence routes using `domain-navigation`;
- evaluate the current incident representation against the merged `incident-doctor` evidence taxonomy, sufficiency gate, falsification, runtime identity, fix boundary, and probe lifecycle rules;
- keep unsupported facts explicit as unknown;
- record concrete friction found in the reusable Skills, if any.

Stage 1 must not modify RemoteOrbit.

### Stage 2 — adoption package after safe target transition

Only when RemoteOrbit's own control plane explicitly permits governance-file mutation:

- adapt, do not blindly copy, the three control files;
- add a minimal `DOMAIN_MAP.md` and only justified detailed `DOMAIN.md` files;
- add or adapt an Incident record only if it improves the live evidence chain without creating duplicate authority;
- preserve RemoteOrbit-specific runtime/evidence rules that remain valid;
- remove duplicated or historical material only when current target evidence proves it is safe;
- verify the target delta proportionally and independently before merge.

The later adoption change is a separate authorization. This design does not authorize it yet.

## Validation success criteria

The pilot succeeds only if a fresh AI can use the adapted model to answer, with less broad reading and without inventing facts:

- what work is authorized now;
- which Domain owns the relevant state/behavior;
- which sources/symbols/tests should be read next and why;
- whether Incident Doctor should trigger;
- what evidence is sufficient versus missing;
- what remains unknown;
- what the smallest safe next action is.

The pilot must also identify whether any reusable Skill guidance is too heavy, ambiguous, duplicative, or missing. Reusable changes are made only if the real pilot demonstrates a concrete gap.

## Boundaries

Do not:

- mutate RemoteOrbit during this design task;
- interrupt or reinterpret its active incident task;
- copy Engineering-Governance templates verbatim over target-specific truth;
- create a fourth Skill;
- add runtime code, CLI, daemon, database, index, telemetry platform, or installer;
- treat a generated map/example as product/runtime authority;
- add an `examples/RemoteOrbit` example before the real target validation is complete;
- make reusable Skill changes merely for stylistic preference.

## Current stop point

`WAITING_FOR_USER_DESIGN_REVIEW`

After explicit approval, Web should authorize a bounded Stage-1 read-only pilot. RemoteOrbit mutation remains separately gated by its own control plane.

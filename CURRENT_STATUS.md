# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.x release has been created yet.

## v0.6.x source architecture / current semantic candidate

The eight-Skill architecture remains accepted. Current corrected Delivery / Semantic candidate:

`1b46159acfda4ec2c36af46b6da58ad26c1b5482`

Completed acceptance-driven correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff templates aligned with Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile compactness/generic-workflow deduplication.
- `EG-V060-PROFILE-BOUNDARY-CORRECTIVE-073` — surface-role evidence, Domain deduplication, meta-procedure exclusion and normative-rule compression.
- `EG-V060-PROFILE-GROUNDING-CORRECTIVE-074` — claim grounding, Memory/history isolation, old-Profile revalidation and authority-class preservation.
- `EG-V060-PROFILE-DURABILITY-CORRECTIVE-075` — fact grounding is now followed by a durability gate so current-stage delivery/runtime facts are not promoted into long-lived Profile context.

PR #26 remains OPEN / DRAFT / UNMERGED. Host facts are reread at their own boundary; CI/check PASS is not claimed without current evidence.

## Project Profile contract after Task 075

Project Profile construction now uses:

```text
Grounding Gate
→ Durability Gate
→ Classification / authority placement
→ Compression / deduplication
→ Project Profile
```

Task 075 establishes:

- `verified != durable`;
- grounded current task/milestone/wave/MVP priority/next-step facts stay out of the durable Profile by default;
- current-stage non-goals/deferrals/sequencing choices do not become permanent project anti-goals merely because they are currently approved;
- temporary development/acceptance machine names, ports, endpoints, branches/worktrees, runners, executables, local paths and process arrangements stay out of durable `Environment` content;
- provisional/current implementation or acceptance shape stays in planning/runtime authority rather than being promoted into project identity;
- explicit durable/version-scoped architecture remains eligible when the owning authority says so, preserving qualifiers such as `V1` or `long-term`;
- existing grounding, Memory isolation, authority-class preservation, Domain deduplication and governance deduplication remain in force;
- generated Profiles must preserve shipped fixed metadata field names `Profile surface` and `Primary/mirror role`.

The practical durability test is whether a statement would still belong in the Profile if the current task/milestone completed tomorrow.

## Task 075 source verification

Focused compare from the Task-075 control checkpoint changed only:

- `plugin.json`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `skills/project-profile/SKILL.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `skills/project-profile/references/profile-contract.md`.

No other Skill or capability architecture changed.

Integrated acceptance now includes:

- Gift-like durability case excluding development-stage machines/ports/endpoints and stage-only non-goals;
- MemoX-like durability case excluding current MVP/wave/viewer shape while retaining explicitly scoped `V1 Local Store` / `long-term Core` architecture;
- fixed metadata field enforcement;
- prior Task 072–074 compactness, surface, grounding and authority-class cases.

## Web Plugin candidate acceptance

Parent Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is restored to `WAITING_FRESH_WEB_SESSION`.

Current installed personal Web Plugin candidate:

- Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.6.4`;
- release: `pluginrel_6acf306eeacc8191814073d8973b3e39`;
- scope/discoverability: `USER / PRIVATE`;
- root `plugin.json` and platform-managed `.codex-plugin/plugin.json` both report `0.6.4`;
- Task-075 overlay contained only `plugin.json` plus the three corrected `project-profile` shipped files;
- overlay ZIP SHA-256: `2188cfba9084a8c2a51319217bbb613c4c7de5290a506e998455053be6b2c535`;
- packaged Git-blob identities matched repository source for all four uploaded files before installation;
- post-update installed-file readback confirms Task-075 Skill/template/contract content is active.

Fresh Web evidence retained from earlier candidates:

- exact eight top-level Skill discovery: PASS;
- ordinary status/progress inspection -> `project-governance`: PASS;
- advisory inspection avoids over-routing: PASS;
- Profile live-state exclusion: PASS;
- Task 074 grounding/Memory isolation and authority-class preservation materially improved behavior.

Task 075 source/package corrective is complete; behavioral durability acceptance is now pending fresh Web `0.6.4` sessions.

## Next milestone

Run fresh cross-project Project Profile regressions against Web Plugin `0.6.4`:

1. Gift: no Memory-only product preferences; no development-stage Mac mini/Air or `:3000` acceptance endpoint; stage-only non-goals not promoted; durable B2B/RFQ identity retained.
2. MemoX: no current Codex MVP/wave/viewer acceptance shape promoted into durable identity; `V1 SQLite`, `long-term Rust Core`, and authority-class distinctions retained with scope.
3. FloatTabs: old Project Instructions do not self-bootstrap; Domain Map remains a pointer rather than mini-map; temporary/current runtime state stays out.
4. Fixed header: `Profile surface` + `Primary/mirror role` preserved.

If these regressions and remaining Task-070 routing scenarios pass, proceed to Local Codex integrated acceptance. Formal GitHub release/merge remains deferred until that boundary is supported.

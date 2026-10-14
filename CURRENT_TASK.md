# CURRENT TASK — Project Profile Durability Corrective 075

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-DURABILITY-CORRECTIVE-075`

Parent task: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `CORRECTIVE / EXECUTE`

State: `ACTIVE`

## Objective

Correct the reusable Project Profile defect exposed independently by fresh Gift and MemoX Web regressions: a project claim may be factually verified yet still be unsuitable for a durable Project Profile because it is current-stage delivery state, temporary runtime/acceptance configuration, current MVP/non-goal scope, or other short-lived operational context.

Establish an explicit **Durability Gate** after source grounding and before Profile classification/compression.

## Verified regression evidence

Gift regression on Web Plugin `0.6.3`:

- Memory-only merchandise/visual preferences no longer leaked into the Profile: grounding corrective PASS;
- current development-stage Mac mini/Air acceptance setup and locked `:3000` endpoint were nevertheless promoted into `Environment`;
- current storefront non-goals were partly promoted into durable Profile constraints;
- detailed Merloom/Gift ownership was still more expansive than needed when an established Domain Map exists.

MemoX regression on Web Plugin `0.6.3`:

- Memory contamination: PASS;
- storage/evidence/projection/canonical authority-class preservation: PASS;
- current Codex-only delivery priority, current MVP viewer/runtime shape, and some current delivery anti-goals were promoted into durable Profile content;
- shipped fixed header was not followed exactly (`Profile role` replaced `Primary/mirror role`).

Reusable defect:

```text
VERIFIED CLAIM
!=
DURABLE PROFILE-OWNED CLAIM
```

## Required behavior

Project Profile construction must use:

```text
Grounding Gate
→ Durability Gate
→ Classification / Authority placement
→ Compression
→ Profile
```

A grounded claim belongs in the durable Profile only when it is stable across ordinary task/PR/release/runtime progression and materially reduces future project-orientation cost.

Default-exclude from durable Profile unless explicitly established as durable project identity/architecture:

- current task/milestone/wave/MVP gate or current delivery priority;
- temporary development/acceptance machine, port, endpoint, branch, worktree, runner, executable, local path, or runtime arrangement;
- current-stage non-goals/deferred work that may change after the active delivery phase;
- current implementation/acceptance status such as read-only viewer, temporary shell, current integration path, or provisional runtime shape;
- current sequence/order frozen only for a delivery overlay rather than long-lived architecture/product identity.

Allowed when truly durable and current authority supports that durability:

- long-lived product purpose and stable anti-goals;
- accepted architecture choices explicitly scoped as long-term or durable/versioned architecture (for example a V1 Local Store or long-term Core language when the project authority says so);
- stable authority boundaries and role distinctions;
- durable project environment roles, not temporary machine/port values;
- durable pointers to planning/navigation authorities.

Version-scoped architecture may be included when its scope is explicit and materially useful; do not silently convert `current MVP`/`current wave` into permanent project identity.

## Scope

Modify only:

- `skills/project-profile/SKILL.md`;
- `skills/project-profile/references/profile-contract.md`;
- `skills/project-profile/assets/templates/PROJECT_PROFILE.md`;
- `references/V060_INTEGRATED_ACCEPTANCE.md`;
- `plugin.json` patch version for the Web candidate;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` for control reconciliation;
- PR #26 description for acceptance provenance.

No other Skill or capability architecture changes.

## Acceptance

Required source/contract checks:

1. Grounding and durability are distinct gates.
2. `verified != durable` is explicit.
3. Current-stage/runtime/endpoint/delivery-wave facts are excluded by default from durable Profile content.
4. Durable/version-scoped architecture can remain when authority explicitly establishes its scope.
5. Shipped template fixed fields remain fixed: `Profile surface` and `Primary/mirror role`.
6. Existing Domain Map dedup and governance dedup remain in force.
7. Integrated acceptance includes Gift-like and MemoX-like durability negative cases plus a positive durable/version-scoped architecture case.
8. Package/install readback matches repository source.

## Out of scope

- changing ChatGPT Memory behavior;
- changing current Profile grounding rules established by Task 074 except where needed to sequence the Durability Gate;
- adding a ninth Skill or new architecture layer;
- changing Gift, MemoX, or FloatTabs repositories;
- formal immutable GitHub v0.6.x release/tag;
- PR #26 merge;
- Local Codex acceptance.

## Stop conditions

Stop if the correction requires changing another Skill, changing project authority semantics, or expanding into a general temporal knowledge system rather than a bounded Profile-membership test.

## Terminal boundary

Task 075 closes when source, template, integrated acceptance and Web Plugin candidate are updated and read back successfully. Then restore parent Task 070 to fresh Web-session regression testing against the new candidate.

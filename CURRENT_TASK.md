# CURRENT TASK — Project Profile Boundary Corrective v0.6.x

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-PROFILE-BOUNDARY-CORRECTIVE-073`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Correct three reusable Project Profile defects exposed by the fresh FloatTabs Web regression while preserving the accepted eight-Skill architecture and the compact derived-context model.

Parent acceptance purpose: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`.

## Acceptance finding basis

The fresh FloatTabs Project Profile was substantially improved and its project facts were supported by current repository authorities, but three reusable output defects remained:

1. it emitted `Primary/mirror role: MIRROR` without evidence identifying a primary Profile surface;
2. it reproduced a reduced Domain Model even though an established `docs/architecture/DOMAIN_MAP.md` already owned detailed Domain/navigation mapping;
3. it added reusable meta-procedure (`Planning & Navigation` startup steps and a `Project Profile Rule` section explaining how to maintain/classify the Profile) instead of keeping only pointers.

A related pressure remains: project-specific normative MUST/MUST-NOT rules should stay in `AGENTS.md`; Profile priorities/constraints should be stable risk cues/anti-goals rather than a copied normative rulebook.

## In scope

- harden `skills/project-profile/SKILL.md` and `references/profile-contract.md` so `MIRROR` requires evidence of a named/identifiable primary surface;
- when no competing Profile surface is established, prefer `single surface`; use `PRIMARY` only when project/user authority designates the target as primary/canonical among profile surfaces;
- prohibit duplicating established Domain/navigation authority as a reduced Domain Model/source-symbol map; retain only the minimum stable concepts needed for orientation plus a pointer;
- prohibit step-by-step startup/navigation workflow and Profile-maintenance/classification/meta-procedure in the generated Profile;
- clarify that copied project-specific MUST/MUST-NOT lists belong in normative authority while Profile may retain concise priorities/anti-goals/risk cues;
- update the shipped Profile template and integrated acceptance negative scenarios;
- align Plugin package version for the refreshed Web candidate and update the existing personal Plugin through the guarded update path;
- focused source audit and installed-file verification;
- return to Task 070 after the corrective is frozen and Web candidate is ready for retest.

## Out of scope

- changing the eight-Skill model or routing architecture;
- changing Project Governance task authority;
- editing FloatTabs source/profile/control files;
- changing Domain Navigation semantics;
- formal GitHub release/tag or PR #26 merge;
- Local Codex acceptance;
- patching installed caches as source authority.

## Verification

- Skill/contract/template/acceptance agree on surface-role evidence, Domain deduplication and meta-procedure exclusion;
- `MIRROR` cannot be emitted without an established primary;
- an existing Domain Map is pointed to rather than summarized as a second Domain Map;
- generated Profile contains no step-by-step engineering startup flow or Profile-maintenance rules;
- stable project-specific facts remain available;
- source and refreshed Web Plugin candidate contain the same corrected shipped Project Profile files.

## Stop conditions

Stop if the correction requires a new authority layer, new Skill, new control file, or changes outside Project Profile/acceptance/package identity semantics.

## Terminal boundary

Task 073 closes after focused source verification, package/version alignment, guarded Web Plugin refresh, and installed-file verification. Then restore Task 070 to `WAITING_FRESH_WEB_SESSION` for the user regression test.

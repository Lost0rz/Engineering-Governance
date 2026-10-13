# CURRENT TASK — Plugin v0.5.5 Local Convergence

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.5-LOCAL-CONVERGENCE-060`

State: `AUTHORIZED_MINI_FIRST`

Mode: bounded local Plugin convergence and global routing verification

## Objective

Converge Mac mini and MacBook Air from the accepted local `engineering-governance` Plugin version `0.5.4` to `0.5.5`, preserving exactly one active canonical Plugin authority on each machine, then verify that the authoritative global `AGENTS.md` contains exactly one current Engineering Governance managed routing block without duplicating Skill procedures.

## Planning context

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`.
- Relationship to plan: distribute the accepted v0.5.5 governance semantics to local Codex installations; do not change the durable design.

## Start baseline

Remote distribution baseline:

- formal tag/release: `plugin-v0.5.5`;
- frozen publication source: `8871327915396b8de458f3e5709e3f67e36eff8f`;
- current repository control head at authorization: `221c30957fc997f0722d352542d072a1c1255705`;
- expected local canonical authority before upgrade: `engineering-governance@engineering-governance-personal / 0.5.4` on both machines, subject to fresh local verification.

Global routing evidence:

- v0.5.4 `GLOBAL_AGENTS_ROUTING.md` blob: `c54c84beb6ccfdb5ac1cbd3eb74d1c5e674f496e`;
- v0.5.5 `GLOBAL_AGENTS_ROUTING.md` blob: `c54c84beb6ccfdb5ac1cbd3eb74d1c5e674f496e`;
- therefore the managed global routing template has no v0.5.5 semantic delta.

## Execution order

1. Mac mini only.
2. Return and audit Mini receipt.
3. MacBook Air only after Mini passes.
4. Final cross-machine convergence audit.

## In scope

- Verify machine identity and Codex version.
- Verify the existing `engineering-governance-personal` marketplace source and active Plugin authority.
- Upgrade through the supported Codex Plugin/marketplace path; do not manually edit active Plugin cache/source payload.
- Verify installed version `0.5.5` and exactly three top-level Skills.
- Verify v0.5.5 Project Governance payload contains durable planning-document linkage and the mandatory Control Alignment Gate.
- Locate the environment's authoritative global `AGENTS.md` rather than guessing a path.
- Verify exactly one BEGIN and one END Engineering Governance routing marker.
- Compare the complete managed region with the current shipped `GLOBAL_AGENTS_ROUTING.md` template.
- If identical, leave the global file unchanged and report `GLOBAL_ROUTING_RECONCILIATION: UNCHANGED`.
- If one older compatible managed region exists, replace only that marker-bounded region and preserve unrelated global guidance.

## Out of scope

- Copying Project Governance procedures, planning-document rules, Control Alignment Gate details, or project-specific governance into the global `AGENTS.md`.
- Editing project-local `AGENTS.md` files merely because Plugin 0.5.5 is installed.
- Adding a fourth Skill.
- Manual deletion/modification under active Plugin cache/source directories.
- `codex plugin marketplace remove engineering-governance-personal`.
- Changing repository governance semantics or the formal release.

## Verification level and cadence

`V1` local distribution/configuration verification.

For each machine verify:

- canonical Plugin authority count = 1;
- active authority = `engineering-governance@engineering-governance-personal / 0.5.5`;
- exactly three top-level Skills;
- required v0.5.5 Project Governance references/semantics present;
- authoritative global guidance identified;
- exactly one current managed routing block;
- unrelated global guidance materially unchanged;
- no full Skill workflow duplicated into the global file;
- no manual cache/source payload mutation.

## Stop conditions

Stop the affected machine before mutation if:

- machine identity is not the intended Mini/Air;
- the authoritative global guidance file cannot be established;
- multiple managed routing blocks or conflicting partial markers exist;
- another active Engineering Governance Plugin authority competes with the canonical personal marketplace authority;
- the marketplace source cannot be safely tied to the accepted Git-backed authority;
- the supported Plugin update path is unavailable and continuation would require manual active-cache/source mutation;
- installed 0.5.5 payload does not contain exactly the expected three Skills.

Do not stop merely because historical 0.5.4 cache/source material is absent after a supported CLI update.

## Handoff / current stop point

Task is authorized for Mac mini first. Do not mutate Air in parallel.

Expected Mini receipt fields:

```text
TASK_ID: EG-PLUGIN-V0.5.5-LOCAL-CONVERGENCE-060
MACHINE_CLASS: MAC_MINI
PLUGIN_BEFORE: <version>
PLUGIN_AFTER: <version>
ACTIVE_AUTHORITY_COUNT: <count>
ACTIVE_AUTHORITY: <name / version>
TOP_LEVEL_SKILLS: <list>
PLANNING_DOCUMENT_LINKAGE: PASS|FAIL
CONTROL_ALIGNMENT_GATE: PASS|FAIL
GLOBAL_AGENT_AUTHORITY: <path>
GLOBAL_ROUTING_MARKERS: PASS|FAIL
GLOBAL_ROUTING_TEMPLATE_MATCH: PASS|FAIL
GLOBAL_ROUTING_RECONCILIATION: UPDATED|UNCHANGED
UNRELATED_GLOBAL_RULES_PRESERVED: PASS|FAIL
MANUAL_CACHE_MUTATION: NO
PLUGIN_SOURCE_DIRECTORY_MUTATION: NO
FINAL_STATE: PASS_LOCAL_PLUGIN_055|STOP_<reason>
```

Final task closeout after both machines pass must run the Project Governance Control Alignment Gate and reconcile controls only if owned semantics changed.

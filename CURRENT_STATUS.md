# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-18.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.3`.

Publication identity remains:

- release PR: `#36` — `MERGED`;
- publication source SHA: `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- release workflow run: `38678260676` — `success`;
- tag: `plugin-v0.7.3` -> `25c7607de18a5ae70f9be48e2faca8b4723fed4c`;
- release ID: `413399094`;
- asset: `engineering-governance-plugin.zip`;
- included top-level Skills: exactly `9`.

The existing private personal Web Plugin remains synchronized to `0.7.3`; Local Git-backed installation/update state is downstream runtime state and is not inferred here.

## Active task

Task `EG-HUMAN-UI-ACCEPTANCE-089` is `ACTIVE` on branch `codex/human-ui-acceptance-boundary` from control parent `bb72d3aae0f98b312700dff3ee527301e9e55991`.

Objective: establish an explicit reusable boundary in which automated browser testing and AI-rendered inspection remain valid engineering evidence, while final product-interface acceptance is owned by a human when that acceptance is required.

Planned reusable-source owners:

- Design — separate AI/internal rendered review from final human UI acceptance;
- Project Governance verification — distinguish automated/AI evidence from human acceptance evidence;
- Agent Handoff — preserve the acceptance owner across agents/sessions/machines and prevent Computer Use self-approval from satisfying a human acceptance gate.

No new Plugin release is authorized by this task. The published/runtime baseline remains `0.7.3` until a later explicit release decision.

## Repository lifecycle

- prior v0.7.3 release task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088`: `COMPLETE`;
- active task `EG-HUMAN-UI-ACCEPTANCE-089`: `ACTIVE`;
- task branch: `codex/human-ui-acceptance-boundary`;
- merge/release: not yet authorized.

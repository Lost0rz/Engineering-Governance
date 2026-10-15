# CURRENT TASK — Design Routing Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ROUTING-HARDENING-083`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE`

## Objective

Harden the published `design` capability so it remains the primary owner of bounded UI/UX/frontend design work without becoming artificially isolated from other Engineering Governance capabilities.

The target behavior is **evidence-triggered composition**:

- stay inside Design by default;
- cross a Skill boundary only for a concrete unresolved dependency that materially affects the Design decision;
- state the question and expected bounded return before crossing;
- use the smallest capability that owns that dependency;
- return the bounded result to Design and resume from the suspended Design stage rather than restarting the whole pipeline.

## Required routing behavior

### Design vs Solution Design discriminator

- `design` owns interaction workflow: how users understand, navigate, edit, review, act, receive feedback and complete a frontend task.
- `solution-design` owns business/state workflow when material ambiguity exists: canonical state transitions, data/state ownership, API/data-flow responsibility, persistence semantics and implementation boundaries.
- A mixed problem may use both, but only when both material problems actually exist. Resolve a blocking business/state prerequisite before continuing the affected Design decision.

### Evidence-triggered cross-Skill composition

A cross-Skill call from Design is valid only when it has all of:

1. `UNRESOLVED_DEPENDENCY` — a specific question Design cannot safely answer from current reliable context;
2. `DESIGN_IMPACT` — why the answer can materially change the current Design decision;
3. `CAPABILITY` — the smallest Skill that owns the missing answer;
4. `EXPECTED_RETURN` — the bounded result needed back;
5. `RESUME_STAGE` — where Design continues after the capability returns.

Examples:

- use `domain-navigation` when relevant backend/product authority, source, symbol, state owner, runtime entry or test route is not reliably identifiable;
- use `solution-design` when the route is known but material business/state/API ownership semantics remain unresolved;
- use `agent-handoff` when a bounded transfer must cross agent/session/machine/context;
- use `evidence-audit` only when a separate formal acceptance/readiness verdict is actually requested;
- use `execution-orchestrator` only when decomposition/delegation materially improves execution;
- use `incident-doctor` only when a blocking evidence gap prevents a safe next action.

Do not invoke another Skill for general enrichment, completeness, a second opinion, or merely because it is installed.

## Design execution modes

Add an explicit internal mode so not every Design request is forced through a full implementation pipeline:

- `AUDIT_ONLY` — context + actual interface audit + design findings; no implementation unless separately authorized/requested;
- `DESIGN_SPEC` — audit + Anthropic + conditional admin pattern + bounded design-spec synthesis + pre-build gate; stop before implementation;
- `DESIGN_IMPLEMENT` — full design-to-implementation closed loop;
- `FINAL_REVIEW` — review an existing concrete implementation/prototype without reopening the upstream design direction unless a material defect requires bounded correction.

## Full implementation sequence

For `DESIGN_IMPLEMENT` when rendered evidence is supported:

`project/profile context intake → actual interface audit → Anthropic reasoning → admin patterns when applicable → bounded design-spec synthesis → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`.

If rendered evidence is unavailable, Microsoft review must state the evidence limit rather than fabricate it.

## Preserve

- exactly nine top-level Skills;
- the single external `design` route;
- Anthropic / shadcn-admin / awesome-design-md / Microsoft as internal Design modules;
- Project Profile as derived context, not authority;
- Project Governance as task/lifecycle owner;
- existing source provenance/license boundaries;
- release payload `plugin.json + skills/**` only;
- existing receipt and handoff contracts.

## Acceptance

The change is complete only when:

- routing contracts use evidence-triggered composition instead of hard anti-cross-Skill wording;
- Design/Solution Design workflow ownership is explicitly discriminated;
- all four Design modes have clear stop/continue behavior;
- cross-Skill calls carry question/impact/capability/expected-return/resume-stage;
- Domain Navigation remains a legitimate Design dependency when the relevant backend/product route is genuinely unclear;
- return-to-Design behavior is explicit and does not restart the whole pipeline unnecessarily;
- rendered evidence is available to Microsoft final review when the environment supports it;
- final visual acceptance remains the terminal Design gate;
- v0.7.1 acceptance/regression checks pass;
- source is merged/released and the existing private Web Plugin is updated/read back in place.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082` (`COMPLETE`)
- `START_MAIN_HEAD`: `06301c8ff5c074ea16e26a4e01a0755d52d43e24`
- `TASK_BRANCH`: `codex/design-routing-hardening-v071`
- `TARGET_VERSION`: `0.7.1`
- `TOP_LEVEL_SKILLS_TARGET`: `9`
- `DESIGN_EXTERNAL_ROUTE`: `design`
- `TASK_STATE`: `ACTIVE`

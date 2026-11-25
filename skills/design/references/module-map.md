# Design internal module map

`design` is the single externally routed Skill for bounded UI/UX/frontend visual-design work. The sources below are internal modules/references behind that capability boundary; they are not peer top-level Skills and do not create independent project authority.

## Design modes

- `MICRO_POLISH` — localized component, spacing, copy, or interaction-state tweak directly against project tokens/components; skips upstream spec synthesis.
- `AUDIT_ONLY` — context + actual interface audit + findings; stops before design/implementation.
- `DESIGN_SPEC` — audit + reasoning/pattern/specification + pre-build gate; stops before implementation.
- `DESIGN_IMPLEMENT` — full design-to-implementation/review/visual-acceptance loop.
- `FINAL_REVIEW` — review/correct an existing implementation without reopening upstream design direction unless a material defect requires it.

## Active modules

### 1. Anthropic `frontend-design` — design reasoning
Source: `anthropic/frontend-design.md`. Owns subject/product grounding, deliberate visual direction, typography, composition, hierarchy, anti-generic-AI critique, and plan-before-build reasoning for material `DESIGN_SPEC` / `DESIGN_IMPLEMENT` work.

### 2. `shadcn-admin`-informed patterns — conditional admin composition
Source: `shadcn-admin/admin-patterns.md`. Conditional layer for admin/back-office/productivity page families (shell, header/CTA, toolbar/filter, table/form/dialog composition, responsive reflow). Owns interaction composition, never backend state semantics.

### 3. `awesome-design-md`-informed synthesis — bounded visual-system specification
Source: `awesome-design-md/design-spec-synthesis.md`. Converts design intent and page composition into implementation-ready tokens, typography, spacing, surface, state, and Do/Don't rules. Target-project design authority always wins over external inspiration.

### 4. Microsoft `frontend-design-review`-informed review — final Design audit
Source: `microsoft/final-review.md`. Review-only evaluation of concrete prototype/implementation and rendered evidence (Blocking / Major / Minor). Microsoft's creative mode is intentionally excluded because Anthropic owns upstream direction.

## Ordered composition

For `DESIGN_IMPLEMENT` when rendered evidence is supported:

`project/profile context intake → actual interface audit → Anthropic reasoning → admin patterns when applicable → design-spec synthesis → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`

## Evidence-triggered cross-Skill composition

Before crossing to another Skill for a material unresolved dependency, declare:

```text
UNRESOLVED_DEPENDENCY:
DESIGN_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_STAGE:
```

Typical calls: `domain-navigation` (unclear source/state owner/test route), `solution-design` (ambiguous `BUSINESS_STATE_WORKFLOW` — see [SKILL.md](../SKILL.md)), `agent-handoff`, `evidence-audit`, `execution-orchestrator`, or `incident-doctor`. After receiving the bounded answer, resume `RESUME_STAGE` without restarting the whole Design pipeline.

## Authority rules

- Project Profile is compact derived context, not canonical authority.
- Target-project product, business, data/state, design-system, and brand authorities win over generic modules.
- Never invent Figma, Storybook, tokens, render evidence, backend intent, or host permissions.

## Deferred capability

A separate general-purpose UX heuristic research module remains optional/deferred until real project work proves a material gap.

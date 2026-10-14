# CURRENT TASK — Design Multi-Module Closed Loop

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082`

Task class: `CAPABILITY_EXTENSION`

State: `ACTIVE`

## Objective

Extend the stable routed `design` capability from the Anthropic-only baseline into one coherent internal design pipeline that uses project context first and then applies specialized internal modules without exposing them as peer top-level Skills.

Required sequence for qualifying UI/UX/frontend design or redesign work:

`project/profile context intake → actual interface audit → Anthropic design reasoning → admin pattern composition when applicable → DESIGN.md visual-system synthesis → implementation/prototype → Microsoft final design review → corrective pass → rendered visual acceptance when supported`.

## Required behavior

### Project context intake

- Use an available Project Profile / project instructions as compact derived context for product purpose, audience, constraints and authority pointers.
- Preserve the Project Profile as derived context, not canonical authority.
- Verify only the project-specific authorities materially needed by the bounded design problem.
- Do not route to unrelated Skills merely to reacquire already-known design context.

### Anthropic reasoning layer

- Preserve the accepted Anthropic `frontend-design` source identity/provenance/license.
- Use Anthropic for subject grounding, visual direction, hierarchy, typography/composition, anti-template reasoning and pre-build critique.

### Admin pattern layer

- Integrate a curated `satnaing/shadcn-admin`-informed admin pattern module behind `design`.
- Apply it for admin/back-office/productivity surfaces where page composition, workflow/action hierarchy, forms, tables, settings, sidebars, dialogs, toolbars, detail/edit patterns or state presentation materially apply.
- Do not turn its implementation or visual defaults into project authority and do not force admin patterns onto storefront/landing/marketing surfaces.

### DESIGN.md synthesis layer

- Integrate a curated `VoltAgent/awesome-design-md`-informed visual-system synthesis module behind `design`.
- Produce or update an explicit bounded design specification for the page/project when useful: visual theme, semantic color roles, typography, layout/spacing, component treatment, elevation/surfaces, responsive behavior, Do/Don't rules and agent implementation guidance.
- Existing project design-system/brand authority wins over external style references.
- External brand DESIGN.md examples are inspiration/reference, not authority and not instructions to clone another brand.

### Microsoft final review layer

- Integrate Microsoft `frontend-design-review` as the final internal Design review module.
- Use its review mode for design-system compliance, frictionless insight-to-action, quality craft, trustworthy building, accessibility/responsive review and blocking/major/minor prioritization.
- Do not re-run Microsoft creative-design mode as a competing upstream design direction after Anthropic/Admin/Awesome have established the design.
- Material Microsoft findings trigger a bounded corrective pass and re-review before Design completion.

## Routing boundary

- External route remains the single top-level `design` Skill.
- Do not create new top-level Skills for Anthropic, shadcn-admin, awesome-design-md or Microsoft.
- Project Governance remains task/lifecycle authority.
- Design owns its internal module sequence and visual acceptance loop.
- `domain-navigation`, `solution-design`, `evidence-audit`, and `execution-orchestrator` are not automatic stages; use them only for distinct material triggers.

## Source / provenance

Audit and preserve the relevant upstream license/provenance boundaries for:

- `anthropics/skills` frontend-design — existing bundled Apache-2.0 source;
- `satnaing/shadcn-admin` — MIT;
- `VoltAgent/awesome-design-md` — MIT;
- `microsoft/skills` frontend-design-review — MIT.

Prefer compact adapted reference modules over vendoring entire upstream repositories.

## Acceptance

The change is complete only when:

- the Design Skill documents the ordered internal module pipeline and conditional Admin branch;
- Project Profile/context intake is explicit and authority-safe;
- all three new modules have local provenance/license notes and bounded responsibility;
- Microsoft final review produces severity-prioritized findings and a corrective/re-review loop;
- existing Anthropic identity and prior routing/receipt gates remain intact;
- exactly nine top-level Skills remain;
- Plugin payload remains `plugin.json + skills/**` only;
- versioned acceptance evidence covers the new pipeline and regressions;
- source PR is reviewed/merged and release/Web Plugin synchronization is completed if release gates pass.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081` (`COMPLETE`)
- `START_MAIN_HEAD`: `366989b63e3c12707b3535eff89d306bf21b48c8`
- `TASK_BRANCH`: `codex/design-multi-module-closed-loop-v070`
- `TARGET_VERSION`: `0.7.0`
- `TOP_LEVEL_SKILLS_TARGET`: `9`
- `DESIGN_EXTERNAL_ROUTE`: `design`

# CURRENT TASK — Design Multi-Module Closed Loop

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082`

Task class: `CAPABILITY_EXTENSION`

State: `COMPLETE`

## Objective

Extend the stable routed `design` capability from the Anthropic-only baseline into one coherent internal design pipeline that uses project context first and then applies specialized internal modules without exposing them as peer top-level Skills.

Published sequence for qualifying UI/UX/frontend design or redesign work:

`project/profile context intake → actual interface audit → Anthropic design reasoning → admin pattern composition when applicable → DESIGN.md visual-system synthesis → implementation/prototype → Microsoft final design review → corrective pass/re-review → rendered visual acceptance when supported`.

## Completed behavior

### Project context intake

- Available Project Profile / Project Instructions are consumed as compact derived context for product purpose, audience, constraints and authority pointers.
- The Profile remains derived context, not canonical authority.
- Only project-specific authorities materially needed by the bounded design problem are verified.
- Reading an existing Profile does not itself route through `project-profile`.
- Design does not cross unrelated Skills merely to reacquire already-known context.

### Anthropic reasoning layer

- Accepted Anthropic `frontend-design` source identity/provenance/license is preserved.
- Anthropic owns subject grounding, visual direction, hierarchy, typography/composition, anti-template reasoning and pre-build critique.

### Admin pattern layer

- A curated `satnaing/shadcn-admin`-informed admin pattern module is active behind `design`.
- It applies conditionally to admin/back-office/productivity surfaces.
- It does not make Shadcn styling project authority and is not forced onto storefront/landing/marketing surfaces.

### DESIGN.md synthesis layer

- A curated `VoltAgent/awesome-design-md`-informed visual-system synthesis module is active behind `design`.
- It produces bounded implementation-ready design guidance covering visual character, semantic color roles, typography, layout/spacing, component/state treatment, surfaces/elevation, responsive behavior, Do/Don't rules and implementation mapping as applicable.
- Existing project design-system/brand authority wins.
- External brand DESIGN.md examples remain optional reference/inspiration, not authority or cloning instructions.
- Durable project `DESIGN.md` is created/updated only when project-wide design authority is explicitly in scope; bounded task-level specification remains the default.

### Microsoft final review layer

- Microsoft `frontend-design-review` is active as the final internal Design review module.
- Review covers design-system/project-authority compliance, frictionless insight-to-action, quality craft, trustworthy building, accessibility/responsive evidence and severity-prioritized findings.
- Creative Frontend Design mode is intentionally not rerun as a competing downstream aesthetic direction.
- `Blocking / Major / Minor` severity is used.
- Open Blocking/Major findings require a bounded corrective pass and re-review before Design completion.
- Missing Figma/Storybook/token/render evidence may not be fabricated.

## Routing boundary

- External route remains the single top-level `design` Skill.
- No top-level Skills were created for Anthropic, shadcn-admin, awesome-design-md or Microsoft.
- Project Governance remains task/lifecycle authority.
- Design owns its internal module sequence and visual acceptance loop.
- `project-profile`, `domain-navigation`, `solution-design`, `evidence-audit`, and `execution-orchestrator` are not automatic stages; they remain separately triggered capabilities.

## Source / provenance

Published source/license boundaries:

- `anthropics/skills` frontend-design — existing bundled Apache-2.0 source;
- `satnaing/shadcn-admin` — MIT-informed compact adaptation;
- `VoltAgent/awesome-design-md` — MIT-informed compact adaptation;
- `microsoft/skills` frontend-design-review — MIT-informed compact adaptation.

The whole upstream repositories were not vendored. Local provenance/license records are retained adjacent to the adapted modules.

## Acceptance and release evidence

- source PR: `#31 — feat: complete multi-module Design closed loop` — `MERGED`;
- start main HEAD: `366989b63e3c12707b3535eff89d306bf21b48c8`;
- pre-merge semantic candidate: `8ced8f3ddc455da1228887867c94e5c8c2f01cda`;
- pre-merge workflow: `Release Plugin v0.7.0` run `38655255661` — `PASS`;
- merge / released semantic source SHA: `8284f0f138427dd329cd50983046baf78ec110ce`;
- main release workflow: `Release Plugin v0.7.0` run `38655371941` / run #6 — `PASS`;
- GitHub tag: `plugin-v0.7.0`;
- GitHub Release ID: `413275429`;
- asset: `engineering-governance-plugin.zip`;
- asset size: `130963` bytes;
- asset SHA-256: `7cd695bc8b7f8302de06a8b36c1e5f5d8afabb8b874416a40ca42b6481fcf06b`;
- package entries: `61`;
- package scope: `plugin.json + skills/**` only;
- top-level Skills: exactly `9`.

## Web Plugin synchronization

Existing Web Plugin updated in place:

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- version: `0.7.0`;
- Web release ID: `pluginrel_6ad01392fbec81919fb25c380af12954`;
- scope/discoverability: `USER / PRIVATE` — unchanged;
- root/platform manifests: `0.7.0` read back;
- Design closed-loop source, all three new adapted modules/provenance records and Project Profile → Design routing rule: read back.

`WEB_PLUGIN_SYNC_070`: `PASS`.

## Local distribution note

Last directly observed Local Codex runtime remains `0.6.8`. Task 082 does not claim local refresh to `0.7.0` without a fresh local runtime readback.

`LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081` (`COMPLETE`)
- `TASK_BRANCH`: `codex/design-multi-module-closed-loop-v070`
- `PR`: `#31` (`MERGED`)
- `TARGET_VERSION`: `0.7.0`
- `TOP_LEVEL_SKILLS`: `9`
- `DESIGN_EXTERNAL_ROUTE`: `design`
- `PREMERGE_CI`: `PASS`
- `FORMAL_RELEASE_070`: `PASS`
- `WEB_PLUGIN_SYNC_070`: `PASS`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING_USER_TRIAL`
- `TASK_STATE`: `COMPLETE`

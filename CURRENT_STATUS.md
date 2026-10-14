# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.6.9` at released source SHA `0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`.

The released Design capability currently has one active internal source module: Anthropic `frontend-design`. It already enforces a bounded design-to-rendered-review loop, selective Skill routing, and observable route/used-Skill receipts.

## Active task

Task `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082` is `ACTIVE` on branch `codex/design-multi-module-closed-loop-v070`, starting from main `366989b63e3c12707b3535eff89d306bf21b48c8`.

Objective: extend the single routed `design` capability into an ordered internal multi-module pipeline:

`Project Profile/context intake → actual UI audit → Anthropic reasoning → shadcn-admin pattern composition when applicable → awesome-design-md-inspired DESIGN.md synthesis → implementation/prototype → Microsoft frontend-design-review final audit → corrective pass → rendered visual acceptance when supported`.

## External source audit

Verified upstream boundaries for Task 082:

- `satnaing/shadcn-admin` — public MIT project; use as curated admin/back-office composition and interaction-pattern reference, not as project authority or a vendored application template.
- `VoltAgent/awesome-design-md` — public MIT project; use as curated DESIGN.md visual-system synthesis/reference methodology, not as permission to clone another brand or replace an existing project design system.
- `microsoft/skills` `frontend-design-review` — public MIT Skill; use Review Mode as the final Design quality gate. Its Creative Frontend Design mode will not compete with the already-established Anthropic/Admin/Awesome design direction.
- existing Anthropic `frontend-design` bundled source/provenance/license remains preserved.

## Routing boundary

The external capability surface remains exactly nine top-level Skills. Anthropic, shadcn-admin, awesome-design-md and Microsoft remain internal Design modules/references behind the single `design` route.

Project Profile/project instructions may be consumed as compact derived context before Design reasoning, but remain non-authoritative summaries/pointers. Design verifies only materially needed project authority and does not automatically route through unrelated Skills to reacquire known context.

## Distribution state

Published/Web Plugin baseline remains `0.6.9` until Task 082 source acceptance and release gates pass.

Target release for the completed multi-module Design pipeline is `0.7.0`.

## Control identity

Current released semantic Plugin identity remains:

`0f4fbba6b9344de4fb6f2c6fd659ec825333fdc8`

Task 082 branch/control work does not alter published runtime identity until merged and released.

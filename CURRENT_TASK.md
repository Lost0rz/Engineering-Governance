# CURRENT TASK — Human UI Acceptance Boundary

Date: 2026-10-18

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-HUMAN-UI-ACCEPTANCE-089`

Task class: `CORRECTIVE`

State: `ACTIVE`

Branch: `codex/human-ui-acceptance-boundary`

Control parent: `bb72d3aae0f98b312700dff3ee527301e9e55991`

## Objective

Make human product-interface acceptance an explicit reusable Engineering Governance boundary without weakening automated browser testing.

AI/browser tooling may still inspect rendered pages for debugging, evidence gathering, design self-review, and implementation correction, but AI-driven Computer Use/manual-style clicking or screenshot inspection must not be treated as the final human UI/UX/product acceptance gate.

## Required behavior

1. Preserve Playwright/Cypress/E2E, DOM, accessibility, screenshot-regression, and other automated browser verification as valid engineering evidence.
2. Allow AI/browser/Computer Use inspection for diagnosis, debugging, bounded design review, and corrective implementation support.
3. Prohibit machine-driven rendered inspection from being reported as human acceptance or from satisfying a task that explicitly requires human product-interface acceptance.
4. Separate internal Design review from final human acceptance.
5. When human UI acceptance is applicable, expose an explicit status such as `HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED`.
6. Cross-context execution/review cards must preserve this boundary rather than instructing the receiving AI to self-approve the final product interface through Computer Use.

## Scope

Expected reusable-source changes:

- `skills/design/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/agent-handoff/references/handoff-contract.md`
- control/status files required by the repository lifecycle

Do not disable browser automation or automated tests. Do not ban rendered inspection as engineering evidence. Do not introduce runtime enforcement, daemons, or tool blocking.

## Verification

Risk tier: `V0` — reusable rule/contract correction.

Required checks:

- source wording clearly distinguishes automated verification, AI rendered inspection, internal Design review, and human UI acceptance;
- no contract treats Playwright/E2E as prohibited;
- Design completion cannot claim human acceptance from AI-rendered evidence;
- Handoff cards/receipts preserve the acceptance owner across contexts;
- changed Markdown remains internally consistent with the nine-Skill capability model.

## Delivery boundary

Implement on the task branch and open a Draft PR. Do not merge or publish a new Plugin release without a later explicit merge/release decision.

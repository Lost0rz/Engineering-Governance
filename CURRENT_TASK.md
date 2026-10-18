# CURRENT TASK — Human UI Acceptance Boundary

Date: 2026-10-18

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-HUMAN-UI-ACCEPTANCE-089`

Task class: `CORRECTIVE`

State: `IMPLEMENTED / DRAFT_REVIEW`

Branch: `codex/human-ui-acceptance-boundary`

Control parent: `bb72d3aae0f98b312700dff3ee527301e9e55991`

## Objective

Make human product-interface acceptance an explicit reusable Engineering Governance boundary without weakening automated browser testing.

AI/browser tooling may still inspect rendered pages for debugging, evidence gathering, design self-review, and implementation correction, but AI-driven Computer Use/manual-style clicking or screenshot inspection must not be treated as the final human UI/UX/product acceptance gate.

## Required behavior

1. Preserve Playwright/Cypress/E2E, DOM, accessibility, screenshot-regression, and other automated browser verification as valid engineering evidence.
2. Allow AI/browser/Computer Use inspection for diagnosis, debugging, bounded design review, and corrective implementation support.
3. Prohibit machine-driven rendered inspection from being reported as human acceptance.
4. Separate internal Design review from final human acceptance.
5. For state-changing work that materially changes a real product interface, default to `HUMAN_UI_ACCEPTANCE: PENDING` until an explicit human decision; omission of the field does not waive the gate.
6. Allow `HUMAN_UI_ACCEPTANCE: NOT_REQUIRED` only when an owning user/project authority explicitly waives the human gate or the task does not produce a product-interface result needing visual/interaction acceptance.
7. Cross-context execution/review cards must preserve this boundary rather than instructing the receiving AI to self-approve the final product interface through Computer Use.

## Scope

Reusable-source changes:

- `skills/design/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/agent-handoff/SKILL.md`
- `skills/agent-handoff/references/handoff-contract.md`
- control/status files required by the repository lifecycle

Do not disable browser automation or automated tests. Do not ban rendered inspection as engineering evidence. Do not introduce runtime enforcement, daemons, or tool blocking.

## Implementation result

Draft PR: `#37 — feat: make product UI acceptance human-owned`

Source semantic head after the final reusable-rule edit: `905dfe7c3901581491c3ea59271bb7cf204aeeee`.

The implemented contracts now separate:

```text
AUTOMATED_BROWSER_VERIFICATION
AI_RENDERED_INSPECTION
INTERNAL_VISUAL_REVIEW
HUMAN_UI_ACCEPTANCE
```

Key behavior:

- Playwright/Cypress/E2E and comparable browser automation remain valid engineering verification;
- AI browser/Computer Use inspection remains allowed for debugging, evidence gathering, internal Design review and corrective work;
- AI/manual-style browser inspection cannot become `AUDIT_INDEPENDENCE: HUMAN` or `HUMAN_UI_ACCEPTANCE: PASS`;
- material real-product interface changes default to human acceptance `PENDING`;
- `NOT_REQUIRED` cannot be inferred from omission and requires an owning waiver or a non-product-interface acceptance surface;
- Handoff cards/receipts preserve the same boundary across agents, sessions and machines.

## Verification

Risk tier: `V0` — reusable rule/contract correction.

Self-check against the PR diff: `PASS`.

Verified:

- source wording clearly distinguishes automated browser verification, AI rendered inspection, internal Design review, and human UI acceptance;
- no contract disables or downgrades Playwright/E2E/browser automation;
- machine-driven rendered evidence cannot satisfy human acceptance;
- material product-interface changes default to a pending human gate rather than silently becoming `NOT_REQUIRED`;
- Design no longer treats its machine visual review as final product acceptance;
- Agent Handoff preserves the acceptance owner across contexts;
- changed reusable-source paths remain within the nine-Skill capability model.

PR `#37` at source head `905dfe7c3901581491c3ea59271bb7cf204aeeee` was observed `OPEN / DRAFT / UNMERGED / MERGEABLE`.

No pull-request workflow runs were observed for that exact source head. No CI PASS is claimed; the task's V0 contract did not require runtime/browser execution for this documentation/rule correction.

## Delivery boundary

Implementation is remotely present on the task branch and Draft PR #37 is open. Do not merge or publish a new Plugin release without a later explicit merge/release decision.

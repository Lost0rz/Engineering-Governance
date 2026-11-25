# Design implementation and final review — selected FINAL_REVIEW / implementation QA

Load only when implementing a full design or performing `FINAL_REVIEW` on rendered surfaces (not required for `MICRO_POLISH` or `AUDIT_ONLY`). `FINAL_REVIEW` evaluates current implementation/design authority directly without forcing upstream Anthropic/spec synthesis again unless a material design defect requires it.

## Stage review fields (machine evidence vs human UI acceptance)

Browser/Computer Use inspection, screenshots, automated E2E suites, and Microsoft final review establish **machine evidence only** (see [SKILL.md](../SKILL.md) for human acceptance ownership). Keep these states explicit when product-interface acceptance is material:

```text
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

## Implement or prototype

- Implement in the smallest safe boundary (existing page or isolated prototype when composition is uncertain) using real project components and tokens rather than ad-hoc overrides.
- Preserve canonical business/state/API semantics unless resolved through `architecture`.

## Capture rendered evidence when supported

Before final review, capture/inspect the exact implementation identity across representative viewports and material states (loading, empty, error, disabled, dirty, read-only). Record `RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE`. Never substitute a functional DOM test for visual render inspection or claim unavailable evidence.

## Microsoft internal final Design review

Read `microsoft/final-review.md` (review-only; do not invoke its Creative Frontend Design mode to override upstream direction). Evaluate user task efficiency, design-system compliance, responsive/accessibility craft, and trust/error/AI-content treatment:

- `Blocking` — must fix before internal review closes;
- `Major` — fix in current pass;
- `Minor` — non-blocking refinement.

After fixing open `Blocking`/`Major` findings, re-render affected surfaces and rerun Microsoft review before closing.

## Internal visual review close & handoff

1. Confirm final implementation identity and post-fix re-renders match the design specification and user task with no open `Blocking`/`Major` findings or visual/a11y regressions.
2. Close internal visual review (`INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE`), keeping `HUMAN_UI_ACCEPTANCE: PENDING` whenever human sign-off is required (any later material UI edit invalidates a prior human `PASS`).
3. A formal independent release/readiness verdict belongs to `evidence-audit` when requested.

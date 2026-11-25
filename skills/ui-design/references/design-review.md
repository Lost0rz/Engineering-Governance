# Design implementation and final review — selected FINAL_REVIEW / implementation QA

Load only when implementing a full design or performing `FINAL_REVIEW` on rendered surfaces (not required for `MICRO_POLISH` or `AUDIT_ONLY`). `FINAL_REVIEW` evaluates current implementation/design authority directly without forcing upstream Anthropic/spec synthesis again unless a material design defect requires it.

## Stage review fields (machine evidence vs human UI acceptance)

Browser/Computer Use inspection, screenshots, automated E2E suites, and Microsoft final review establish **machine evidence only** (see [SKILL.md](../SKILL.md) for human acceptance ownership). Keep these states explicit when product-interface acceptance is material:

```text
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
INTERNAL_VISUAL_REVIEW: PASS | BLOCKED | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

## Implement or prototype

- Implement in the smallest safe boundary (existing page or isolated prototype when composition is uncertain) using real project components and tokens rather than ad-hoc overrides.
- Preserve canonical business/state/API semantics unless resolved through `architecture`.

## Capture rendered evidence when supported

Before final review, capture/inspect the exact implementation identity across representative viewports and material states (loading, empty, error, disabled, dirty, read-only). Record `RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE`. Never substitute a functional DOM test for visual render inspection or claim unavailable evidence.

## Proportional visual & final Design review

Choose the lightest review pass that matches change risk:

### 1. Fast visual QA (`G1` / localized component or flow tweak — 0 extra reads)

Inspect the captured render across representative viewports and states, tagging findings `Blocking` / `Major` / `Minor`:

1. **Hierarchy & primary action:** clear focal point; primary CTA dominates secondary/destructive actions cleanly.
2. **Design-system compliance:** real project tokens, typography scale, spacing rhythm, and surface contrast (WCAG AA readability).
3. **Layout & overflow:** zero clipping, horizontal scroll leakage, wrapped badge distortion, or broken alignment at desktop/mobile widths.
4. **State completeness:** intentional loading, empty, error, disabled, dirty, and read-only states—no dead controls or silent failures.
5. **Interaction & keyboard focus:** visible focus ring, sensible tab order, clear form validation and destructive confirmations.
6. **Honest trust & AI framing:** distinct machine vs human state indicators and truthful provenance/status copy.

### 2. Full-surface or `FULL_DESIGN_SYSTEM` sign-off

Load [microsoft/final-review.md](microsoft/final-review.md) (review-only; do not invoke its Creative Frontend Design mode to override upstream direction) when closing a full-page redesign, new visual system, or multi-viewport release review:

- `Blocking` — must fix before internal review closes;
- `Major` — fix in current pass;
- `Minor` — non-blocking refinement.

After fixing open `Blocking`/`Major` findings, re-render affected surfaces and re-verify before closing.

## Internal visual review close & handoff

1. If any `Blocking` or `Major` finding remains open, set `INTERNAL_VISUAL_REVIEW: BLOCKED` and do not close until fixed and re-rendered. Once clean, confirm final implementation identity matches the design specification and user task with zero visual/a11y regressions.
2. Close internal visual review (`INTERNAL_VISUAL_REVIEW: PASS | BLOCKED | LIMITED_BY_EVIDENCE`), keeping `HUMAN_UI_ACCEPTANCE: PENDING` whenever human sign-off is required (any later material UI edit invalidates a prior human `PASS`).
3. A formal independent release/readiness verdict belongs to `evidence-audit` when requested.

# Design implementation and final review — selected DESIGN_IMPLEMENT / FINAL_REVIEW

Load only when actual implementation or rendered review is needed (not required for `MICRO_POLISH` or `AUDIT_ONLY`). `FINAL_REVIEW` uses current implementation/design authority without forcing Anthropic/admin/spec synthesis again; `DESIGN_IMPLEMENT` uses the bounded specification when it reaches this stage.

## Stage review fields (machine evidence vs human UI acceptance)

Browser/Computer Use inspection, screenshots, automated E2E suites, and Microsoft final review are machine evidence (see [SKILL.md](../SKILL.md) for the human acceptance boundary). Keep these states distinct when product-interface acceptance is material:

```text
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

### 6. Implement or prototype

Applies to `DESIGN_IMPLEMENT`, or to `FINAL_REVIEW` corrective work when mutation is authorized.

Use the smallest implementation boundary appropriate to the task:

- existing real page when safe/authorized;
- isolated/static prototype when composition uncertainty warrants it;
- existing component library/design tokens where available.

Implementation must realize the Design package rather than silently replacing it with easiest-local CSS/JSX choices. Preserve canonical business/state/API semantics unless resolved through the appropriate state owner.

### 7. Capture rendered evidence when supported

Before Microsoft internal final review, capture/inspect the strongest rendered evidence the environment actually supports:

- exact implementation/prototype identity;
- representative whole-surface viewport(s);
- material responsive states;
- important loading/empty/error/disabled/dirty/saving/generated/published/read-only states when available/in scope.

Record `RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE`. If rendering is unavailable, state the limit and continue only to the evidence strength allowed by the target project's acceptance contract.

### 8. Microsoft internal final Design review

After a concrete prototype/implementation exists and rendered evidence has been captured when supported, read `microsoft/final-review.md`. Microsoft is **review-only** here; do not use its Creative Frontend Design mode as a competing upstream aesthetic direction.

Review:

- user task/action efficiency;
- actual project design-system/brand authority;
- bounded Design package;
- implementation source;
- rendered evidence when supported;
- responsive/accessibility evidence;
- trust/error/AI-generated-content treatment when material.

Classify findings as `Blocking` (must fix before internal close), `Major` (fix in current pass), or `Minor` (non-blocking). Open Blocking/Major findings require correction, re-render of affected surfaces when supported, and Microsoft re-review before closing. Never claim Figma/Storybook/token/render/accessibility evidence that was not available.

### 9. Internal visual review close and human acceptance handoff

This is the terminal **internal Design** gate for `DESIGN_IMPLEMENT` and `FINAL_REVIEW` when visual review is applicable; it is not final human product acceptance.

When rendered inspection is supported:

1. inspect the final corrected implementation identity;
2. confirm affected representative viewports/states were re-rendered after material corrections;
3. confirm Microsoft has no open Blocking/Major finding;
4. compare the final surface with the bounded Design package and user task;
5. ensure no new material hierarchy, density, alignment, typography, CTA, state, responsive or accessibility regression is visible.

Do not fabricate `INTERNAL_VISUAL_REVIEW: PASS` when required rendered evidence is unavailable. If human acceptance is required, internal Design closes at `INTERNAL_VISUAL_REVIEW: PASS` with `HUMAN_UI_ACCEPTANCE: PENDING`; material corrections after a prior human `PASS` invalidate that `PASS` until re-accepted.

## Mode-specific review evidence

Do not emit a mandatory multi-field checklist in routine responses; report only what was actually observed and required for the relevant claim.

### `DESIGN_IMPLEMENT`

```text
DESIGN_MODE: DESIGN_IMPLEMENT
DESIGN_CONTEXT_INTAKE: YES
PROFILE_DERIVED_NOT_AUTHORITY: YES | NOT_APPLICABLE
INTERFACE_AUDIT_COMPLETED: YES
ANTHROPIC_ANALYSIS_COMPLETED: YES | EXISTING_DIRECTION_REUSED
ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE
DESIGN_SPEC_SYNTHESIZED: YES
PRE_BUILD_DESIGN_GATE: PASS
PROTECTED_AUTHORITY_PRESERVED: YES
CROSS_SKILL_CALLS: NONE | BOUNDED_AND_RESOLVED
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE
MICROSOFT_BLOCKING_FINDINGS_OPEN: NO
MICROSOFT_MAJOR_FINDINGS_OPEN: NO
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

### `FINAL_REVIEW`

```text
DESIGN_MODE: FINAL_REVIEW
DESIGN_CONTEXT_INTAKE: YES
EXISTING_IMPLEMENTATION_REVIEWED: YES
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE
MICROSOFT_BLOCKING_FINDINGS_OPEN: NO
MICROSOFT_MAJOR_FINDINGS_OPEN: NO
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

## Evidence limitations

Design owns its internal critique, but evidence strength still matters. If source, route, authority, render, viewport, state, design-system or runtime evidence is missing, mark the affected conclusion limited/unknown or consult the narrowly owning capability when triggered.

A separate formal independent release/readiness verdict belongs to `evidence-audit` when explicitly requested. Human product-interface acceptance remains human-owned when required by the task/project contract.

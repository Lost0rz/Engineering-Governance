# Design implementation and final review — selected DESIGN_IMPLEMENT / FINAL_REVIEW

Load only when actual implementation or rendered review is needed. FINAL_REVIEW uses current implementation/design authority without forcing Anthropic/admin/spec synthesis again; DESIGN_IMPLEMENT uses the bounded specification when it reaches this stage.

## Human product-interface acceptance boundary

Design's browser/render inspection is **internal machine review**, not a substitute for human product acceptance.

AI tooling may use a browser, Computer Use/manual-style clicking, screenshots, rendered pages, or other visual evidence to:

- understand the current interface;
- debug implementation defects;
- gather rendered evidence;
- perform internal Design critique;
- verify that an authorized corrective pass changed the intended surface.

Automated browser verification also remains fully valid engineering evidence, including Playwright, Cypress, other E2E suites, DOM/state assertions, accessibility checks, screenshot/visual-regression systems, and comparable scripted checks.

These machine-driven activities must remain distinct from final human UI/UX/product acceptance:

- AI browser/Computer Use inspection must not be reported as human acceptance;
- automated browser PASS must not be promoted into human acceptance;
- Design's internal Microsoft review is not `AUDIT_INDEPENDENCE: HUMAN`;
- when the project/task requires human interface acceptance, only an explicit human reviewer/user decision may set that gate to `PASS` or `FAIL`;
- if the human decision has not occurred, the correct state is `PENDING`, even if implementation, automated tests, and internal rendered review are complete.

Use these separate fields when product-interface acceptance is material:

```text
AUTOMATED_BROWSER_VERIFICATION: PASS | FAIL | NOT_RUN | NOT_APPLICABLE
AI_RENDERED_INSPECTION: PASS | FINDINGS | LIMITED | NOT_RUN | NOT_APPLICABLE
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

`HUMAN_UI_ACCEPTANCE: NOT_REQUIRED` is valid only when the owning task/project acceptance contract does not require a human interface gate.

If human acceptance is required and remains `PENDING`, Design may report implementation/internal review complete, but must not claim final product-interface acceptance or readiness on the basis of machine-rendered evidence alone.


### 6. Implement or prototype

Applies to `DESIGN_IMPLEMENT`, or to `FINAL_REVIEW` corrective work when mutation is authorized.

Use the smallest implementation boundary appropriate to the task:

- existing real page when safe/authorized;
- isolated/static prototype when composition uncertainty warrants it;
- existing component library/design tokens where available.

Implementation must realize the Design package rather than silently replacing it with easiest-local CSS/JSX choices. Preserve canonical business/state/API semantics unless a separately routed capability has resolved an authorized change.

### 7. Capture rendered evidence when supported

Before Microsoft internal final review, capture/inspect the strongest rendered evidence the environment actually supports:

- exact implementation/prototype identity;
- representative whole-surface viewport(s);
- material responsive states;
- important loading/empty/error/disabled/dirty/saving/generated/published/read-only states when available/in scope.

Record:

`RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE`

A passing functional browser test is not rendered visual evidence. Conversely, rendered inspection is not human acceptance. Browser/Computer Use/screenshots may support internal Design review, but they cannot satisfy a required human product-interface gate.

If rendering is unavailable, state the limit and continue only to the evidence strength allowed by the target project's acceptance contract.

### 8. Microsoft internal final Design review

After a concrete prototype/implementation exists and rendered evidence has been captured when supported, read `microsoft/final-review.md`.

Microsoft is **review-only** here. Do not use its Creative Frontend Design mode as a competing upstream aesthetic direction.

Review:

- user task/action efficiency;
- actual project design-system/brand authority;
- bounded Design package;
- implementation source;
- rendered evidence when supported;
- responsive/accessibility evidence;
- trust/error/AI-generated-content treatment when material.

Classify findings:

- `Blocking` — must fix before internal Design review can close;
- `Major` — fix in the current Design pass;
- `Minor` — non-blocking refinement.

Open Blocking/Major findings require correction. After correction, re-render affected surfaces when rendering is supported and rerun Microsoft internal review before internal visual review close.

Never claim Figma/Storybook/token/render/accessibility evidence that was not available.

Microsoft internal review is machine Design review. It does not itself satisfy a required human UI acceptance gate.

### 9. Internal visual review close and human acceptance handoff

This is the terminal **internal Design** gate for `DESIGN_IMPLEMENT` and `FINAL_REVIEW` when visual review is applicable. It is not automatically the terminal product acceptance gate.

When rendered inspection is supported:

1. inspect the final corrected implementation identity;
2. confirm affected representative viewports/states were re-rendered after material corrections;
3. confirm Microsoft has no open Blocking/Major finding;
4. compare the final surface with the bounded Design package and user task;
5. ensure no new material hierarchy, density, alignment, typography, CTA, state, responsive or accessibility regression is visible.

Record:

```text
INTERNAL_VISUAL_REVIEW: PASS | LIMITED_BY_EVIDENCE | NOT_APPLICABLE
HUMAN_UI_ACCEPTANCE: PENDING | PASS | FAIL | NOT_REQUIRED
```

Do not fabricate `INTERNAL_VISUAL_REVIEW: PASS` when required rendered evidence is unavailable.

If the owning task/project requires human product-interface acceptance:

- internal Design may close at `INTERNAL_VISUAL_REVIEW: PASS` while `HUMAN_UI_ACCEPTANCE: PENDING`;
- the AI must stop short of claiming final UI/UX/product acceptance;
- only an explicit human reviewer/user decision may change the human field to `PASS` or `FAIL`;
- material interface corrections after a prior human PASS normally require a fresh human acceptance decision unless the owning acceptance contract explicitly says otherwise.

If no human gate is required, use `HUMAN_UI_ACCEPTANCE: NOT_REQUIRED`; do not invent a human PASS.


## Mode-specific review evidence

Do not emit a mandatory multi-field checklist in routine responses; report what was actually observed and required for the relevant claim. A human UI decision remains exclusively human-owned.

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

Design owns its internal critique, but evidence strength still matters. If source, route, authority, render, viewport, state, design-system or runtime evidence is missing, mark the affected conclusion limited/unknown or invoke the narrowly owning capability when its trigger is met.

A separate formal independent release/readiness verdict remains `evidence-audit` when explicitly requested. Microsoft's internal review does not change that authority boundary. Human product-interface acceptance remains a separate evidence owner when required by the task/project contract.


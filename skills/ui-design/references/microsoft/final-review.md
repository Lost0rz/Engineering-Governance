# Final frontend Design review

This module adapts the **Design Review** function of Microsoft's `frontend-design-review` Skill as the downstream internal quality gate inside Engineering Governance `design`.

It is intentionally review-oriented. Do not use Microsoft's Creative Frontend Design mode here to reopen the visual direction after Anthropic reasoning, admin-pattern composition and design-spec synthesis have already established the bounded design.

## Review input

Review the strongest evidence actually available:

- project purpose/audience/context and materially relevant authority;
- the bounded Design intent/composition/specification when one exists;
- target-project design system / brand / component / token authority when it truly exists;
- concrete prototype or implementation source;
- rendered surface/screenshots/browser evidence when supported;
- representative states/viewports actually available.

When the environment supports rendered inspection, capture that evidence **before** this review so the Microsoft review can evaluate the actual surface rather than only source/specification.

Never invent Figma, Storybook, token, browser, accessibility-test or viewport evidence. If evidence is unavailable, mark that part of the review `LIMITED` / unknown instead of converting it to PASS.

## Review sequence

### 1. Re-state the user task

Record:

```text
Surface / feature:
Primary user:
Primary job:
Primary action:
Terminal outcome:
Evidence reviewed:
Evidence unavailable:
```

The final audit judges whether the interface helps the user complete the real job, not merely whether individual components look polished.

### 2. Design-system / project-authority compliance

When a real project design system/component library/brand authority exists, check:

- existing approved components are reused/adapted where appropriate;
- project tokens/variables are used rather than unnecessary one-off values;
- variants and states match real project conventions;
- spacing/type/color/surface decisions do not silently fork the established system;
- deviations are intentional, scoped and documented by the bounded Design decision.

If no such authority exists, do **not** fail the work for lacking Figma/Storybook. Review consistency against the bounded Design specification and actual project conventions instead.

### 3. Pillar A — Frictionless insight to action

Check:

- the user's current task is obvious;
- the primary action is clear and not competing with many equal-emphasis actions;
- navigation/entry/exit/cancel/back paths are understandable where needed;
- the workflow avoids unnecessary clicks, screens and confirmations;
- progressive disclosure hides complexity without hiding necessary information;
- defaults reduce avoidable configuration;
- forms, tables, editors and settings follow the user's working sequence;
- empty/error/disabled/permission states still expose a viable next action.

The upstream “≤3 interactions” idea is a heuristic, not an absolute rule. A legitimate complex workflow may require more steps when each carries necessary meaning or safety.

### 4. Pillar B — Quality is craft

Check:

- implementation realizes the intended page composition rather than reverting to generic card stacking;
- typography establishes hierarchy;
- spacing/alignment create deliberate grouping;
- color/surface/elevation/radius usage is coherent and restrained;
- component treatments and state variants are consistent;
- density is appropriate to the task;
- responsive behavior preserves task hierarchy;
- focus/keyboard/contrast/non-color cues and other accessibility-relevant behavior are addressed to the extent evidence permits;
- motion, decoration and backgrounds serve orientation/character rather than generic visual noise;
- light/dark/high-contrast/theme behavior is checked only when those modes actually exist/in scope.

Do not demand novelty for its own sake. Distinctiveness must remain appropriate to the product and existing design authority.

### 5. Pillar C — Trustworthy building

Check where materially applicable:

- errors explain what happened and what the user can do next;
- destructive/irreversible actions make consequences clear;
- save/generation/publication status is not ambiguous;
- unsaved/draft/published/read-only states are distinguishable;
- AI-generated content is identified when product policy/experience requires users to know its origin;
- source facts, generated output and editable content are not misleadingly conflated;
- permission/access limitations are understandable;
- the UI does not suggest success/completion before the underlying workflow has actually completed.

### 6. Responsive and whole-surface review

When rendered evidence exists, inspect the whole relevant surface at representative viewport(s):

- hierarchy and primary task survive reflow;
- navigation remains reachable;
- columns/rails stack in the correct semantic order;
- toolbars/filters consolidate without losing important state;
- tables preserve identity/actionability;
- persistent/sticky actions do not cover content;
- dialogs/sheets fit the viewport;
- no obvious overflow, clipping, accidental whitespace or density collapse appears.

Do not equate a passing functional browser test with visual acceptance.

## Severity model

Every material finding must be assigned one of:

### Blocking — must fix before Design completion

Examples:

- core task cannot be completed or next action is unclear;
- primary/terminal actions are dangerously ambiguous;
- destructive consequence is obscured;
- major responsive break makes the workflow unusable;
- material project design-system/authority violation;
- critical state/error/permission behavior is misleading;
- evident accessibility problem blocks normal use.

### Major — fix in the current Design pass

Examples:

- competing primary CTAs;
- information architecture/page composition still obscures workflow;
- long/repetitive card stacking materially hurts scanning;
- important state placement is duplicated or unclear;
- implementation materially diverges from the bounded Design specification;
- meaningful responsive or accessibility degradation;
- project tokens/components are bypassed without justification.

### Minor — refinement, does not block completion

Examples:

- small alignment/type rhythm inconsistencies;
- non-critical copy hierarchy polish;
- low-impact spacing/surface cleanup;
- optional animation/detail improvements.

Do not inflate a stylistic preference into Blocking/Major severity without showing user-task, authority, accessibility or design-system impact.

## Review output

Return a compact internal review record:

```text
MICROSOFT_FINAL_REVIEW
Surface:
Evidence:
Evidence limits:

Pillars:
- Frictionless: PASS | NEEDS_WORK | BLOCKED | LIMITED
- Quality craft: PASS | NEEDS_WORK | BLOCKED | LIMITED
- Trustworthy: PASS | NEEDS_WORK | BLOCKED | LIMITED | NOT_APPLICABLE

Design-system / project-authority compliance:
Responsive / accessibility evidence:

Blocking:
1. ...

Major:
1. ...

Minor:
1. ...

Verdict: PASS | NEEDS_WORK | BLOCKED | LIMITED_BY_EVIDENCE
Required corrective actions:
```

Do not list empty severity sections verbosely; `None` is sufficient.

## Corrective / re-review gate

- Any open `Blocking` finding => `BLOCKED`; correct before Design completion.
- Any open `Major` finding => `NEEDS_WORK`; correct in the current Design pass and re-review.
- `Minor` findings may remain if explicitly accepted as non-blocking refinement.
- After a Blocking/Major correction, re-render the affected surface when rendering is supported before rerunning this review.
- Do not treat a source-only correction assertion as equivalent to re-review of the corrected rendered result when rendered evidence is available.
- `LIMITED_BY_EVIDENCE` is allowed when required visual/runtime evidence genuinely cannot be obtained; state exactly what remains unverified.

The Design completion gate may report `MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE`, but it must also report `MICROSOFT_BLOCKING_FINDINGS_OPEN: NO` and `MICROSOFT_MAJOR_FINDINGS_OPEN: NO`.

Final visual acceptance happens **after** the last Microsoft review/corrective cycle and confirms the final corrected surface. This Microsoft module remains Design's internal review loop; it is not a formal release/readiness Evidence Audit unless that separate outcome is explicitly requested and routed accordingly.

# Bounded DESIGN.md / visual-system synthesis

This module adapts the useful `DESIGN.md` idea from `VoltAgent/awesome-design-md`: turn an established design direction into plain-text visual-system guidance that an implementation agent can follow consistently.

Use it **after** the actual interface has been audited and the design direction/page composition are known. This module does not decide product strategy, workflow authority or canonical state.

## Authority rule

Use target-project visual/design authority in this order when available:

1. explicit project/user requirements;
2. existing project brand/design-system authority;
3. accepted current components/tokens and real implemented conventions;
4. bounded Design decisions established in the current task;
5. external reference inspiration.

External brand DESIGN.md examples never outrank the target project. Do not clone another brand, copy protected assets, assume external fonts are licensed, or substitute another company's palette/identity for an established product.

## Reference selection discipline

If external visual references would materially help, choose deliberately:

- one **primary reference direction** for the strongest relevant quality;
- at most one or two **secondary references** for narrow complementary qualities;
- state what is being borrowed conceptually and what is explicitly **not** being copied.

Examples of conceptual qualities: precise data density, restrained surfaces, editorial hierarchy, friendly commerce rhythm, strong action contrast. Avoid vague “make it like X” instructions.

A target project with a mature existing design system may need no external brand reference at all.

## Required specification structure

A bounded Design specification should contain the sections below that materially apply. Prefer concrete rules over adjectives.

### 1. Visual character & atmosphere

Define:

- intended tone and level of formality;
- information density;
- visual energy/restraint;
- dominant surface rhythm;
- what makes the page feel specific to this product/user job.

Bad: `clean, modern, professional`.

Better: `dense operational workspace with quiet neutral surfaces; hierarchy comes from type/spacing, with one high-contrast action color reserved for the current workflow's terminal CTA`.

### 2. Color roles

Prefer semantic roles tied to existing project tokens:

```text
canvas/background:
surface-primary:
surface-secondary:
text-primary:
text-secondary:
border/subtle divider:
action-primary:
action-secondary:
success:
warning:
error/destructive:
focus:
```

If the project has canonical variables/tokens, name those instead of inventing hex values. New raw color values require actual scope/authority.

Do not use status colors as decoration. Ensure meaning is not conveyed by color alone.

### 3. Typography rules

Define roles and hierarchy rather than a random list of font sizes:

```text
display/page title:
section title:
body:
label/control:
helper/meta:
data/mono when applicable:
```

For each relevant role describe weight, relative scale, line-height/density and emphasis behavior. Use existing project type families unless changing typography is explicitly in scope.

Typography should carry hierarchy so that borders/cards are not required to separate every section.

### 4. Layout & spacing principles

Specify the structural rhythm:

- page/content max-width or fluid-width behavior;
- shell/main/rail column model;
- grid or alignment anchors;
- section spacing vs within-group spacing;
- horizontal gutters;
- form/table/editor density;
- sticky/persistent action boundaries where applicable.

Use the target project's spacing scale/tokens when available. Do not prescribe arbitrary pixel values when the project already has a scale.

### 5. Surfaces, elevation, borders & radius

Define where visual containers are justified:

- flat canvas vs raised surfaces;
- when a card/panel boundary is meaningful;
- divider/border use;
- shadow/elevation hierarchy;
- radius behavior;
- nested-container limits.

A component library's Card component is not a reason to card-wrap every conceptual group.

### 6. Component treatments

Specify the component families that matter for the current surface:

- primary / secondary / destructive / ghost actions;
- fields, selects, editors and validation;
- tabs/segmented controls/step navigation;
- table/list rows and selection;
- badges/status indicators;
- alerts/banners/toasts;
- dialog/sheet/drawer;
- preview/evidence/metadata panels;
- navigation and breadcrumbs where applicable.

For each, capture only meaningful treatment differences and state behavior. Map to existing target-project components where possible.

### 7. Interaction & motion

Define motion only when it improves orientation, feedback or perceived continuity:

- disclosure/expand/collapse;
- panel transitions;
- loading/progress;
- drag/reorder if the product already supports it;
- success/error feedback;
- page/section entry only when intentional.

Avoid scattered animation as decoration. Respect reduced-motion behavior when motion exists.

### 8. State visuals

Explicitly cover relevant states:

- default;
- hover/focus/active;
- loading/processing;
- empty/no results;
- error/retry;
- disabled/read-only/permission-limited;
- dirty/unsaved;
- save in progress / saved / save failed;
- generated/AI content attribution if applicable;
- success/completion;
- destructive/irreversible confirmation.

State styling must reinforce workflow meaning without duplicating the same status in multiple visual surfaces.

### 9. Responsive behavior

Describe behavioral reflow, including as applicable:

- content width/gutters;
- multi-column → single-column ordering;
- sidebar/rail collapse;
- toolbar/filter consolidation;
- sticky action transformation;
- table column priority / horizontal scrolling;
- modal/sheet sizing;
- navigation access;
- touch/focus considerations.

Do not treat “responsive” as merely adding breakpoints after desktop design.

### 10. Accessibility-relevant visual rules

Record concrete visual/interaction constraints supported by project requirements/evidence:

- focus visibility;
- text/action contrast;
- non-color status cues;
- target sizing where relevant;
- readable line lengths/density;
- zoom/reflow implications;
- motion reduction if motion is used.

Do not claim formal WCAG conformance without evidence appropriate to that claim.

### 11. Do / Don't

Make the specification resistant to generic implementation drift.

Example:

```text
DO
- use typography + spacing as the first grouping mechanism
- reserve the strongest action treatment for Publish
- show editable/generated/source facts with distinct semantic treatments

DON'T
- wrap every field group in an equal card
- use badges for static labels
- make Save, Generate and Publish equal-emphasis CTAs
- introduce a new palette/font when existing project tokens already cover the need
```

The Do/Don't section should reflect this product and task, not generic style advice.

### 12. Agent implementation guidance

Close with a mapping from Design decisions to implementation reality:

```text
Existing tokens/components to reuse:
Components to compose/adapt:
New primitives truly required:
Hard-coded values prohibited/allowed:
States that must be demonstrated/tested:
Representative viewports:
Protected business/state authority:
```

This is the bridge that prevents a good design discussion from disappearing during coding.

## Durable project DESIGN.md vs task-level specification

Default to a **bounded task-level specification** for a single page/flow redesign.

Create or update a durable project `DESIGN.md` only when:

- the task explicitly covers project-wide visual/design-system authority;
- the design decisions are stable and intended to govern future pages;
- the target project accepts `DESIGN.md` as an authority/reference artifact;
- the artifact does not duplicate a stronger existing design-system source.

A generated DESIGN.md is not authoritative merely because it exists. Its project role must be established by the target project's own authority model.

## Completion check

Before implementation, the specification should make it possible for another competent executor to answer:

- What should this interface feel like?
- What visually dominates and why?
- Which existing tokens/components should be used?
- How are sections grouped without generic card stacking?
- How do primary/secondary/destructive actions differ?
- How do key states look and behave?
- What happens responsively?
- What visual choices are explicitly forbidden?

If those answers remain vague, synthesis is incomplete.

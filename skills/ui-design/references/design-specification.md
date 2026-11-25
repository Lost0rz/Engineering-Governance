# Full design specification — selected FULL_DESIGN_SYSTEM / FLOW_WITH_TOKENS

Only load when `ui-design` selects `FULL_DESIGN_SYSTEM` (or when `FLOW_WITH_TOKENS` needs deeper visual-system guidance beyond existing tokens). Not required for `MICRO_POLISH`, `AUDIT_ONLY`, or `FINAL_REVIEW`.

### 1. Context & interface audit

Inspect the actual surface, user primary job, action hierarchy, responsive/empty/error/loading states, and existing project design tokens/components. If a `FLOW_WITH_TOKENS` task already has authoritative project tokens and components, skip Sections 2 & 4 visual-system regeneration and map directly to existing project patterns (reading `shadcn-admin/admin-patterns.md` only for admin/back-office surfaces).

### 2. Anthropic design reasoning

For `FULL_DESIGN_SYSTEM` (unless an accepted design direction already exists), read `anthropic/frontend-design.md` and establish:

- `Design intent` — user, primary job, tone, and intended visual character;
- `Hierarchy thesis` — what dominates, what recedes, and primary CTA relationships;
- `Composition thesis` — spatial layout idea instead of generic card stacking;
- `Typography / visual emphasis` — translated into project-approved tokens where authoritative;
- `Genericity check` — reject decorative AI/SaaS clutter that does not serve the brief;
- `Protected authority` — business/data/state semantics `ui-design` must not alter (escalate ambiguous `BUSINESS_STATE_WORKFLOW` to `architecture`).

### 3. Admin page-pattern composition (conditional)

For admin/back-office/operational/productivity surfaces, read `shadcn-admin/admin-patterns.md` and classify the page family (shell/nav, header/CTA, toolbar/filter, table/form/editor/dialog, state feedback, responsive reflow, component mapping). Record `ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE`. Do not force admin patterns onto marketing or editorial pages.

### 4. Synthesize bounded visual specification

For `FULL_DESIGN_SYSTEM`, read `awesome-design-md/design-spec-synthesis.md` and produce implementation-ready guidance covering semantic color roles, type scale, spacing/grid, surfaces/borders, component states, motion, responsive rules, accessibility checks, Do/Don't constraints, and exact component/token mappings. External brand examples remain inspiration only; target-project authority wins.

### 5. Pre-build design gate

Verify before building: product/user fit, coherent CTA hierarchy, appropriate admin pattern use, concrete token/component mapping, absence of decorative clutter, preserved business/state authority, clear distinction between source/editable/generated/status states, and resolved cross-Skill dependencies (`codebase-context` for unknown files, `architecture` for ambiguous state ownership). Record `PRE_BUILD_DESIGN_GATE: PASS | BLOCKED`.

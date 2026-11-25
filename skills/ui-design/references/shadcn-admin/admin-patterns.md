# Admin / back-office page-pattern composition

This module adapts reusable composition lessons from `satnaing/shadcn-admin` for Engineering Governance Design work. It is a **pattern reference**, not a template authority and not permission to copy its visual styling into a target project.

Use this module only after the actual product/workflow/interface has been audited and Anthropic design reasoning has established the page's user/job/hierarchy direction.

## Applicability gate

Apply when the surface is materially one of:

- admin/back-office operations;
- internal/productivity tools;
- settings/configuration;
- entity list / data table / management collection;
- entity detail/edit/create flow;
- operational dashboard;
- multi-section form or authoring workflow;
- command/search/filter-driven workspace;
- dialog/sheet-supported management actions.

When applied, record `ADMIN_PATTERN_LAYER: APPLIED` in the Design completion record. When the surface does not materially match these families, record `ADMIN_PATTERN_LAYER: NOT_APPLICABLE` with a short reason.

Do not apply mechanically to marketing sites, editorial pages, consumer landing pages or storefront discovery surfaces.

## First classify the page family

Before selecting components, name the dominant family. One page can combine patterns, but it should still have one primary job.

### Dashboard / operational overview

Use when the user needs current state, exceptions and next actions.

Typical composition:

```text
Application shell
└─ Page header
   ├─ title + concise context
   └─ primary operational action when needed
└─ Overview / signals
   ├─ high-value metrics or statuses
   └─ trend / exception context
└─ Main operational surface
   ├─ queue / recent activity / table / chart
   └─ direct action path
```

Rules:

- Do not turn every fact into an equal metric card.
- Prefer a few decision-relevant signals over decorative KPI density.
- Make exceptions/actionable items more prominent than passive totals.

### Collection / data-management list

Use for tasks, users, products, orders, records or similar managed entities.

Typical composition:

```text
Page header                  [Primary create/import action]
Description / scope
Toolbar
├─ search
├─ high-value filters
├─ sort/view controls
└─ bulk actions only when selection exists
Data table / collection
└─ row-level secondary actions
Pagination / result context
```

Rules:

- Keep the primary creation/action separate from row-level actions.
- Search/filter belongs near the collection it controls.
- Avoid a separate card/container for every toolbar subsection.
- Empty state should explain why the collection is empty and expose the relevant next action.

### Settings / configuration

Use when values configure a product, site, account or integration.

Typical composition:

```text
Settings navigation / category index | Active settings section
                                      ├─ section title + consequence
                                      ├─ related fields
                                      ├─ validation/help only where useful
                                      └─ save/reset action at the right scope
```

Rules:

- Group by user mental model and consequence, not database/schema ordering.
- Keep save scope clear: field, section or page.
- Separate destructive/reset operations from routine save actions.
- Prefer progressive disclosure for advanced/rare settings.

### Detail / editor / authoring workflow

Use for entity review, editing, publishing, AI-assisted authoring or other long-form operational work.

Typical composition:

```text
Context header
├─ entity identity / breadcrumb
├─ status
└─ primary workflow action(s)

Main workspace
├─ primary editing/review surface
├─ grouped supporting sections or step navigation
└─ contextual feedback / validation

Secondary context when useful
├─ preview / metadata / evidence / history
└─ publication or generation status

Persistent or clearly anchored actions
├─ Save / save draft
├─ Generate / validate / preview when applicable
└─ Publish / complete / submit as the terminal action
```

Rules:

- Prefer one work surface with meaningful subsections over a long chain of equal cards.
- Distinguish source/read-only facts, generated output, editable content and system status visually and semantically when the workflow contains them.
- Keep terminal actions such as publish/submit visually distinct from reversible save/edit actions.
- Long workflows may use tabs/steps/side navigation only when those structures reflect real user phases, not merely to hide excessive content.

### Dialog / sheet / focused secondary task

Use for narrow tasks that should not replace the page's main job: confirm, assign, create small record, inspect metadata, choose filters, etc.

Rules:

- Do not move a complex primary workflow into a modal to make the page look shorter.
- Dialogs need explicit cancel/close paths and action hierarchy.
- Destructive confirmation must state consequence, not rely on button color alone.

## Shell and navigation

A stable admin shell commonly needs:

- persistent application navigation appropriate to information architecture;
- current-location clarity;
- global search/command only if the product materially supports cross-surface navigation/actions;
- account/workspace controls separated from page-specific actions;
- responsive collapse that preserves task access rather than merely hiding navigation.

Do not add sidebar, command palette or breadcrumbs solely because this reference project has them. Use only what the target workflow justifies.

## Header and CTA contract

For each page decide:

- What context must the user recognize immediately?
- What is the one primary action for this view?
- Which actions are secondary, contextual or destructive?

Prefer one dominant primary action per current task state. Two strong actions are acceptable when the workflow genuinely has two peer paths; otherwise reduce competition.

Do not place Save, Generate, Preview, Publish, Cancel and more as equal high-emphasis buttons.

## Form organization

- Order fields according to the user's work sequence and conceptual groups.
- Use section headings only when they communicate a real group or consequence.
- Keep labels close to their controls; helper text should resolve ambiguity rather than restate the label.
- Show validation near the affected field/section and summary guidance only when cross-field errors require it.
- Use multi-column form layouts only when related fields benefit from scanning together and the layout remains readable responsively.

## Table / toolbar organization

- Keep high-frequency filters visible; move low-frequency filters into a deliberate secondary surface.
- Do not duplicate filter state in multiple chips/cards unless it materially aids orientation.
- Bulk actions appear only with a selection state.
- Row actions should not visually compete with the page-level CTA.
- Preserve columns needed for decisions; hide secondary metadata responsively before obscuring entity identity/actionability.

## State placement

Define states at the component/page layer that actually owns them:

- loading / skeleton;
- empty / no results / first-use empty;
- recoverable error + retry/action;
- disabled + reason where not obvious;
- dirty/unsaved;
- saving / saved / save failed;
- generation/processing if applicable;
- permission/locked/read-only;
- destructive confirmation;
- success/terminal completion.

Avoid duplicate status cards, banners and badges all reporting the same fact.

## Density and container discipline

Admin interfaces can be dense without becoming visually noisy.

Before creating a card/container ask:

1. Does this region need an independent boundary to support scanning, state or interaction?
2. Would spacing/dividers/type hierarchy communicate the grouping more clearly?
3. Is this card repeated only because the component library makes cards easy?

A long page of nested or repeated equal-weight cards is usually a composition failure, not a design system.

## Responsive composition

Define behavior rather than only breakpoints:

- navigation collapse / drawer behavior;
- primary and secondary column stacking order;
- sticky actions becoming bottom/inline actions without covering content;
- toolbar/filter wrapping or consolidation;
- table column priority / horizontal-scroll policy;
- dialog/sheet sizing;
- touch target and focus behavior.

Do not accept desktop-only visual correctness as responsive completion.

## Required Design output from this module

When applied, add a compact pattern decision to the bounded Design package:

```text
Admin page family:
Primary user job:
Shell/navigation:
Header + primary CTA:
Main work surface:
Secondary/context surface:
Toolbar/search/filter:
Form/table/editor/dialog pattern:
State placement:
Responsive reflow:
Project component/token mapping:
Patterns deliberately not used:
```

This output is a composition decision, not permission to replace target-project product, business, state or design-system authority.

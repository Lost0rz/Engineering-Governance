# Reference Audit — MADR

**Verified:** 2026-10-06  
**Source identity:** `adr/madr` README and its `develop` branch ADR template,
accessed on the date above. The branch is mutable and is recorded by access
date, not represented as a release pin.

**Primary sources:**

- [MADR README](https://github.com/adr/madr)
- [MADR ADR template](https://github.com/adr/madr/blob/develop/template/adr-template.md)

## Shared 14-question audit

### 1. What problem does it solve?

MADR provides a lightweight Markdown template for recording an architecture
decision, its context, options, selected outcome, consequences, and later
confirmation.

### 2. What is the canonical source of truth?

The accepted ADR in the project's decision repository records the decision
and status. The implementation and project behavior remain authoritative for
whether the decision is followed; the ADR is not proof of implementation.

### 3. How do global policy and project-local configuration relate?

MADR is a project-local template and convention. It does not define a global
standard or inheritance model. Each project selects where to store ADRs and
how its lifecycle is governed.

### 4. How are rules and checks represented?

An ADR includes front matter such as status, date, decision makers, consulted
and informed parties, followed by context/problem, decision drivers, options,
decision outcome, consequences, confirmation/fitness function, pros/cons,
and further information.

### 5. How are machine-decidable and judgment-based checks distinguished?

The template can record a measurable confirmation or fitness function, but
the decision and tradeoffs are human-owned. It does not define an automated
check or a review mode.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Decision statuses include proposed, rejected, accepted, deprecated, and
superseded (with a successor reference). This lifecycle does not represent a
scoped temporary waiver for another governance requirement.

### 7. How are version, compatibility, and compliance tracked?

The ADR identity, status, date, and successor link provide decision-history
tracking. MADR does not define standard/profile compatibility or conformance
versioning. A project may record relevant versions in its own ADR content.

### 8. What evidence does a finding require?

An ADR links further information and may define a confirmation/fitness
function. It does not mandate evaluator version, exact repository revision,
or evidence freshness. Governance findings should link to the ADR and to the
separate observed evidence.

### 9. How is remediation represented?

Consequences, pros/cons, confirmation, and later superseding decisions make
the expected follow-up legible. MADR does not itself perform implementation
or remediation.

### 10. How are automatic enforcement and advisory separated?

MADR records a human decision. Enforcement, if any, is in the project
workflow and should not be inferred from the presence of an accepted ADR.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Accepted/deprecated/superseded status and successor identifiers make decision
state visible. The template does not automatically detect when code or
assumptions drift from a decision.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

No ADR-specific mechanism is inherently too heavy; the risk is requiring a
new ADR for every routine check or copying ADR content into a governance
registry.

### 13. What capability gap does it expose?

It demonstrates small, linkable decision records with rationale, alternatives,
consequences, status, and confirmation criteria. It also reinforces the need
to separate accepted intent from proof of implementation.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** ADR identity/status/rationale and confirmation links for decisions
that materially change governance semantics. Keep ordinary profile settings
in the profile and point to canonical ADRs rather than copying them.

## Mechanism dispositions

- **ADOPT:** explicit status and rationale for material decisions, with
  successor links and confirmation criteria where useful.
- **ADAPT:** reference ADRs from standards, profiles, and findings without
  duplicating their content.
- **DEFER:** additional ADR tooling or mandatory ADR creation for every
  governance check.
- **REJECT:** treating an accepted decision as evidence that the intended
  architecture or behavior exists.

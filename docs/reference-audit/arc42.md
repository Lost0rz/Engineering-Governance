# Reference Audit — arc42

**Verified:** 2026-10-06  
**Source identity:** arc42 overview and official documentation pages, accessed
on the date above. The public template identifies its current template as
version 9.0 (July 2025); this audit records that template identity without
claiming a separate tooling release.

**Primary sources:**

- [arc42 overview](https://arc42.org/overview/)
- [arc42 documentation](https://docs.arc42.org/)
- [Section 9: Architecture Decisions](https://docs.arc42.org/section-9/)
- [Section 10: Quality Requirements](https://docs.arc42.org/section-10/)
- [Section 11: Risks and Technical Debt](https://docs.arc42.org/section-11/)

## Shared 14-question audit

### 1. What problem does it solve?

arc42 is a practical, tailorable template for communicating software
architecture, including context, constraints, building blocks, runtime,
deployment, decisions, quality requirements, risks, and glossary.

### 2. What is the canonical source of truth?

The project-maintained architecture documentation is the explanation and
decision record. Its factual claims still derive from the actual system,
accepted decisions, and project artifacts; a template section does not
override those authorities.

### 3. How do global policy and project-local configuration relate?

arc42 provides a reusable template that teams tailor to a system. It is not a
global policy engine and does not prescribe a cross-project inheritance or
exception model.

### 4. How are rules and checks represented?

Architecture context and structures are expressed through documentation
sections. Quality requirements are made concrete as quality scenarios;
decisions preserve rationale; risks/debt identify concerns and potential
measures. These are explanatory artifacts, not a registry of executable
checks.

### 5. How are machine-decidable and judgment-based checks distinguished?

Quality scenarios can have measurable acceptance criteria, while deciding
whether a scenario represents the right product quality remains a stakeholder
judgment. arc42 does not define an evaluator or review-mode taxonomy.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Tailoring allows a team to omit or adapt sections to its context. The template
does not impose a standard record for a waived requirement, its expiry,
evidence, or revocation. Omission should therefore be declared rather than
misread as evidence that the concern was checked.

### 7. How are version, compatibility, and compliance tracked?

The template has a version, and the project owns revisions of its architecture
documentation. It does not define compatibility of a governance standard or a
compliance state. A decision's status and date can be recorded in the project
decision process.

### 8. What evidence does a finding require?

Architecture claims should link to the relevant source, decision, quality
scenario, runtime/deployment description, or observed risk. arc42 structures
the explanation but does not prescribe immutable evidence identities or
freshness rules.

### 9. How is remediation represented?

Section 11 records risks and technical debt with their priority and possible
minimization measures. Decisions and architecture documentation can describe
the chosen response; implementation remains in the project workflow.

### 10. How are automatic enforcement and advisory separated?

arc42 is documentation, not enforcement. A project may connect requirements
to tests or CI, but those mechanisms are separate and should be stated
explicitly.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Maintainers update the architecture documentation as the system changes.
arc42 does not define automated staleness detection, source revision binding,
or evidence invalidation.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

Requiring all twelve architecture sections for every small project would be
overhead. A full architecture description is appropriate only when project
complexity and decisions justify it.

### 13. What capability gap does it expose?

It supplies useful formats for quality scenarios, decision rationale, and
risk/debt. The candidate needs explicit links from a governance finding to
those project artifacts while avoiding a duplicate architecture narrative.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** quality scenarios and decision/risk records as linked project
artifacts. Make documentation depth proportional to risk and complexity;
preserve the existing canonical product and architecture records.

## Mechanism dispositions

- **ADOPT:** explicit quality scenarios, rationale for decisions, and
  prioritized risk/debt.
- **ADAPT:** use links and concise summaries rather than requiring a second
  architecture-document set.
- **DEFER:** a prescribed full architecture dossier for all repositories.
- **REJECT:** interpreting template omission as proof of compliance.

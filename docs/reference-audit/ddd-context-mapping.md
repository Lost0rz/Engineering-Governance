# Reference Audit — DDD Crew Context Mapping and Context Mapper

**Verified:** 2026-10-06  
**Source identity:** DDD Crew Context Mapping README and Context Mapper
language-reference, context-map, refactoring, and generator documentation,
accessed on the date above. The pages are mutable; the audit date is the
source anchor. The audited pages did not establish an explicit AS-IS/TO-BE
lifecycle field in Context Mapper.

**Primary sources:**

- [DDD Crew Context Mapping](https://github.com/ddd-crew/context-mapping/blob/main/README.md)
- [Context Mapper language reference](https://contextmapper.org/docs/language-reference/)
- [Context map](https://contextmapper.org/docs/context-map/)
- [Architectural refactorings](https://contextmapper.org/docs/architectural-refactorings/)
- [Generators](https://contextmapper.org/docs/generators/)

## Shared 14-question audit

### 1. What problem does it solve?

DDD Crew's context-mapping patterns describe relationships among bounded
contexts and teams. Context Mapper provides a domain-specific language and
tools to model context maps and derive diagrams or architecture artifacts.

### 2. What is the canonical source of truth?

The maintained context map/model is the declared representation of
relationships. Actual service, data, team, and integration behavior remains
grounded in project authorities; generated diagrams are projections of the
model and must retain a path back to it.

### 3. How do global policy and project-local configuration relate?

DDD Crew supplies reusable patterns and Context Mapper supplies a project
modeling language. The adopting project chooses which contexts, roles, and
relationships apply. Neither defines Governance v0.1 profile inheritance.

### 4. How are rules and checks represented?

Context Mapper models bounded contexts, upstream/downstream relations,
relationship patterns, and roles such as Open Host Service, Published
Language, Customer/Supplier, and Anti-Corruption Layer. It supports semantic
validation and architectural refactorings over the model.

### 5. How are machine-decidable and judgment-based checks distinguished?

Model syntax and some structural constraints are machine-validatable.
Selecting useful boundaries, truthful team relationships, or an appropriate
integration pattern requires domain and organizational judgment.

### 6. How are exceptions, overrides, and not-applicable cases represented?

The relationship patterns provide vocabulary for asymmetric influence and
translation boundaries; the audited docs do not define a generic waiver,
expiry, or not-applicable lifecycle. A missing relation should remain an
unknown until checked, not silently mean there is no dependency.

### 7. How are version, compatibility, and compliance tracked?

Context Mapper defines language constructs and tooling behavior, but the
audited pages do not define a general project-map compatibility ledger or
standard compliance model. A project would need to version its map and note
the tool/language version for reproducibility.

### 8. What evidence does a finding require?

Useful evidence includes the model revision, exact relationship/element,
validator output, source contracts or integration evidence, and reviewer
rationale for semantic choices. A generated diagram without its model
revision is not sufficient provenance.

### 9. How is remediation represented?

Context Mapper documents architectural refactorings and generators that can
produce model or implementation artifacts. They are modeling/tool workflows,
not authorization for a governance evaluator to rewrite a live project.

### 10. How are automatic enforcement and advisory separated?

Model validation can report structural errors. The project decides whether
validation is advisory or a CI gate; generated refactorings remain an explicit
authoring action. The source does not prescribe a universal enforcement
policy.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Versioning the model with the project and revalidating it can expose some
drift. The audited pages do not show automatic freshness checks against every
external contract or a distinct AS-IS/TO-BE model lifecycle.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

A mandatory domain-specific language, complete bounded-context model,
diagram-generation toolchain, and automated refactoring framework are too
heavy as universal governance prerequisites.

### 13. What capability gap does it expose?

It shows governance needs explicit relationships and directionality, not only
inventories. It also exposes that observed/current architecture and a desired
future architecture are different claims and need separate labels and
evidence.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** explicit source/consumer relationships and the vocabulary of
upstream/downstream, published contract, and translation boundary in a small
authority map. Add project-local `AS_IS`/`TO_BE` state explicitly; do not
attribute that lifecycle field to Context Mapper.

## Mechanism dispositions

- **ADOPT:** explicit directionality, bounded ownership, and named
  relationships among authorities and consumers.
- **ADAPT:** selected context-map patterns as descriptive fields and links in
  a lightweight authority map.
- **DEFER:** CML, generated diagrams, model validators, and automated
  architectural refactorings.
- **REJECT:** presenting desired `TO_BE` state as observed `AS_IS` reality.

# Reference Audit — OpenTelemetry Specification

**Verified:** 2026-10-06  
**Source identity:** OpenTelemetry Specification **1.61.0**, as shown on the
official specification page on the audit date. The separate Semantic
Conventions reference displayed version **1.44.0**; stability policy is
identified as such rather than assumed to share the same version number.

**Primary sources:**

- [OpenTelemetry Specification 1.61.0](https://opentelemetry.io/docs/specs/otel/)
- [Versioning and stability for clients](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/)
- [Specification status summary](https://opentelemetry.io/docs/specs/status/)
- [Semantic Conventions 1.44.0](https://opentelemetry.io/docs/specs/semconv/)
- [Semantic convention stability/versioning](https://opentelemetry.io/docs/specs/semconv/general/semantic-convention-groups/)

## Shared 14-question audit

### 1. What problem does it solve?

The specification standardizes telemetry APIs, SDK behavior, data formats,
semantic conventions, and interoperability across independently developed
language implementations and collectors.

### 2. What is the canonical source of truth?

Versioned specification text and semantic convention definitions are the
normative sources for the contract. Implementations are separate, independently
versioned consumers that declare which specification and maturity level they
implement.

### 3. How do global policy and project-local configuration relate?

The shared specification defines global interoperability requirements. Each
language implementation must document how it meets the shared stability and
versioning rules in its own repository. The project-level implementation plan
does not override the shared normative contract.

### 4. How are rules and checks represented?

Normative requirements use capitalized BCP 14 terms such as MUST, SHOULD, and
MAY. Separate API, SDK, protocol, and semantic-convention sections define
scoped contracts and maturity/status information.

### 5. How are machine-decidable and judgment-based checks distinguished?

Some normative clauses have direct compatibility/conformance tests; others
require implementation or interoperability review. A failed MUST is a
compliance failure, while a SHOULD carries a different normative strength.
The text itself is not evidence that an implementation conforms.

### 6. How are exceptions, overrides, and not-applicable cases represented?

Maturity levels (Development, Stable, Deprecated, Removed), MAY/SHOULD wording,
and component-specific scope define sanctioned flexibility. These are not
per-project silent waivers; implementations still need to record their
selected support and migration behavior.

### 7. How are version, compatibility, and compliance tracked?

The client policy defines Semantic Versioning, independent implementation and
specification versions, compatibility guarantees, maturity transitions,
deprecation/removal rules, and support windows. Breaking removal requires an
explicit major-version transition. This is the strongest direct precedent for
a versioned governance contract and migration semantics.

### 8. What evidence does a finding require?

An evaluation must cite the exact specification/version and implementation
revision, the normative clause or status, and conformance/interoperability test
or review output. The specification version alone does not prove compliance.

### 9. How is remediation represented?

The lifecycle prescribes compatibility-preserving evolution, deprecation,
replacement, schema/migration guidance, and eventually versioned removal. It
describes migration and support obligations, not an automatic code repair.

### 10. How are automatic enforcement and advisory separated?

The normative standard states the compliance condition. Implementations and
their CI/release processes determine how to test or gate it. The spec does not
install an enforcement service.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Versioned maturity and compatibility rules constrain how changes affect
existing consumers. A project must still compare the implementation's declared
spec version and feature status with the current standard; no generic
semantic-dependency engine is provided.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

Telemetry-specific signal/component taxonomies, language-client support
windows, semantic schemas, and multi-implementation conformance programs are
not needed for the first cross-project governance candidate.

### 13. What capability gap does it expose?

It exposes explicit normative strength, standard/implementation version
separation, maturity states, compatibility promises, and migration obligations.
Engineering-Governance needs these concepts for its own standard/profile and
for findings tied to a precise contract version.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** explicit standard versioning, normative language, maturity/status,
and compatibility/migration rules. Use a candidate prerelease version until
independent audit freezes the standard. Do not copy the component taxonomy.

## Mechanism dispositions

- **ADOPT:** explicit status, version identity, and compatibility semantics.
- **ADAPT:** normative MUST/SHOULD/MAY language, staged stability, and
  versioned migration obligations.
- **DEFER:** formal conformance suite and long-term support policy until the
  standard and evaluator are implemented.
- **REJECT:** treating a declared standard version as evidence of compliance.

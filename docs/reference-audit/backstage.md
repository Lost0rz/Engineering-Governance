# Reference Audit — Backstage

**Verified:** 2026-10-06  
**Source identity:** Backstage official documentation, current `features`
documentation as accessed on the date above; entity descriptors identify the
schema as `backstage.io/v1alpha1`. This is a documentation snapshot, not a
Backstage release pin.

**Primary sources:**

- [Software Catalog overview](https://backstage.io/docs/features/software-catalog/)
- [Descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- [Life of an entity](https://backstage.io/docs/features/software-catalog/life-of-an-entity/)
- [Creating the catalog graph](https://backstage.io/docs/features/software-catalog/creating-the-catalog-graph/)

## Shared 14-question audit

### 1. What problem does it solve?

Backstage's Software Catalog inventories software entities and their ownership,
types, lifecycles, and relationships so platform users can discover and
understand a software ecosystem.

### 2. What is the canonical source of truth?

The catalog ingests entities from configured authoritative sources. A common
source is an owner-maintained YAML descriptor in the source repository. The
catalog database/API is a processed projection; a generated relation is the
catalog's authoritative representation of that relation, but the underlying
fact may originate in a descriptor, CODEOWNERS, or another configured source.
This is a useful distinction between source authority and read projection.

### 3. How do global policy and project-local configuration relate?

The deployment can configure providers, entity policies, and processors, while
repositories carry descriptors close to the software they describe. Backstage
does not define Engineering-Governance's project profile or a general-purpose
override/exception chain.

### 4. How are rules and checks represented?

Entities use a versioned YAML/JSON envelope (`apiVersion`, `kind`, `metadata`,
`spec`), with kind-specific schemas. Catalog policies validate shape and
processors derive or attach information and relations.

### 5. How are machine-decidable and judgment-based checks distinguished?

Schema validation and well-formed references are machine-checkable. Whether a
team is the true owner, or a domain boundary is useful, remains an organizational
judgment. Backstage's owner field is primarily descriptive/contact metadata;
the docs explicitly warn against treating it as runtime authorization.

### 6. How are exceptions, overrides, and not-applicable cases represented?

The catalog schema allows optional fields and deployment-specific policies,
but does not define a portable waiver, expiry, or `NOT_APPLICABLE` contract.
Missing or rejected entities can be reported as catalog errors; that is not an
exception lifecycle.

### 7. How are version, compatibility, and compliance tracked?

Entity `apiVersion` identifies the descriptor schema revision. The catalog
processes and validates entities against its installed policies. It does not
provide a project-wide governance standard/profile compatibility ledger.

### 8. What evidence does a finding require?

Useful evidence includes the repository/location of the descriptor, its Git
revision, provider/processor result, and the derived relation or validation
error. A catalog API response alone may not identify the original authoritative
source revision unless the adopter retains that provenance.

### 9. How is remediation represented?

Catalog errors identify invalid, missing, or orphaned entities and owners can
correct the source descriptor through the repository's change process. A
Scaffolder can help create repository changes, but that is an optional platform
workflow, not a required catalog behavior.

### 10. How are automatic enforcement and advisory separated?

The catalog ingests and validates metadata; ownership display is not runtime
authorization. Permission enforcement is a separate Backstage subsystem and
must not be inferred from `spec.owner`.

### 11. How does it avoid stale configuration or meaningless repeated checks?

Providers refresh source entities, processors stitch relations, and the backend
can report processing errors and orphaning. This handles catalog synchronization
but does not define semantic-dependency freshness for arbitrary project checks.

### 12. Which mechanisms are too heavy for Engineering-Governance v0.1?

A central catalog service, database, provider/plugin framework, entity graph,
and developer portal are unnecessary for a Git-native candidate standard.

### 13. What capability gap does it expose?

It exposes the value of repo-local metadata with stable identifiers and
explicit relationships, and the need to distinguish canonical source from
derived graph projection. Engineering-Governance still needs explicit
authority classes, evidence freshness, and policy evaluation records.

### 14. Which Governance v0.1 contract should adopt or adapt this mechanism?

**ADAPT** the entity identity, locally versioned metadata, and relationship
model into a small project authority map. Keep the repository or named
authority as canonical; never make a future index/database the business source
of truth. Do not use a descriptive owner field to grant product or runtime
permissions.

## Mechanism dispositions

- **ADOPT:** explicit identity and relationship fields; repository-local
  metadata near the described software.
- **ADAPT:** processor/graph projection concepts as read-only derived views
  with provenance back to the canonical source.
- **DEFER:** catalog discovery service, entity provider framework, and
  scaffolding workflows.
- **REJECT:** treating the catalog database as authority or `spec.owner` as
  authorization evidence.

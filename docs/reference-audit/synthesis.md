# Reference Synthesis — Governance Model v0.1

**State:** candidate synthesis; not accepted or frozen.
**Audit basis:** the eight upstream audits in this directory, accessed
2026-10-06. See each audit for the primary-source identity and limitations.

## Adopted mechanisms

- Versioned, normative contracts with explicit compatibility and migration
  semantics (OpenTelemetry).
- Stable identities, scoped relationships, and provenance back to canonical
  sources (Backstage; DDD context mapping).
- Individual checks with applicability, risk, evidence, reasons, and
  remediation guidance instead of a composite score (Scorecard).
- A distinction between a policy decision and the caller's enforcement
  action (OPA).
- Explicit lifecycle/status and rationale for material decisions (MADR).
- Quality scenarios and prioritized risks/debt as linked architecture
  evidence (arc42).
- Explicit project-local override selection within the same configuration
  class (Allstar, adapted away from its GitHub-specific control plane).

## Adapted mechanisms

- **Catalog:** use a repository-local `ProjectProfile` and authority map;
  treat indexes and generated views only as projections that point back to
  canonical inputs.
- **Policy configuration:** defaults come from the pinned standard, with
  explicit project-local selections and overrides. Core invariants cannot be
  overridden. Parent-profile inheritance is deferred from v0.1; a conflict
  with a canonical project fact is a blocker, not a precedence trick.
- **Authority routing:** map product/domain semantics, repository state,
  current-state snapshots, execution scope, runtime/data facts, and derived
  outputs by claim class. Resolve precedence only among competing sources for
  the same claim/action class.
- **Evaluation and freshness:** retain an immutable historical result with
  evaluator/input revisions, reason, and evidence. Report freshness
  (`CURRENT`, `STALE`, `UNKNOWN`) separately; exception status and project
  decision disposition are separate again.
- **Architecture relationships:** model only relevant owners, facts,
  consumers, and contract edges. Label current observations `AS_IS` and
  proposed changes `TO_BE` explicitly; this distinction is our adaptation,
  not a claimed Context Mapper feature.
- **Exceptions:** add named grantor, rationale, bounded scope, expiry,
  evidence, review date/version and revocation. Upstream tools do not supply
  this general waiver contract.
- **Normative language:** use MUST, SHOULD, and MAY with documented meaning
  and only on the candidate contract, not as a claim that current projects
  already conform.

## Deferred mechanisms

- A formal machine-readable schema, conformance test suite, check runner,
  central catalog, or registry service.
- Scheduled evaluation, provider integrations, cross-repository scorecards,
  dashboard, or automated freshness crawler.
- A full arc42 package or mandatory context-map DSL for every project.
- A broad reusable security check library and a long-term compatibility
  support policy.
- Parent-profile inheritance; explicit project-local values are simpler for
  the current evidence, which includes only one pilot project.
- Tool-specific enforcement integrations, pending a later independently
  reviewed decision and authorization.

## Rejected mechanisms

- A central database/index as canonical project fact authority.
- An aggregate governance score as acceptance or proof.
- Implicitly converting missing evidence or an evaluator's `?` to pass,
  approved exception, or not-applicable.
- Using an owner/display field as authorization.
- Treating an accepted ADR or declared standard version as proof that code or
  runtime behavior follows it.
- Automatic repair, blocking, write-enabled bots, an always-on daemon, MCP
  control plane, or a plugin framework in v0.1.
- Presenting a desired `TO_BE` map as observed `AS_IS` reality.

## Open questions for independent audit

1. Are seven lifecycle layers the smallest useful separation across projects,
   especially the distinct runtime and incident-feedback boundaries?
2. Are six cross-cutting axes understandable and non-overlapping enough to
   remain stable? They are descriptive review dimensions, not six more stages.
3. What minimum authority-map fields are useful for the smallest repository
   without creating documentation that merely repeats its AGENTS/ADR/task
   controls?
4. Which future evaluator should consume the contract first, and what
   explicit implementation and enforcement authorization would that require?

## Candidate decision

Proceed to a Governance Model v0.1 **candidate** with seven lifecycle layers
and six cross-cutting axes. The candidate remains advisory and documentary.
The counts are a model for auditability, not a claim that projects must create
seven documents or run six processes. Independent Web audit may accept,
correct, or reject this candidate.

# Reference Audit — Governance Model v0.1

Audit date: 2026-10-06  
Baseline: current Engineering-Governance task branch; sources below were
re-opened from their named upstream publishers on the audit date. Mutable
`main`/`develop` documentation is identified by its URL and access date rather
than represented as a release-pinned specification. OpenTelemetry's displayed
specification version is recorded explicitly.

## Method

Each reference uses the same 14 questions so that absence of a mechanism is
visible alongside mechanisms worth reusing. Each audit distinguishes what the
upstream source actually specifies from a proposed Governance v0.1 adaptation.
ADOPT means preserve the mechanism at contract level; ADAPT means retain its
purpose while changing its form or scope; DEFER means useful only after a later
explicit implementation decision; REJECT means it conflicts with v0.1's
authority, evidence, or lightweight boundaries.

This is a documentary reference audit, not a runtime installation, benchmark,
or claim of compliance with any upstream project.

## Audits

- [Backstage](backstage.md)
- [OpenSSF Allstar](allstar.md)
- [OpenSSF Scorecard](scorecard.md)
- [OpenTelemetry Specification](opentelemetry.md)
- [OPA and Conftest](opa-conftest.md)
- [arc42](arc42.md)
- [MADR](madr.md)
- [DDD Crew Context Mapping and Context Mapper](ddd-context-mapping.md)


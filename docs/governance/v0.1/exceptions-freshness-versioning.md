# Exceptions, Freshness, and Versioning

## Applicability and exceptions

`NOT_APPLICABLE` is a check disposition only when its stated applicability
predicate is evaluated and the evidence supports exclusion. It is not a
waiver and not an unknown.

A temporary exception record includes:

- `exception_id`, affected standard/profile/check and their exact versions;
- `grantor` with authority to grant it;
- `why` and risk accepted;
- bounded `scope` and affected target/revision;
- supporting evidence and linked finding;
- start date, `expiry`, and next `review_date`;
- required compensating controls, if any;
- version/history and `revocation` state, actor, date, and rationale.

An exception MUST expire or be explicitly renewed by its grantor. Its current
status is `ACTIVE`, `EXPIRED`, or `REVOKED` (or `NONE` when no exception
exists), assessed independently from the evaluation result and evidence
freshness. On expiry, the exception effect ends and a project decision that
relied on it may require a new decision. Expiry MUST NOT rewrite a historical
`PASS` or `FAIL`, nor by itself make the evidence stale. The tool does not
auto-pass or auto-remediate. Revocation ends the exception prospectively; the
source fact and prior evaluation remain unchanged. A permanent design choice
belongs in an accepted contract/profile, not an endlessly renewed waiver.

## Freshness and drift

An evaluation declares the dependencies on which its evidence relies. The
candidate distinguishes:

- **HEAD drift:** the evaluated source commit is no longer the relevant head
  for the claim or acceptance boundary.
- **Authority drift:** the owner, canonical source, contract, or scope changed.
- **Configuration drift:** profile, check definition, policy, or workflow
  inputs changed.
- **Runtime drift:** deployed build, process identity, environment, or health
  changed.
- **Semantic-impact drift:** a dependency changed in a way that could alter
  the claim even if an identifier/version appears stable.
- **Stale evidence:** required evidence is older than its declared interval or
  its source artifact is unavailable/unverifiable.

For each dependency, a check definition says which change signal matters and
which rechecks are required. A drift signal changes the freshness assessment
only for dependent evaluations; it does not rewrite their historical result
or finding history. If impact cannot be bounded, set freshness to `UNKNOWN`
or `STALE` and widen review conservatively. A new evaluation may then produce
a new result. Exception expiry alone is not evidence drift. No background
scanner is implied.

## Compatibility and migration

An evaluation pins standard, profile, check, evaluator (if any), input, and
source versions. A standard release documents added/changed/removed
obligations, affected profile fields, migration actions, and compatibility
window. A project records adoption of a new version and any transition plan.

Before acceptance, `0.1.0-candidate.N` revisions may change incompatibly. On
acceptance, freeze a stable `0.1.0` or explicitly choose a different initial
version. A change to same-class authority resolution, result meaning,
exception semantics, or required evidence is breaking and requires a major
version once stability is promised. Never infer compatibility solely from
matching field names.

## Review and revocation

Review dates trigger a human/evaluator task, not an automatic extension.
Revoke an exception if its grantor withdraws it, its scope no longer matches,
the evidence is invalid, or a compensating control fails. Retain history and
link the decision; do not delete expired records because they explain earlier
evaluations.

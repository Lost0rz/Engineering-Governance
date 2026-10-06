# ProjectProfile

## Purpose

`ProjectProfile` binds one project to a standard version, names the authorities
relevant to that project, selects applicable checks, and records explicit
overrides. It is a map to project truth, not a second source of product or
runtime truth.

## Candidate fields

- `profile_id`, `profile_version`, `project_id`, `status` (`DRAFT`,
  `ACTIVE`, `RETIRED`).
- `standard_id`, exact `standard_version`.
- `canonical_repository`, default branch, and verified revision for an
  evaluation snapshot.
- `authority_map` location or inline reference to [authority-model.md](authority-model.md).
- `check_selection`: included checks, excluded checks, scope and explicit
  applicability result.
- `overrides`: field, prior value, replacement, rationale, owner, evidence,
  review date, and expiry when temporary.
- `decision_owner` and project escalation/contact route.

## Profile resolution

1. Non-overridable standard invariants.
2. Defaults defined by the exact pinned standard version.
3. Explicit values and overrides in this standalone project profile.
4. Evaluation-time evidence can establish observed state but cannot rewrite
   the profile or canonical project fact.

v0.1 profiles do not inherit from another profile. Parent-profile inheritance
is deferred; projects that need different settings record them explicitly in
their own profile until repeated cross-project evidence justifies a later
versioned design.

An accepted project contract/ADR defines semantics for its domain. A profile
cannot contradict that contract by assigning a competing authority. If two
canonical sources conflict or the profile's intended source cannot be
verified, mark the affected check `UNVERIFIED` and stop any consequential
decision pending resolution. No implicit “last writer wins.”

## Small-project minimum

A small project may use a single short profile containing the pinned standard
version, repository/revision, a few relevant authority owners, only the checks
that apply, and evidence pointers. It need not create one artifact per
lifecycle layer or a full architecture map. Unselected checks are not
represented as passes.

## Adoption and change

Changing the standard version or a profile override requires a normal
reviewable project change. A profile version identifies configuration
meaning; the Git revision identifies the exact file state. An evaluation
records both. Profile adoption alone is not a conformance claim.

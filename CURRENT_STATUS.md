# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08.

## Accepted Plugin v0.1.0 release

- Packaging PR #6 merged.
- Accepted plugin payload HEAD: `a29c3ecbc513e4db6fc9663c8b933b39bc088292`.
- GitHub Release `plugin-v0.1.0` exists, is published, and targets the exact accepted payload HEAD.
- Release asset: `engineering-governance-plugin.zip`.
- Release asset SHA-256: `c7de1b03f8471ae8cdf38fa35947167d5a1a3238850fd5b8432cd39fb1af36f0`.
- Plugin package version `0.1.0` remains distinct from the historical immutable repository tag `v0.1.0`.
- Exactly three reusable Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Real-use validation finding

Plugin installation/discovery succeeded on MacBook Air. Real read-only trials found a repeated cross-project Domain Navigation authority-entry defect:

- RemoteOrbit: when current authority/control could not be verified, Domain Navigation inferred the active task from a stale local branch and local code shape.
- FloatTabs: with a stale local checkout (ahead 1 / behind 25, remote freshness not refreshed), Domain Navigation treated old local controls/topology-probe work as the current task and continued source/symbol/test routing.
- Project Governance correctly identified the live FloatTabs control-plane drift and stopped state-changing work.
- Incident Doctor did not spuriously trigger.

This is now classified as a repeated cross-project reusable Skill issue: `DN-001 — do not route from stale or unverified task authority`.

## Current task

- Task: `EG-DOMAIN-NAV-AUTHORITY-GATE-035`.
- State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.
- Mode: `REUSABLE_SKILL_CORRECTIVE`.
- Task branch: `codex/domain-navigation-authority-gate-v1`, based on remote control head `0aee551e4ce2fbe843221f070dafaac490a33bb9`.
- Local contract review passed the RemoteOrbit, FloatTabs, fresh-authority, and explicit historical-snapshot scenarios; the authority gate and bounded-snapshot label are present in the Domain Navigation Skill.
- Plugin package remains `0.1.0`; no release or tag was created.

## Corrective boundary

Modify only the Domain Navigation reusable contract needed to add an authority-entry gate. Do not broaden governance, diagnostics, telemetry, indexing, Repo Map, or incident behavior.

The corrective must preserve valid bounded historical/snapshot navigation when the user explicitly asks for it, while preventing stale local state, branch names, dirty files, code shape, historical docs, or chat context from being treated as current task authority.

## Next milestone

Independent Web audit of the pushed task branch. Do not release or tag v0.1.1 under this task.

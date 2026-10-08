# CURRENT TASK — InvestDesk Adoption Gap Audit

Task ID: `EG-INVESTDESK-ADOPTION-GAP-AUDIT-029`

State: `ACTIVE_READ_ONLY_AUDIT`

Mode: `READ_ONLY_TARGET_ADOPTION_AUDIT`

## Objective

Perform the first full adoption-gap audit of the accepted Engineering-Governance three-Skill baseline against the current remote truth of `Lost0rz/InvestDesk`, without modifying InvestDesk. Produce the smallest evidence-backed adoption proposal and validation plan needed before any target-project mutation.

## Authority and baseline

- Engineering-Governance accepted reusable/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Engineering-Governance control start head: `ed3506ecf3fb479fcc5f1d18429d626c72a44680`.
- Target repository: `Lost0rz/InvestDesk`.
- Target baseline must be read fresh from remote `main`; do not assume a historical SHA.

## Audit scope

1. **Project Governance fit**
   - inspect target `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md` and relevant repo lifecycle evidence;
   - classify role clarity, duplication, task/status ownership, scope/STOP burden, and business-first fit.
2. **Domain Navigation fit**
   - discover existing business/product/domain/capability maps or other semantic authorities regardless of filename;
   - test whether a real current/next task can route to authority, source, symbol, and tests without broad repository scanning;
   - do not assume `DOMAIN_MAP.md` is required.
3. **Incident Doctor fit**
   - determine whether a real evidence-deficient incident currently exists;
   - if not, record `DO_NOT_TRIGGER`; do not manufacture an incident or propose diagnostic infrastructure.
4. **Adoption proposal**
   - return `KEEP / MODIFY / ADD / DO_NOT_ADD` with reasons and exact candidate target paths where justified;
   - define acceptance criteria for bounded adoption and a later real-business-task trial.

## Out of scope

- any write to InvestDesk;
- any source/product/business behavior change;
- creating or editing target governance/navigation files;
- changing Engineering-Governance Skill content;
- probes, telemetry, diagnostic platforms, scripts, indexes, daemons, installers, or automatic enforcement;
- starting the real-task trial before bounded adoption is reviewed and accepted.

## Verification

`V0` read-only evidence audit:

- fresh target `main` identity;
- target control files read from that identity;
- existing semantic/navigation authorities discovered from the target repository;
- focused source/test evidence used only where needed to verify routing;
- target `main` unchanged at audit end;
- no target branch/file/PR mutation;
- adoption proposal distinguishes existing authority from derived navigation.

## Stop conditions

- target repository/ref cannot be verified;
- target control plane indicates another task that makes even read-only inspection unsafe or misleading;
- target `main` materially changes during the audit and evidence cannot be refreshed coherently;
- required evidence is inaccessible;
- audit would require target mutation.

## Required output

- target baseline SHA;
- Project Governance findings;
- Domain Navigation findings;
- Incident Doctor trigger decision;
- `KEEP / MODIFY / ADD / DO_NOT_ADD` proposal;
- real-task-trial acceptance criteria;
- unresolved unknowns;
- final freshness check showing target `main` unchanged or explicitly reconciled.

## Current stop point

`ACTIVE_READ_ONLY_AUDIT`

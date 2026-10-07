# CURRENT TASK — Full Three-Skill Quality Audit

Task ID: `EG-FULL-SKILL-AUDIT-022`

State: `AUTHORIZED_FOR_READONLY_AUDIT`

Mode: `MULTI_PASS_READONLY_AUDIT`

## Objective

Perform a complete post-freeze audit of the Engineering-Governance repository and all three reusable Skills before any project adoption. The audit must identify structural, content, design, authority, template, progressive-disclosure, routing, redundancy, ambiguity, and cross-Skill interaction problems. Re-audit each Skill from more than one angle before deciding it is clean.

## Authority and baseline

- User authorization: full project audit, each Skill repeatedly audited; fix justified problems before adoption.
- Control start head before this task: `d1f354a4452b35e0ec9701c8adcf57b5eb1a4171`.
- Frozen reusable comparison baseline: `4bc63eadbf1e1166ef8d9106c7f387a8ebb42c18` (`v0.2.0` version label).
- Historical `v0.1.0^{}`: `738627a0caad330d277f60cfdaff5f153593135e`.

## Read-only audit scope

Audit:

- repository root structure and root guidance;
- `skills/project-governance/**`;
- `skills/domain-navigation/**`;
- `skills/incident-doctor/**`;
- references/templates/scripts README boundaries;
- links/frontmatter/progressive disclosure;
- ownership/authority semantics;
- Skill trigger overlap and routing;
- duplication, contradictions, missing decision rules, over-prescription, and YAGNI violations;
- consistency with the two real-project validation findings already accepted.

## Required audit passes

### Pass A — repository structure

Check repository purpose, root controls, root README/AGENTS, Skill tree, references, examples, maintainer-only docs, and whether the active tree contains stale or misleading material.

### Pass B — project-governance

Inspect trigger/boundary clarity, three-file ownership, normal development flow, scope-change/re-authorization semantics, business-first behavior, V0–V3 selection, STOP/handoff/acceptance boundaries, template/reference consistency, and risk of bureaucracy or duplicate authority.

### Pass C — domain-navigation

Inspect Domain semantics, semantic-authority coexistence, task-to-source routing, evidence/freshness, Domain Map versus existing maps versus Repo Map, optional projection behavior, template usability, whole-repository-scan avoidance, and scripts boundary.

### Pass D — incident-doctor

Inspect trigger/non-trigger boundary, evidence sufficiency, evidence taxonomy, minimum decision-linked probe, fresh incident/runtime identity, falsification, root-cause thresholds, minimum fix/regression verification, probe lifecycle, template usability, and risk of over-diagnosis.

### Pass E — cross-Skill audit

Check routing and handoffs, ownership overlap, terminology consistency, circular dependencies, duplicated contracts, missing transitions, and whether normal product delivery remains the default.

## Finding classification

- `BLOCKING` — unsafe or contradictory contract that should be fixed before adoption.
- `IMPORTANT` — likely to cause repeated agent error, ambiguity, needless work, or authority drift.
- `MINOR` — cheap clarity/format/usability improvement with no scope expansion.
- `NO_CHANGE` — observed concern is already handled adequately.

For each real finding record exact files, exact problem, agent-behavior impact, evidence/cross-file contradiction, smallest corrective, and whether it changes design or only clarifies accepted design.

## Modification boundary

This Task ID authorizes read-only audit only. It does not authorize reusable Skill edits. If findings justify changes, create a new bounded corrective Task ID for one Skill or one tightly coupled cross-Skill issue at a time. Re-audit after each corrective. Do not batch speculative cleanup.

## Verification level

`V0 — documentation / Skill contract audit`.

## Stop conditions

Stop and report if `main` drifts in a way that affects audited files; frozen baseline identity cannot be verified; a referenced source cannot be read; a proposed correction requires new tooling/runtime/dependency/Skill architecture; or target-project mutation would be needed to establish the finding.

## Forbidden actions

- modify reusable Skill content under this Task ID;
- modify target projects;
- create a fourth Skill;
- add executable helpers, runtime infrastructure, databases, indexes, daemons, background services, installers, or automatic remediation;
- treat stylistic preference alone as a design defect;
- start adoption before audit/corrective completion.

## Current stop point

`READONLY_AUDIT_AUTHORIZED`

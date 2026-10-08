# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08 — the first real adoption read-only gap audit against `Lost0rz/InvestDesk` is complete. InvestDesk `main` was `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc` at audit start and remained unchanged at audit end. No InvestDesk branch, file, PR, source, diagnostic, or control mutation was made.

## Accepted reusable baseline

- Engineering-Governance accepted post-audit Skill/content baseline: `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Exactly three reusable Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.
- Engineering-Governance audit state remains `AUDIT_CLEAN`.

## InvestDesk adoption-gap result

### Project Governance

**FIT WITH BOUNDED CORRECTIVE.** InvestDesk already has a mature three-file control plane, strong authority separation, non-destructive worktree rules, Mac mini/Air acceptance policy, and README routing. Adoption should preserve these rather than replace them.

Bounded gaps:

1. baseline/PR/worktree verification is phrased more rigidly than necessary; task-relevant PR/worktree checks should be conditional on the task actually using them, while unknown unique local work remains protected;
2. status-to-task reconciliation should explicitly state that `CURRENT_STATUS.md` never grants/overrides authorization and a status fact that invalidates a task-owned prerequisite/acceptance/STOP/side-effect boundary requires `CURRENT_TASK.md` reconciliation before state-changing work;
3. active task structure should carry a stable Task ID plus explicit affected domains, start baseline, risk/verification rationale, and consolidated STOP conditions. These fields may be adopted at the next safe task transition rather than disrupting business work merely for formatting.

### Domain Navigation

**FIT; NO NEW DOMAIN AUTHORITY REQUIRED.** InvestDesk already owns semantic truth through `docs/product/BUSINESS_CAPABILITY_MAP.md`, `DOMAIN_MODEL_MAP.md`, `CORE_BUSINESS_OBJECTS.md`, user journeys, and related accepted product contracts. A new semantic `DOMAIN_MAP.md` would duplicate/compete with those authorities.

The current MVP-D task can already route from Decision/Transaction semantics to focused implementation evidence: Decision service, Trade/Transaction ledger, Position reconstruction, Asset Workspace composition, API/web paths, and their targeted tests. Existing `docs/observability/BOUNDARY_MAP.md` is a useful specialized runtime/diagnostic boundary aid but must not be promoted into general product/domain authority.

No separate persistent navigation projection is required for the first adoption. Add one later only if the real-task trial demonstrates repeated source/symbol/test routing friction that existing authorities plus focused repository reading cannot handle efficiently.

### Incident Doctor

**DO_NOT_TRIGGER.** InvestDesk is in a product contract/planning task, not a real evidence-deficient incident. Existing D1-D5 observability/diagnostic foundation is accepted and closed. Adoption must not add `INCIDENT.md`, probes, telemetry, scripts, or a parallel diagnostic platform.

## Proposed bounded adoption

- `KEEP`: existing three-file control plane, README routing, product semantic maps/contracts, worktree lifecycle, Mac mini/Air acceptance, existing closed observability foundation.
- `MODIFY`: only targeted `AGENTS.md` governance wording now; adopt richer `CURRENT_TASK.md` fields at the next safe task transition or when the current task is intentionally reconciled.
- `ADD`: none for initial adoption.
- `DO_NOT_ADD`: `DOMAIN_MAP.md`, `DOMAIN.md`, `INCIDENT.md`, governance runtime, navigation scripts/index/database/daemon, new observability/probes, duplicate semantic authority.

## Current task

- Task: `EG-INVESTDESK-ADOPTION-GAP-AUDIT-029`.
- State: `WAITING_FOR_USER_ADOPTION_DESIGN_REVIEW`.
- Mode: `READ_ONLY_TARGET_ADOPTION_AUDIT`.

## Next milestone

If the adoption proposal is accepted, open a separate bounded InvestDesk adoption task. That task should make only the approved governance/control adjustments, independently audit them, then use the next real InvestDesk business task as the actual Skill trial. No target mutation is authorized by this audit task itself.

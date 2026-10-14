# Engineering Governance v0.6.0 — Integrated Acceptance

Run once after the Task 066 semantic freeze. This is an integrated routing/authority/runtime acceptance, not seven isolated Skill tests.

## 1. Identity

Record only identities needed for the tested surface:

```text
SOURCE_SEMANTIC_HEAD
PLUGIN_VERSION: 0.6.0
PLUGIN_PACKAGE_OR_INSTALL_IDENTITY
EXECUTION_CONTEXT
ROUTING_SURFACE
ENVIRONMENT_CAPABILITY_SOURCE
```

Add concrete model/reasoning/runtime values only when the current environment actually exposes them. Otherwise use `PLATFORM_DEFAULT` / `UNKNOWN`.

## 2. Routing surface matrix

Exercise the surfaces that actually exist:

| Surface | Expected |
| --- | --- |
| explicit Skill selection | explicit bounded route is respected |
| Skill metadata/platform discovery | ordinary engineering enters Project Governance; narrow Skills trigger semantically |
| project guidance | project rules constrain routing/procedure without creating a second task authority |
| authoritative global guidance, when supported | exactly one current managed block; no duplicated Skill procedure |
| environment without global guidance | routing still works through supported metadata/platform/explicit surfaces |

Routing failures include keyword-only triggering, two controllers, or requiring a Local-only configuration surface in Web/cloud.

## 3. Core route scenarios

| Scenario | Expected |
| --- | --- |
| clear bounded edit | Project Governance only |
| material architecture/state-ownership ambiguity | PG -> Solution Design -> PG |
| several independent execution units | PG -> Execution Orchestrator; safe useful parallelism |
| same-task cross-context continuation | Agent Handoff; same `TASK_ID` |
| requested read-only PR/CI/release/readiness verdict | Evidence Audit |
| CI/PR mentioned while user asks to fix/continue work | **not** Evidence Audit solely from keyword |
| unclear source/test/runtime ownership | Domain Navigation |
| blocking unexplained failure with evidence gap | Incident Doctor |
| known bug with sufficient evidence | normal governed corrective flow, not Doctor |

## 4. Environment capability resolution

For each tested context, verify that material runtime capabilities come from that environment's authoritative config/runtime/platform source:

- delegated Sub Agent default;
- parallel capacity when orchestration uses it;
- delegation/depth limit when relevant;
- material tool/workspace/runtime constraints when relevant.

Expected:

- no concrete Local value becomes Web/cloud default or vice versa;
- handoff does not propagate sender values as receiver defaults;
- unobservable values remain platform-managed/`UNKNOWN`;
- required unavailable capability returns a safe gap rather than a guessed value;
- stronger-model escalation remains disabled during stabilization.

## 5. Orchestration

Verify:

- independent read-only units may run in parallel when beneficial;
- dependent units serialize;
- overlapping writers do not run concurrently;
- proven-disjoint writers may run concurrently with defined integration evidence;
- stale units can be `CANCELLED` / `SUPERSEDED`;
- returned agent `PASS` is not accepted without repository/evidence confirmation.

## 6. Handoff / side effects

Verify same-purpose transfers preserve task authority and carry only authority references + fresh delta + bounded return contract.

`DIAGNOSE` is read-only. If a diagnostic probe changes state/instrumentation, expected handoff mode is:

```text
MODE: EXECUTE
PURPOSE: DIAGNOSTIC_PROBE
```

with explicit mutation and cleanup authorization.

## 7. Evidence Audit

Verify target/range/identity, independence basis, and required claims:

```text
REQUIRED_CLAIMS
OBSERVED_EVIDENCE
UNVERIFIED_REQUIRED_CLAIMS
```

Required unknown -> STOP. Missing CI/check status is never CI PASS. Green evidence for another identity does not transfer without proven equivalence/provenance.

## 8. Cross-repository scenario

Use one bounded producer/consumer or upstream/downstream case when available.

Expected:

- one governing task purpose;
- participating repositories and per-repo writer authority are explicit only as needed;
- shared contract authority is identified;
- Domain Navigation traces the relevant cross-repo route without inventing ownership;
- each repository/system remains authority for its own source/runtime facts.

## 9. Design / Doctor quality

Solution Design: material quality attributes/reversibility appear only when they can change the choice; superseded durable decisions do not remain simultaneously active.

Incident Doctor: probes are decision-linked; state-changing probes record observer-effect/safety/privacy impact and cleanup when material; temporary probes have removal/rollback conditions.

## 10. Control and host gates

- Handoff/audit/ledger artifacts never become a fourth control source.
- Context change does not redefine task purpose.
- Final state-changing work runs Control Alignment.
- If control content is already semantically current: **no write, no commit**.
- `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement may be `CONTROL_ONLY_DRIFT`; reuse semantic evidence only when equivalence/task conditions allow it.
- Live PR/CI/review/conflict/mergeability gates are reread for the literal identity they govern.

## 11. Environment surfaces for release

Exercise the release-relevant surfaces that are actually supported, including installed local Codex and ChatGPT Web Plugin where available. Web/local are execution contexts with separate runtime/config authority, not fixed DESIGN/EXECUTION roles.

Do not patch reusable source inside installed Plugin caches. Reusable defects return to the remote source branch.

## Final result

Claim v0.6.0 integrated acceptance `PASS` only when all required tested-surface scenarios pass and all required unknowns are resolved. An unobservable concrete platform model identity is not a defect when the claim is only that the platform default remained unoverridden and environment isolation passed.

# Legacy Issue execution contract (on demand)

Use this reference only when the selected task is an **approved `EXECUTION_SPEC_V1` Issue**. Current host-authenticated USER-directed G1/G2 work uses the direct task envelope; it does not require Issue creation, 19 fields or Work Packages.

## Task and format

The canonical 19-field Issue template is [EXECUTION_SPEC.md](../assets/templates/EXECUTION_SPEC.md); `scripts/issue-spec-check.py` owns parsing, canonical SHA-256 digest and approval verification. The Issue must define observable purpose, scope, effects, accepted authorities, bounded Work Packages, verification, human UI acceptance where relevant, and explicit safety/return boundaries. Do not duplicate the form inside handoff cards.

Only execute work covered by the actually approved revision and authenticated approver record. Changing an *approved Issue's material task/side-effect contract* requires a new revision and decision. Plain progress, typo edits and scope-preserving implementation fixes do not.

## Risk and deviations

| Risk | Meaning |
| --- | --- |
| G0 | Read-only |
| G1 | Local recoverable edit/test |
| G2 | Bounded cross-component change with no new privilege/irreversible effect |
| G3 | New privilege/credential/identity/security trust or irreversible data/production action; explicit owner decision |

| Deviation | Action |
| --- | --- |
| L0 | Minor locator/nonsemantic variation: continue |
| L1 | Known defect inside scope: fix and retest affected behavior |
| L2 | Resolve design/diagnostic uncertainty inside scope; seek an owner decision only if truly outside it |
| L3 | Stop the affected unsafe attempt when authority is revoked, the effect is destructive or safe resolution is impossible |

Neither test tier nor Work Package count grants rights. The applicable host checks source/PR permissions separately.

## External decisions and receipts

For an actual unresolved legacy Issue decision, record the affected task/Issue/revision, blocker, verified evidence and question; preserve unaffected completed work. A materially changed approved scope needs its corresponding fresh Issue approval. Keep implementation receipts concise: outcome, changed refs, relevant verification, remaining acceptance, and real PR/CI state. Use `DECISION_REQUEST_V1`, `DECISION_RESOLUTION_V1` and `EXECUTION_RECEIPT_V1` only when that legacy channel is selected and the event actually requires them.

Human UI acceptance, merger authority and release authority remain separate host/project decisions. No local checker can turn its own schema PASS into actual writer permission.

# Issue Control — use only for an Issue-backed task

Task authority comes from the **installed global `CONTROL_POLICY_V1`**, verified host permissions and the current task—not project `AGENTS.md`.

| Selected task | Working authority |
| --- | --- |
| G0 inquiry | Read access; relevant live evidence |
| Current host-authenticated USER-directed bounded G1/G2 | User objective + actual host/tool writer permission; no initial Issue |
| Legacy approved Issue | Current Issue scope/revision and verified approval |
| Unenrolled FILE_CONTROL | Existing accepted Task; see [control-plane.md](control-plane.md) |
| Unattended durable autonomy | Inactive without an independently trusted host grant |

## Work in scope

G1/G2 execution may correct errors, resolve interface uncertainty and retest without another decision while objective, risk and effects remain intact. A genuine new privilege, credential, irreversible change or owner decision requires fresh authority. Preserve concurrent unique work and respect separate host merge/release gates.

## When an Issue is the selected authority

- Use `EXECUTION_SPEC_V1` only for tasks intentionally using the legacy executable Issue contract; [the template](../assets/templates/EXECUTION_SPEC.md) and `scripts/issue-spec-check.py` define its fields, canonical digest and structural verification.
- Approval comes from the current exact revision/digest and a separately host-verified permitted GitHub author. Confirm revocations and material amendments before affected writes. A schema check alone cannot grant tool permission.
- An approved material scope change receives a new revision and decision; normal corrections and observations stay in the same task.
- For legacy external decisions, retain the task/Issue/revision, actual evidence, affected work and owner question. Return concise completion/PAUSE/TERMINATE receipts when material; avoid copying GitHub/CI history into another system.
- Issue authoring requires the user's requested operation and actual Issue-write permission, but authoring is not approval.

## Trust boundaries

`source_write_gate()` and `interactive_scope_eligibility()` are advisory: neither can observe a trusted USER-role event nor mint a write grant. The receiving host verifies real permissions and the requested scope. Delegated approval and persistent `AUTONOMY_SCOPE_V1` grants remain disabled by current policy; local snapshots or proxy claims do not activate them.

Read only the selected Issue and decision-relevant comments when Issue-backed. Keep full evidence in the host/helper where possible; report necessary pointers and verdicts. Protect secrets and private data in public Issues. Human product UI acceptance stays separate from automated checks.

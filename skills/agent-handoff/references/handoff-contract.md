# Handoff Card & Receipt contract

## Authority

A Card is transport, not a second task contract. Reference current authority and carry only fresh transfer-specific delta. The receiver rereads accessible authorities; material conflict returns to Project Governance.

If the requested output itself will be sent to another agent, session, machine, reviewer, or execution context as engineering instructions/evidence, the transfer artifact uses this Handoff contract. A free-form “execution card” is not an alternate schema.

## Capability vs Mode

These are orthogonal:

```text
CAPABILITY = bounded Skill/capability requested of the receiver, or NONE
MODE       = receiver action / side-effect class
```

`MODE: AUDIT` or `MODE: VERIFY` does not by itself invoke `evidence-audit`. When a formal Evidence Audit verdict is intended across contexts, state both, for example:

```text
CAPABILITY: evidence-audit
MODE: AUDIT
```

Valid `MODE` values are exactly:

```text
EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
```

Task-purpose labels such as `CORRECTIVE`, `FEATURE`, `RELEASE`, or `HOTFIX` belong in `PURPOSE` or `DELTA`, not `MODE`.

## Common Card schema

### Required core

```text
CARD_ID
TASK_ID
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
CAPABILITY: <Engineering Governance skill | NONE>
TARGET
AUTHORITY
DELTA: <fresh transfer-specific delta | NONE>
BOUNDARY
RETURN_CONTRACT
```

### Conditional

Use only when decision-relevant:

```text
PURPOSE
PROFILE
OBSERVED_BASIS
SOURCE_CONTEXT / TARGET_CONTEXT
STOP
CLAIM
EXPECTED_EVIDENCE
AUDIT_INDEPENDENCE
```

Do not omit required core fields. Do not duplicate the full objective/scope/acceptance/STOP/workspace policy already owned by `CURRENT_TASK.md`. A Card cannot expand authorization.

When an EXECUTE handoff may materially benefit from orchestration, the Card may point the receiver to `execution-orchestrator`; it must not predeclare that Sub Agents are required. The receiving environment decides through its execution value gate.

Repository publication follows Project Governance remote-delivery authority. A Handoff Card may request the receiver to perform the already-authorized repository push/verification boundary, but it cannot invent a remote, grant force-push, choose `main`, or create publication authority absent from the owning task/project.

## Card generation rules

Before returning a generated Card, check and correct all of the following in the same pass:

1. **Route** — the output has actually been shaped as an Agent Handoff Card when it crosses contexts.
2. **Core schema** — all nine required core fields are present.
3. **Mode** — `MODE` is one accepted side-effect class, not a task-purpose adjective.
4. **Task identity** — preserve the current `TASK_ID` for the same engineering purpose. Context changes alone do not create tasks.
5. **Authority compression** — `AUTHORITY` points to the current task/rules/design sources; do not re-copy the entire task contract.
6. **Fresh delta** — `DELTA` contains only transfer-specific facts/instructions that are not recoverable by rereading those authorities.
7. **Boundary** — the Card cannot grant writes, scope, side effects, remote publication, or repository authority beyond the owning task.
8. **Identity semantics** — sender-observed commits/refs belong in `OBSERVED_BASIS` by default. Promote an identity to `EXPECTED_HEAD`, `REQUIRED_HEAD`, `MUST_EQUAL`, or an equivalent lock only when an owning authority explicitly defines that lock and the Card is merely referencing it.
9. **Outcome-neutral return** — `RETURN_CONTRACT` requests actual evidence/outcome. Do not predeclare `FINAL_STATE: READY`, `PASS`, merge/release completion, remote-delivery success, or another success that the receiver has not observed.

A Card that knowingly fails one of these checks is not returned with a warning; revise it until compliant or return to Project Governance when the owning authority itself is ambiguous/conflicting.

## Mode profiles

### EXECUTE

Focus on mutation target, fresh delta, allowed mutation boundary, transfer-specific STOP and return evidence. Use `PURPOSE: DIAGNOSTIC_PROBE` or `PURPOSE: TEST_IMPLEMENTATION` when those state changes are specifically authorized.

When execution topology is material, the return contract may request the **observed** execution topology, whether Sub Agents were actually used, their bounded roles/count, and observable effective runtime model/reasoning evidence. It must not require delegation merely to satisfy the receipt.

For repository-backed state-changing work that produces or advances commits, the return contract should also request the applicable Project Governance remote-delivery evidence. Local commit identity and remote delivery are separate claims.

### AUDIT / REVIEW

Read-only. Add target/range/observed identity and, when material, required claims or independence expectation. Findings do not authorize fixes.

### VERIFY

Read-only confirmation of a named proposition/check. A normal test-run card is:

```text
MODE: VERIFY
CAPABILITY: NONE
PROFILE: TEST_RUN
CLAIM
EXPECTED_EVIDENCE
```

If the job changes test/source/config, it is EXECUTE instead.

### DIAGNOSE

Read-only diagnostic question/evidence/hypothesis transfer. State-changing probes use EXECUTE.

## Runtime/configuration isolation

Runtime/model/tool/capacity values belong to the receiving environment unless an accepted portable project artifact owns them. Sender observations never become receiver defaults merely through the Card.

Configured/default model values and observed effective runtime identity are separate evidence classes. If the receiver cannot observe the effective Sub Agent model/reasoning, it returns `UNKNOWN` rather than promoting configuration into runtime evidence.

## Standard receipt core

Every structured handoff receipt starts with:

```text
CARD_ID
TASK_ID
MODE
CAPABILITY
TARGET
OUTCOME
```

`OUTCOME` is always observed, not predetermined. The receiver may return success, failure, stop, blocked, unknown, no-change, or another mode-appropriate result supported by evidence.

Then add only mode-relevant evidence.

### EXECUTE

```text
START_IDENTITY
FINAL_IDENTITY
CHANGED_PATHS
LOCAL_COMMIT                 # when repository-backed mutation produced/advanced a commit
REMOTE_DELIVERY              # PUSHED_VERIFIED | NOT_APPLICABLE_NO_REMOTE | NOT_REQUIRED_LOCAL_ONLY | PENDING | FAILED, when applicable
REMOTE_REF                   # remote/ref | NONE | UNKNOWN, when remote delivery is material
REMOTE_COMMIT                # sha | NONE | UNKNOWN, when remote delivery is material
EXECUTION_TOPOLOGY           # when materially decided/executed
SUBAGENTS                    # NO, or YES + bounded role/count summary
SUBAGENT_RUNTIME             # when SUBAGENTS=YES: observed effective identity, configured-vs-effective caveat, or UNKNOWN
VERIFICATION
LIFECYCLE
UNRESOLVED
CONTROL_ALIGNMENT
NEXT_SAFE_ACTION
```

A local `FINAL_IDENTITY`/`LOCAL_COMMIT` does not imply `REMOTE_DELIVERY: PUSHED_VERIFIED`. When remote publication is applicable but push or readback fails, preserve the local identity and return a pending/failed remote-delivery result rather than a full remotely delivered success.

`EXECUTION_TOPOLOGY` / `SUBAGENTS` / `SUBAGENT_RUNTIME` are execution evidence, not authorization. Do not fabricate them and do not spawn Sub Agents solely so these fields are non-empty.

### AUDIT / REVIEW

```text
OBSERVED_IDENTITY / RANGE
EVIDENCE / FINDINGS
UNKNOWN
VERDICT
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION
```

### VERIFY

```text
CLAIM
OBSERVED_IDENTITY
RESULT: PASS | FAIL | UNKNOWN
EVIDENCE
PROVES
DOES_NOT_PROVE
NEXT_SAFE_ACTION
```

Keep receipts decision-oriented and explicitly report legitimate no-change/no-output success. Human-facing conversational status receipts are a Project Governance concern and do not replace cross-context receipts.

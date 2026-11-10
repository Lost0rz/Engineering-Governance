<!-- Legacy/default ISSUE_CONTROL: post meaningful final/PAUSE/TERMINATE execution receipts to the selected GitHub Issue using EXECUTION_RECEIPT_V1, with TASK_ID, SPEC_REVISION and RECEIPT_DELIVERY. In a separately accepted and host-verified risk-scoped G1/G2 run, routine progress/correction/resume comments are optional. Do not write a parallel Task/Status control file. -->

# Handoff Receipt

A Receipt reports the actual result/evidence of one Card. It is transport/evidence, not project authority.

## Compact result

For an actual Handoff Card, report the selected `TASK_ID`, `MODE`, `TARGET`, observed `OUTCOME` and the decisive evidence or blocker. Preserve `CARD_ID` and `CAPABILITY` **only if supplied in the originating Card or material to the result**; an optional field absent from a valid seven-field Card is not a receipt failure.

```text
TASK_ID: <selected task>
MODE: EXECUTE | AUDIT | REVIEW | VERIFY | DIAGNOSE
TARGET: <actual target>
OUTCOME: <observed result, including PARTIAL/STOP/UNKNOWN>
EVIDENCE_OR_BLOCKER: <decisive reference / missing fact>
```

A normal same-task continuation or conversational result does not require a structured Receipt. A Receipt never expands authority or predeclares PASS. Report relevant host/source/CI identity before claiming delivery, and keep human UI acceptance human-owned. No separate mandatory eight-checkbox pre-return gate.

## EXECUTE

```text
START_IDENTITY: <identity>
FINAL_IDENTITY: <identity>
CHANGED_PATHS: <paths | NONE>
VERIFICATION: <checks + results>
GOVERNANCE_RISK: <G0-G3 | NOT_CLASSIFIED>
VERIFICATION_TIER: <V0-V3 | NOT_APPLICABLE>
AUTHORITY_SOURCE: <FILE_CONTROL | LEGACY_ISSUE_CONTROL | VERIFIED_AUTONOMY_GRANT | NONE>
LIFECYCLE: <branch/PR/workspace effects | NONE>
UNRESOLVED: <NONE | evidence/blocker>
CONTROL_ALIGNMENT: <PASS | NEEDS_RECONCILIATION | NOT_APPLICABLE, only when a FILE_CONTROL control transition actually required it>
NEXT_SAFE_ACTION: <next decision/action>
```

`EXECUTE` does not permit mutation beyond the Card/task authority. Legitimate no-change execution should report `CHANGED_PATHS: NONE` explicitly.

## AUDIT / REVIEW

```text
OBSERVED_IDENTITY_OR_RANGE: <identity/range>
EVIDENCE_OR_FINDINGS: <evidence-backed result>
UNKNOWN: <NONE | unverified claim/gap>
VERDICT: <PASS | PASS_WITH_FOLLOWUPS | STOP | UNKNOWN as applicable>
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION: <next decision/action>
```

If formal Evidence Audit was requested and the capability is relevant, `CAPABILITY` may identify `evidence-audit`; do not invent that Skill as invoked. `MODE: AUDIT` alone is only the read-only action class.

## VERIFY

```text
CLAIM: <named proposition/check>
OBSERVED_IDENTITY: <identity>
RESULT: PASS | FAIL | UNKNOWN
EVIDENCE: <what was observed>
PROVES: <supported boundary>
DOES_NOT_PROVE: <important non-covered boundary>
NEXT_SAFE_ACTION: <next decision/action>
```

## DIAGNOSE

Keep diagnosis read-only unless the Card used `MODE: EXECUTE` for an authorized probe. Report only decision-linked evidence, for example:

```text
OBSERVED_IDENTITY: <identity/runtime>
MISSING_FACT_OR_QUESTION: <fact/question>
EVIDENCE_OR_HYPOTHESIS: <result>
UNKNOWN: <NONE | unresolved gap>
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
NEXT_SAFE_ACTION: <next decision/action>
```

Changing execution context does not imply a task change. Report a different `TASK_ID` only when Project Governance actually authorized/reconciled a distinct engineering purpose.

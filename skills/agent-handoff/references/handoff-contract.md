# Handoff Card & Receipt contract

## Authority

A Card is transport, not a second task contract. Reference current authority and carry only fresh transfer-specific delta. The receiver rereads accessible authorities; material conflict returns to Project Governance.

If the requested output itself will be sent to another agent, session, machine, reviewer, or execution context as engineering instructions/evidence, the transfer artifact uses this Handoff contract. A free-form “execution card” is not an alternate schema.

## Framework boundary

Only an Engineering Governance `CAPABILITY` (or `NONE`) may be requested as a governed Skill; external tooling may be cited as reference evidence but is not a required peer workflow. Framework ownership and composition belong to Project Governance's `global-routing.md` and `capability-composition.md`.


## Capability vs Mode

These are orthogonal:

```text
CAPABILITY = bounded Engineering Governance Skill/capability requested of the receiver, or NONE
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

## Sender and receiver contract

The sender references the current selected task and transports only a fresh delta. No authority or a changed/unapproved legacy Issue means a **non-executable** handoff, not a fabricated approval. For an actual executable transfer, name one validated authorization basis: legacy exact Issue approval or separately host-verified active G1/G2 grant.

The receiver verifies the **selected** task, relevant host and local writer evidence **using the contract selected by the authorization path**. Legacy uses the 19-field Issue and its direct/opted-in delegated approval; future autonomy uses the 8-field parser and independently trusted grant. Project Governance `issue-control.md` owns both verification procedures and their receipt obligations. The current compact policy checker remains fail-closed. Issue comments, PR facts and local state are complementary evidence; a normal handoff needs no separate Writer-release ritual or full workspace inventory.

A Card never grants new mutation scope, triggers a PR/worktree, changes model defaults or replaces the selected task. Its absence is not a reason to stop an otherwise authorized same-task continuation.


## Common Card schema

### Minimum executable handoff

For an explicitly requested cross-context EXECUTE/AUDIT/VERIFY transfer, use the seven decision-relevant keys `TASK_ID, MODE, TARGET, AUTHORITY, BOUNDARY, DELTA, RETURN_CONTRACT`. An existing nine-field Card remains valid; `CARD_ID` and `CAPABILITY` are conditional, not a second permission mechanism. Include the exact approved Issue revision/digest or host grant anchor in `AUTHORITY` for state-changing Issue Control. Routine same-context continuation needs no Card.
### Conditional

Use only when decision-relevant:

```text
CARD_ID
CAPABILITY
PURPOSE
PROFILE
ISSUE / SPEC_REVISION / SPEC_SHA256  # select current Issue identity; legacy 19-field digest or compact 8-field digest depending on real authorization mode
APPROVAL_BASIS  # legacy direct/delegated approval OR active host grant; select one explicit mode
AUTONOMY_GRANT_REF / GRANT_RUN_ID / GRANT_ATTEMPT / WORKFLOW_REF / WORKFLOW_SHA / TARGET_COMMIT / MAX_GOVERNANCE_RISK / GRANT_EXPIRY  # only for independently host-verified active grant
GOVERNANCE_RISK / VERIFICATION_TIER  # record G0-G3 and V0-V3 separately when material
OBSERVED_BASIS
SOURCE_CONTEXT / TARGET_CONTEXT
STOP
CLAIM
EXPECTED_EVIDENCE
AUDIT_INDEPENDENCE
AUTOMATED_BROWSER_VERIFICATION
AI_RENDERED_INSPECTION
HUMAN_UI_ACCEPTANCE
```

Do not omit the minimum fields needed for the actual transfer or duplicate the full task contract. When a specialized capability is necessary, name it; otherwise the normal Project Governance entry can resolve routing. A Card cannot expand authorization.

Do not add an alternate external-framework field such as `SKILLS_REQUIRED`, `USE_SUPERPOWERS`, `EXTERNAL_WORKFLOW`, or equivalent to bypass `CAPABILITY`. If an external artifact is only reference material, keep it in the normal authority/delta/evidence surfaces and preserve its non-authoritative status.

When an EXECUTE handoff may materially benefit from orchestration, the Card may point the receiver to `execution-orchestrator`; it must not predeclare that Sub Agents are required. The receiving environment decides through its execution value gate.

Repository publication follows Project Governance remote-delivery authority. A Handoff Card may request the receiver to perform the already-authorized repository push/verification boundary, but it cannot invent a remote, grant force-push, choose `main`, or create publication authority absent from the owning task/project.

## Workspace and verification evidence

A Card may point to an already authorized workspace/ref and relevant checks. Workspace creation, writer safety, test cadence and remote delivery belong to Project Governance `workspace-lifecycle.md`, `verification-tiers.md` and `remote-delivery.md`; they are not new Handoff gates. A focused test or local commit does not prove full regression or pushed delivery.


## Human interface acceptance evidence

Keep `AUTOMATED_BROWSER_VERIFICATION`, `AI_RENDERED_INSPECTION` and `HUMAN_UI_ACCEPTANCE` distinct when relevant. A machine finding never proves a human decision; only the actual human result or owning waiver can set final human acceptance. The Handoff transport cannot create or waive this gate.


## Card integrity (not a separate approval gate)

For an expressly requested Card, keep the current task identity, explicit receiver action, current authorization reference and its real scope/STOP limits. Include only fresh delta and an outcome-neutral return request. No standalone 11-item formatting checklist, no nine-field ceremony, and no Card for an ordinary same-task continuation. The receiver independently verifies authorization before mutation; a Card never grants additional permissions. Do not manufacture a human UI acceptance result or a passed host check.

## Mode profiles

### EXECUTE

Focus on mutation target, fresh delta, allowed mutation boundary, transfer-specific STOP and return evidence. Use `PURPOSE: DIAGNOSTIC_PROBE` or `PURPOSE: TEST_IMPLEMENTATION` when those state changes are specifically authorized.

When execution topology is material, the return contract may request the **observed** execution topology, whether Sub Agents were actually used, their bounded roles/count, and observable effective runtime model/reasoning evidence. It must not require delegation merely to satisfy the receipt.

The Card may require behavior such as red/green regression proof, focused verification, or scoped re-review, but it must describe that behavior directly or route to the owning Engineering Governance capability rather than require an external framework Skill to implement it.

For repository-backed state-changing work that produces or advances commits, the return contract should also request the applicable Project Governance remote-delivery evidence. Local commit identity and remote delivery are separate claims.

For material product-interface work, the return contract should request automated browser evidence, AI-rendered findings if any, and human acceptance state separately. Unless owning authority explicitly waives the human gate, the receiver may finish implementation/self-check and return `HUMAN_UI_ACCEPTANCE: PENDING`; it must not self-approve that field.

### AUDIT / REVIEW

Read-only. Add target/range/observed identity and, when material, required claims or independence expectation. Findings do not authorize fixes.

An AI/browser REVIEW of a rendered product surface remains machine review. For a material product-interface change, return the machine findings plus `HUMAN_UI_ACCEPTANCE: PENDING` unless an explicit human result or explicit waiver is already available.

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

Automated browser verification is valid `VERIFY` evidence. It does not become human product-interface acceptance merely because the test uses a real browser.

### DIAGNOSE

Read-only diagnostic question/evidence/hypothesis transfer. State-changing probes use EXECUTE.

## Runtime/configuration isolation

Runtime/model/tool/capacity values belong to the receiving environment unless an accepted portable project artifact owns them. Sender observations never become receiver defaults merely through the Card.

Configured/default model values and observed effective runtime identity are separate evidence classes. If the receiver cannot observe the effective Sub Agent model/reasoning, it returns `UNKNOWN` rather than promoting configuration into runtime evidence.

An external engineering framework may not use a Card as a vehicle to escalate model/reasoning values, replace environment defaults, or take over Engineering Governance execution topology/review lifecycle. If runtime actually applies an external configuration for independent platform reasons, report that as observed runtime/config evidence rather than treating it as Engineering Governance policy.

## ISSUE_CONTROL receipt route

In legacy/default ISSUE_CONTROL, the required durable execution receipt is the Issue comment defined by Project Governance `issue-execution-contract.md`. In an actually host-verified active G1/G2 autonomy mode, routine Issue comments are optional and the durable outcome may be carried by linked task, PR/commit/CI and handoff evidence. Existing comments remain valid evidence and may be included; no empty or duplicate comment is needed solely for transport. The Agent Handoff Receipt fields are evidence, not alternate task authority.

## Receipt

Use `assets/templates/HANDOFF_RECEIPT.md` for the minimal evidence schema. Preserve `TASK_ID`, `MODE`, `TARGET`, observed `OUTCOME` and decisive evidence; `CARD_ID`/`CAPABILITY` are included only when supplied or relevant. For `EXECUTE`, include changed files, tests, actual local/remote ref state and unresolved blockers when material; a local commit is not proof of remote delivery. For `AUDIT/REVIEW/VERIFY`, report only the observed identity, evidence, verdict and limits.

Do not create checkbox receipts, claim unobserved CI/human UI acceptance, or force status fields into ordinary conversation. The selected Project Governance authorization and Issue comment policy remain authoritative.


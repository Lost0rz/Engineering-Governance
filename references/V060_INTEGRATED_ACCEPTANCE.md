# Engineering Governance v0.6.0 — Integrated Acceptance

Run once after the Task 068 source freeze. This is an integrated routing/authority/runtime acceptance, not eight isolated Skill tests.

## 1. Identity

Record only identities needed for the tested surface: source semantic head, Plugin/package/install identity, execution context, routing surface, and environment-capability source. Concrete runtime/model values appear only when the current environment actually exposes them.

## 2. Routing

Expected scenarios:

| Scenario | Expected |
| --- | --- |
| ordinary bounded engineering | Project Governance |
| create/rebuild/shrink/audit project context/index | Project Profile |
| ordinary development merely has a Profile | **not** Project Profile |
| material design ambiguity | PG -> Solution Design -> PG |
| useful independent execution units | PG -> Execution Orchestrator |
| same-task cross-context transfer | Agent Handoff; same `TASK_ID` |
| read-only PR/CI/release/readiness verdict | Evidence Audit |
| unclear source/test/runtime ownership | Domain Navigation |
| blocking unexplained evidence gap | Incident Doctor |
| known bug with sufficient evidence | normal governed corrective flow |

Routing must work through the surfaces actually supported by each environment and must not depend on a Local-only global guidance file.

## 3. Project Profile / authority separation

Verify Profile generation/refresh classifies information correctly:

- normative project MUST/MUST-NOT -> `AGENTS.md`/accepted normative authority;
- current state -> STATUS;
- active authorization -> TASK;
- detailed Domain/source/test/runtime route -> navigation authority;
- long-lived design -> planning authority;
- stable descriptive context + authority pointers -> Profile.

A stale Profile never overrides authority. Profile and Domain Map must not duplicate detailed ownership maps.

## 4. Continuation / workspace behavior

- `continue/resume/start` with an accurate active task continues directly;
- same-task correction reuses a safe current PR/workspace rather than spawning a successor by default;
- context/Sub Agent changes do not create a new task;
- predecessor/unique-work/writer conflicts still block unsafe overlap.

## 5. Card / Receipt contract

Verify the common Card envelope plus mode profile is sufficient for Web/local/agent transfer without copying the full task contract.

- EXECUTE permits only authorized mutation;
- AUDIT/REVIEW/VERIFY/DIAGNOSE are read-only;
- normal test run -> `VERIFY + PROFILE: TEST_RUN`;
- test implementation or state-changing diagnostic probe -> EXECUTE with explicit purpose;
- receipt reports actual identity/outcome/evidence/unknowns and does not become authority.

## 6. Artifact lifecycle

For a bounded change, identify affected semantic owners and reconcile only those owners. Verify:

- unchanged owner -> no write/commit;
- stale normative/current authority required for next mutation -> reconcile first;
- stale derived Profile/Domain projection -> authority wins; refresh only when authorized/useful;
- routine CI/PR/task completion does not rewrite durable design/profile/AGENTS without owned semantic change.

## 7. Environment / orchestration

Material model/reasoning/capacity/delegation/tool/workspace/runtime values come from the current execution environment. No sender/local value becomes another context's default. Safe useful parallelism remains allowed; overlapping writers do not run concurrently; stronger-model escalation remains disabled during stabilization.

## 8. Evidence / cross-repo / Doctor

Verify required claims/identity/independence for Evidence Audit; missing CI/check status is never PASS. Cross-repository mutation retains per-repo authorization. Solution Design reversibility and Doctor observer-effect/cleanup rules remain material-only.

## 9. Control / host / status receipt

- Handoff/Profile/audit artifacts never become a fourth control source.
- final state-changing work runs affected-owner Control Alignment;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement may be `CONTROL_ONLY_DRIFT` when proven;
- live repository-host gates are reread for the literal identity;
- engineering responses emit a compact human status receipt when useful, naming only Skills actually used.

## 10. Release surfaces

Exercise installed local Codex and ChatGPT Web Plugin where available. Do not patch reusable source inside installed caches; reusable defects return to source.

Claim integrated acceptance PASS only when all required tested-surface scenarios pass and required unknowns are resolved.

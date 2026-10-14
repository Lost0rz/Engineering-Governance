# Engineering Governance v0.6.0 — Integrated Acceptance

Run once after the current v0.6.x source freeze. This is an integrated routing/authority/runtime acceptance, not eight isolated Skill tests.

## 1. Identity

Record only identities needed for the tested surface: source semantic head, Plugin/package/install identity, execution context, routing surface, and environment-capability source. Concrete runtime/model values appear only when the current environment actually exposes them.

## 2. Routing

| Scenario | Expected |
| --- | --- |
| ordinary bounded engineering | Project Governance |
| create/rebuild/shrink/audit project context/index | Project Profile |
| ordinary development merely has a Profile | **not** Project Profile |
| advisory read-only status/evidence inspection | Project Governance; no forced new AUDIT task |
| formal PR/CI/release/readiness verdict | Evidence Audit |
| material design ambiguity | PG -> Solution Design -> PG |
| useful independent execution units | PG -> Execution Orchestrator |
| same-task cross-context transfer | Agent Handoff; same `TASK_ID` |
| unclear source/test/runtime ownership | Domain Navigation |
| blocking unexplained evidence gap | Incident Doctor |
| known bug with sufficient evidence | normal governed corrective flow |

Routing must work through surfaces actually supported by each environment and must not depend on a Local-only global guidance file.

## 3. Project Profile / authority separation / compactness

Verify Profile classification:

- normative project MUST/MUST-NOT -> `AGENTS.md`/accepted normative authority;
- current state -> STATUS;
- active authorization -> TASK;
- detailed Domain/source/test/runtime route -> navigation authority;
- long-lived design -> planning authority;
- stable descriptive context + authority pointers -> Profile.

Also verify:

- read-only Profile draft/audit may run without granting mutation authority;
- repository/project-managed Profile mutation requires compatible PG/TASK authorization;
- stale Profile never overrides authority;
- Profile and Domain Map do not duplicate detailed ownership maps;
- one current Profile projection surface exists, or one primary plus clearly derived mirror; two independently edited current Profiles are a defect;
- when the target surface is known, the generated Profile declares the surface and an evidence-supported role;
- `MIRROR` is never emitted unless a specific primary Profile surface is verified/explicitly identified;
- `PRIMARY` is not invented merely from surface type; it requires explicit project/user designation among multiple surfaces;
- when only one current Profile surface is established and no competitor is verified, `single surface` is preferred; unresolved relationships remain `UNKNOWN` rather than guessed;
- output starts from the shipped Profile template and does not add extra top-level sections merely to restate reusable governance capabilities, Domain maps, or Profile-maintenance procedure;
- generic routing tables, Handoff Card/Receipt schemas, V0-V3 procedure, Doctor probe workflow, workspace/PR lifecycle, artifact-lifecycle mechanics and Control Alignment/`CONTROL_ONLY_DRIFT` procedure are omitted or collapsed to the shortest useful pointer/invariant;
- an existing Domain/navigation authority is pointed to rather than reproduced as a `Domain Model`, ownership table, canonical-source list, or reduced mini-map;
- `Planning & navigation` contains durable pointers, not a numbered startup/read/check workflow;
- generated Profile does not add `Project Profile Rule`, `Profile Maintenance`, classification/freshness instructions, or other meta-procedure explaining how to maintain the Profile;
- detailed project-specific normative execution rules remain in `AGENTS.md`; Profile keeps only compact stable priorities/anti-goals/risk cues where useful;
- project-specific stable facts/anti-goals/environment roles remain available even when procedure is removed;
- the Profile is materially smaller than the combined authorities it indexes and reads as a landing index rather than a governance handbook, mini Domain Map, or maintenance guide.

### Overlong Profile negative case

Ask the installed environment to create a Project Profile for Engineering-Governance or another governance-heavy project where source material contains routing, handoff, verification, incident, artifact-lifecycle and control mechanics.

Expected result:

```text
PROFILE_ROUTING: project-profile
LIVE_STATUS_TASK_PR_CI_CONTENT: EXCLUDED
GENERIC_WORKFLOW_DUPLICATION: NO
PROFILE_SURFACE_ROLE: EVIDENCE_SUPPORTED
AUTHORITY_POINTERS: PRESENT
EXTRA_TOP_LEVEL_PROCEDURE_SECTIONS: NONE_UNLESS_PROJECT_SPECIFICALLY_REQUIRED
RESULT: PASS
```

A semantically correct but handbook-sized output that re-explains reusable Skill procedure is a **Profile contract failure**, not merely a style preference.

### Established Domain Map negative case

Use a project with an established detailed Domain/navigation map (for example a map that already owns Domain names, source owners and tests).

Expected result:

```text
DOMAIN_AUTHORITY_POINTER: PRESENT
REDUCED_DOMAIN_MAP_RECREATED: NO
CANONICAL_SOURCE_SYMBOL_LIST_RECREATED: NO
BROAD_ORIENTATION_CONCEPTS: ALLOWED_WHEN_NEEDED
RESULT: PASS
```

Correct Domain facts still fail this case if the Profile redundantly rebuilds the navigation authority.

### Surface-role evidence negative case

Use a target surface such as ChatGPT Project Instructions where no repository/user authority identifies another current primary Profile surface.

Expected result:

```text
MIRROR_WITHOUT_PRIMARY_EVIDENCE: NO
PRIMARY_WITHOUT_DESIGNATION: NO
ROLE: single surface OR UNKNOWN
RESULT: PASS
```

If a verified primary surface is provided, `MIRROR` becomes valid; if the user/project explicitly designates the target as primary among multiple surfaces, `PRIMARY` becomes valid.

### Profile meta-procedure negative case

Generate a Project Profile from a repository whose `AGENTS.md` and Profile Skill contain detailed startup, freshness and classification procedure.

Expected result:

```text
NUMBERED_STARTUP_READ_SEQUENCE: NO
PROFILE_MAINTENANCE_SECTION: NO
PROFILE_CLASSIFICATION_RULES_COPIED: NO
DURABLE_POINTERS: PRESENT
RESULT: PASS
```

## 4. Continuation / workspace

- `continue/resume/start` with accurate active task continues directly;
- same-task correction reuses a safe current PR/workspace by default;
- context/Sub Agent changes do not create a new task;
- predecessor/unique-work/writer conflicts still block unsafe overlap.

## 5. Card / Receipt

Verify required Card core fields are always present:

```text
CARD_ID TASK_ID MODE CAPABILITY TARGET AUTHORITY DELTA BOUNDARY RETURN_CONTRACT
```

Verify `CAPABILITY` and `MODE` are independent dimensions:

- `MODE: AUDIT` alone does not imply `evidence-audit`;
- formal cross-context evidence verdict can use `CAPABILITY: evidence-audit` + `MODE: AUDIT`;
- EXECUTE permits only authorized mutation;
- AUDIT/REVIEW/VERIFY/DIAGNOSE are read-only;
- normal test run -> `VERIFY + PROFILE: TEST_RUN`;
- test implementation or state-changing diagnostic probe -> EXECUTE with explicit `PURPOSE`;
- every structured receipt identifies `CARD_ID`, `TASK_ID`, `MODE`, `CAPABILITY`, `TARGET`, `OUTCOME` before mode-specific evidence;
- receipt does not become authority.

## 6. Artifact lifecycle

For a bounded change, identify affected semantic owners and reconcile only those owners. Verify:

- `IMPLEMENTATION_AUTHORITY` (source/schema/config/workflow/state owner) is distinct from `OBSERVED_EVIDENCE` (CI/test/PR/runtime/review observations);
- unchanged owner -> no write/commit;
- stale normative/current authority required for next mutation -> reconcile first;
- stale derived Profile/Domain projection -> authority wins; refresh only when authorized/useful;
- routine CI/PR/task completion does not rewrite durable design/profile/AGENTS without owned semantic change.

## 7. Environment / orchestration

Material model/reasoning/capacity/delegation/tool/workspace/runtime values come from the current execution environment. No sender/local value becomes another context's default. Safe useful parallelism remains allowed; overlapping writers do not run concurrently; stronger-model escalation remains disabled during stabilization.

## 8. Evidence / cross-repo / Doctor

Verify required claims/identity/independence for formal Evidence Audit; missing CI/check status is never PASS. Advisory inspection must not silently upgrade itself into a formal acceptance verdict. Cross-repository mutation retains per-repo authorization. Solution Design reversibility and Doctor observer-effect/cleanup rules remain material-only.

## 9. Control / host / status receipt

- Handoff/Profile/audit artifacts never become a fourth control source;
- final state-changing work runs affected-owner Control Alignment;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement may be `CONTROL_ONLY_DRIFT` when proven;
- live repository-host gates are reread for the literal identity;
- governed engineering/status/audit/CI/PR/merge responses emit one compact human status receipt;
- when a detailed Handoff Receipt is already present, the human receipt stays compact rather than duplicating the full transfer receipt.

## 10. Context recovery / progressive disclosure

If a current Profile exists, it may act as an optional landing index. Verify it does not become a mandatory extra read or replace AGENTS/STATUS/TASK needed for authority-sensitive decisions. Domain Navigation top-level loading should remain compact, with detailed current-task/history/refresh logic progressively disclosed through references.

## 11. Release surfaces

Exercise installed local Codex and ChatGPT Web Plugin where available. Do not patch reusable source inside installed caches; reusable defects return to source.

Claim integrated acceptance PASS only when all required tested-surface scenarios pass and required unknowns are resolved.

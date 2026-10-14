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

## 3. Project Profile / authority separation / compactness / grounding / durability / adherence

Verify Profile construction order:

```text
Grounding Gate
→ Durability Gate
→ Classification / authority placement
→ Compression / deduplication
→ Mandatory Pre-return Compliance Gate
→ Project Profile
```

The pre-return gate is corrective, not advisory. A draft with a known violation is revised before being returned.

### Grounding

- every substantive project-specific Profile claim is traceable to a current verified project authority appropriate to that claim, or to an explicit user instruction/reaffirmation in the current Profile task that establishes durable context;
- ChatGPT/model Memory, prior conversations, conversation summaries, previous assistant output, previous Profile/Project Instructions, old handoffs/audits/task cards/PR prose/status summaries do not independently establish Profile facts;
- historical/Memory context may suggest what to verify, but an unverified candidate is omitted or reported outside the Profile rather than promoted into durable-looking context;
- an existing Profile/Project Instructions surface is `DERIVED_PROJECT_CONTEXT`; rebuilding revalidates retained substantive claims instead of inheriting them;
- an explicit current-task user durable decision may be included as user-authorized context, but is not mislabeled as repository-established fact when not persisted there;
- materially distinct authority classes remain distinct: storage/persistence, Raw Evidence, derived projection, implementation authority, runtime evidence, and canonical fact/state authority are not flattened without project authority establishing that relationship;
- ordinary conversational Memory remains usable outside Profile construction; this acceptance does not require Memory to be disabled.

### Durability

- **verified != durable** is enforced: a currently true claim does not enter the Profile solely because it is grounded;
- current task/milestone/wave/gate/MVP phase, immediate delivery priority and next-step state are excluded from the durable Profile unless authority explicitly establishes durable/version-scoped architectural meaning;
- current-stage non-goals, deferrals and temporary sequencing choices are not silently promoted into permanent project anti-goals;
- a non-goal sourced only from language such as `current`, `current work`, `MVP`, `phase`, `wave`, `deferred`, `not yet`, or equivalent stage scope is rejected unless separate durable authority establishes the same lasting boundary;
- temporary development/acceptance machine names, ports, endpoints, branches, worktrees, runners, executables, local paths and process arrangements are excluded from durable `Environment` content;
- provisional/current implementation or acceptance shape is not promoted into long-lived project identity;
- durable/version-scoped architecture remains allowed when its authority explicitly establishes the scope, such as `V1 Local Store` or `long-term production Core`;
- version/durability qualifiers are preserved rather than erased by compression;
- useful current-stage facts are pointed to through STATUS/TASK/current delivery planning/runtime authority rather than copied into the Profile.

### Classification / compactness / surface

Verify Profile classification:

- normative project MUST/MUST-NOT -> `AGENTS.md`/accepted normative authority;
- current state -> STATUS;
- active authorization -> TASK;
- current delivery wave/milestone/runtime arrangement -> current planning/runtime authority;
- detailed Domain/source/test/runtime route -> navigation authority;
- repository directories/module paths/source files/symbols/code-responsibility maps -> implementation/navigation authority, not `Environment`;
- long-lived design -> planning authority;
- stable durable descriptive context + authority pointers -> Profile.

Also verify:

- read-only Profile draft/audit may run without granting mutation authority;
- repository/project-managed Profile mutation requires compatible PG/TASK authorization;
- stale Profile never overrides authority;
- Profile and Domain Map do not duplicate detailed ownership maps;
- one current Profile projection surface exists, or one primary plus clearly derived mirror;
- generated output preserves shipped fixed metadata field names `Profile surface` and `Primary/mirror role`;
- `MIRROR` is never emitted unless a specific primary Profile surface is verified/explicitly identified;
- `PRIMARY` is not invented merely from surface type;
- when only one current Profile surface is established and no competitor is verified, `single surface` is preferred; unresolved relationships remain `UNKNOWN`;
- output starts from the shipped Profile template;
- generic routing tables, Handoff Card/Receipt schemas, V0-V3 procedure, Doctor probe workflow, workspace/PR lifecycle, artifact-lifecycle mechanics and Control Alignment/`CONTROL_ONLY_DRIFT` procedure are omitted or collapsed to the shortest useful pointer;
- an existing Domain/navigation authority is pointed to rather than reproduced as a `Domain Model`, ownership table, canonical-source list, reduced mini-map, or ownership subcatalog;
- repository source/module responsibility lists are not placed in `Environment`;
- `Planning & navigation` contains durable pointers, not current delivery progress or a numbered startup/read/check workflow;
- `Environment` contains stable platform/environment roles, not temporary runtime/acceptance values or code navigation;
- generated Profile does not add Profile-maintenance/grounding/durability meta-procedure;
- detailed project-specific normative execution rules remain in owning authority;
- `Engineering Governance` uses the shipped compact hook and does not append per-Skill trigger prose or enumerate conditional Skills unless routing documentation was explicitly requested;
- project-specific durable facts/anti-goals/environment roles remain available even when procedure/current delivery detail is removed;
- the Profile is materially smaller than the combined authorities it indexes.

### Mandatory pre-return gate

Before returning a generated Profile, the installed environment must be able to satisfy:

```text
GROUNDED: YES
DURABILITY_QUALIFIED: YES
CORRECTLY_CLASSIFIED: YES
AUTHORITY_CLASSES_PRESERVED: YES
DOMAIN_AND_CODE_MAP_DEDUPED: YES
ENGINEERING_GOVERNANCE_HOOK_COMPACT: YES
TEMPLATE_FIELDS_PRESERVED: YES
```

A known `NO` is a generation failure and must be corrected in the same pass rather than explained after output.

### Overlong Profile negative case

Ask the installed environment to create a Project Profile for Engineering-Governance or another governance-heavy project.

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

### Established Domain Map negative case

Use a project with an established detailed Domain/navigation map.

Expected result:

```text
DOMAIN_AUTHORITY_POINTER: PRESENT
REDUCED_DOMAIN_MAP_RECREATED: NO
OWNERSHIP_SUBCATALOG_RECREATED: NO
CANONICAL_SOURCE_SYMBOL_LIST_RECREATED: NO
BROAD_ORIENTATION_CONCEPTS: ALLOWED_WHEN_NEEDED
RESULT: PASS
```

### Surface-role / fixed-field negative case

Use a target surface such as ChatGPT Project Instructions where no repository/user authority identifies another current primary Profile surface.

Expected result:

```text
PROFILE_SURFACE_FIELD: PRESENT
PRIMARY_MIRROR_ROLE_FIELD: PRESENT
FREEFORM_PROFILE_ROLE_REPLACEMENT: NO
MIRROR_WITHOUT_PRIMARY_EVIDENCE: NO
PRIMARY_WITHOUT_DESIGNATION: NO
ROLE: single surface OR UNKNOWN
RESULT: PASS
```

### Profile meta-procedure negative case

Generate a Project Profile from a repository whose authorities contain detailed startup, freshness, grounding, durability and classification procedure.

Expected result:

```text
NUMBERED_STARTUP_READ_SEQUENCE: NO
PROFILE_MAINTENANCE_SECTION: NO
PROFILE_CLASSIFICATION_RULES_COPIED: NO
GROUNDING_OR_DURABILITY_REPORT_SECTION: NO
DURABLE_POINTERS: PRESENT
RESULT: PASS
```

### Memory / conversation contamination negative case

Provide Memory or prior-chat context containing plausible stable project constraints that are **not** established by current repository authorities and are not explicitly reaffirmed as durable decisions in the current Profile task.

Expected result:

```text
MEMORY_USED_AS_PROFILE_AUTHORITY: NO
PRIOR_CHAT_USED_AS_PROFILE_AUTHORITY: NO
UNVERIFIED_MEMORY_DERIVED_CLAIMS_INCLUDED: NO
MEMORY_MAY_SUGGEST_VERIFICATION_TARGETS: YES
RESULT: PASS
```

### Previous Profile / Project Instructions inheritance negative case

Rebuild a Profile when existing Project Instructions/Profile contains substantive claims absent from current authorities.

Expected result:

```text
OLD_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT
OLD_PROFILE_CLAIMS_REVALIDATED: YES
UNVERIFIED_OLD_PROFILE_CLAIMS_INHERITED: NO
OLD_PROFILE_SELF_BOOTSTRAPS_TRUTH: NO
CURRENT_AUTHORITY_WINS: YES
RESULT: PASS
```

### Explicit current durable user decision positive case

During the current Profile task, the user explicitly establishes or reaffirms a durable project boundary that is not yet persisted in repository authority.

Expected result:

```text
CURRENT_USER_DECISION_RECOGNIZED: YES
MAY_APPEAR_AS_USER_AUTHORIZED_DURABLE_CONTEXT: YES
MISLABELED_AS_REPOSITORY_ESTABLISHED: NO
UNRELATED_PRIOR_MEMORY_IMPORTED: NO
RESULT: PASS
```

### Authority-class preservation case

Use a project whose current authorities distinguish durable storage/raw evidence, derived retrieval/projection, implementation/runtime evidence, and explicitly canonical state/facts.

Expected result:

```text
DISTINCT_AUTHORITY_CLASSES_PRESERVED: YES
STORAGE_PROMOTED_TO_UNIVERSAL_TRUTH: NO
PROJECTION_PROMOTED_TO_CANONICAL_AUTHORITY: NO
RUNTIME_EVIDENCE_PROMOTED_TO_DURABLE_SEMANTIC_AUTHORITY: NO
RESULT: PASS
```

### Gift-like durability/adherence case

Use a storefront project where current authority contains development-stage acceptance details and current-work non-goals while durable business authority defines Product/RFQ/storefront identity and a detailed Domain map exists.

Expected result:

```text
DEVELOPMENT_STAGE_MACHINE_IN_PROFILE_ENVIRONMENT: NO
TEMP_ACCEPTANCE_PORT_OR_ENDPOINT_IN_PROFILE: NO
CURRENT_STAGE_NON_GOAL_PROMOTED_TO_PERMANENT_ANTI_GOAL: NO
STOREFRONT_CMS_STAGE_ONLY_NON_GOAL_IN_DURABLE_PROFILE: NO
REDUCED_DOMAIN_OWNERSHIP_CATALOG: NO
DURABLE_PRODUCT_IDENTITY_RETAINED: YES
DURABLE_RFQ_IDENTITY_RETAINED: YES
RESULT: PASS
```

### MemoX-like durability negative/positive case

Use a project where current authority contains a current delivery overlay plus accepted version-scoped/durable architecture and distinct authority classes.

Expected result:

```text
CURRENT_MVP_WAVE_PROMOTED_TO_PROJECT_IDENTITY: NO
CURRENT_VIEWER_OR_ACCEPTANCE_SHAPE_PROMOTED_TO_DURABLE_ENVIRONMENT: NO
V1_STORAGE_CHOICE_RETAINED_WITH_SCOPE: YES
LONG_TERM_CORE_CHOICE_RETAINED_WITH_SCOPE: YES
AUTHORITY_CLASSES_PRESERVED: YES
RESULT: PASS
```

### Merloom-like code-map / routing-hook adherence case

Use a project with durable architecture/business authorities, a detailed Domain/navigation surface, stable greenfield/authority rules, and repository directories that map implementation responsibilities.

Expected result:

```text
DURABLE_GREENFIELD_IDENTITY_RETAINED: YES
DURABLE_SINGLE_AUTHORITY_BOUNDARY_RETAINED: YES
DURABLE_SAVE_PUBLISH_BOUNDARY_RETAINED: YES
SOURCE_DIRECTORY_RESPONSIBILITY_MAP_IN_ENVIRONMENT: NO
CODE_PATH_CATALOG_IN_PROFILE: NO
DOMAIN_NAVIGATION_POINTER: PRESENT
PER_SKILL_TRIGGER_PROSE_IN_ENGINEERING_GOVERNANCE: NO
ENGINEERING_GOVERNANCE_HOOK_MATCHES_COMPACT_TEMPLATE: YES
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

- `IMPLEMENTATION_AUTHORITY` is distinct from `OBSERVED_EVIDENCE`;
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

If a current Profile exists, it may act as an optional landing index. Verify it does not become a mandatory extra read or replace AGENTS/STATUS/TASK needed for authority-sensitive decisions. Existing Profile content remains derived context and must not bootstrap its own truth during rebuild. Current delivery/runtime detail remains in its owning authority rather than being imported merely for context recovery. Domain Navigation top-level loading should remain compact, with detailed current-task/history/refresh logic progressively disclosed through references.

## 11. Release surfaces

Exercise installed local Codex and ChatGPT Web Plugin where available. Do not patch reusable source inside installed caches; reusable defects return to source.

Claim integrated acceptance PASS only when all required tested-surface scenarios pass and required unknowns are resolved.

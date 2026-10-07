# Engineering-Governance Skill Repository Redesign

Date: 2026-10-07
Status: Proposed written design — awaiting user review
Task: `EG-SKILLS-RESTRUCTURE-DESIGN-007`
Design-start baseline: `d13e6895f6d4bddb753cabcc87566613eaa9bbec`

## 1. Purpose

Engineering-Governance will be reset into a source repository for reusable AI engineering-governance Skills, templates, operating rules, and governance context.

It is intentionally **not**:

- a business-product repository;
- a generic governance runtime;
- an installer or Bootstrap CLI;
- a background governance service;
- a central database or enforcement plane;
- a repository whose whole tree is copied mechanically into target projects.

A capable AI agent should read this repository, inspect the target repository, then adapt the applicable templates and rules to that project's verified reality.

## 2. Problem this redesign solves

The previous repository evolved toward a Python Doctor runtime and planned Bootstrap tooling. That direction is now misaligned with the intended use. The desired value is lighter: encode reliable ways for AI agents to establish project controls, navigate a codebase, respond to real incidents only when needed, and scale verification effort to risk.

The redesign therefore moves the repository from **governance product/tooling** to **governance Skill source**.

## 3. Fixed v1 principles

### 3.1 Three-file project control plane

Every governed project should have three distinct project-local controls:

- `AGENTS.md` — durable project operating rules and agent guidance;
- `CURRENT_STATUS.md` — concise verified current-state snapshot, not a history log;
- `CURRENT_TASK.md` — one active execution contract defining the work authorized now.

The Skill templates define required semantics and section responsibilities. The adopting AI fills them from the target project's actual structure and evidence.

### 3.2 Domain navigation is mandatory

Each target project needs a semantic navigation layer. A Domain Map exists to answer:

- what capabilities/domains exist;
- what each domain owns and does not own;
- where the primary code entry points and important symbols are;
- where state/authority lives;
- which domains depend on or consume one another;
- which tests and runtime paths are relevant;
- which invariants and known unknowns matter;
- what source paths support the map.

A Domain is not defined merely by directory boundaries. Capability, ownership, state, and authority are the primary grouping concepts.

### 3.3 Business-first; Doctor is reactive

Normal product/business development is the default flow.

Doctor is entered only when:

1. a real failure, unexplained behavior, or unsafe ambiguity appears;
2. existing evidence is insufficient to answer the blocked question safely.

The response is to add the **minimum** probe/evidence needed, capture a fresh incident where applicable, test hypotheses, make the minimum fix, verify it, then retire or explicitly promote the probe. Diagnostic infrastructure is not developed in parallel by default.

### 3.4 Verification is proportional

Verification depth follows the change's risk and radius:

- `V0` — documentation/control/layout;
- `V1` — localized behavior;
- `V2` — domain-level behavior;
- `V3` — cross-domain/high-risk/release behavior.

The active task states which level applies and why. The existence of a large historical suite is not sufficient reason to run it for unrelated low-risk changes.

## 4. Target repository structure

The intended v1 live tree after the skeleton reset is:

```text
Engineering-Governance/
├── README.md
├── AGENTS.md
├── CURRENT_STATUS.md
├── CURRENT_TASK.md
│
├── skills/
│   ├── project-governance/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── control-plane.md
│   │   │   ├── development-flow.md
│   │   │   └── verification-tiers.md
│   │   └── assets/
│   │       └── templates/
│   │           ├── AGENTS.md
│   │           ├── CURRENT_STATUS.md
│   │           └── CURRENT_TASK.md
│   │
│   ├── domain-navigation/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── domain-model.md
│   │   │   ├── mapping-workflow.md
│   │   │   ├── evidence-rules.md
│   │   │   ├── refresh-policy.md
│   │   │   └── repo-map.md
│   │   ├── assets/
│   │   │   └── templates/
│   │   │       ├── DOMAIN_MAP.md
│   │   │       └── DOMAIN.md
│   │   └── scripts/
│   │       └── README.md
│   │
│   └── incident-doctor/
│       ├── SKILL.md
│       ├── references/
│       │   ├── evidence-gate.md
│       │   ├── probe-design.md
│       │   ├── fresh-incident.md
│       │   └── probe-lifecycle.md
│       └── assets/
│           └── templates/
│               └── INCIDENT.md
│
├── references/
│   ├── UPSTREAMS.md
│   └── LICENSE_NOTES.md
│
├── examples/
│   └── README.md
│
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

`docs/superpowers/` is maintainer-only planning history for this repository and is not part of the reusable Skill payload.

The `domain-navigation/scripts/README.md` file exists only to state that v1 has no required executable navigation dependency and that future scripts must remain optional/read-only. It is not a placeholder for an installer.

## 5. Skill module boundaries

## 5.1 `project-governance`

**Trigger:** establishing or repairing the normal governance/control structure of a project, or starting a normal governed development task.

**Owns:**

- three-file control-plane role definitions;
- task start/scope-change flow;
- business-first delivery rule;
- verification-tier selection;
- minimal stop conditions and handoff expectations;
- templates for the three root controls.

**Does not own:**

- repository architecture discovery beyond routing to Domain Navigation;
- incident probes or root-cause investigation;
- product/domain truth for the target project;
- installers or automatic project mutation.

## 5.2 `domain-navigation`

**Trigger:** mapping/onboarding into a codebase, refreshing a stale Domain Map, or locating the correct code/authority for a task when the existing map is insufficient.

**Owns:**

- semantic Domain Map schema;
- evidence-first mapping workflow;
- stable domain-to-code navigation;
- refresh/staleness policy;
- the distinction between Domain Map and dynamic Repo Map;
- optional future read-only code-ranking helpers.

**Does not own:**

- normal task authorization;
- incident diagnosis;
- automatic code edits;
- a mandatory index database or daemon.

### Domain Map vs Repo Map

`DOMAIN_MAP.md` is the stable, human/agent-readable semantic navigation layer: capabilities, boundaries, owners, authority, entry points, dependencies, tests, invariants, and evidence.

A Repo Map is a dynamic code-level aid for selecting relevant files/symbols under limited context. It may use syntax/dependency information and ranking. It accelerates reading but cannot become the canonical semantic authority.

Expected routing:

```text
CURRENT_TASK
  -> affected domain(s)
  -> DOMAIN_MAP
  -> candidate entry points / symbols / tests
  -> optional Repo Map or targeted search
  -> focused source reading
```

## 5.3 `incident-doctor`

**Trigger:** a real failure/unexplained behavior blocks safe progress and current evidence is insufficient.

**Owns:**

- problem classification;
- evidence sufficiency gate;
- existing-evidence review;
- minimum probe design;
- fresh-incident capture guidance;
- hypothesis/falsification discipline;
- minimum-fix boundary;
- regression verification guidance;
- probe retirement/promotion lifecycle;
- incident record template.

**Does not own:**

- routine feature development;
- speculative observability expansion;
- permanent instrumentation by default;
- automatic remediation or enforcement.

## 6. Template semantics

### 6.1 `AGENTS.md` template

Must teach the adopting AI where project truth comes from and how to work safely. Expected sections include:

- project purpose and durable boundaries;
- authoritative entry points and important project-specific references;
- Domain Map location;
- normal development flow;
- business-first / Doctor-on-demand rule;
- verification-tier policy;
- Git/branch/worktree expectations only where the project actually needs them;
- stop conditions;
- commands that are genuinely project-specific.

It must not become a dump of current task state.

### 6.2 `CURRENT_STATUS.md` template

Must answer: **what is verified true about the project now?**

Expected fields:

- accepted baseline;
- current business/product milestone;
- accepted capabilities;
- active known problems/blockers;
- active development state;
- next intended milestone;
- last verification/freshness basis where relevant.

It must not become a chronological journal.

### 6.3 `CURRENT_TASK.md` template

Must answer: **what work is authorized now?**

Expected fields:

- Task ID;
- State / mode;
- objective;
- affected domain(s);
- start baseline;
- in scope;
- out of scope;
- known evidence;
- risk level and rationale;
- verification level and rationale;
- acceptance criteria;
- stop conditions;
- handoff/current stop point.

### 6.4 `DOMAIN_MAP.md` template

A concise index of project domains. For each domain it should identify responsibility, owner/authority, major entry points, key dependencies/consumers, relevant tests, and a link to a detailed `DOMAIN.md` only when the project is large enough to justify one.

### 6.5 `DOMAIN.md` template

Expected fields:

- domain name and responsibility;
- owns / explicitly does not own;
- state and authority owner;
- primary entry points and important symbols;
- upstream dependencies / downstream consumers;
- primary data/control flow;
- relevant tests;
- runtime/operational entry points;
- invariants;
- evidence/source paths;
- known unknowns.

## 7. Upstream reference model

The repository should record, not hide, the public work that informs the design.

### Agent Skills / Anthropic skill creator

Reference concepts:

- one `SKILL.md` per capability;
- optional `references/`, `assets/`, and `scripts/`;
- progressive disclosure so detailed material is loaded only when needed;
- Skill description should be specific enough to control triggering.

Reference: `anthropics/skills`, `skills/skill-creator/SKILL.md`.

### AGENTS.md open format

Reference concept:

- predictable repository-level agent instructions separated from human-facing README content.

Reference: `agentsmd/agents.md` and `https://agents.md/`.

### GitHub `acquire-codebase-knowledge`

Reference concepts:

- inspect repository intent documents before inventing architecture explanations;
- only document what can be verified from files or terminal/repository evidence;
- keep unknowns explicit rather than filling gaps by inference;
- attach concrete source-path evidence to non-trivial claims.

Reference: `github/awesome-copilot/skills/acquire-codebase-knowledge`.

The v1 Domain Navigation Skill compresses those ideas into a smaller Domain Map instead of requiring seven permanent codebase documents.

### Aider Repo Map

Reference concepts:

- large codebases need context selection rather than wholesale loading;
- definitions/references and dependency structure can rank relevant code;
- only the highest-value portions should be emitted under a context/token budget;
- the map helps the model decide which specific files to read next.

Reference: `Aider-AI/aider`, `aider/website/docs/repomap.md`.

Aider is a design reference, not a v1 runtime dependency.

## 8. Legacy live-tree retirement

The first implementation slice should remove obsolete active files rather than move them into an archive directory.

Expected retirement candidates include:

- `src/engineering_governance/`;
- `tests/` associated with the retired runtime;
- `docs/governance/v0.1/`;
- `docs/reality-checks/`;
- `docs/reference-audit/`;
- the old Doctor/Bootstrap implementation plans/specs that are no longer current, except the new redesign spec/plan needed for maintainer traceability.

The exact delete list must be produced from the live tree at execution time, not guessed from this document.

Historical preservation is provided by Git history and the existing stable tag. The tag must not be moved.

## 9. Phased implementation

### Phase A — repository skeleton reset

Purpose: make the live tree match the new repository identity before writing deep Skill content.

Actions:

- replace README with the new repository purpose and usage model;
- remove retired runtime/research trees from the live branch;
- create the complete directory/file skeleton above;
- create minimal valid `SKILL.md` files with correct names, trigger boundaries, and links to their future references/assets;
- create minimal template/reference files with clear section contracts, not speculative long-form content;
- create `UPSTREAMS.md` and `LICENSE_NOTES.md`;
- create `examples/README.md` stating that examples are added only after real-project validation;
- do not add executable product code.

Verification: `V0` only — tree, frontmatter, links/path references, absence of retired runtime, Git cleanliness, remote head match.

Independent Web review is required before Phase B.

### Phase B — enrich `project-governance`

Complete the three control templates and references for:

- role separation;
- task start/scope change;
- business-first flow;
- risk classification;
- verification-tier selection;
- stop/handoff rules.

Validate against one real project without altering unrelated product behavior.

### Phase C — enrich `domain-navigation`

Complete:

- Domain schema;
- mapping workflow;
- evidence rules;
- refresh/staleness policy;
- Domain Map and Domain templates.

Test manually on a real project: a fresh AI should be able to route from a task to the correct domain and narrow the source-reading set faster than broad repository scanning.

### Phase D — optional read-only Repo Map proof

Only after Phase C shows a concrete navigation gap, evaluate a minimal read-only Repo Map helper inspired by Aider. This is not mandatory for v1.

A script may be introduced only if it measurably improves code navigation and does not require a daemon, central index, or automatic mutation.

### Phase E — enrich `incident-doctor`

Define the evidence gate, minimum probe workflow, fresh-incident process, hypothesis/falsification discipline, and probe lifecycle.

Validate it only against a real incident/problem scenario. A normal feature task should not trigger this Skill.

### Phase F — adoption validation

Use a separate real project as the acceptance target.

A fresh AI should be able to:

1. read Engineering-Governance;
2. inspect the target project;
3. generate/adapt the three root controls;
4. create an evidence-backed Domain Map;
5. select a real business task;
6. use Domain Navigation to find the right code;
7. choose an appropriate verification tier;
8. complete normal work without invoking Doctor when no incident exists;
9. invoke Doctor only when a genuine evidence gap appears.

Passing this flow is the v1 success criterion.

## 10. Phase A acceptance criteria

Phase A is accepted only when:

- the live tree has the full target skeleton;
- the previous Python governance runtime and its tests are absent from the live tree;
- README clearly states Skill-source, AI-adapted, no-installer behavior;
- exactly the three intended top-level Skill modules exist;
- each Skill has valid `SKILL.md` frontmatter with a distinct trigger/boundary;
- the three control templates, Domain templates, and Incident template exist;
- all planned reference filenames exist and their purpose is explicit;
- `UPSTREAMS.md` identifies the main public references and what is borrowed conceptually;
- `LICENSE_NOTES.md` states whether code/text was copied; Phase A should report none unless separately justified;
- `examples/README.md` prevents hypothetical examples from being represented as validated;
- no installer, Bootstrap CLI, daemon, service, database, enforcement engine, or automatic remediation is introduced;
- no new executable product/runtime code is added;
- the historical `v0.1.0` tag remains unchanged;
- the worktree and remote task branch are clean/matched at handoff.

## 11. Non-goals for v1

- installer or one-click adoption;
- project mutation without AI review;
- central template registry service;
- continuous background compliance scanning;
- automatic repair/remediation;
- MCP service as a prerequisite;
- database-backed governance state;
- mandatory semantic index service;
- permanently maintaining the old Doctor CLI;
- copying whole upstream projects or forking immature Repo Map Skills as a core dependency.

## 12. Key design decision

The most important structural distinction is:

```text
Project Governance = how normal work is governed
Domain Navigation  = how an AI understands and finds the right code/authority
Incident Doctor    = what happens only when normal work encounters an evidence-deficient problem
```

And within Domain Navigation:

```text
Domain Map = stable semantic navigation / ownership map
Repo Map   = optional dynamic code-context selection aid
```

Keeping these boundaries explicit is what prevents the repository from turning back into a heavy governance platform.

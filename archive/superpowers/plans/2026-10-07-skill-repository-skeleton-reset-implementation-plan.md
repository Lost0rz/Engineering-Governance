# Skill Repository Skeleton Reset Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reset the live `Engineering-Governance` tree from the retired governance-runtime/tooling direction into the approved three-Skill source-repository skeleton, without implementing deep Skill behavior yet.

**Architecture:** Phase A is a documentation/layout migration only. Git history and the existing `v0.1.0` tag preserve the retired runtime; the live branch removes obsolete runtime/research files and establishes exactly three Skill modules with minimal valid entrypoints, explicit reference/template contracts, and no executable product code. Deeper content is deferred to separate plans for `project-governance`, `domain-navigation`, and `incident-doctor`.

**Tech Stack:** Markdown, Git, POSIX shell, and read-only Python 3 standard-library one-liners only when useful for verification. No new package/runtime dependency.

**Spec:** `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`

## Global Constraints

- Repository identity: reusable AI engineering-governance Skill/template/rule/context source; not a governance runtime/product and not an installer.
- Preserve root controls `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`; do not repurpose them as reusable templates.
- Target reusable modules are exactly `skills/project-governance/`, `skills/domain-navigation/`, and `skills/incident-doctor/`.
- `DOMAIN_MAP.md` is the stable semantic navigation layer; any future Repo Map is only a dynamic read-only code-navigation aid.
- Doctor remains reactive: normal product/business delivery is the default; no speculative diagnostics platform is introduced.
- Verification for this slice is `V0` only: tree/layout, frontmatter, link/path references, retired-runtime absence, Git cleanliness, remote-head match, and stable-tag immutability.
- Do not add an installer, Bootstrap CLI, daemon, service, database, enforcement engine, automatic remediation, MCP prerequisite, or new executable runtime code.
- Do not copy upstream source code or long-form upstream text. Phase A borrows concepts only and records attribution in `references/UPSTREAMS.md` and `references/LICENSE_NOTES.md`.
- The stable tag must continue to resolve to commit `738627a0caad330d277f60cfdaff5f153593135e`.
- Before any edit, execution must start from the exact implementation baseline authorized later in `CURRENT_TASK.md`; unexpected remote/control drift is a STOP.

## File Structure Locked by This Plan

Create and retain the following live structure:

```text
README.md
AGENTS.md
CURRENT_STATUS.md
CURRENT_TASK.md
skills/
  project-governance/
    SKILL.md
    references/
      control-plane.md
      development-flow.md
      verification-tiers.md
    assets/templates/
      AGENTS.md
      CURRENT_STATUS.md
      CURRENT_TASK.md
  domain-navigation/
    SKILL.md
    references/
      domain-model.md
      mapping-workflow.md
      evidence-rules.md
      refresh-policy.md
      repo-map.md
    assets/templates/
      DOMAIN_MAP.md
      DOMAIN.md
    scripts/
      README.md
  incident-doctor/
    SKILL.md
    references/
      evidence-gate.md
      probe-design.md
      fresh-incident.md
      probe-lifecycle.md
    assets/templates/
      INCIDENT.md
references/
  UPSTREAMS.md
  LICENSE_NOTES.md
examples/
  README.md
docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md
docs/superpowers/plans/2026-10-07-skill-repository-skeleton-reset-implementation-plan.md
```

Retire from the live tree:

```text
src/engineering_governance/**
tests/**
docs/governance/**
docs/reality-checks/**
docs/reference-audit/**
docs/superpowers/plans/2026-10-07-bootstrap-minimal-control-plane-implementation-plan.md
docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md
docs/superpowers/specs/2026-10-07-tooling-foundation-design.md
```

At execution time, use `git ls-files` to enumerate the exact tracked files under retired roots before deletion. If an unexpected tracked path exists outside the categories above, STOP rather than broadening deletion by guesswork.

## Review Focus

1. **Historical preservation:** deleting live runtime files must not move or recreate `v0.1.0`; verify the tag still dereferences to `738627a0caad330d277f60cfdaff5f153593135e`.
2. **Runtime residue:** no `.py`, runtime test tree, Bootstrap/Doctor executable surface, or dependency manifest may remain or be newly introduced as part of Phase A unless it is maintainer-only read-only verification outside the committed tree.
3. **Skill-trigger ambiguity:** the three `SKILL.md` descriptions must have distinct triggers so routine work does not invoke Doctor and navigation does not claim task authorization.
4. **Broken navigation:** every path named by a `SKILL.md` must exist after the skeleton reset; no entrypoint may point to a retired document.
5. **Accidental upstream copying:** `LICENSE_NOTES.md` must state that Phase A copied no upstream code/text beyond names/short concepts, and `UPSTREAMS.md` must identify sources conceptually rather than vendoring them.

---

### Task 1: Retire the old live product identity and establish repository-level source metadata

**Files:**
- Modify: `README.md`
- Create: `references/UPSTREAMS.md`
- Create: `references/LICENSE_NOTES.md`
- Create: `examples/README.md`
- Delete: `src/engineering_governance/**`
- Delete: `tests/**`
- Delete: `docs/governance/**`
- Delete: `docs/reality-checks/**`
- Delete: `docs/reference-audit/**`
- Delete: `docs/superpowers/plans/2026-10-07-bootstrap-minimal-control-plane-implementation-plan.md`
- Delete: `docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md`
- Delete: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`

**Interfaces:**
- Consumes: accepted redesign spec and Git history.
- Produces: a live repository whose top-level identity is Skill-source-only, plus attribution/licensing metadata used by all later modules.

- [ ] **Step 1: Capture the exact retirement manifest before deleting anything**

Run:

```bash
git ls-files src tests docs/governance docs/reality-checks docs/reference-audit \
  docs/superpowers/plans/2026-10-07-bootstrap-minimal-control-plane-implementation-plan.md \
  docs/superpowers/plans/2026-10-07-doctor-foundation-implementation-plan.md \
  docs/superpowers/specs/2026-10-07-tooling-foundation-design.md
```

Expected: only files belonging to the retired runtime/research/tooling direction. If unrelated or newly added files appear, STOP and report them.

- [ ] **Step 2: Run the pre-change identity checks and prove they currently fail the new-state contract**

Run:

```bash
test -d src/engineering_governance
test -d tests
grep -q 'governance system' README.md
```

Expected: all three succeed, proving the old live identity/runtime still exists before the reset.

- [ ] **Step 3: Rewrite `README.md` around the approved usage model**

Required sections: repository purpose; what this repository is not; the three Skill modules; AI-adapted adoption flow; four fixed principles (three control files, Domain navigation, reactive Doctor, proportional verification); contributor/maintainer note pointing to `docs/superpowers/` as repository-maintainer history only.

Do not document any install command or runtime CLI.

- [ ] **Step 4: Create repository-level reference metadata**

`references/UPSTREAMS.md` must name and summarize the conceptual influence of:

- Agent Skills / Anthropic skill structure and progressive disclosure;
- AGENTS.md open format;
- GitHub `awesome-copilot` `acquire-codebase-knowledge` evidence-first discovery;
- Aider Repo Map context-selection/ranking concepts.

`references/LICENSE_NOTES.md` must say Phase A copies no upstream source code or long-form text and that any future copying requires explicit license review.

`examples/README.md` must say examples are added only after validation against a real target project and must identify their validation context.

- [ ] **Step 5: Remove the retired live-tree files from the manifest captured in Step 1**

Delete only the enumerated tracked files/roots and the three explicitly retired `docs/superpowers/` artifacts. Do not move them into an archive directory; Git history and the stable tag are the archive.

- [ ] **Step 6: Verify the Task 1 state**

Run:

```bash
test ! -e src/engineering_governance
test ! -e tests
test ! -e docs/governance
test ! -e docs/reality-checks
test ! -e docs/reference-audit
test -f references/UPSTREAMS.md
test -f references/LICENSE_NOTES.md
test -f examples/README.md
! grep -Eq 'bootstrap (preview|apply)|engineering_governance doctor|pip install|installer' README.md
[ "$(git rev-parse 'v0.1.0^{}')" = "738627a0caad330d277f60cfdaff5f153593135e" ]
```

Expected: all commands exit 0.

- [ ] **Step 7: Commit Task 1**

```bash
git add -A
git commit -m "refactor: reset repository to Skill source"
```

### Task 2: Add the `project-governance` Skill skeleton and three control templates

**Files:**
- Create: `skills/project-governance/SKILL.md`
- Create: `skills/project-governance/references/control-plane.md`
- Create: `skills/project-governance/references/development-flow.md`
- Create: `skills/project-governance/references/verification-tiers.md`
- Create: `skills/project-governance/assets/templates/AGENTS.md`
- Create: `skills/project-governance/assets/templates/CURRENT_STATUS.md`
- Create: `skills/project-governance/assets/templates/CURRENT_TASK.md`

**Interfaces:**
- Consumes: repository identity and reference metadata from Task 1.
- Produces: the normal-development Skill entrypoint and stable schema contracts that later enrichment will deepen without changing file ownership.

- [ ] **Step 1: Run the pre-change absence check**

```bash
test ! -e skills/project-governance/SKILL.md
```

Expected: exit 0.

- [ ] **Step 2: Create minimal valid `SKILL.md` frontmatter and boundary text**

Frontmatter must contain exactly this stable identity:

```yaml
---
name: project-governance
description: Establish or repair a project's normal AI development governance, including the three-file control plane, business-first task flow, and risk-proportional verification. Use for normal governed development; do not use for repository architecture discovery beyond routing to Domain Navigation or for incident diagnosis.
---
```

The body must link to the three references and three templates, state that templates are adapted from verified project facts rather than blindly copied, and route codebase discovery to `domain-navigation` and evidence-insufficient incidents to `incident-doctor`.

- [ ] **Step 3: Create the three reference contract files**

`control-plane.md`: roles and anti-overlap rules for `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`.

`development-flow.md`: task start, scope change, business-first delivery, and minimal STOP/handoff contract.

`verification-tiers.md`: define `V0` documentation/control/layout, `V1` localized behavior, `V2` domain-level behavior, `V3` cross-domain/high-risk/release behavior; require rationale in `CURRENT_TASK.md`.

Phase A content must be concise contracts, not a complete handbook.

- [ ] **Step 4: Create the three template contracts**

`AGENTS.md` template sections: purpose/boundaries; project truth and authoritative entry points; Domain Map location; normal development flow; Doctor-on-demand rule; verification policy; project-specific Git/runtime commands only when actually needed; STOP conditions.

`CURRENT_STATUS.md` template sections: accepted baseline; current business/product milestone; accepted capabilities; active known problems/blockers; active development state; next intended milestone; freshness/verification basis.

`CURRENT_TASK.md` template sections: Task ID; State/Mode; Objective; Affected Domains; Start Baseline; In Scope; Out of Scope; Known Evidence; Risk + rationale; Verification Level + rationale; Acceptance Criteria; Stop Conditions; Handoff/Current Stop Point.

Use placeholder markers that instruct the adopting AI to derive values from the target repository; do not invent sample project facts.

- [ ] **Step 5: Verify Task 2**

```bash
test -f skills/project-governance/SKILL.md
for f in control-plane development-flow verification-tiers; do test -f "skills/project-governance/references/$f.md"; done
for f in AGENTS CURRENT_STATUS CURRENT_TASK; do test -f "skills/project-governance/assets/templates/$f.md"; done
grep -q '^name: project-governance$' skills/project-governance/SKILL.md
grep -q 'domain-navigation' skills/project-governance/SKILL.md
grep -q 'incident-doctor' skills/project-governance/SKILL.md
```

Expected: all commands exit 0.

- [ ] **Step 6: Commit Task 2**

```bash
git add skills/project-governance
git commit -m "feat: add project governance Skill skeleton"
```

### Task 3: Add the `domain-navigation` Skill skeleton and Domain Map contracts

**Files:**
- Create: `skills/domain-navigation/SKILL.md`
- Create: `skills/domain-navigation/references/domain-model.md`
- Create: `skills/domain-navigation/references/mapping-workflow.md`
- Create: `skills/domain-navigation/references/evidence-rules.md`
- Create: `skills/domain-navigation/references/refresh-policy.md`
- Create: `skills/domain-navigation/references/repo-map.md`
- Create: `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`
- Create: `skills/domain-navigation/assets/templates/DOMAIN.md`
- Create: `skills/domain-navigation/scripts/README.md`

**Interfaces:**
- Consumes: repository identity from Task 1 and routing from `project-governance`.
- Produces: the stable semantic codebase-navigation contract and the explicit Domain Map / Repo Map separation used by later enrichment.

- [ ] **Step 1: Run the pre-change absence check**

```bash
test ! -e skills/domain-navigation/SKILL.md
```

Expected: exit 0.

- [ ] **Step 2: Create minimal valid `SKILL.md` frontmatter and routing boundary**

Frontmatter must contain:

```yaml
---
name: domain-navigation
description: Build or refresh an evidence-backed semantic Domain Map and use it to route an AI from a task to the correct capability, authority, entry points, symbols, tests, and focused source-reading set. Use for codebase onboarding/navigation when the existing map is absent or stale; do not use to authorize tasks, diagnose incidents, or mutate product code.
---
```

The body must link to all five references, both templates, and `scripts/README.md`.

- [ ] **Step 3: Create the five reference contract files**

`domain-model.md`: domains are grouped by capability/ownership/state/authority, not directory shape alone.

`mapping-workflow.md`: `CURRENT_TASK -> affected domains -> DOMAIN_MAP -> candidate entry points/symbols/tests -> optional targeted search/Repo Map -> focused source reading`.

`evidence-rules.md`: inspect intent docs and code; support non-trivial claims with concrete paths/symbols; unknown remains unknown; derived maps are not product truth authorities.

`refresh-policy.md`: refresh only when the map is absent, stale for the affected area, or contradicted by verified repository facts; avoid whole-repository remapping for unrelated changes.

`repo-map.md`: Repo Map is optional/dynamic/read-only context selection; it may rank files/symbols/dependencies but cannot replace `DOMAIN_MAP.md` or become semantic authority.

- [ ] **Step 4: Create Domain templates and script boundary**

`DOMAIN_MAP.md` template: project-level domain index with responsibility, owner/authority, entry points, dependencies/consumers, relevant tests, evidence paths, and optional links to detailed domain files only when justified.

`DOMAIN.md` template: Domain Name/Responsibility; Owns; Does Not Own; State/Authority Owner; Primary Entry Points/Important Symbols; Upstream Dependencies; Downstream Consumers; Main Data/Control Flow; Relevant Tests; Runtime/Operational Entry Points; Invariants; Evidence/Source Paths; Known Unknowns.

`scripts/README.md`: v1 requires no executable navigation helper; future scripts must be optional and read-only, justified by a measured navigation gap, and must not require a daemon/central index/automatic mutation.

- [ ] **Step 5: Verify Task 3**

```bash
test -f skills/domain-navigation/SKILL.md
for f in domain-model mapping-workflow evidence-rules refresh-policy repo-map; do test -f "skills/domain-navigation/references/$f.md"; done
for f in DOMAIN_MAP DOMAIN; do test -f "skills/domain-navigation/assets/templates/$f.md"; done
test -f skills/domain-navigation/scripts/README.md
grep -q '^name: domain-navigation$' skills/domain-navigation/SKILL.md
grep -q 'Repo Map' skills/domain-navigation/references/repo-map.md
grep -q 'Known Unknowns' skills/domain-navigation/assets/templates/DOMAIN.md
find skills/domain-navigation/scripts -type f ! -name README.md -print -quit | grep -q . && exit 1 || true
```

Expected: all commands exit 0; scripts directory contains no executable helper.

- [ ] **Step 6: Commit Task 3**

```bash
git add skills/domain-navigation
git commit -m "feat: add domain navigation Skill skeleton"
```

### Task 4: Add the `incident-doctor` Skill skeleton and incident contract

**Files:**
- Create: `skills/incident-doctor/SKILL.md`
- Create: `skills/incident-doctor/references/evidence-gate.md`
- Create: `skills/incident-doctor/references/probe-design.md`
- Create: `skills/incident-doctor/references/fresh-incident.md`
- Create: `skills/incident-doctor/references/probe-lifecycle.md`
- Create: `skills/incident-doctor/assets/templates/INCIDENT.md`

**Interfaces:**
- Consumes: task context from `project-governance` and domain routing from `domain-navigation`.
- Produces: a reactive incident workflow contract that later enrichment can deepen without normal feature work depending on it.

- [ ] **Step 1: Run the pre-change absence check**

```bash
test ! -e skills/incident-doctor/SKILL.md
```

Expected: exit 0.

- [ ] **Step 2: Create minimal valid `SKILL.md` frontmatter with a strict reactive trigger**

Frontmatter must contain:

```yaml
---
name: incident-doctor
description: Investigate a real failure, unexplained behavior, or unsafe ambiguity only when current evidence is insufficient for safe progress. Use to assess evidence sufficiency, add the minimum missing probe, capture a fresh incident, falsify hypotheses, bound the minimum fix, and retire or explicitly promote probes; do not use for routine feature development or speculative observability expansion.
---
```

The body must link to the four references and incident template and must explicitly say that sufficient existing evidence bypasses new probe work.

- [ ] **Step 3: Create the four reference contract files**

`evidence-gate.md`: classify the blocked question and decide whether existing evidence is sufficient before adding instrumentation.

`probe-design.md`: add only evidence that can distinguish current hypotheses or close the specific evidence gap; avoid behavior changes disguised as diagnostics.

`fresh-incident.md`: identify runtime/build/config/context, capture the reproduction window, preserve timestamps/identities, and distinguish observed facts from user report and inference.

`probe-lifecycle.md`: temporary probe is removed after use unless repeated evidence justifies explicit promotion to durable diagnostics.

- [ ] **Step 4: Create `INCIDENT.md` template**

Required sections: Incident ID; blocked question; user-observed symptom; verified runtime/context; existing evidence; evidence gap; hypotheses; minimum probe (if needed); fresh reproduction/capture; findings with source evidence; minimum fix boundary; verification; probe retirement/promotion decision; unresolved unknowns.

- [ ] **Step 5: Verify Task 4**

```bash
test -f skills/incident-doctor/SKILL.md
for f in evidence-gate probe-design fresh-incident probe-lifecycle; do test -f "skills/incident-doctor/references/$f.md"; done
test -f skills/incident-doctor/assets/templates/INCIDENT.md
grep -q '^name: incident-doctor$' skills/incident-doctor/SKILL.md
grep -qi 'minimum' skills/incident-doctor/references/probe-design.md
grep -qi 'retire' skills/incident-doctor/references/probe-lifecycle.md
```

Expected: all commands exit 0.

- [ ] **Step 6: Commit Task 4**

```bash
git add skills/incident-doctor
git commit -m "feat: add incident doctor Skill skeleton"
```

### Task 5: Perform whole-slice V0 verification and prepare independent Web audit handoff

**Files:**
- Modify: `CURRENT_TASK.md` on the authorized task branch only to record executor evidence and set the handoff state.
- Do not modify reusable Skill content after verification except to correct a failing Phase A acceptance check.

**Interfaces:**
- Consumes: Tasks 1-4.
- Produces: one clean remote task branch ready for independent Web audit; no merge authorization.

- [ ] **Step 1: Verify exactly three top-level Skill modules**

```bash
find skills -mindepth 1 -maxdepth 1 -type d -print | sort
```

Expected exactly:

```text
skills/domain-navigation
skills/incident-doctor
skills/project-governance
```

- [ ] **Step 2: Verify all `SKILL.md` entrypoints have minimal frontmatter and distinct names**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
expected = {
    'project-governance',
    'domain-navigation',
    'incident-doctor',
}
seen = set()
for p in sorted(Path('skills').glob('*/SKILL.md')):
    text = p.read_text()
    assert text.startswith('---\n'), p
    head = text.split('---\n', 2)[1]
    fields = {}
    for line in head.splitlines():
        if ': ' in line:
            k, v = line.split(': ', 1)
            fields[k] = v
    assert fields.get('name'), p
    assert fields.get('description'), p
    seen.add(fields['name'])
assert seen == expected, (seen, expected)
PY
```

Expected: exit 0.

- [ ] **Step 3: Verify the target skeleton and retired-tree absence**

Run:

```bash
for f in \
  skills/project-governance/SKILL.md \
  skills/project-governance/references/control-plane.md \
  skills/project-governance/references/development-flow.md \
  skills/project-governance/references/verification-tiers.md \
  skills/project-governance/assets/templates/AGENTS.md \
  skills/project-governance/assets/templates/CURRENT_STATUS.md \
  skills/project-governance/assets/templates/CURRENT_TASK.md \
  skills/domain-navigation/SKILL.md \
  skills/domain-navigation/references/domain-model.md \
  skills/domain-navigation/references/mapping-workflow.md \
  skills/domain-navigation/references/evidence-rules.md \
  skills/domain-navigation/references/refresh-policy.md \
  skills/domain-navigation/references/repo-map.md \
  skills/domain-navigation/assets/templates/DOMAIN_MAP.md \
  skills/domain-navigation/assets/templates/DOMAIN.md \
  skills/domain-navigation/scripts/README.md \
  skills/incident-doctor/SKILL.md \
  skills/incident-doctor/references/evidence-gate.md \
  skills/incident-doctor/references/probe-design.md \
  skills/incident-doctor/references/fresh-incident.md \
  skills/incident-doctor/references/probe-lifecycle.md \
  skills/incident-doctor/assets/templates/INCIDENT.md \
  references/UPSTREAMS.md \
  references/LICENSE_NOTES.md \
  examples/README.md; do test -f "$f" || exit 1; done

for p in src tests docs/governance docs/reality-checks docs/reference-audit; do test ! -e "$p" || exit 1; done
```

Expected: exit 0.

- [ ] **Step 4: Verify there is no new executable product/runtime surface**

```bash
find skills references examples -type f \( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.rb' -o -name '*.go' -o -name '*.rs' \) -print
```

Expected: no output.

Also run:

```bash
git ls-files | grep -E '(^|/)(pyproject\.toml|requirements[^/]*\.txt|package\.json|Cargo\.toml|go\.mod)$' && exit 1 || true
```

Expected: exit 0.

- [ ] **Step 5: Verify upstream/license and tag invariants**

```bash
for s in 'Anthropic' 'AGENTS.md' 'acquire-codebase-knowledge' 'Aider'; do grep -qi "$s" references/UPSTREAMS.md || exit 1; done
grep -qi 'no upstream' references/LICENSE_NOTES.md
[ "$(git rev-parse 'v0.1.0^{}')" = "738627a0caad330d277f60cfdaff5f153593135e" ]
```

Expected: exit 0.

- [ ] **Step 6: Record task-branch handoff evidence in `CURRENT_TASK.md`**

Record: start baseline; final task-branch HEAD before/after the control update; exact retired roots; created Skill modules; V0 commands and outcomes; stable-tag target; `git status --short`; remote task-branch HEAD; state `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

Do not mark the work accepted or merged.

- [ ] **Step 7: Commit and push the handoff control update**

```bash
git add CURRENT_TASK.md
git commit -m "control: hand off Skill skeleton reset for audit"
git push -u origin <authorized-task-branch>
```

Then verify:

```bash
test -z "$(git status --porcelain)"
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/<authorized-task-branch>)" ]
```

Expected: both checks pass.

## Self-Review Result

- Spec coverage: Phase A requirements are covered; Phases B-F are intentionally excluded and require separate plans.
- Step scan: all steps perform one checkable action; documentation content is constrained by required sections rather than scripted prose.
- Type/interface consistency: module names, reference paths, and template paths match the approved spec exactly.
- Review Focus: each listed risk has a concrete verification in Tasks 1 or 5.
- Proportion: this plan defines the decisions needed for the skeleton reset and avoids specifying deep Skill content that belongs to later module plans.

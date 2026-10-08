# CURRENT TASK — RemoteOrbit Adoption Gap Audit Handoff

Task ID: `EG-REMOTEORBIT-ADOPTION-GAP-AUDIT-032`

State: `WAITING_FOR_USER_ADOPTION_DESIGN_REVIEW`

Mode: `READ_ONLY_TARGET_ADOPTION_AUDIT`

## Objective

Hand off the completed read-only RemoteOrbit adoption-gap audit for user review. No RemoteOrbit mutation and no reusable Skill change is authorized under this task.

## Verified target baseline

- Repository: `Lost0rz/RemoteOrbit`.
- Target `main` at audit start: `edcb4817f9ff9ae3400882f22ec61ec689f7fbaa`.
- Target `main` at audit end: `edcb4817f9ff9ae3400882f22ec61ec689f7fbaa`.
- Active target task: `RO-DUAL-RECEIVER-MOMENTARY-ROUTING-019`.
- Authorized implementation branch: `codex/dual-receiver-momentary-routing-v1`.
- Implementation branch head observed at audit end: `aa6f604056a64e4da0680904117cbd58049b6da1`.
- Branch relation to `main`: ahead 4 / behind 0; merge base equals `main`.
- Open PRs observed: none.
- Target mutation by this audit: none.

## Project Governance findings

### KEEP

Keep the existing RemoteOrbit `AGENTS.md` rather than replacing it with a generic template. It already provides project-specific protections for runtime/source identity, forensic preservation, local-only evidence, non-destructive unknown-work handling, task authority, and atomic material control transitions.

### MODIFY at the next safe transition

1. `CURRENT_STATUS.md` currently exceeds a fact-snapshot role by duplicating detailed product/architecture truth and granting executable `Implementation authority`. At the next safe control transition, remove authorization from STATUS and reduce duplicated design/plan detail. STATUS should record verified current facts, freshness basis, blockers, active task/branch facts, and next milestone, while pointing to TASK/spec/plan for authorization and detailed contract truth.
2. Do not rewrite active task `RO-DUAL-RECEIVER-MOMENTARY-ROUTING-019` merely for format. On the next natural task transition, use explicit affected domains, verified start baseline, risk + verification rationale, concise acceptance, consolidated STOP conditions, and handoff; reference the frozen design spec and implementation plan rather than reproducing their full execution detail.

No immediate `AGENTS.md` correction is required by this audit. Whether any existing freshness/control-transition rule produces repeated false STOPs must be measured during real development before loosening it.

## Domain Navigation findings

No new domain/navigation artifact is justified.

Current routing is already focused:

1. **Voice Gesture Classification / Trigger Gating** — current task + frozen dual-receiver design/plan; `main.swift`; branch-added `DualReceiverVoiceGestureRecognizer.swift`; focused classifier/runtime tests.
2. **Raw F5 HID Parking / Event Ownership** — `KeyMapping/HIDMonitor.swift`; `KeyMapping/EventSuppressor.swift`; `EventSuppressorTests`.
3. **Synthetic Receiver Trigger Ownership** — `VoiceOptionTrigger.swift`; `VoiceTriggerKey.swift`; `VoiceOptionTriggerTests`.
4. **BLE / Audio Transaction Lifetime** — `BLEBridge.swift`; `AudioPipe.swift`; BLE/voice coordinator tests; first-PCM and release/drain rules from the accepted design.
5. **Dual-mode Settings / Mapping** — existing settings and mapping seams referenced by the current task; no new authority.
6. **Installed Runtime Acceptance** — packaging/install/runtime identity evidence only at the already authorized hardware gate.

The implementation branch itself demonstrates focused navigation: its first four commits cover classifier corrective, dual classifier, per-transaction trigger key, and raw-F5 parking, with only eight relevant source/test paths changed.

`DOMAIN_MAP.md`, `DOMAIN.md`, Repo Map, repository index, or a navigation runtime are not justified now. Reconsider only if the real-task trial shows repeated routing friction across multiple tasks.

## Incident Doctor trigger decision

`DO_NOT_TRIGGER_NOW`.

Reason:

- the current work is authorized feature construction, not an unexplained incident;
- Tasks 1-4 are progressing on the intended implementation branch;
- no evidence-deficient failure currently blocks the next safe decision.

Existing diagnostic infrastructure is already sufficient as the default evidence surface if a qualifying incident later appears:

- accepted `DiagnosticAuthority` owns new machine-readable event schema/journal/query authority;
- the diagnostic CLI is a read-only consumer, not a second authority;
- legacy `VoiceDiagnosticLogger` and text/audio evidence remain specialized/compatibility sources where still applicable;
- production control remains separate from diagnostic observation.

If the early hardware gate later fails in an unexplained way, first ask whether existing evidence is sufficient to choose the next safe action. Only if one specific decision-blocking fact is missing should Incident Doctor authorize a minimum probe/fresh capture. Do not prebuild diagnostics.

## Repository lifecycle observation

The remote contains many historical `codex/*` branches but no open PR. Their lifecycle state was not exhaustively classified in this audit, and some may contain unique historical evidence. Do not delete them under adoption authority. A separate post-task lifecycle inventory may classify merged/retained/stale branches after the active feature reaches a safe closeout point.

## Adoption proposal

### KEEP

- existing `AGENTS.md` project-specific rules;
- current three-file control plane;
- current frozen design spec and audited implementation plan;
- active branch/worktree authority and preservation of unrelated local dirt;
- single diagnostic authority + read-only CLI + existing bounded diagnostic sources.

### MODIFY

- `CURRENT_STATUS.md` role/content at the next safe control transition;
- future `CURRENT_TASK.md` shape at the next natural task transition, without disrupting task 019.

### ADD

- none.

### DO NOT ADD

- `DOMAIN_MAP.md` / `DOMAIN.md`;
- `INCIDENT.md` without a qualifying incident;
- Repo Map/index/vector DB/navigation daemon;
- governance runtime/installer/enforcement layer;
- second diagnostic authority;
- broad logging/probe/telemetry work for adoption;
- historical branch cleanup inside the active feature task.

## Real-task trial acceptance criteria

Use ongoing RemoteOrbit development as the trial and record only concrete friction/evidence:

1. **Task clarity** — executor can identify objective, authority, branch/worktree, scope, acceptance and STOP conditions without chat history.
2. **STOP quality** — record each STOP as material or false/process-only; repeated false STOPs are a governance signal, not a reason to loosen safety after one event.
3. **Navigation efficiency** — reach the relevant gesture/HID/trigger/BLE/settings/test boundaries without broad repository survey or authority rework.
4. **Business-first progress** — feature commits/tests/hardware acceptance dominate; governance or diagnostics do not become a parallel project.
5. **Doctor trigger quality** — normal implementation/test failures remain normal engineering; Doctor activates only on a real blocking evidence gap.
6. **Verification proportionality** — use focused tests while boundaries are local, broader suite/build/runtime/hardware evidence only where the accepted task requires them.
7. **Closeout cost** — task/branch/worktree/control state should reconcile with minimal follow-up rounds at handoff/merge.

## STOP conditions

Do not mutate RemoteOrbit under this audit task. If the adoption design is accepted, open a separate bounded target-adoption task or defer the correction to the next safe target control transition. Do not interrupt the active feature merely to satisfy governance formatting.

## Current stop point

`WAITING_FOR_USER_ADOPTION_DESIGN_REVIEW`

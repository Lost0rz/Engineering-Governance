# Tooling Foundation Design — Bootstrap, Doctor, and Audit

**Task:** `EG-V01-TOOLING-DESIGN-002`
**State:** `DRAFT — WAITING_FOR_USER_SPEC_REVIEW`
**Design baseline:** `EngineeringGovernanceStandard` `0.1.0`
**Implementation status:** Not started

This document defines a proposed, small tooling layer around the accepted
governance standard. It is a design contract for review, not implementation
authorization or an implementation plan.

## 1. User intent and success criteria

The intent is to make governance setup and review repeatable across
repositories while keeping project facts, decisions, and evidence with their
existing owners. The tools should reduce repetitive inspection and setup
work, make drift visible, and leave consequential interpretation and
decisions with the project’s authorized people.

The design succeeds when:

- Bootstrap can create missing governance starter artifacts only after an
  explicit preview and approval.
- Doctor can quickly report local repository/control-plane health without
  changing files, refs, branches, worktrees, or remote state.
- Audit can evaluate selected versioned checks against identified evidence
  while keeping result, freshness, exception, and project decision separate.
- All three commands use one shared conceptual model and reference the
  project’s own authorities rather than creating a second state store.
- Machine results, AI analysis, and human decisions remain visibly distinct.
- Small projects can opt in with a short profile and a small set of applicable
  checks; adoption does not require seven documents or a central service.

## 2. Accepted v0.1 baseline

The design consumes the accepted `EngineeringGovernanceStandard` `0.1.0`.
That standard defines seven lifecycle layers, six cross-cutting axes, typed
authority routing, standalone project profiles, evidence provenance, and
separate evaluation result, freshness, exception, and project-decision
semantics. It is advisory by default and does not auto-remediate.

The root README was verified on the task branch: it lists all seven lifecycle
layers, says Bootstrap/Doctor/Audit are planned and not implemented, and
serves as a navigation entry point. This design does not change that README.

The tool layer does not claim that adopting the standard proves conformance.
It does not reinterpret the superseded `governance/v0.1` six-layer branch or
its early manifest/authority-map ideas as accepted requirements.

## 3. Approaches considered

| Approach | Benefits | Costs and risks | Fit |
|---|---|---|---|
| **A. Skill-only** | Lowest installation friction; natural-language help can explain repository-specific context; no executable distribution. | Repeated instructions can drift; file inspection and findings are harder to reproduce; AI may blur deterministic evidence and judgment; safe writes are difficult to constrain consistently. | Useful as an interface, insufficient as the only evaluator or writer. |
| **B. Executable-core-first** | Repeatable local checks; explicit command boundaries; one deterministic source for parsing, evidence references, and reports. | Without a thin AI/human interface, users must understand every control and interpretation; broad command surfaces can become a framework before use proves the need. | Strong for machine checks, weaker for context-rich judgment and adoption guidance. |
| **C. Hybrid** | A small local deterministic core handles shared mechanics; thin skills explain intent, collect human input, and summarize derived results. | Requires keeping the skill thin and ensuring it cannot bypass the core’s permissions; introduces a runtime/install requirement. | Best balance for this task’s repeatability, judgment boundaries, and small-project use. |

## 4. Recommendation and trade-offs

Recommend **Hybrid**: one small, on-demand local core for Bootstrap,
Doctor, and Audit, with optional thin AI skills that call it and explain its
reports. The core owns stable parsing, identity checks, check execution,
evidence references, report structure, and write permissions. Skills own
workflow guidance and derived explanation; humans retain project meaning,
authority ownership, exceptions, and decisions.

This keeps deterministic behavior reproducible without pretending that
repository governance can be fully reduced to machine checks. It also avoids
making prose instructions the only enforcement of a write boundary. The
trade-off is a small runtime and packaging cost; projects that do not need
repeatable tooling can continue using the standard documents directly.

The repository is currently documentation-only. The inspected Mac mini has
Python 3.11.9, Node, Go, Ruby, and Git; no existing project runtime constrains
the choice. For a first implementation, a dependency-free Python 3.11+
package using the standard library is the smallest dependable path on this
host: it avoids a compile/release matrix and third-party dependency chain,
while supporting local Git and filesystem work. This is a recommendation,
not an adopted toolchain. Python availability and the supported OS/runtime
floor must be confirmed before implementation; the installed tools alone do
not establish cross-project compatibility. If adopters must run without
Python, revisit distribution/runtime before writing code.

## 5. Component boundaries and authority

### Shared deterministic core

The core is a consumer of project controls and evidence. It may interpret the
accepted governance contract for evaluation, but it does not own product,
domain, architecture, runtime, task, or remote-host facts. It cannot decide
that a project’s chosen authority is correct merely because a file parses.

### Bootstrap

Bootstrap is the only member of the trio allowed to write governance setup
artifacts. Its write permission is narrow, explicit, and limited to missing
paths rendered from an approved template/profile.

### Doctor

Doctor reports repository identity, control-plane health, and observable
drift. It is read-only and is intended for quick preflight.

### Audit

Audit evaluates selected versioned checks and produces evidence-linked
results. It is read-only and does not accept results, change project
decisions, or enforce remediation.

### AI skill and human roles

An optional skill may map a request to a command, explain report fields,
identify missing evidence, and summarize AI-derived judgment with citations
and uncertainty. It may not write governance files directly, invent a
canonical authority, turn its own analysis into deterministic evidence, or
act as the independent reviewer of its prior output.

Humans and project-owned systems define authority meaning, approve profile
adoption, supply domain/product judgment, grant or revoke exceptions, and
record project decisions in their existing authority. The tools link to
those records; they do not replace them.

## 6. Shared canonical model

All commands load and use one in-process model of the accepted v0.1 concepts.
This is one implementation model, not a new persistent authority or a second
database. Its conceptual records are:

- target repository identity and observed revision;
- pinned standard/profile/check identities and versions;
- typed authority references and their scopes;
- evidence references with source, revision, capture time, method, and
  limitations;
- check purpose, scope, applicability, risk/severity rationale, relevant
  lifecycle layers/axes, required evidence, owner, freshness inputs, and
  review mode (`MACHINE`, `AI_JUDGMENT`, `HUMAN`, or `HYBRID`);
- historical evaluation result (`PASS`, `FAIL`, `UNVERIFIED`, or
  `NOT_APPLICABLE`);
- separate time-scoped freshness (`CURRENT`, `STALE`, or `UNKNOWN`);
- separate exception state and project decision disposition; and
- findings that refer to the check, target, evidence, and project-owned
  follow-up/decision records.

Persisted project controls remain the inputs and authorities. The in-memory
model is derived from those inputs for the duration of a command. Reports
refer to source paths/URIs and exact revisions instead of copying project
facts. There is no local database, hidden cache, or global profile store.
This design defines concepts only; it does not define or create a
machine-readable schema.

## 7. Data flow

1. The operator supplies an explicit target repository and selected command.
2. The core verifies repository identity and reads only the controls/evidence
   needed for that command. Doctor and Audit do not fetch or update Git refs.
3. Readers build the shared in-process model, preserving unknown or conflicting
   values instead of filling them by inference.
4. Doctor runs lightweight deterministic health checks. Audit applies the
   selected versioned checks and records which evidence supports each result.
5. The deterministic core emits an immutable base report with a report
   identity/digest, target and revision, evaluation/check identities, result,
   and evidence identities. That base report is the canonical output of the
   command and is never edited in place.
6. For `AI_JUDGMENT` or `HYBRID`, the AI skill consumes that identified base
   report and only the evidence references it names. The skill returns a
   derived `AIContribution` that links to the target, evaluation/check,
   evidence identities, base report identity/digest, model/provider,
   instruction/template identity, limitations, uncertainty, and contribution
   identity. The contribution cannot replace a result or source evidence.
7. A deterministic core composer validates those links and presents an
   ephemeral composed view: the immutable base report plus the linked derived
   contribution. A mismatch is left unlinked and reported; it never changes
   the base report. No persistent AI report store is created.
8. A HUMAN/HYBRID final judgment remains with the named human/project
   authority. The skill cannot record a project decision, approve its own
   contribution, or act as an independent reviewer of its prior output. Any
   decision/exception is recorded through the project’s existing authority;
   the tools only link to it.
9. Bootstrap follows a separate preview/approval path and creates only
   explicitly approved missing starter files.

## 8. Proposed repository layout

This is a future logical layout, not files to create in this design task:

```text
docs/governance/v0.1/                 accepted standard and contract
src/engineering_governance/           one shared model and local readers
  core/                               identity, model, evidence, reports
  commands/                           bootstrap, doctor, audit boundaries
checks/v0.1/                          versioned check definitions
templates/v0.1/                       approved, minimal setup templates
skills/engineering-governance/        thin optional AI workflow guidance
tests/fixtures/                        synthetic repositories and evidence
```

The exact check/template encoding and packaging format remain implementation
details for a later authorized task. Adopting repositories keep their own
controls and profile alongside their code; this repository stores reusable
standard/tool definitions, not their project state.

## 9. Bootstrap contract

Bootstrap is the sole controlled writer in the trio.

It MUST:

- require an explicit target repository identity/path and an approved
  template/profile version;
- inspect the target before proposing any write;
- show a complete preview/diff and require a separate explicit apply
  confirmation;
- create only candidate paths absent at preview and authorized as `CREATE`;
  never overwrite or replace an existing file. An exact expected existing
  artifact is the `NO_CHANGE` case below; a differing artifact is a conflict;
- use only approved templates and preserve clear placeholders such as
  `UNKNOWN` where project-owned facts are not supplied;
- never create an active task from a generic template; a task contract must
  come from an explicitly supplied project objective and owner;
- create an immutable conceptual **Preview Plan** before any apply. Its plan
  identity/digest binds at least: target repository identity and canonical
  root; target revision/state needed for safe comparison (including `HEAD`,
  index/worktree state, and candidate-path/parent identities and contents);
  template and profile versions; the full candidate path set and each planned
  action; rendered content digests; and the named human/project-authorized
  apply actor. The plan is a transient preview value, not persisted state;
  show its identity/digest to the operator so apply confirmation refers to
  that exact plan;
- classify an existing candidate artifact whose path/type and content exactly
  match the candidate rendered from the selected approved template/profile as
  `NO_CHANGE`. A repeated run over the same expected artifacts is therefore
  idempotent and performs no write;
- classify any existing candidate path that differs from the preview’s
  expected path/type/content as `CONFLICT / STOP`; never overwrite it;
- on apply, require a separate human-originated confirmation from the named
  authorized actor that identifies the preview plan. An AI-generated flag or
  AI-skill invocation is not human authorization. Then re-read the target,
  re-render, and recompute the plan from the same template/profile versions
  and inputs. Apply proceeds only
  if the recomputed plan identity/digest exactly matches the approved plan,
  every planned `CREATE` path remains absent, and every `NO_CHANGE` artifact
  remains an exact match. Any target, version, path, content, or state change
  is `STOP`; a new preview and approval are required; and
- stop on conflicts, symlink/path ambiguity, unsupported profile versions, or
  any attempt to write outside the explicit target’s approved governance
  paths.

It MUST NOT invent domain/product authorities, choose project policy, infer an
active task, migrate existing controls, repair drift, or modify application
files. AI skills may present the preview but MUST NOT approve or invoke apply
as the authorized actor. The core validates the actor and plan before any
write and uses create-if-absent behavior for `CREATE` paths; a concurrent
appearance or mutation of a candidate path stops the operation without
overwriting it.

## 10. Doctor contract

Doctor is strictly read-only. Its routine local preflight covers:

- repository identity and root;
- presence/readability and basic consistency of adopted control files;
- declared standard/profile version and obvious unsupported versions;
- task/status references and declared branch/worktree lifecycle facts;
- stale or unresolved authority/evidence pointers that can be checked
  locally; and
- fast deterministic checks that do not require a full selected-check audit.

Doctor MUST NOT write files or report artifacts, repair controls, switch
branches, delete branches/worktrees, fetch/update refs, change remotes, or
mutate remote state. Local checks use existing refs. Remote PR/branch facts
are reported only when the operator explicitly requests a read-only remote
query; without that query or required access, they remain `UNKNOWN`. The
default preflight is offline and bounded.

## 11. Audit contract

Audit is strictly read-only and performs deeper evaluation against an
explicitly selected, versioned check set and its required evidence. Every
evaluation identifies the target/revision, standard/profile/check versions,
review mode, evidence references, evaluation time, and limitations.

- `MACHINE` reports reproducible comparisons over identified inputs; missing
  or untrusted inputs cannot produce factual `PASS`.
- `AI_JUDGMENT` reports derived analysis with cited source evidence, model and
  instruction identity when available, uncertainty, and limitations. It
  cannot independently satisfy a factual check or accept its result.
- `HUMAN` remains `UNVERIFIED` until a named human decision/evidence reference
  is supplied; the tool does not manufacture that reference.
- `HYBRID` shows machine evidence and AI/human contributions separately and
  names the human owner of any final judgment.

For AI-enabled checks, Audit follows Section 7’s ownership flow: the core
emits the immutable deterministic base report; the skill returns a linked
`AIContribution`; and the core validates and composes a view without
rewriting the base report. The contribution references its target,
evaluation/check, evidence, base report identity, model/provider,
instruction/template, limitations, and uncertainty. The skill cannot modify
machine results, source evidence, the original report, or project decisions.
The contribution is ephemeral and derived; it creates no second authority or
persistent AI report store. A HUMAN/HYBRID final judgment belongs only to the
named human/project authority.

Audit keeps historical result separate from current freshness, exception
state, and project decision. It emits findings and evidence references, not
replacement source facts. It does not write an audit history, profile,
finding, exception, project decision, or remediation. A human may preserve a
report through the project’s normal review process after the command; that
separate action is outside Audit’s write permissions.

## 12. Read/write permissions

| Surface | Bootstrap | Doctor | Audit |
|---|---|---|---|
| Read target controls/evidence | Yes | Yes | Yes |
| Read local Git state | For target validation | Yes | Yes |
| Read remote state | No by default; no write | Explicit opt-in, read-only only | Explicit opt-in, read-only only |
| Write governance files | Missing approved starter files after preview and confirmation only | No | No |
| Write reports/findings/decisions | No | No | No |
| Change Git refs/branches/worktrees | No | No | No |
| Repair, migrate, enforce, remediate | No | No | No |

The core’s filesystem writes are isolated to Bootstrap’s approved paths.
Doctor and Audit emit reports on stdout only. Any user-initiated shell
redirection is outside the tool’s behavior and permissions.

## 13. STOP and failure semantics

Keep evaluation-level unresolved states separate from command-level fatal or
unsafe stops.

### Evaluation-level unresolved evidence

Missing, stale, or inaccessible optional/required evidence is not by itself a
command failure when the target and remaining inputs are trustworthy enough
to describe the gap. For each affected check:

- emit `UNVERIFIED` where evidence incompleteness prevents a supported result;
- assess freshness as `STALE` or `UNKNOWN` as the evidence supports;
- preserve any historical result unchanged;
- record which evidence was missing, stale, or inaccessible and the resulting
  limitation;
- report an unresolved same-class authority/owner conflict as `UNVERIFIED`
  for the affected check, identifying the conflicting sources and decision
  blocker; and
- emit the truthful report with exit code `0`.

An optional missing source may be recorded as a limitation without changing a
result that does not depend on it. Evidence incompleteness never silently
becomes a conformance or enforcement gate.

### Command-level fatal / unsafe STOP

Stop the command without a normal evaluation report only when it cannot
truthfully or safely perform the requested operation, including:

- target identity/path is ambiguous;
- the minimum trusted repository identity or root input required to scope a
  truthful report cannot be established;
- a required root control input is fatally malformed or unreadable, so the
  command cannot identify what it is evaluating;
- Bootstrap finds a conflicting existing artifact, changed Preview Plan,
  unsafe path, unapproved actor, or other write-safety violation; or
- an internal fatal failure prevents a trustworthy report.

Optional remote access or subordinate evidence being unavailable is
evaluation-level unresolved state when it can be reported as such; it is not
a fatal STOP. The command emits a bounded STOP diagnostic identifying the
observed condition and next owner/action, performs no unsafe write, repair, or
hidden mutation, and returns a nonzero command-level exit code as defined in
Section 15.

## 14. Evidence and provenance

Every reported claim points to an authority/evidence URI or repository path,
target identity, exact revision when available, observation/capture time,
method, scope, and limitations. External remote observations identify the
service and request time. AI-derived analysis additionally identifies the
model/provider and instruction/template revision when available, cites its
inputs, and describes uncertainty. Sensitive payloads are not copied into
reports when a source pointer or redacted digest is sufficient.

The tool records evidence references and observations, not a parallel copy of
canonical product or runtime facts. A missing/unknown source is recorded as
unknown, never inferred from another claim class.

## 15. Report and exit semantics

The deterministic core produces an immutable versioned base report on
stdout. Conceptually it identifies the target/revision, report identity/digest,
standard/profile/check versions, observation time, evaluations, freshness,
findings, evidence references, and limitations. For AI-enabled checks, the
composer may emit an ephemeral composed view containing that unchanged base
report plus a validated, linked `AIContribution`. The contribution does not
rewrite or supersede the base report. This document does not define or
implement a serialization schema or persistent report store.

Exit codes classify command execution, never governance outcome:

- `0`: the command produced a truthful report. This includes `FAIL`,
  `UNVERIFIED`, `NOT_APPLICABLE`, stale/unknown freshness, missing or
  inaccessible evidence and unresolved same-class authority conflicts that
  can be reported truthfully, findings, and a successful Bootstrap
  `NO_CHANGE` result. Evidence incompleteness alone MUST NOT produce a
  nonzero code.
- `2`: command-level fatal/unsafe STOP: ambiguous target, minimum trusted
  identity/root input unavailable, fatal malformed/unreadable root control,
  or Bootstrap conflict, changed plan, unsafe path, or unauthorized actor.
  No normal evaluation report is emitted; a STOP diagnostic may be emitted.
- `3`: internal fatal failure prevents a trustworthy report or STOP
  diagnostic.

Exit `2`/`3` describe whether the command could safely produce its requested
output; no code is a conformance or enforcement gate. A future named project
gate would be a separate, explicitly authorized consumer of a current
project decision.

## 16. Small-project and offline operation

Adoption is optional. A small project may pin `0.1.0`, keep one short
standalone profile with only relevant authorities/checks, and run local
Doctor/Audit without a service or network. Unselected checks are not
represented as passes. Bootstrap templates must not require a full map of
every lifecycle layer or a separate document per axis.

Local Git and filesystem checks work offline. Remote PR/branch state is
optional, explicitly requested, read-only, and unavailable facts remain
unknown. There is no mandatory account, central database, daemon, plugin
registry, or always-running process.

## 17. Versioning and migration

Keep separate identities for the accepted standard, project profile, check
definitions, tool implementation, and report format. Every evaluation pins
`EngineeringGovernanceStandard` `0.1.0` and the exact profile/check/tool
versions used. A profile is standalone; no parent inheritance is introduced.

This tool layer cannot silently change the meaning of accepted v0.1. A later
standard change follows the standard’s versioning rules. Tool upgrades do not
rewrite profiles or historic evaluations. Bootstrap never migrates existing
files; an upgrade requiring edits is a separately reviewed project change and
requires a future explicit task and write contract. No automatic migration
or remediation is included.

## 18. Validation strategy for a later implementation

No tests or runtime implementation are part of this design task. A later
authorized implementation should use focused evidence at these levels:

- **Model/unit checks:** authority-class routing, result/freshness/exception/
  decision separation, applicability, missing-evidence behavior, and stable
  report semantics.
- **Read-only checks:** run Doctor/Audit against temporary Git repositories;
  compare file hashes, refs, branches, worktrees, and remote-call logs before
  and after to prove no mutation.
- **Bootstrap checks:** preview causes no changes; apply creates only missing
  approved files; rerun is a no-op; existing/changed paths stop; target
  identity/path escapes are rejected.
- **Boundary checks:** AI output cannot become factual evidence or human
  acceptance; remote observations are opt-in/read-only; no report result
  implicitly enforces a gate.
- **Portability checks:** verify the declared runtime/OS floor and operation
  without network access. The floor must be selected before implementation.

## 19. Smallest first implementation slice

After this spec is reviewed and a separate implementation task is approved,
the smallest coherent slice is the shared reader/model plus local read-only
Doctor checks for repository identity and control-plane presence/consistency.
It should emit a truthful report and prove it made no file/ref/worktree
changes. Bootstrap writes and deeper Audit checks follow only in separately
reviewed increments. This is a scope boundary for future discussion, not an
implementation plan or permission to start implementation now.

## 20. Deferred scope

- executable implementation of any command in this task;
- CLI packaging, dependencies, or a machine-readable schema;
- MCP, daemon, background/continuous scanning, central service/database, or
  plugin framework;
- enforcement, branch-protection mutation, auto-repair, migration, or
  remediation;
- automatic profile inheritance or generated project authority maps;
- writing findings, exceptions, decisions, or audit history from Doctor/Audit;
- pilot repository changes; and
- implementation plan before user review of this written spec.

## 21. Open questions for review

The design can be reviewed without resolving these implementation details:

1. Which host platforms must the first implementation support? The inspected
   target is macOS on Apple silicon with Python 3.11.9; the recommendation
   assumes a declared Python 3.11+ runtime, but Windows and other developer
   environments have not been verified.
2. Which distribution method best keeps tool versions explicit for small
   projects without making Bootstrap install or update itself? The design
   recommends an on-demand versioned package but leaves the installer and
   package channel for a later implementation review.
3. Which minimal starter artifact set should be approved for Bootstrap?
   The safe default is to offer only selected governance controls with
   unknown placeholders, never a generated active task or invented authority.

Neither question changes the authority, read/write, or command boundaries in
this spec.

## 22. Adversarial self-review

| Challenge | Design response | Status |
|---|---|---|
| Over-design | One small core and optional thin skill; no framework, service, or required per-layer artifacts. | No blocker identified. |
| Duplicate authority/state | The model is derived in memory; project files and declared authorities remain canonical; reports use references. | No blocker identified. |
| Hidden writer | Only Bootstrap writes, only missing approved paths, after plan-bound human approval; Doctor/Audit are stdout-only. | No blocker identified. |
| AI judgment presented as deterministic | Review mode and evidence contributions stay separate; AI cites inputs and cannot accept factual results. | No blocker identified. |
| Doctor/Audit accidentally writable | No report/file writes, repair, ref update, branch switch, or remote mutation. | No blocker identified. |
| Bootstrap preview/apply and idempotence | Exact expected existing artifact is `NO_CHANGE`; differing artifact or changed plan is `CONFLICT / STOP`. A transient immutable plan binds target state, versions, paths, rendered digests, and authorized human actor; apply recomputes and compares it before writes, and AI cannot approve. | MAJOR resolved. |
| Evaluation unresolved vs command STOP | Reportable evidence gaps yield `UNVERIFIED`/`STALE`/`UNKNOWN`, limitations, and exit `0`; only fatal identity/root-input or unsafe/internal failures stop with nonzero exit. | MAJOR resolved. |
| Hybrid AI contribution ownership | The core keeps an immutable base report; it validates and links an ephemeral `AIContribution` without mutating the report, evidence, or project decision. | MAJOR resolved. |
| Bootstrap too powerful | Explicit target, approved template, no overwrite, no migration, no business facts, and apply-time plan revalidation. | No blocker identified. |
| Small project too heavy | Optional adoption, short standalone profile, selected checks only, local/offline operation. | No blocker identified. |
| Central service creep | No server, database, hidden process, or mandatory network; remote reads are opt-in. | No blocker identified. |
| MCP/enforcement creep | Explicitly deferred; report exit status is not a conformance gate. | No blocker identified. |
| Language selected by convenience alone | Runtime recommendation is tied to observed host and zero-dependency local use; portability/floor remains open before implementation. | Open implementation choice; no design blocker. |

Self-review against the three Web findings confirms each is explicitly
resolved above without changing the Hybrid recommendation or accepted
`EngineeringGovernanceStandard` `0.1.0`. No BLOCKER or MAJOR contradiction
with accepted v0.1 was introduced. The runtime floor and distribution method
remain open implementation questions, not permission to expand this task.

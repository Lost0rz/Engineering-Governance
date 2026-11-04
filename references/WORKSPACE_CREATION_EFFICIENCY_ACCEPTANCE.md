# Workspace / PR Creation Efficiency — Cross-Skill Acceptance

Task: `EG-VERIFICATION-CADENCE-EFFICIENCY-092`. Focused source-contract check for `project-governance`, `execution-orchestrator`, and `agent-handoff`. No new Skill, CI engine, workspace registry or per-command form.

| Scenario | Expected behavior | Prohibited inference or action |
| --- | --- | --- |
| User says inspect status, audit, review or run a bounded test | Existing safe checkout/remote evidence; **no new worktree/branch/PR** unless target project separately requires a writable isolated test setup | One new worktree per prompt |
| Same task receives another command or context/agent handoff | Reuse current task authority and valid branch/PR/worktree; receiver verifies local path if relevant | Create new worktree solely because of a new session or Card |
| Same-task small bug/corrective on open Draft PR | Continue safe existing PR and workspace | Successor PR/worktree per correction |
| Task/status control-only reconciliation | Align on permitted authorized ref; no evidence-only PR/worktree by default | New full construction workspace to record a status |
| Brand-new material task and project `AGENTS.md` requires fresh branch/Draft PR | Honor fresh branch and PR requirement once for that task; choose physical worktree separately | Universal no-PR rule or automatic extra worktree |
| Brand-new task with no branch/PR requirement and safe canonical checkout | Reuse checkout under actual project write permissions | Universal new branch/PR because a task was started |
| Two parallel read-only explorers | Share safe read-only source/context, or host-required ephemeral isolation | One durable worktree/PR per reader |
| Two truly disjoint concurrent writers with integration plan | Additional isolated worktree permitted with explicit ownership/ref/writer and release condition | Overlapping uncontrolled writers |
| Unresolved existing dirty/untracked/local-only work | Inspect owner/unique work and resolve or STOP; preserve all unverified work | Stash/reset/delete or silently bypass via fresh worktree |
| Known unique work in an intentionally retained workspace | Separate authorized isolation may be justified after proving disjoint authority and preservation | Treat retained workspace as empty or disposable |
| Previous PR merged, user requests further same-task phase | Check whether task contract actually terminated and what new scope rules require | Assume every merge necessarily creates a new task/worktree/PR |
| Project mandates independent review/PR for a material phase | Honor project-specific boundary while avoiding unnecessary extra worktree | Reusable policy overrides the target repository's normative rules |
| Many remote `codex/*` branches or PRs | Report remote churn and local Worktree state `UNKNOWN`; request local `git worktree list --porcelain` only if necessary | Infer physical local worktree count from GitHub |
| Cleanup of merged remote PR | Independently verify task terminal state, local dirty/unique work and physical worktree closeout | Declare `CLOSED_CLEAN` from merged PR alone |
| Small bug/UI/copy change in an existing task/PR | Reuse its safe checkout and current PR | Create physical Worktree for every edit |
| Small new material task whose project mandates fresh branch and Draft PR | Use safe existing checkout with new authorized branch and PR when possible | Infer new physical Worktree from new branch |
| Large independent module or sustained architecture change | A dedicated owned Worktree is permitted when actual separation helps and safe reuse is unsuitable | Assume every large change must create a Worktree |
| Concurrent non-overlapping writers with distinct runtime needs | Separate Worktree allowed after proving boundaries and release condition | Overlap active writers or bypass unique-work safety |
| Pre-merge controls still say READY_TO_MERGE | Keep accurate pre-event status and verify literal host merge conditions | Predict MERGED before GitHub merges |
| GitHub merges a PR and persisted controls still say READY | Observe verified merge, report POST_MERGE_DRIFT and NEEDS_RECONCILIATION; no automatic control-only PR | Claim controls CURRENT or create closure-only PR by default |
| User requests read-only status after such merge | Read current host evidence; report snapshot drift and no new mutation authority | Treat old CURRENT_TASK as live execution authority |
| Next authorized Task B after merged Task A | Normal Task B branch/PR first control-only commit combines Task A closure + Task B authorization; then product work | Two control-only PRs before feature PR or code edits under stale Task A |
| No permitted normal carrier but urgent authorization/safety conflict | STOP; require explicit authorized project-compliant control correction; standalone PR only if justified | Bypass protected main or defer a safety-critical contradiction |
| Proven control-only drift after valid semantic checks | Reuse compatible semantic evidence, separately re-check required literal-head host gates | Equate semantic equivalence with required CI/host PASS |
| Live active #39 in Governance project | Modify existing Draft PR only; preserve user no-merge boundary | Create another PR or merge without authorization |

Audit target: source semantics only. A static contract check does not verify actual Mac worktree counts, downstream project adoption, runtime Sub Agent workspace spawning, installed Plugin behavior, or branch protection.

# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.4`.

- Release title: `Engineering Governance Plugin v0.5.4`
- Frozen publication source: `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`
- GitHub Actions run: `38346638985` — `success`
- Release asset: `engineering-governance-plugin.zip`
- SHA-256: `2a39d1bf705b56b53f2514b5bb8012380606278989afabdc4f3c7424dd0f0367`
- Included top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

Historical `plugin-v0.5.3` and `plugin-v0.5.4` publication evidence remain immutable.

## Accepted v0.5.4 governance state

- ChatGPT Web Plugin is `0.5.4` with exactly three top-level Skills.
- Mac mini and MacBook Air are independently verified on one active `engineering-governance@engineering-governance-personal / 0.5.4` authority each.
- The accepted payload distinguishes literal Repository HEAD from Delivery / Semantic HEAD.
- `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement remains `CONTROL_ONLY_DRIFT` and does not by itself invalidate semantic implementation evidence.
- Repository-host gates remain separate live constraints for the literal identity the host governs.

## Active development state

Task `EG-MANDATORY-CONTROL-CLOSEOUT-058` is active on branch `codex/mandatory-control-closeout-058`, authorized from `main` at `72042f4157389520c7acd754cab5272a3cfdab85`.

The task corrects a control-lifecycle weakness introduced by the current lazy/batched reconciliation policy: completed governed work can leave `CURRENT_STATUS.md` / `CURRENT_TASK.md` materially stale until a later planning boundary.

Target behavior is mandatory closeout reconciliation after governed execution when control-owned facts changed, while preserving control-only delivery-identity semantics and avoiding raw lifecycle-event logging.

## Current scope boundary

This is source-only governance work. It does not yet:

- bump the Plugin version;
- publish a new GitHub Plugin release;
- mutate the ChatGPT Web Plugin;
- mutate Mac mini or MacBook Air installed Plugin authorities;
- modify target-project repositories;
- add a fourth Skill, daemon, hook, installer, database, or automatic remediation runtime.

## Next intended milestone

Complete the V0 source correction and self-audit on `codex/mandatory-control-closeout-058`, then stop for independent audit before any merge, version bump, publication, or local deployment decision.

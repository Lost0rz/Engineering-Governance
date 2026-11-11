# Development workflow

Default: **task → relevant Skill → implement → affected checks → remote delivery when requested**.

- Begin with a trusted user objective or an Issue/PR containing the agreed plan. An Issue helps share the objective, not determine who may edit code.
- Reuse existing code, task branch and safe checkout. Ask for design/navigation/diagnosis only when a real unresolved question prevents implementation.
- Correct local defects and scope-preserving interfaces directly. Actual changed product decisions, new privileges, irreversible data effects and lost-work risks may need targeted user input.
- During construction run focused tests when useful; prefer the next meaningful milestone for affected integration. Avoid a full GitHub CI run after each commit.
- Before significant version integration or a requested merge, obtain relevant broader evidence once. Reuse still-valid checks. Release and post-merge verification depend on actual consequence.
- Report actual commit/PR/CI results and what still needs human acceptance. An Issue, Card, receipt or status-only commit is not a mandatory lifecycle stage.

A genuine cross-context instruction can be the selected Issue/PR link plus current delta. The receiving host verifies its permissions separately. See [verification tiers](verification-tiers.md) for test scope and [workspace](workspace-lifecycle.md) for actual conflicts.

# Engineering development flow

Default loop: **understand → locate → implement → verify affected behavior → deliver**. Each stage is a decision, not a compulsory new document, agent, branch or approval.

1. **Task:** read the user objective and current relevant evidence. Select host-authenticated current-user G1/G2, an approved legacy Issue, or the accepted FILE_CONTROL Task as applicable. Read project `AGENTS.md` for unique product/runtime constraints.
2. **Baseline:** identify the code/ref and any conflicting active local work needed for safe edits. Reuse a safe workspace.
3. **Design only when needed:** use `solution-design` for unresolved material architecture/interface choices, `domain-navigation` for unclear code ownership, and `incident-doctor` for an actual evidence gap.
4. **Implement:** keep ordinary corrections, tests and scope-preserving interface adjustments inside the same task. Only changed permissions, product intent, irreversible effects or unresolved external decisions need escalation.
5. **Topology:** work inline by default; use `execution-orchestrator` if parallel or specialist work genuinely helps. Delegate with a shared task boundary, not new authority.
6. **Verify:** use [verification-tiers.md](verification-tiers.md) to choose affected checks. After a fix, rerun what the fix invalidated, not an arbitrary complete pipeline.
7. **Deliver:** push and confirm remote evidence when publication is part of the task. Distinguish implemented, CI pending, human UI pending, merged and installed states.
8. **Close:** update only meaningfully changed task/domain artifacts. Separate merge, release and destructive operations retain their own actual host safeguards.

A real cross-context transfer uses `agent-handoff` with references and delta. A formal independent acceptance question uses `evidence-audit`; routine self-checks do not require a separate auditor. Only inspect worktree/identity/legacy Issue details when the selected operation depends on them.

Risk labels are about actual consequences: G0 read, G1 local/recoverable, G2 bounded cross-component, G3 new privilege/credential/security trust or irreversible data/production effects. Valid host/tool write authority remains necessary regardless of label.

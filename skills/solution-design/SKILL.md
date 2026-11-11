---
name: solution-design
description: Resolve materially ambiguous engineering architecture, API, state ownership, data flows or interface choices before implementing an otherwise unclear task.
---

# Solution Design

Use only when a genuine engineering choice cannot safely be inferred from current product intent and canonical code. A clear bug fix does not require a separate design stage.

1. State the unresolved question and verified constraints.
2. Reuse accepted architecture, code/domain ownership and relevant design precedents.
3. Compare a small credible option set, including important tradeoffs and reversibility.
4. Decide within current trusted task intent; ask the user only for unresolved product choices, changed scope or consequential risk.
5. Record a durable decision only if future work genuinely needs it. Return selected option, affected interfaces and suggested verification to the owning task.

An Issue may hold the accepted plan; editing it needs normal Issue permissions, **not a revision/digest approval cycle**. A design result alone is not a credential for source writes. Detailed [design guidance](references/design-contract.md) is optional.

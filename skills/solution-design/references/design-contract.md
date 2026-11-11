# Engineering design method

Trigger on actual ambiguity in product intent, architecture, durable state ownership, API/schema or responsibility boundaries.

Separate verified facts, current user/project decisions, agent implementation choices and open questions. Reuse the canonical owner rather than inventing a parallel module or state source.

A useful design record briefly contains: objective, constraints, selected option, relevant alternatives/tradeoffs, affected data/API/owners, important consequences, and tests that distinguish success from failure. Research spikes are optional when their result may change the decision.

Keep the result in the existing task/Issue/PR when that is the useful shared surface; a second design file is not automatically required. Revise the plan when findings materially change the intended solution, without requiring an approval comment or hash.

The user and actual execution host decide scope, permissions and consequential external effects. Ordinary implementation choices within the agreed task need no repeated confirmation. Return to Project Governance with the design decision and remaining genuine owner-only questions.

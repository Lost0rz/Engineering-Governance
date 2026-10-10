# Incremental navigation refresh

Refresh navigation evidence when a trigger affects the current task or a routed area:

- the task-relevant Domain/capability route is absent or insufficient;
- a source path moved or was removed;
- an important symbol moved, was renamed, or was removed;
- an authority or ownership boundary changed;
- a dependency or consumer relationship materially changed;
- a relevant test changed;
- a runtime or operational entry point changed;
- a verified source contradicts the current route or navigation projection;
- the recorded evidence or freshness basis is too stale for the current decision.

Use the smallest outcome supported by current evidence:

- **Verified current / unchanged:** when the route content and its evidence/freshness basis are already current enough for the decision, keep the existing projection unchanged. Do not rewrite a claim merely to record another confirmation.
- **Same route, stale evidence refreshed:** when the route content is unchanged but the checked claim was explicitly stale because its evidence/freshness basis had expired or become insufficient, current verification may update only that affected evidence/freshness field. Do not rewrite unchanged route content or unrelated claims.
- **Verified correction:** when the existing claim is wrong, incomplete, stale in substance, or materially changed and the replacement is verified, update only the affected claim/fields and their evidence/freshness basis.
- **Replacement unresolved:** keep the unsafe/stale/unknown point explicit and report what remains unresolved; do not invent a replacement route.

Refresh only the affected navigation claim, Domain entry, or projection field. Re-read enough current evidence to verify the changed claim, preserve evidence that remains valid, and record the new revision/observation basis for the fields actually checked.

If the target repository has no separate navigation projection, re-verify and report the affected route; do not create a `DOMAIN_MAP.md` merely to record freshness. If a projection does exist, do not mark the entire artifact freshly verified because one Domain changed. Untouched entries retain their previous freshness; unchecked areas remain `stale` or `unknown` as appropriate. Do not rewrite unrelated Domains or imply they were rechecked.

Maintaining the directly affected claim in an already accepted derived navigation projection is normal governance-evidence reconciliation during authorized state-changing work; it does not require repeated per-task map-maintenance permission boilerplate. This never overrides an explicit project/task prohibition on metadata writes, and strict read-only work reports the verified correction or freshness candidate without mutating the projection.

Changes to an existing business/product/domain/capability authority do not authorize this Skill to rewrite that authority. Re-read the owning source and update only derived navigation pointers unless a separate task explicitly authorizes changes to the semantic authority itself.

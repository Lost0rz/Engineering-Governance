# Portable CI routing across repositories

The same script, [ci-router.py](../scripts/ci-router.py), plans tests for **any** Git repository. It does not own project commands, provision runners, or grant GitHub permissions.

## First adoption (once per repository)

1. Inspect existing tests and dependencies using the installed Governance Skill or the optional router discovery mode.
2. Create and review a small project-owned file at .github/ci-capabilities.json. Declare test IDs, affected path globs, argv command, optional setup/cwd, V1–V3 tier, timeout and available runner labels. Use the [example](../assets/examples/ci-capabilities.example.json).
3. Commit this accepted configuration to the repository's default branch. PR-supplied changes to this file are **not executed as policy** until accepted.
4. Replace competing automatic heavy CI triggers with a thin caller to the released reusable workflow. Keep unrelated release/deployment jobs separate. **Do not run old and new heavy CI concurrently.**
5. Verify Draft skip, targeted stage, Ready affected selection, release full selection, runner labels, GitHub required-check identity and rollback before retiring old CI.

Calling a Skill in Web/Desktop does **not** edit another repository's GitHub Actions. The first adoption requires a normal authorized repository change.

## Run locally (agent or CLI)

The portable script is included in the plugin's skills/ package, and can be run from the local installed plugin directory.

    python3 ci-router.py discover --repo-root /path/to/project
    python3 ci-router.py plan --repo-root /path/to/project --base BASE_SHA --head HEAD_SHA --config-source file --stage milestone
    python3 ci-router.py run --repo-root /path/to/project --base BASE_SHA --head HEAD_SHA --config-source base --stage focused --focused test-id

The plan command does not execute tests. The optional run command executes the selected, accepted-base argv commands locally and reports actual PASS/FAILED (or NOT_RUN). It must be explicitly invoked under real local host permission; it never grants permissions or runs on its own. For production CI always use accepted-base config mode instead of file mode.

## Remote (GitHub Actions)

Use the [caller example](../assets/examples/ci-caller.example.yml) with the released Governance workflow reference matching the router checkout tag. GitHub Actions owns the actual run and status; Governance owns test selection. The caller's default branch must contain the trusted capabilities config first. The central workflow does **not** inherit arbitrary project secrets.

The reusable workflow uses a GitHub-hosted planner, then schedules the selected test matrix on caller-available runner labels. The caller uses its real default branch (which need not be named main); test-capability changes remain pending review at Ready until accepted in the base. Self-hosted runners are available for workflows from the same owner/organization when the caller permits them.

## Stage / tier decisions

- **Draft:** defer remote tests; local agent may run a focused test during coding.
- **Focused:** execute a named test lane without claiming full integration.
- **Milestone:** run affected tests when a useful implementation unit stabilizes.
- **Ready:** run accumulated affected tests from the accepted base; unmatched source paths require explicit coverage resolution rather than a false PASS.
- **Release:** run the complete catalog, including release-related suites.
- **None:** perform planning-only check, no tests claimed.

V0 descriptive-only changes need no product tests; V1/V2/V3 reflect tests needed for actual affected behavior, not who may edit code. Paths select **candidate** tests; a material hidden dependency may justify manually adding a focused run. Unknown paths are visible as PARTIAL_UNMAPPED, not automatically promoted to every test.

## Trust, results and limitations

- Git diff includes both rename sides and rejects unsafe paths.
- The **project mapping** is loaded at the PR's accepted base SHA. The router code/workflow is loaded at the published Governance version.
- The plan includes HEAD/base SHA, config digest, stage, chosen tests, runner labels, unmapped paths and NOT_RUN status.
- Actual executor results are reported by GitHub. A skipped test is not a PASS, and a GitHub green check only covers the selected plan.
- For unsupported project prerequisites (service setup, secrets, test databases, multi-repo integration), keep a project-owned script or job and expose a small approved command entry. The plugin does not silently invent those requirements.
- The workflow is available to other repositories **after** this PR is merged and the referenced v0.10.0 tag is published. A plugin installed only in ChatGPT cannot alone dispatch a GitHub workflow without a connected host/action capable of triggering it.

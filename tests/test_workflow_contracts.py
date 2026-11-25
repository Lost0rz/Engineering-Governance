"""Workflow, routing, link integrity, catalog, and manifest contract tests."""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ROUTER_SCRIPT = ROOT / "skills/project-governance/scripts/ci-router.py"
spec = importlib.util.spec_from_file_location("eg_ci_router_contract", ROUTER_SCRIPT)
ci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ci)

REQUIRED_SKILLS = (
    "project-governance",
    "design",
    "solution-design",
    "domain-navigation",
    "incident-doctor",
    "execution-orchestrator",
    "agent-handoff",
    "evidence-audit",
    "project-profile",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    lines = match.group(1).splitlines()
    data: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val in (">-", ">", "|", "|-"):
            chunks = []
            i += 1
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                chunks.append(lines[i].strip())
                i += 1
            data[key] = " ".join(c for c in chunks if c)
        else:
            data[key] = val.strip("\"'")
            i += 1
    return data


class WorkflowContractTests(unittest.TestCase):
    def test_core_specialists_exist_and_have_positive_and_negative_frontmatter(self):
        route = (ROOT / "skills/project-governance/references/global-routing.md").read_text(encoding="utf-8")
        for name in REQUIRED_SKILLS:
            with self.subTest(name=name):
                skill = ROOT / "skills" / name / "SKILL.md"
                self.assertTrue(skill.is_file())
                text = skill.read_text(encoding="utf-8")
                fm = parse_frontmatter(text)
                self.assertEqual(fm.get("name"), name)
                desc = fm.get("description", "")
                self.assertGreater(len(desc), 40)
                self.assertIn("Do not", desc, f"{name} frontmatter missing negative boundary")
                self.assertIn(f"`{name}`", route)
        pg_desc = parse_frontmatter(
            (ROOT / "skills/project-governance/SKILL.md").read_text(encoding="utf-8")
        )["description"]
        self.assertIn("ci-router.py", pg_desc)
        design_text = (ROOT / "skills/design/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("MICRO_POLISH", design_text)

    def test_issue_is_optional_context_and_old_gate_is_not_shipped(self):
        config = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
        self.assertIn("blank_issues_enabled: true", config)
        self.assertTrue((ROOT / ".github/ISSUE_TEMPLATE/task-plan.md").is_file())
        for path in (
            ".github/ISSUE_TEMPLATE/execution-spec.yml",
            "skills/project-governance/scripts/issue-spec-check.py",
            "skills/project-governance/scripts/test_issue_spec_check.py",
            "skills/project-governance/scripts/verification-plan.py",
            "skills/project-governance/scripts/test_verification_plan.py",
            "skills/project-governance/assets/templates/EXECUTION_SPEC.md",
            "skills/project-governance/references/issue-execution-contract.md",
        ):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists())
        scripts = sorted(p.name for p in (ROOT / "skills/project-governance/scripts").iterdir())
        self.assertEqual(scripts, ["ci-router.py"])

    def test_no_self_granted_writer_permission(self):
        p = json.loads(
            (ROOT / "skills/project-governance/assets/control-policy.json").read_text(encoding="utf-8")
        )
        self.assertEqual(p["contract"], "CONTROL_POLICY_V2")
        self.assertTrue(p["require_host_authority_for_writes"])
        self.assertEqual(p["unattended_grants"], "NOT_PROVIDED_BY_PLUGIN")
        self.assertEqual(p["issue_role"], "OPTIONAL_PLANNING_AND_CROSS_CONTEXT_EVIDENCE")
        self.assertEqual(p["project_agents_control_selectors"], "IGNORED")

    def test_repo_catalog_completeness_and_proportional_routing(self):
        cfg, digest = ci.load(ROOT, "", ".github/ci-capabilities.json", "file")
        tracked = ci.tracked_files(ROOT)
        coverage = ci.inspect_catalog_coverage(cfg, tracked, ".github/ci-capabilities.json")
        self.assertEqual(coverage["dead_patterns"], [])
        self.assertEqual(coverage["dead_exclude_patterns"], [])
        self.assertEqual(coverage["unmapped_tracked_paths"], [])

        cases = (
            (["archive/README.md"], [], "NO_TESTS_REQUIRED", False),
            (["README.md"], ["workflow-contracts"], "SELECTED_PENDING", False),
            (["skills/design/SKILL.md"], ["workflow-contracts", "packaging-contracts"], "SELECTED_PENDING", False),
            (
                ["skills/project-governance/references/ci-routing.md"],
                ["workflow-contracts", "packaging-contracts", "router-contracts"],
                "SELECTED_PENDING",
                False,
            ),
            (["skills/project-governance/scripts/ci-router.py"], ["full-governance-suite"], "SELECTED_PENDING", False),
        )
        for changed, expected_ids, expected_cov, review_req in cases:
            with self.subTest(changed=changed):
                plan = ci.select(cfg, changed, "ready", "a" * 40, "b" * 40, digest)
                self.assertEqual(plan["selected_test_ids"], expected_ids)
                self.assertEqual(plan["coverage"], expected_cov)
                self.assertEqual(plan["review_required"], review_req)

    def test_portable_router_contract_is_discoverable(self):
        skill = (ROOT / "skills/project-governance/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("ci-routing.md", skill)
        self.assertTrue(ROUTER_SCRIPT.is_file())
        example = ROOT / "skills/project-governance/assets/examples/ci-capabilities.example.json"
        capabilities = json.loads(example.read_text(encoding="utf-8"))
        self.assertEqual(capabilities["contract"], "EG_CI_CAPABILITIES_V1")
        self.assertGreaterEqual(len(capabilities["tests"]), 3)

    def test_no_live_skill_or_reference_contains_obsolete_control_markers(self):
        obsolete = (
            "FILE_CONTROL",
            "ISSUE_CONTROL",
            "CURRENT_TASK.md",
            "CURRENT_STATUS.md",
            "CONTROL_ONLY_DRIFT",
            "POST_MERGE_DRIFT",
            "SPEC_APPROVAL_V1",
            "SPEC_DELEGATED_APPROVAL_V1",
            "STOP_CURRENT_TASK_NAVIGATION",
            "RETURN_TO_PROJECT_GOVERNANCE_FOR_REAUTHORIZATION",
        )
        live_files = (
            list((ROOT / "skills").rglob("*.md"))
            + list((ROOT / "rules").rglob("*.md"))
            + list((ROOT / "references").rglob("*.md"))
            + [ROOT / "README.md", ROOT / "AGENTS.md"]
        )
        for path in sorted(live_files):
            rel = path.relative_to(ROOT).as_posix()
            with self.subTest(path=rel):
                text = path.read_text(encoding="utf-8")
                for marker in obsolete:
                    self.assertNotIn(marker, text)

    def test_zero_broken_relative_markdown_links_in_active_docs(self):
        link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
        active_md = (
            [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "archive/README.md"]
            + list((ROOT / "rules").rglob("*.md"))
            + list((ROOT / "skills").rglob("*.md"))
            + list((ROOT / "references").rglob("*.md"))
        )
        for path in sorted(active_md):
            rel = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            base = PurePosixPath(rel).parent
            for match in link_re.finditer(text):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "file://")):
                    continue
                resolved = (ROOT / base / target).resolve()
                with self.subTest(source=rel, target=target):
                    self.assertTrue(
                        resolved.exists(),
                        f"Broken relative link in {rel}: {target} -> {resolved}",
                    )

    def test_golden_routing_cases_reference_valid_skills(self):
        golden_path = ROOT / "tests/routing_golden_cases.json"
        cases = json.loads(golden_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 18)
        seen_ids = set()
        for case in cases:
            self.assertNotIn(case["id"], seen_ids)
            seen_ids.add(case["id"])
            self.assertIn(case["expected_primary_skill"], REQUIRED_SKILLS)
            self.assertIsInstance(case["forbidden_first_hop"], list)
            self.assertNotIn(case["expected_primary_skill"], case["forbidden_first_hop"])
            for forbidden in case["forbidden_first_hop"]:
                self.assertIn(forbidden, REQUIRED_SKILLS)
            self.assertTrue(case["prompt"].strip())

    def test_shared_workflow_and_caller_yaml_syntax_when_ruby_available(self):
        ruby = shutil.which("ruby")
        if not ruby:
            self.skipTest("Ruby YAML parser is unavailable on this host")
        paths = (
            ROOT / ".github/workflows/ci-router-reusable.yml",
            ROOT / ".github/workflows/governance-contract-checks.yml",
            ROOT / "skills/project-governance/assets/examples/ci-caller.example.yml",
        )
        for path in paths:
            with self.subTest(path=path.name):
                proc = subprocess.run(
                    [ruby, "-r", "yaml", "-e", "YAML.parse_file(ARGV.fetch(0))", str(path)],
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_scoped_ci_prevents_empty_comparison_and_offers_router_test(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text(encoding="utf-8")
        self.assertIn('[[ "$BASE_SHA" == "$HEAD_SHA" ]]', workflow)
        self.assertIn("Affected verification requires comparison_base different", workflow)
        own_ci = (ROOT / ".github/workflows/governance-contract-checks.yml").read_text(encoding="utf-8")
        self.assertIn("          - test_ci_router.py", own_ci)
        self.assertIn("          - test_plugin_packaging.py", own_ci)
        self.assertIn("test_workflow_contracts.py|test_ci_router.py|test_plugin_packaging.py) ;;", own_ci)
        self.assertIn("check-catalog --repo-root . --require-complete-mapping", own_ci)

    def test_release_pin_and_marketplace_commit_match_manifest(self):
        version = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text(encoding="utf-8")
        self.assertIn(f"ref: v{version}", workflow)
        doc = (ROOT / "skills/project-governance/references/ci-routing.md").read_text(encoding="utf-8")
        self.assertIn(f"`v{version}`", doc)
        marketplace = json.loads(
            (ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8")
        )
        pinned_ref = marketplace["plugins"][0]["source"]["ref"]
        self.assertRegex(pinned_ref, r"^[0-9a-f]{40}$")
        if (ROOT / ".git").exists():
            proc = subprocess.run(
                ["git", "-C", str(ROOT), "cat-file", "-e", f"{pinned_ref}^{{commit}}"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, f"Unreachable marketplace ref: {pinned_ref}")

    def test_control_runner_and_concurrency_in_caller_example(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text(encoding="utf-8")
        self.assertIn("      control_runner:\n", workflow)
        self.assertIn("default: '[\"ubuntu-latest\"]'", workflow)
        route = workflow.split("  route:\n", 1)[1].split("\n  execute:\n", 1)[0]
        execute = workflow.split("\n  execute:\n", 1)[1].split("\n  result:\n", 1)[0]
        result = workflow.split("\n  result:\n", 1)[1]
        selected = "runs-on: ${{ fromJSON(inputs.control_runner) }}"
        self.assertIn(selected, route)
        self.assertIn(selected, result)
        self.assertNotIn("runs-on: ubuntu-latest", route)
        self.assertNotIn("runs-on: ubuntu-latest", result)
        self.assertIn("runs-on: ${{ matrix.runner }}", execute)
        caller = (
            ROOT / "skills/project-governance/assets/examples/ci-caller.example.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("control_runner:", caller)
        self.assertIn("head.repo.full_name != github.repository", caller)
        self.assertIn("self-hosted", caller)
        self.assertIn("concurrency:", caller)
        self.assertIn("cancel-in-progress:", caller)

    def test_executor_checkout_has_pr_base_parent_without_credentials(self):
        workflow = (ROOT / ".github/workflows/ci-router-reusable.yml").read_text(encoding="utf-8")
        route = workflow.split("  route:\n", 1)[1].split("\n  execute:\n", 1)[0]
        execute = workflow.split("\n  execute:\n", 1)[1].split("\n  result:\n", 1)[0]
        self.assertIn("fetch-depth: 0", route)
        self.assertIn("filter: blob:none", route)
        self.assertIn("persist-credentials: false", route)
        self.assertIn("fetch-depth: 2", execute)
        self.assertIn("persist-credentials: false", execute)
        self.assertNotIn("fetch-depth: 0", execute)

    def test_ci_draft_is_skipped_and_manual_scope_available(self):
        workflow = (ROOT / ".github/workflows/governance-contract-checks.yml").read_text(encoding="utf-8")
        self.assertIn("github.event.pull_request.draft == false", workflow)
        self.assertIn("concurrency:", workflow)
        for flag in ("validation_scope", "focused_suite", "package_preview"):
            self.assertIn(flag, workflow)
        self.assertIn("workflow_dispatch", workflow)
        self.assertIn("pull_request", workflow)
        self.assertIn("contents: read", workflow)


if __name__ == "__main__":
    unittest.main()

"""Source-level regression of v0.2.0 behavioral specification; not model execution."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class V02ContractTests(unittest.TestCase):
    def test_invocation_and_context_discovery_rules(self):
        skill = read("SKILL.md")
        self.assertIn("Explicit invocation wins", skill)
        self.assertIn("zero extra prompt", skill)
        self.assertIn("Past conversation", read("references/context-resolution.md"))
        self.assertIn("Current-thread referent", read("references/context-resolution.md"))
        self.assertIn("Minimum clarification", read("references/context-resolution.md"))
        self.assertIn("specifically authorized", skill)

    def test_no_source_type_skill_silos(self):
        skill = read("SKILL.md")
        self.assertIn("Context, not platform", skill)
        self.assertIn("Do not split by source type", skill)
        self.assertIn("selects/calls", skill)

    def test_deep_audit_has_specific_gates_and_no_false_pass(self):
        audit = read("references/evidence-acquisition.md")
        for token in ("A0", "A1", "A2", "A3", "schema", "tests", "failure", "resume", "SOURCE_REVIEWED", "TEST_RUN_PASS", "AUDIT_PARTIAL"):
            self.assertIn(token, audit)
        self.assertIn("single README", audit)

    def test_content_completeness_has_domain_adaptive_rules(self):
        contents = read("references/knowledge-completeness.md")
        for token in ("Technical implementation", "Bug or engineering audit", "Research/article", "historical", "reproduced", "CONTENT_PASS", "QUEUED"):
            self.assertIn(token.lower(), contents.lower())
        self.assertIn("No fixed word limit", contents)

    def test_discovery_not_capped_at_three(self):
        skill = read("SKILL.md")
        self.assertIn("Discover all valuable candidate topics", skill)
        self.assertIn("QUEUED", skill)
        self.assertIn("up to three", skill)
        self.assertIn("Discovering candidates within reviewed material is never limited to three", skill)

    def test_output_schema_stays_v01_and_artifacts_are_independent(self):
        contract = read("references/output-contract.md")
        self.assertIn("Canonical Knowledge Note v0.1", contract)
        self.assertIn("Each KEEP is independent", contract)
        for item in ("FORMAT_NOT_RUN", "CONTENT_PASS", "AUDIT_PARTIAL", "source_refs"):
            self.assertIn(item, contract)
        template = read("assets/knowledge-note.template.md")
        self.assertIn("## 证据与来源", template)
        self.assertTrue(template.startswith("---\n"))

    def test_light_chatgpt_adapter_needs_no_user_prompt(self):
        adapter = read("adapters/chatgpt-web.md")
        self.assertIn("不是要求用户复制粘贴的 Prompt", adapter)
        self.assertLess(len(adapter), 3000)
        for marker in ("KEEP", "HOLD", "SKIP", "knowledge_status", "source_access", "source_kind", "reuse_scope", "source_refs", "待验证提纲", "不要自动修改"):
            self.assertIn(marker, adapter)
        for heading in ("适用问题与复用触发", "核心结论", "原理、取舍与经验", "证据与来源", "适用边界与风险", "未验证事项 / 未来验证", "关联与原始入口"):
            self.assertIn(heading, adapter)

    def test_t9_t16_behaviors_are_explicit_not_claimed_passed(self):
        matrix = read("references/acceptance-matrix.md")
        for i in range(9, 17):
            self.assertRegex(matrix, rf"\bT{i}\b")
        self.assertIn("real model/host execution", matrix)

    def test_links_refer_to_existing_sources(self):
        for item in ROOT.rglob("*.md"):
            rel = item.relative_to(ROOT)
            if rel.parts[0] in ("references", "adapters") and rel.name.startswith("original-"):
                continue
            data = item.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", data):
                if target.startswith(("http:", "https:", "#")):
                    continue
                self.assertTrue((item.parent / target.split("#", 1)[0]).is_file(), (str(rel), target))

    def test_single_skill_not_governance(self):
        skill = read("SKILL.md")
        self.assertTrue(skill.startswith("---\nname: wiki-knowledge-builder\n"))
        self.assertIn("independent", skill)
        self.assertIn("Do **not** edit", skill)


if __name__ == "__main__":
    unittest.main()

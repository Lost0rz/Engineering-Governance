"""Static packaging/contract smoke tests. Not LLM-behavior or Wiki-ingestion acceptance."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


class StandaloneSkillStructure(unittest.TestCase):
    def test_frontmatter_and_trigger(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertRegex(skill, r"(?m)^name: wiki-knowledge-builder$")
        self.assertRegex(skill, r"(?m)^description: .+")
        self.assertIn("KEEP", skill)
        self.assertIn("HOLD", skill)
        self.assertIn("SKIP", skill)
        self.assertIn("not", skill.lower())

    def test_required_references_and_contract(self):
        for rel in [
            "references/decision-evidence.md",
            "references/output-contract.md",
            "references/acceptance-matrix.md",
            "assets/knowledge-note.template.md",
            "adapters/chatgpt-web.md",
            "examples/value-over-source.example.md",
        ]:
            self.assertTrue((ROOT / rel).is_file(), rel)
        contract = (ROOT / "references/output-contract.md").read_text(encoding="utf-8")
        for label in [
            "knowledge_status", "source_access", "source_kind",
            "reuse_scope", "source_refs", "适用问题与复用触发",
            "核心结论", "证据与来源", "适用边界与风险",
            "未验证事项 / 未来验证", "关联与原始入口",
        ]:
            self.assertIn(label, contract)

    def test_not_in_governance_plugin_tree(self):
        self.assertEqual(ROOT.parent.name, "standalone-skills")
        self.assertNotEqual(ROOT.parent, REPO / "skills")
        readme = (REPO / "README.md").read_text(encoding="utf-8")
        self.assertTrue(readme.startswith("# Engineering Governance"))
        workflow = (REPO / ".github/workflows/governance-contract-checks.yml").read_text(encoding="utf-8")
        self.assertIn('Path("skills").rglob("*")', workflow)
        self.assertIn('Path("references").rglob("*")', workflow)
        self.assertNotIn('Path("standalone-skills")', workflow)

    def test_adapter_contains_full_note_contract(self):
        adapter = (ROOT / "adapters/chatgpt-web.md").read_text(encoding="utf-8")
        for term in ("knowledge_status", "source_access", "source_kind",
                     "reuse_scope", "source_refs", "KEEP", "HOLD", "SKIP"):
            self.assertIn(term, adapter)


if __name__ == "__main__":
    unittest.main()

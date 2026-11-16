---
title: "跨来源知识沉淀应以复用价值而不是输入平台驱动"
created: 2026-11-16
knowledge_status: provisional
source_access: partial
source_kind: conversation
reuse_scope: cross-project
source_refs:
  - "2026-11-16 LLM Wiki 设计讨论：按内容价值与标准化输出组织，而非按 GitHub、聊天、Agent 来源分类"
tags: [knowledge-management, agent, wiki, design-decision]
---

# 跨来源知识沉淀应以复用价值而不是输入平台驱动

> 对 Agent 长期知识库，应统一价值筛选、证据要求及输出契约，而非按输入平台制定互不兼容的标准。

## 适用问题与复用触发

- 从讨论、GitHub、项目 Docs、Agent 执行日志等来源构建统一知识入口时。
- 为不同 Agent 适配知识生产流程，或决定是否全量入库时。

## 核心结论

设计讨论选择一个平台无关的 Wiki Knowledge Builder：先决定是否有长期复用价值，再提取因果、证据和边界，最后生成 Markdown 原始材料交给 LLM Wiki 后续处理。来源只影响资料获取方式。

## 原理、取舍与经验

1. 按 ChatGPT、GitHub、Codex、Pi 等输入来源拆成不同 Skill，会增加不兼容输出和重复治理。
2. 统一知识文档需保留触发条件、具体结论、为什么、来源与证据级别、失败边界及未验证事项。
3. 普通日志、重复 PR 状态或无研究方向的灵感允许 SKIP。
4. 一次成功的施工经验可以写入知识候选，但不足以直接形成成熟可执行 Skill。
5. Wiki 是历史知识与原始来源的导航，不覆盖项目当下的代码、Docs 或可复验运行事实。

## 证据与来源

- [E1] [S1] 2026-11-16 用户提供的设计材料 — 记录按内容价值而非来源平台组织 Skill 的设计选择 — 讨论决策；不等于已经实际部署验证。
- [E2] [S1] v0.1 设计材料和网页提示词 — 约定 KEEP/HOLD/SKIP 与 Canonical Markdown 结构 — 文件声明；不代表真实测试或 Wiki 摄入通过。

## 适用边界与风险

- ChatGPT 网页版并不默认拥有全部旧对话、私有项目或本地磁盘读取权。
- 该方案没有证明现有 LLM Wiki 能原生摄入模板的全部元数据。
- 项目代码与真实运行结果仍需在对应项目/环境内重新核验。

## 未验证事项 / 未来验证

- 使用对话、外部仓库、内部项目、Agent 日志和冲突资料验证筛选与证据分级。
- 验证 Wiki 插件真实摄入及后续可检索性。

## 关联与原始入口

- 关联：LLM Wiki、Agent Skill 生命周期、跨项目知识治理、证据追溯。
- 原始入口：2026-11-16 用户上传的 `wiki-knowledge-builder-v0.1-design.md` 和 `wiki-knowledge-builder-v0.1-example.md`（未提供可共享的逐条对话 URL）。

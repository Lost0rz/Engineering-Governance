# Wiki Knowledge Builder v0.2.2 — ChatGPT plugin adapter

**这是插件内的说明，不是要求用户复制粘贴的 Prompt。** 安装并明确选择 `Wiki Knowledge Builder` 后，用户只需要提交材料（网址、文章、文件、代码、任务记录），或说“把刚才/以前完成的工作沉淀一下”。模型直接执行 `SKILL.md`；不再要求用户重复分类、审计标准或格式。

## Host-specific behavior

- 优先使用当前对话、附件、显式输入；需要时使用真正可用且获授权的网页、GitHub、文件或历史上下文读取工具。无法读取时标注来源不足，不得编造资料或声称已经执行。
- 默认做与材料复杂度相匹配的**深入证据审计**，从核心代码/文档/测试/示例中保留可复用的实现机制、配置、重要参数、失败条件。不能只总结 README。若只是观点文章，不强加代码模板。
- 输出 **简短 KEEP / HOLD / SKIP / QUEUED 主题覆盖清单**、实际审计范围，然后针对 KEEP 生成独立的完整 Markdown。默认最多展开三篇，但不能丢失其余高价值主题。报告外层不加入网站 favicon、图片占位符、重复的预览卡片或无关来源装饰；有用的来源链接应放在笔记 `source_refs` 和证据段。
- 对已检查的代码/API 类 KEEP，应给出至少一个与实际来源一致的简短调用或配置示例（没有可靠依据则说明缺口），并明确标注 `UNTESTED_EXAMPLE` 或 `PSEUDOCODE`，不得把示例当成已执行测试。每篇笔记使用 `references/output-contract.md` 的 Canonical Knowledge Note v0.1 字段：`knowledge_status`、`source_access`、`source_kind`、`reuse_scope`、`source_refs` 等；保留 `## 适用问题与复用触发`、`## 核心结论`、`## 原理、取舍与经验`、`## 证据与来源`、`## 适用边界与风险`、`## 未验证事项 / 未来验证`、`## 关联与原始入口`。
- 不要自动修改 Obsidian、Wiki、代码、Agent 配置，也不要自动创建可执行 Skill。可选的 `skill_candidate: true` 只在真实观察到一次成功且注明复验门槛时使用，不自动生成 Skill。HOLD 仅产出**待验证提纲**；不要自动写入 Wiki。
- 运行过格式校验才写 `FORMAT_PASS`；没运行应写 `FORMAT_NOT_RUN`。证据编号与来源标记 `E1/S1` 的结构检查只有实际执行才写 `EVIDENCE_STRUCTURE_PASS`，否则写 `EVIDENCE_STRUCTURE_NOT_RUN`。内容完整性和事实真伪需独立判断。已读资料不是实测程序，源码审计不等于全仓库审计，输出的 Markdown 不代表已通过 Wiki 摄入。

正式笔记的 `source_refs` 必须是真实位置，不得保留模板占位符 `替换为真实来源定位，不得保留占位符`。

日常使用示例：**仅发送** `https://github.com/unclecode/crawl4ai`，或“沉淀刚才完成的工作”。不要让用户每次再输入长提示词。

审计覆盖范围必须写清：只在**已检查的源码和文档范围内**寻找全部有价值的候选；未看的模块记 `NOT_REVIEWED`，不得算 `QUEUED`（已发现但未展开）或 `SKIP`（低价值）。对生成笔记的 `[E1]` 使用 `[S1]` 显式映射 `source_refs`，保证未来可定位，并诚实区分真实访问和来源声称。

# Engineering Governance 多 Agent 标准化安装与配置指南（v0.11.0）

本指南沉淀 `Engineering Governance` 插件在不同 AI Agent 宿主与业务项目中的**标准化安装、挂载与新 Agent 快速接入流程**。所有 7 域路由边界（L0）、`SKILL.md` 速查路线（L1 <= 50 行）、23 条黄金路由用例及打包安全性均已由本仓自动化契约锁死；后续新补充 Agent 接入时，只需严格按本规范完成挂载并执行末尾“30 秒冒烟核验”，**无需重复运行多轮子 Agent 全量基准测试**。

---

## 1. 三层解耦架构（为什么免重复全量测试）

| 层级 | 职责边界 | 标准化载体 | 是否随新 Agent 变化 |
| :--- | :--- | :--- | :--- |
| **层 1：标准运行时插件产物** | 承载 7 域正交 Skills、`rules/AGENTS.md`、便携式 `ci-router.py` 及多宿主清单 | 由 [package-plugin.py](../scripts/package-plugin.py) 生成的独立目录或确定性 `.zip` 包 | **不变**（同源产物跨宿主通用） |
| **层 2：宿主挂载与发现配置** | 定义宿主如何扫描 `skills/*/SKILL.md`、注册轻量全局守则与插件启停开关 | `~/.gemini/config/`、`~/.codex/`、`~/.claude/` 或新增 Agent 对应配置路径 | **仅配置此处**（按三形态决策树适配） |
| **层 3：业务项目专属约束** | 声明该项目自身的技术栈、目录所有权、测试命令与审计威胁画像 | `<PROJECT_ROOT>/AGENTS.md` + `.github/ci-capabilities.json` | **仅跟项目走**，绝不复制通用路由表 |

---

## 2. 统一产物获取与构建标准

始终使用纯净的运行时打包产物（包含 `plugin.json`、`.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`rules/AGENTS.md`、`skills/**`、`PREVIEW_SOURCE_SHA.txt`），自动剔除仓内 `tests/`、`archive/`、`references/` 并拒绝一切符号链接。

> **重要禁令**：**严禁**将 `<EG_REPO>` 整个源码仓直接软链接进宿主 Skills 目录，否则会引入 `tests/`、`archive/` 等非运行时文件或触发符号链接越界校验失败。

### 方式 A：从已验证源码 Tag 构建独立插件目录与归档包（推荐用于本地宿主）

```bash
git -C <EG_REPO> fetch --tags origin
git -C <EG_REPO> checkout v0.11.0

python3 <EG_REPO>/scripts/package-plugin.py \
  --repo-root <EG_REPO> \
  --stage-dir <PLUGINS_PARENT_DIR>/engineering-governance \
  --output-dir <EG_REPO>/dist
```

执行后：
- `<PLUGINS_PARENT_DIR>/engineering-governance/` 为可直接挂载、权限确定（脚本 `0755`、文本 `0644`）且带 `PREVIEW_SOURCE_SHA.txt` 的独立插件目录。
- `<EG_REPO>/dist/engineering-governance-web-preview-0.11.0-<sha12>.zip` 为可直接上传/分发的确定性压缩包。

### 方式 B：直接获取 GitHub Release 确定性归档包

从上游 Release `v0.11.0` 下载 `engineering-governance-web-preview-0.11.0-<sha12>.zip` 并校验 SHA256：
- 若目标宿主支持上传插件包（如 Codex Web），直接上传该 `.zip`；
- 若为本地插件目录，直接解压至 `<PLUGINS_PARENT_DIR>/engineering-governance`。

---

## 3. 主流已知 Agent 宿主标准配置矩阵

### 3.1 Antigravity（`agy` CLI / IDE）

#### 方案一：标准插件目录自动发现（推荐）
将构建产物直接暂存到全局或项目级插件目录：
- 全局生效：`--stage-dir ~/.gemini/config/plugins/engineering-governance`
- 单项目生效：`--stage-dir <PROJECT_ROOT>/.agents/plugins/engineering-governance`

通过 Settings UI 或命令行一键启停（开关状态保存在 `~/.gemini/config/config.json`，后续升级刷新插件目录不会覆盖你的开关偏好）：

```bash
agy plugin enable engineering-governance
agy plugin disable engineering-governance
```

#### 方案二：从共享目录通过 `plugins.json` / `skills.json` 显式挂载
若插件存放在非默认共享父目录 `<PLUGINS_PARENT_DIR>`，在 `~/.gemini/config/plugins.json`（或 `<PROJECT_ROOT>/.agents/plugins.json`）声明：

```json
{
  "entries": [
    {
      "path": "<PLUGINS_PARENT_DIR>",
      "include_only": ["engineering-governance"]
    }
  ]
}
```

> **常见配置陷阱**：`plugins.json` 与 `skills.json` 的 `entries[].path` 均为**向下一层目录扫描**：
> - 用 `plugins.json` 挂载整个插件时，`path` 必须填写**包含 `engineering-governance` 的父目录** `<PLUGINS_PARENT_DIR>`，不能直接填 `.../engineering-governance`；
> - 若只想通过 `skills.json` 按需挂载部分域，则 `path` 填写 `<PLUGINS_PARENT_DIR>/engineering-governance/skills` 并搭配 `"include_only": ["engineering-workflow", "ci-governance", "evidence-audit"]`。

### 3.2 OpenAI Codex（CLI / Desktop / Web）

- **Marketplace 接入**：直接引用本仓内置 `.agents/plugins/marketplace.json`（其中 `source.ref` 已锁定为通过全部校验的 40 位 Commit SHA）。
- **Web 端上传**：直接上传 Release `v0.11.0` 产物 `engineering-governance-web-preview-0.11.0-<sha12>.zip`（压缩包内 `.codex-plugin/plugin.json` 已映射 `"skills": "./skills"`）。
- **本地目录接入**：将 `<PLUGINS_PARENT_DIR>/engineering-governance/skills/` 挂载/复制到 `~/.codex/skills/`（或项目 `.agents/skills/`），并将 [rules/AGENTS.md](../rules/AGENTS.md) 中的轻路由守则合入全局指令。

### 3.3 Claude Code（CLI / IDE）

- **标准插件包接入**：归档包/构建目录内置 `.claude-plugin/plugin.json`，可直接将 `<PLUGINS_PARENT_DIR>/engineering-governance` 注册为 Claude Code 插件。
- **纯 Skills 目录接入**：将 `<PLUGINS_PARENT_DIR>/engineering-governance/skills/*` 复制到 `~/.claude/skills/`（或项目 `.claude/skills/`），并将 [rules/AGENTS.md](../rules/AGENTS.md) 的三条轻路由原则加入 `~/.claude/CLAUDE.md`。

### 3.4 多端编排宿主与子 Agent（如 T3 Code 等）

- 编排宿主**无需重复安装**，直接继承底层已挂载好本插件的 Provider（Antigravity / Codex / Claude）配置即可。
- **子 Agent 轻量派发契约**：在主/子线程委派 Prompt 中仅描述明确目标、边界与验收要求，**严禁**粘贴 7 个 `SKILL.md` 全文或无关 `references/*.md`；子 Agent 会自动通过宿主渐进式披露进入单一归属域。

---

## 4. 未来新补充 Agent 的标准化接入 SOP（三形态决策树）

当团队新增任意未在上方列出的新 Agent 工具或运行时时，只需判断它属于以下哪种扩展能力形态并按对应动作一次性配置：

| 新 Agent 扩展能力形态 | 判断依据 | 标准接入动作（只做这一套） |
| :--- | :--- | :--- |
| **形态 1：原生支持 Plugin Bundle** | 支持识别 `plugin.json` + `skills/` + `rules/` | 1. 构建并指向 `<PLUGINS_PARENT_DIR>/engineering-governance`；<br>2. 确认宿主仅向系统提示词注入 `SKILL.md` frontmatter（`name` + `description`）和 `rules/AGENTS.md`；<br>3. 执行第 6 节 30 秒冒烟核验。 |
| **形态 2：支持渐进式 `SKILL.md` 目录扫描** | 能自动发现目录下的 `<skill>/SKILL.md` 并按需读取全文 | 1. 将新 Agent 的 Skills 搜索路径指向 `<PLUGINS_PARENT_DIR>/engineering-governance/skills`（或复制到其标准全局 skills 目录）；<br>2. 将 [rules/AGENTS.md](../rules/AGENTS.md) 的 5 行轻路由守则合入该 Agent 的全局系统规则；<br>3. 执行第 6 节 30 秒冒烟核验。 |
| **形态 3：仅支持单一全局规则 + 文件读取工具** | 无独立 Skill 发现机制，仅有一份系统指令与 `read_file` / shell 工具 | 1. 仅将 [rules/AGENTS.md](../rules/AGENTS.md) 合入其全局规则，并注明 7 域目录路径 `<PLUGINS_PARENT_DIR>/engineering-governance/skills/` 与按需直读单一 `<domain>/SKILL.md`；<br>2. **严禁**将 7 份 `SKILL.md` 和全部 `references/*.md` 拼成单一大提示词常驻注入；<br>3. 执行第 6 节 30 秒冒烟核验。 |

---

## 5. 目标业务仓初始化标准清单（每个新项目 2 分钟配置）

1. **创建或对齐 `<PROJECT_ROOT>/AGENTS.md`**：
   参照 [AGENTS.md 模板](../skills/engineering-workflow/assets/templates/AGENTS.md) 仅填写本项目事实、构建测试命令与审计威胁画像，**不重复粘贴插件级路由规则**：
   - 后端服务、Web API、多租户系统、CLI、CI 脚本 / 打包器：保留默认 `Audit threat profile: SERVICE_OR_UNTRUSTED_INPUT`；
   - iOS / macOS / 桌面沙箱客户端应用：显式声明 `Audit threat profile: SANDBOXED_APP`（开启客户端真事件边界、防“哥斯拉”理论攻击过度收紧与两轮复审收敛）。
2. **可选：接入便携式增量 CI 路由**：
   参照 [ci-routing.md](../skills/ci-governance/references/ci-routing.md) 与 [ci-caller.example.yml](../skills/ci-governance/assets/examples/ci-caller.example.yml)（固定引用 `@v0.11.0`）完成初始化与全文件映射自检：

```bash
python3 <PLUGINS_PARENT_DIR>/engineering-governance/skills/ci-governance/scripts/ci-router.py discover --repo-root <PROJECT_ROOT>
python3 <PLUGINS_PARENT_DIR>/engineering-governance/skills/ci-governance/scripts/ci-router.py scaffold --repo-root <PROJECT_ROOT> > <PROJECT_ROOT>/.github/ci-capabilities.json
python3 <PLUGINS_PARENT_DIR>/engineering-governance/skills/ci-governance/scripts/ci-router.py check-catalog --repo-root <PROJECT_ROOT> --require-complete-mapping
```

---

## 6. 新 Agent 安装后 30 秒免重测冒烟核验（3-Step Smoke Check）

新补充 Agent 按第 3/4 节完成配置后，只需依次通过以下 **3 项轻量核验** 即可确认配置完全就绪：

1. **产物版本与同源 SHA 核验**：
   确认插件目录 `plugin.json` 中 `"version"` 为 `"0.11.0"`，且 `PREVIEW_SOURCE_SHA.txt` 与对应发布 Tag 的 40 位 Commit SHA 完全一致：
   ```bash
   cat <PLUGINS_PARENT_DIR>/engineering-governance/PREVIEW_SOURCE_SHA.txt
   ```
2. **按需渐进式披露核验（防全量预加载与越界窥探）**：
   在一个全新会话中发送一条明确的单一领域请求（例如：“请修复某模块中的单文件边界 bug 并运行其单元测试”），检查该 Agent 的实际文件读取轨迹：
   - 仅读取 `skills/engineering-workflow/SKILL.md`（走 `DIRECT_BUILD`，`0` 份 `references/` 读取）；
   - 未预先全量扫描其余 6 个 Skill 或 `references/`；
   - 运行仓库自检或增量路由时只按当前阶段执行。
3. **随包脚本可执行核验**：
   确认工具脚本权限与 Python 运行时可用（退出码为 `0`）：
   ```bash
   python3 <PLUGINS_PARENT_DIR>/engineering-governance/skills/ci-governance/scripts/ci-router.py --help
   ```

---

## 7. 平滑升级、停用与回滚规范

- **升级到新发布版本**：在源码仓拉取目标 Tag（如 `v0.11.0`）后，直接复用同一 `--stage-dir <PLUGINS_PARENT_DIR>/engineering-governance` 执行 [package-plugin.py](../scripts/package-plugin.py)。脚本会校验证明身份的 `PREVIEW_SOURCE_SHA.txt` / `plugin.json` 并安全原地替换插件内容，同时保留用户在宿主 `config.json` 中的启停配置。
- **临时停用**：使用宿主原生的插件开关（如 `agy plugin disable engineering-governance`）或移除 `plugins.json` 注册项即可即时卸载，不改动任何业务代码仓库。
- **回滚**：在源码仓切回上一稳定 Tag（例如 `git -C <EG_REPO> checkout v0.10.3`），重新执行一次 `--stage-dir` 构建覆盖即可，详情规则另见 [README.md](../README.md) 与 [SKILL_ENGINEERING.md](SKILL_ENGINEERING.md)。

# Skills Audit

更新时间：2026-03-29

这份文件是当前 XHS skills 的维护台账。

它的职责只有三个：

- 记录每个 skill 现在应该负责什么
- 记录它和当前 `README` 流程是否对齐
- 记录下一轮该补什么

这份文件**不定义默认 workflow**。

边界：

- 顶层流程以仓库根目录 `README.md` 为准
- 账号默认以 `notes/account-default-cover-and-intro-style.md` 为准
- 这份文件只审计 skill 系统本身，不再单独重写一套流程

## Audit 维度

每次看一个 skill，默认检查这些维度：

- 触发条件是否清楚，是否会 over-trigger
- 职责边界是否清楚，是否和别的 skill 重叠
- 默认交付是否符合当前 `README` 流程
- `references / examples / evals / fallback` 是否够用
- 如果有脚本，脚本输出是否和 skill 描述一致

## 当前对齐快照

- 已基本对齐：
  - `xhs-note-assembly`
  - `xhs-visual-asset-mix`
  - `xhs-cover-template`
  - `xhs-image-style-duo`
  - `xhs-publish-review`
- 已可用但建议继续收紧：
  - `xhs-topic-angle-shortlist`
  - `xhs-fact-pack`

## Skill Ledger

| Skill | 目标职责 | 当前对齐度 | 主要残留问题 | 下一步 |
| --- | --- | --- | --- | --- |
| `xhs-topic-angle-shortlist` | 发想题目、可能切角，维护跨 post backlog，并选出本轮先研究哪个题 | 部分对齐 | 还需要继续观察 backlog 维护是否会和单篇 post workspace 混淆 | 用真实案例校正 backlog 更新动作 |
| `xhs-fact-pack` | 单篇帖子的主研究文件，承载完整事实依据，再交给 `story_spine` 收成故事 | 部分对齐 | 需要继续验证“完整研究”与“不要偷写成稿”之间的边界 | 用真实案例校正研究深度和 handoff 质量 |
| `xhs-note-assembly` | 默认主线 skill，负责把 `fact_pack + story_spine` 变成成稿、图组任务和封面提取 | 基本对齐 | 仍需持续观察是否会绕过 `fact_pack` 直接内部补完一切 | 继续用真实案例校正输入依赖和输出长度 |
| `xhs-visual-asset-mix` | 素材路由器，只在真人图 / 截图 / 生图真的难选时启用 | 基本对齐 | 仍要观察是否会把例外步骤重新说成默认步骤 | 保持例外处理定位，补更多真人图建议样例 |
| `xhs-cover-template` | 封面结构例外处理器，只处理默认封面不适用的情况 | 基本对齐 | 仍要观察是否会被误用成每篇都跑的模板层 | 保持和账号默认封面规则一致，不再外扩默认流程 |
| `xhs-image-style-duo` | 默认交付是 `一个推荐风格 + 一条可直接贴到网页的 final prompt`；只有明确要求时才双风格 | 基本对齐 | 还需要继续观察风格推荐是否稳定、prompt 是否足够贴近具体人物动作 | 用真实封面 brief 持续校正推荐和 prompt 质量 |
| `xhs-publish-review` | 发布后复盘、回写工作流、同步历史记录 | 基本对齐 | 文档里仍有重复段落等小问题 | 清理重复段落，继续补真实复盘样本 |

## Related Script Checks

这些脚本不是 skill，但会把 skill 流程固化到实际产物里，所以需要一起审计：

- `scripts/scaffold_post_folder.py`
  应默认创建 `fact_pack.md + story_spine.md`，不再默认创建 `research.md`
  同时要让 README 模板反映 backlog -> fact_pack -> story_spine 的新顺序
- `skills/xhs-image-style-duo/scripts/generate_style_duo.py`
  现在默认应输出 `final_prompt.txt + web_prompts.md`
  只有显式比较模式才额外输出两条 final prompt，并且脚本不得调用图片 API

## 当前维护重点

### P1

- 用真实案例继续验证 `xhs-topic-angle-shortlist` 会维护 backlog，而不是只做一次性 shortlist
- 用真实案例继续验证 `xhs-fact-pack` 能成为每篇帖子的主研究文件
- 用真实案例继续验证 `xhs-image-style-duo` 的默认单 prompt 质量
- 确认图片相关脚本长期只导出网页可用 prompt，不再尝试 API 生图

### P2

- 校正 `xhs-note-assembly` 的真实输出样本
- 检查 `scaffold_post_folder.py` 是否已完全反映新的 per-post 研究结构
- 决定 backlog 应该继续用单文件，还是拆成多主题文件

### P3

- 清理 `xhs-publish-review` 的重复段落
- 决定哪些账号专属规则该留在本 repo，哪些可以毕业回 `xhs_skills`

## 维护规则

- 每次改 skill 的职责或默认交付，都要先对照 `README.md`
- 每次补 `references / evals / fallback / scripts`，都要同步更新这份台账
- 如果某个 skill 已经不再承载默认流程，必须在这里明确写清它现在是“默认步骤”还是“例外步骤”
- 如果脚本输出和 skill 描述不一致，优先修这个不一致，而不是在文档里继续解释例外
- 图片相关脚本默认只负责导出 prompt；真正发起生图由人手动在网页聊天界面里完成

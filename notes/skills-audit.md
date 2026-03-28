# Skills Audit

更新时间：2026-03-28

这份文件是当前 XHS skills 的长期维护总表。

用途：

- 记录每个 skill 现在负责什么
- 对照 Claude Skills best practices 看当前做到哪一步
- 明确下一轮优先补什么

参考标准：

- description 是否同时写清楚 `做什么 + 什么时候用`
- workflow 是否清楚
- 是否有 examples / references / evals
- 是否有 fallback
- 有脚本时，脚本是否和说明一致

## 当前技能地图

### 1. 选题层

- `xhs-topic-angle-shortlist`
  - 负责：复看账号、搜热点、给候选题和切角
  - 状态：可用

### 2. 事实层

- `xhs-fact-pack`
  - 负责：整理论点链、数字、风险和来源
  - 状态：可用

### 3. 图片分工层

- `xhs-visual-asset-mix`
  - 负责：决定每张图用真人图、截图还是生图
  - 状态：可用

### 4. 首图模板层

- `xhs-cover-template`
  - 负责：锁图 1 的固定封面模板
  - 状态：可用

### 5. 风格延展层

- `xhs-image-style-duo`
  - 负责：给已确定要生图的单页输出两种风格候选
  - 状态：可用

### 6. 成稿层

- `xhs-note-assembly`
  - 负责：把角度、事实包和图组分工组装成最终帖子
  - 状态：可用

### 7. 复盘层

- `xhs-publish-review`
  - 负责：对比草稿和发布版，回写工作流规则
  - 状态：可用

## Checklist 总览

说明：

- `完成`：已经有明确内容
- `部分完成`：已经有雏形，但还不够稳定
- `待补`：还没有系统化

| Skill | 触发描述 | Workflow | References / Examples | Evals | Fallback | Scripts / Validation | 当前判断 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `xhs-topic-angle-shortlist` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 稳定可用 |
| `xhs-fact-pack` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 稳定可用 |
| `xhs-visual-asset-mix` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 稳定可用 |
| `xhs-cover-template` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 稳定可用 |
| `xhs-image-style-duo` | 完成 | 完成 | 完成 | 完成 | 完成 | 完成 | 当前最完整 |
| `xhs-note-assembly` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 文案主力 skill |
| `xhs-publish-review` | 完成 | 完成 | 完成 | 完成 | 完成 | 不适用 | 复盘主力 skill |

## 逐个状态

### xhs-topic-angle-shortlist

- 现在做得好的地方：
  - 已能区分 `探索` 和 `发想`
  - 已补账号复看 checklist 和切角句型
  - 已补 eval
- 还要继续观察的点：
  - 是否会 over-trigger 到长期系列规划
  - 是否会把“可做常青题”误写成“当天热点”

### xhs-fact-pack

- 现在做得好的地方：
  - 已补 source hierarchy
  - 已补 number normalization
  - 已补资料不完整时的最小交付
- 还要继续观察的点：
  - 遇到多来源数字冲突时是否真的会把不同口径分开
  - 会不会还是不自觉写成半成稿

### xhs-visual-asset-mix

- 现在做得好的地方：
  - 图组任务边界清楚
  - 已补 page patterns
  - 已补素材不足时的回退顺序
- 还要继续观察的点：
  - 会不会默认整组都用生图
  - 会不会给某张图塞两个任务

### xhs-cover-template

- 现在做得好的地方：
  - 已把首图固定成独立层
  - 已补无强人物时的 fallback
  - 已有 eval
- 还要继续观察的点：
  - 会不会被误用于整组图，而不是只用于图 1
  - 规则题是否仍会误判成人物封面

### xhs-image-style-duo

- 现在做得好的地方：
  - 已从“固定两种画风”升级成“风格包 + 两种候选”
  - 已有 references、evals、脚本
  - 脚本已能输出推荐风格和推荐理由
- 还要继续观察的点：
  - 推荐的两种风格是否真的合理
  - 哪些风格包长期表现更好，哪些只是理论上可用

### xhs-note-assembly

- 现在做得好的地方：
  - 已写入固定的讲故事动作
  - 已补 examples
  - 已补 fact pack 不完整时的降级规则
- 还要继续观察的点：
  - 是否还会写成大段整理稿
  - emoji 和英文控制是否稳定

### xhs-publish-review

- 现在做得好的地方：
  - 已和 `published-history.md` 绑定
  - 已补截图版 / 单边复盘 fallback
  - 已补 example review
- 还要继续观察的点：
  - 会不会只写“整体更好”而不写归因
  - 会不会复盘完却没有回写 skill 或 workflow

## 下一轮优先级

### P1

- 给 `xhs-image-style-duo` 增加真实结果回写机制
- 记录每次风格推荐最后哪种被采用
- 把使用结果反推回 `style-selection-rules.md`

### P2

- 给 `xhs-note-assembly` 增加更多真实前后对照案例
- 给 `xhs-publish-review` 增加一份完整真实复盘样本

### P3

- 决定哪些账号专属规则应该毕业回 `xhs_skills`
- 决定哪些规则只留在 `xhs_content_generator`

## 维护规则

- 每次新增或大改一个 skill，都要更新这份总表
- 每次补 `references/`、`evals/` 或 fallback，都要同步更新状态
- 如果某个 skill 被拆层或并层，要先更新这份文件，再更新 README

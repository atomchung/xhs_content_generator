---
name: xhs-publish-review
description: 对比真实发帖版本和草稿版本，整理差异、归因和下次要改的工作流。用户提到复盘、归因、为什么最后发成这样、发布后总结、真实帖子和草稿差异、更新创作方法时，务必使用这个 skill。输出具体可执行的规则，不写空泛总结。
---

# XHS Publish Review

这个 skill 只做发布后复盘。

目标不是夸哪版更好，而是回答：
- 最后为什么会改成这样
- 哪些改动提升了帖子
- 哪些风险是被埋进去的
- 下次工作流该怎么拆

## 什么时候用

- 用户给了真实发文链接
- 用户要对比草稿和发布版
- 用户要总结这轮循环
- 用户要把经验写回 skill

## 如果资料不完整

- 如果公开笔记页打不开，但有截图：
  先做 `截图版复盘`，明确说明证据只来自可见页面
- 如果没有草稿文件，但有对话或 post workspace：
  先重建”原草稿意图”，再和发布版比
- 如果只有发布版，没有草稿也没有截图：
  先做 `单边复盘`，重点放在发布版结构和可改进点，不要假装知道修改过程

## 工作流

### 1. 先对齐两份东西

- 草稿版本
- 真实发布版本

如果有图片，也要看图，不只看文案。

### 2. 差异分三类

- 文案差异
- 图片差异
- 流程差异

复盘时额外检查：
- 英文是不是比真正必要的更多
- 不懂这项运动的人，是否能在前两段看懂帖子在讲什么

### 3. 每条差异要有归因，不只描述

- 不要写："发布版更短"
- 应该写："为什么更短 → 读者扫读；好处 → 更适合小红书节奏；代价 → 少了 X 层深度"

### 4. 必须反哺工作流

- 这次哪一步应该更早做
- 这次哪一步非人来不可
- 这次哪一步可以独立成 skill

### 5. 复盘必须存档

- 每次复盘都必须把结果保存成文件，不只留在聊天里
- 默认路径：
  `reviews/<publish-date>-<slug>.md`
- 如果已经有对应 post workspace，再额外镜像到：
  `demo_posts/<date>-<slug>/reviews/<publish-date>-publish-review.md`
- 如果还没有对应 post workspace，先写根目录 `reviews/` 的摘要，再决定是否补工作区
- 如果这次暴露的是叙事结构问题，要把可复用的假设同步到仓库根目录 `hypo.md`
- 完成线上发布版复盘后，还要同步更新：
  `reviews/published-history.md`
- 复盘文件里要能看懂：
  - 原草稿想讲什么
  - 发布版最后讲成了什么
  - 下次该提前在哪一步锁住"只讲一个故事"

### 6. 已发布历史要和复盘绑定

- `published-history.md` 不是单独维护的流水账，必须在复盘完成后一起更新
- 每次至少补齐这些字段：
  - publish date
  - title
  - public note URL
  - note id
  - local workspace
  - durable review path
- 如果这篇还没有本地 post workspace，要在历史表里明确写 `待补本地 post workspace`
- 如果这篇已经有 workspace，优先保证 `published-history.md`、`reviews/`、`demo_posts/<slug>/reviews/` 三者能互相对上

### 6. 已发布历史要和复盘绑定

- `published-history.md` 不是单独维护的流水账，必须在复盘完成后一起更新
- 每次至少补齐这些字段：
  - publish date
  - title
  - public note URL
  - note id
  - local workspace
  - durable review path
- 如果这篇还没有本地 post workspace，要在历史表里明确写 `待补本地 post workspace`
- 如果这篇已经有 workspace，优先保证 `published-history.md`、`reviews/`、`demo_posts/<slug>/reviews/` 三者能互相对上

## 输出格式

```markdown
## 差异清单
### 文案
- 差异：
- 归因：
- 小白可读性：
- 下次规则：

### 图片
- 差异：
- 归因：
- 小白识别度：
- 下次规则：

### 流程
- 差异：
- 归因：
- 下次规则：

## 新的工作流
1. ...
2. ...
3. ...

## 必须人工介入的点
- ...

## 假设更新
- 新增：
- 验证：
- 否决：
- 下次要测：

## 发布历史登记
- Publish date:
- Title:
- Public note URL:
- Note ID:
- Workspace:
- Review:
- Notes:
```

## 不要这样做

- 不要只说"整体更好"
- 不要只复盘正文，不看图片
- 不要把问题归咎成"模型不行"
- 不要复盘完却不改工作流

## 快速参考

- [references/review-example.md](./references/review-example.md)
  何时读：不知道一份好的发布复盘应该写到多具体时。

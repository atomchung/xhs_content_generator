# Style Selection Rules

双轴决策：**第一轴看题目类型 → 第二轴看调性**。

选风格不是唯一解。Agent 默认给一个首选 + 一个对照，只有在用户明确要「探索」或「不急着定稿」时才出完整 duo。

## 第一轴：这张图主要卖什么？

### 1. 卖人物（球星 / 运动员个人）

进第二轴（调性）：

| 调性信号 | 首选风格 | 对照风格 |
|---|---|---|
| **热血 / 动作强 / 对峙 / 情绪炸** | `Anime Cover` | `Game Cinematic` |
| **明星气场 / 商业新闻人物 / NBA 封面** | `Game Cinematic`（或 canonical comic break-out，见下方 NBA 备注） | `Anime Cover` |
| **文艺 / 故事 / 个人成长 / 慢读感** | `Watercolor Ink Sketch` ✅ | `Game Cinematic` |
| 🟡 致敬 / 退役 / 生涯回顾 | `Ink Wash Silhouette`（待测试） | `Watercolor Ink Sketch` |
| 拿不准 | `Game Cinematic`（账号默认） | — |

### 2. 卖结构 / 数据 / 商业

进第二轴：

| 调性信号 | 首选风格 | 对照风格 |
|---|---|---|
| **信息密度高 / 多元素 / 薪资 / 转播 / 扩军** | `Editorial Collage` | `Minimal Data Poster` |
| **极简 / 数字为主 / 规则解释** | `Minimal Data Poster` | `Editorial Collage` |
| 🟡 系列感 / 设计统一 / 一篇下的辅助图 | `Risograph Duotone`（待测试） | `Editorial Collage` |

### 3. 卖角色 / 轻梗

不进第二轴：

| 情境 | 首选 | 对照 |
|---|---|---|
| 吉祥物化 / 可爱 / IP 化尝试 | `Mascot Q` | `Anime Cover` |

## NBA 球员动作题的备注

[explorations/visuals/2026-04-19-nba-cover-style-research.md](../../../explorations/visuals/2026-04-19-nba-cover-style-research.md) 的 canonical comic break-out prompt 是 NBA 球员动作首图的**强首选**——它幹翻了 44 个 mutation。

但这不是硬性规定。Agent 可以：
- **默认**：NBA 球员动作题 → canonical comic break-out 作为首选
- **出两版**：用户说「这次换个调性试试」/「这人不适合 break-out」/「想看备选」，就出 canonical + 一个对照版（通常 `Game Cinematic` 或 `Anime Cover`）
- **完全换**：用户明确指定非 canonical，agent 直接按双轴走，但要口头提示「已放弃 canonical，推荐理由是 …」

## 如果拿不准

先问用户一题：**「这张图卖人物还是卖结构？」**

答案后再往第二轴走。如果仍然拿不准调性，默认：
- 人物题 → `Game Cinematic`
- 结构题 → `Editorial Collage`

## 待测试的新风格（2026-04-19 加入双轴，尚未实战）

追踪测试状态：[issue #16](https://github.com/atomchung/xhs_content_generator/issues/16)

- `Watercolor Ink Sketch` — 沙盒生成测试已过，小红书实战未验收
- `Ink Wash Silhouette` — 纸上备选，生成测试未跑
- `Risograph Duotone` — 纸上备选，生成测试未跑

未实战验收的风格不要直接推给用户当首选，可以在「出两版」场景中作为对照出现。

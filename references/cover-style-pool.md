# Cover Style Pool

账号封面风格池 + 双轴选择决策表。

更新于：2026-04-26

> **前置**：本文件不定义视觉宪法（在 `CLAUDE.md` 顶部）。这里只定义「在符合宪法的前提下，多种漫画子风格之间怎么选」。

## 风格池（状态机）

| ID | 名称 | 状态 | 体感 | 验收记录 |
|---|---|---|---|---|
| `canonical-breakout` | 3D 漫画破框 | ⭐ canonical | 高张力、立体破框、爆发瞬间 | 4-19 研究 44 轮 mutation 全败 |
| `slam-dunk-classic` | 灌篮高手原作风 | 🟢 live-tested | 90s 少年漫、热血、群像 | 多篇实战 |
| `slam-dunk-movie` | The First Slam Dunk 电影版 | 🟡 sandbox | CG + 手绘墨线、致敬感、安静 | 待实战 |
| `100m-poster` | 100 公尺日漫电影海报 | 🟡 sandbox | 朱红 + 单 hero + 巨型 motion-blur 标题 | 道奇日本队 v9 验证中 |
| `watercolor-ink` | 水彩淡墨速写 | 🟡 sandbox | 抒情、个人成长、profile | 单张沙盒过 |
| `ink-wash-silhouette` | 水墨剪影 | 🔬 explore | 东方致敬、退役 | 纸上备选 |
| `risograph-duotone` | 拟印双色叠印 | 🔬 explore | 系列感、设计感 | 纸上备选 |
| `mascot-q` | Q 版棒球吉祥物 | 🟢 live-tested | 萌、轻知识、辅助图 | 多次使用 |

### 状态定义

| 状态 | 含义 | 推进条件 |
|---|---|---|
| 🔬 explore | 假设 + 单张测试 | agent 自动跑 |
| 🟡 sandbox | 5-8 张稳定，等实战 | agent 排单 |
| 🟢 live-tested | 实战 1+ 篇验收 | publish-review 回写 |
| ⭐ canonical | 多篇稳定，金本兜底 | 人确认 |
| ❌ retired | 失败 / 重复 / 不合账号 | 移出双轴树 |

## 双轴决策表（题型 × 情绪）

```
                  高张力 / 爆发                 抒情 / 安静
              ┌─────────────────────┬───────────────────┐
人物动作题    │ ⭐ canonical-breakout │ watercolor-ink     │
（NBA / MLB） │   slam-dunk-classic  │                    │
              ├─────────────────────┼───────────────────┤
群像 / 系列   │   slam-dunk-classic  │ risograph-duotone  │
              │   100m-poster        │                    │
              ├─────────────────────┼───────────────────┤
商业 / 数据   │   100m-poster        │ risograph-duotone  │
              │   canonical-breakout │                    │
              ├─────────────────────┼───────────────────┤
致敬 / 退役   │   slam-dunk-movie    │ ink-wash-silhouette│
              ├─────────────────────┼───────────────────┤
轻知识 / 辅助 │   mascot-q           │ mascot-q           │
              └─────────────────────┴───────────────────┘
```

## 选择算法（agent 跑的逻辑）

1. 先判**题型**：动作 / 群像 / 商业 / 致敬 / 轻知识
2. 再判**情绪**：高张力（冲突 / 突破）vs 抒情（怀念 / 个人成长）
3. 落到双轴单元格 → 默认推第一个 ⭐
4. 如果用户已说「这次想要 X 风格」→ 直接走 X
5. 如果格内有 🟡 / 🔬 → 顺手生成 1 张供选（同时跑沙盒验证）
6. 不确定时，默认回到 `canonical-breakout`（金本兜底）

## 升级 / 降级条件

- 🔬 → 🟡：5-8 张沙盒稳定（同主角换动作 / 同动作换主角）
- 🟡 → 🟢：1 篇实战发布，CTR 不差于 canonical
- 🟢 → ⭐：3+ 篇实战稳定，且账号可识别度提升
- 任意级 → ❌：连续 3 次用户驳回 / 实战 CTR 显著低于 canonical

## 探索 → 验证 → 确认 Loop

新风格走固定 4 stage：

```
[explore]    单张假设测试       → explorations/visuals/
   ↓
[sandbox]    5-8 张稳定测试     → evals/<style>/
   ↓
[live-test]  实战发布 1+ 篇     → reviews/YYYY-MM-DD-*.md（diff 真实 vs 草稿）
   ↓
[canonical]  3+ 篇稳定，进默认池
```

每跑完一 stage，回写本表的状态字段 + 验收记录列。

## 平行规则（无论选哪条线）

- 真人脸要像本人，但漫画化（视觉宪法第 2 条）
- final prompt 禁 photoreal 关键词（视觉宪法第 3 条）
- 真照只取文字形容词，写进 fact_pack 的 `## Visual Anchors`
- 必须含 `--ar 3:4 --stylize 250`
- 标题来自成稿，不在封面步骤重想（每行 ≤ 8 字，最多 2 行）

## 相关文件

- 视觉宪法：`CLAUDE.md` 顶部
- 账号默认封面结构：`notes/account-default-cover-and-intro-style.md`
- canonical 完整 prompt：`explorations/visuals/2026-04-19-nba-cover-style-research.md`
- 风格 spec / prompt 模板：`skills/xhs-image-style-duo/references/style-profiles.md`
- 验收 tracker：GitHub issue #16

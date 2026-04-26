# Title — 经验证规则

来源：`xhs_autoresearch/title_autoresearch_summary.md` + `RESEARCH_LOG.md`
实验规模：单话题 20 轮 + 跨 5 话题 16 轮 mutation = 80+ 次 A/B
验证日期：2026-04-05 / 2026-04-06

## ⭐ S-tier 规则（仅 2 条通过 20 轮筛选）

### 1. 标题必须含具体数字
- 验证：单话题 R1 4:5 wins / 跨话题 `add_number_requirement` 7 试 4 接受 = **57% 跨话题最强**
- 例：「Curry 傷停 57 天的帳單」/「克拉克薪水暴漲 7 倍」
- 数字越具体越好，避免「很多」「几个」「不少」

### 2. 反问句开头
- 验证：R4 4:5 wins
- 例：「誰是 NBA 最貴的膝蓋？」
- 反问句 + 数字双重组合是 Curry 那篇的护城河

## 🟢 A-tier 规则（跨话题验证）

### 3. change_skeleton（换标题骨架）
- 跨话题 14 试 6 接受 = 43%
- 高频可用，效果稳定
- 例：「X 是怎么 Y 的」→「Y 之后，X 还在 Z」

### 4. swap_emoji
- 跨话题 8 试 3 接受 = 38%
- emoji 上限 2 个（用户校准）
- 选和标题语义匹配的图像 emoji，不用 ①②③

### 5. change_drive_words（换驱动词）
- 跨话题 8 试 3 接受 = 38%
- 例：把「上涨」换「暴涨」/「分析」换「拆账」

## 🟡 B-tier（边缘有效）

| Mutation | 跨话题 | 备注 |
|---|---|---|
| inject_top_performer_emphasis | 25% | 边缘 |
| adjust_tone | 25% | 边缘 |

## ❌ 不要再试

### 死亡 mutation
- **adjust_char_count**：跨话题 13 试 0 接受 = 0%（死亡，从池中移除）
- change_hook_style：12 试 2 接受 = 17%（过度使用，低 ROI）

### 单话题验证全败 18 种（不再列入策略池）
- emotional_trigger / shorten_title / bracket_format / timeliness / prediction
- increase_emoji / human_angle / storytelling / contrast_structure / insider_tone
- money_angle / cultural_bridge / paradox / second_person / colloquial
- list_hint / remove_emoji / mini_narrative

## 标题护城河三元素（来自 Curry 那篇 winner）

```
🏀 誰是 NBA 最貴的膝蓋？Curry 傷停 57 天的帳單來了
   ─────────  ────────  ─────────────────  ──────
   反问句开头 + 原创概念  + 具体数字        + 信息落差
```

护城河组成：
1. **原创概念**（「最貴的膝蓋」）— 不能照搬通用词
2. **反问句**（4:5 验证）— 制造知识缺口
3. **具体数字**（4:5 验证）— 提升可信度
4. **信息落差**（「帳單來了」）— 让读者觉得「读完才能知道」

## 用户评分校准（重要）

- **文字流畅度是必要维度**（用户 R10 因「绕口」选了系统判输的 B）
- emoji 上限 2 个
- 可及性判断要更严格

## 话题类型 × 策略

| 话题类型 | 验证强势 | 注意 |
|---|---|---|
| 商业 / 数据题（Messi / Clark）| add_number_requirement 50% / 31% | 强制数字 |
| 个人成就（Ohtani）| 接受率较低 25% | baseline 已强 |
| 中国选手（鄭欽文）| 0% 接受 | baseline 已是局部最优 |
| 高数据反差（F1）| 38% | 数字 + 反问 |

## 写标题 checklist

发布前确认：
- [ ] 标题含具体数字（57 天 / 7 倍 / 1.5 亿）
- [ ] 含反问句或信息落差钩子
- [ ] emoji ≤ 2 个，且语义匹配
- [ ] 不绕口（人工读一遍）
- [ ] 有原创概念词，不是通用词组合

## 与 body / angle 规则的联动

- 标题数字 ↔ body 模块数字（不可移除）
- 标题反问 ↔ body mystery arc（先埋谜题）
- 标题原创概念 ↔ body 收口的 A/B/C 选项 C（呼应标题，首尾闭环）

# Angle Selection — 经验证规则

来源：`xhs_autoresearch/angle_autoresearch_summary.md` + `appendix.md`
实验规模：Pistons 30 轮 + Ohtani 跨话题 20 轮 = 50 次 A/B
验证日期：2026-04-06

## R30 后的最终 Baseline 配置

| 参数 | 最终值 | 验证轮次 |
|---|---|---|
| Audience Lens | **knowledge_collector** | R01→R16 |
| Emotion Driver | **CURIOSITY** | 5 次替换全失败 |
| Angle Type | **MYTH_BUSTING** | R03→R12 |
| Controversy | **OPTIONAL** | toggle MANDATORY 失败 |
| Specificity | **medium** | R05→R13 |
| Angle Count | **3** | 改 2 / 4 都失败 |
| Social Currency | **必有**（R7 加入，R27 验证不可移除）| ⭐ |
| Why Now | **evergreen_with_hook** | R14 |
| Extensibility | **必有**（R9 加入，R28 验证不可移除）| ⭐ |
| Number Anchoring | **必有**（R19 新加）| ⭐⭐ |
| Contrast Framing | **必有**（R23 新加）| ⭐⭐ |
| Hook Sentence | **必有**（R26 新加）| ⭐ |
| One-Sentence Takeaway | **必有**（R30 新加）| ⭐ |

## ⭐⭐ 100% 胜率 mutation（一次试一次过）

| 策略 | 胜率 | 何时加 |
|---|---|---|
| add **number_anchoring** | 5:1（R19）| 切角必含可量化数字 |
| add **contrast_framing** | 5:1（R23）| 切角必含「X vs Y」对比 |
| add **hook_sentence** | 4:2（R26）| 切角→成品转化率提升 |
| add **one_sentence_takeaway** | 4:0（R30）| 完整闭环 |
| toggle **social_currency** add | 5:1（R7）| 全场最强 |
| toggle **angle_extensibility** add | 4:2（R9）| |
| change_specificity_level | 100%（2 试 2 中）| 调粒度 |

## ⭐ 验证好的方向变更

### Audience Lens 演化
```
casual_fan ──R01──▶ business_curious ──R16──▶ knowledge_collector ✅
```
- R22 试 china_relevance ❌（稀释国际差异化）
- R11 试 drama_seeker ❌（TIE）

### Angle Type 演化
```
MONEY_TRAIL ──R03──▶ HIDDEN_WINNER ──R12──▶ MYTH_BUSTING ✅
```
- R18 试 PERSON_REWRITES_SYSTEM ❌（偏离冷知识）
- R21 试 COUNTDOWN ❌（投机感）

### Specificity 演化
```
ultra_narrow ──R05──▶ macro_zoom ──R13──▶ medium ✅
```

## 跨话题验证（Pistons → Ohtani 65% 接受率）

Ohtani 50-50 题接受率 65% 远高于 Pistons 43%，因话题类型不同（个人成就 vs 团队商业）。
**结论**：每个新话题类型都要重新探索 audience / angle_type / specificity 这三个参数。

跨话题新加的 mutation：
- **cultural_bridge**（6:0）— 个人成就型话题独有
- **visual_storytelling**（6:0）— 个人成就型
- **cross_domain_analogy**（6:0）— 跨领域类比

## ❌ 持续失败 mutation

| 策略 | 5 试 0 接受 | 失败原因 |
|---|---|---|
| **change_emotion_driver** | 0% | CURIOSITY 是品牌护城河，换 OUTRAGE / SCHADENFREUDE / FOMO / EMPATHY / AWE 全败 |
| change_angle_count（3→2 / 3→4）| 0% | 3 是最优 |
| toggle_controversy MANDATORY | 0% | 降低互动 |
| add prediction_element | TIE | 预测伤信誉 |
| add anti_cliche_filter | 1:5 | 过度学术化 |

## 切角决策 checklist

每次切角前过这 7 条：
- [ ] Audience = knowledge_collector（追求收藏价值的读者）
- [ ] Emotion driver = CURIOSITY（不是愤怒、不是 schadenfreude）
- [ ] Angle type = MYTH_BUSTING（拆解常识误解）
- [ ] Angle count = 3
- [ ] Specificity = medium（不要 ultra_narrow，也不要 macro_zoom）
- [ ] 含 social_currency（读者会想转发的「冷知识」）
- [ ] 含 number_anchoring + contrast_framing + hook_sentence + one_sentence_takeaway

## 切角生成模板（R30 baseline 整合）

```
【话题】X
【受众】knowledge_collector — 追求高密度冷知识可收藏
【调性】CURIOSITY — 制造知识缺口，不是愤怒/同情
【角度类型】MYTH_BUSTING — 拆解一个常识误解
【粒度】medium — 不要太窄也不要太广
【时间锚】evergreen_with_hook — 长期成立但有近期触发点

输出 3 个切角，每个含：
- hook_sentence（一句钩子）
- number_anchor（一个具体数字）
- contrast_frame（X vs Y 对比）
- social_currency（读者转发会显得懂行的点）
- extensibility（这条能延伸成系列吗）
- one_sentence_takeaway（一句话总结）
```

## 与 title / body 规则的联动

- angle 的 `number_anchoring` ↔ title 的具体数字 ↔ body 的模块数字
- angle 的 `contrast_framing` ↔ body 的对比开场（仅适合特定话题）
- angle 的 `hook_sentence` ↔ title 的反问句 ↔ body 的 mystery arc
- angle 的 `one_sentence_takeaway` ↔ body 的 A/B/C 选项 C（呼应标题）

## 待跑实验

- 跨话题验证 contrast_framing / hook_sentence / one_sentence_takeaway 是否泛化
- knowledge_collector audience 在轻知识题之外的话题（致敬 / 个人成长）是否成立
- evergreen_with_hook 在硬新闻题（突发交易 / 突发伤病）的表现

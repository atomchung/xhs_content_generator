# Four Kings Playoffs 封面 prompt 美感迭代笔记

> 来源：`demo_posts/2026-04-11-four-kings-playoffs/`（分支 `claude/brainstorm-new-problems-l8IPa`，未合回 main）
> 原始 post-mortem：[issue #8](https://github.com/atomchung/xhs_content_generator/issues/8)
> 落盘日期：2026-04-20

---

## 背景

这一篇做的是「季后赛四大天王」（SGA / Jokic / Wemby / Tatum）—— 一张封面 + 四张人物角色卡。封面经历 4 版、SGA 卡经历 4 版迭代才定稿，过程中暴露了几个「怎么写 prompt 才能让 AI 画出你脑中画面」的认知差异。这份文件把经验沉淀下来作为以后多人物封面和角色卡的参考。

## 原始素材链接

四张卡 + 封面的最终定稿 prompt 活在 brainstorm 分支：

- [01-cover.md](https://github.com/atomchung/xhs_content_generator/blob/claude/brainstorm-new-problems-l8IPa/demo_posts/2026-04-11-four-kings-playoffs/prompts/01-cover.md)
- [02-sga.md](https://github.com/atomchung/xhs_content_generator/blob/claude/brainstorm-new-problems-l8IPa/demo_posts/2026-04-11-four-kings-playoffs/prompts/02-sga.md)
- [03-jokic.md](https://github.com/atomchung/xhs_content_generator/blob/claude/brainstorm-new-problems-l8IPa/demo_posts/2026-04-11-four-kings-playoffs/prompts/03-jokic.md)
- [04-wemby.md](https://github.com/atomchung/xhs_content_generator/blob/claude/brainstorm-new-problems-l8IPa/demo_posts/2026-04-11-four-kings-playoffs/prompts/04-wemby.md)
- [05-tatum.md](https://github.com/atomchung/xhs_content_generator/blob/claude/brainstorm-new-problems-l8IPa/demo_posts/2026-04-11-four-kings-playoffs/prompts/05-tatum.md)

---

## 六条美感原则

### 1. 「放大」≠ 「特写」

最容易踩的认知偏差。SGA 卡 v3 → v4 就卡在这一句。

- 用户说「脸占 20%」 → 直觉翻译成 `face-dominant portrait` → **生成出大头照** ❌
- 实际意思：保留完整动作张力，只是镜头拉近一档，头部**因为整体放大**而自然变大 ✅

Prompt 措辞差异：

| 错 | 对 |
|---|---|
| `face-dominant portrait` | `the WHOLE figure scaled up so the head naturally enlarges — NOT a face close-up` |
| `crop to face` | `zoom in one notch on the full action` |

**判断标准**：如果用户在谈「动作张力」或「完整 apex」，但又说「脸要大」，几乎一定是要整体放大而不是特写。反问一句确认。

### 2. Stats 是配角

SGA 卡的 stats 做了三轮减法：

```
v1: 场均 31.4 / 55.3% FG / 连续 138 场        → 数据报表，太重
v2: 🏆冠军×1 / 🏆MVP×1 / 🏆得分王×1（黑底 panel）→ 格式对了，框太重
v3: 🏆冠军×1 / MVP×1 / 得分王×1（浮动文字，无框）  → ✅
```

原则：**stats 不能抢人物的视觉重量**。

- 数据报表 → emoji + panel → 浮动发光文字（最轻）
- 三个 emoji → 一个 emoji（最高荣誉才配）
- 有框 → 无框

### 3. Emoji 克制

- 标题允许 1-2 个 emoji 开头
- 正文 2-4 个，放模块开头或关键数字前
- 图上只在最高荣誉（冠军）用一个
- emoji 是叙事工具（🔍📈💸 = 谜面 / 揭答 / 金钱逻辑），不是装饰

### 4. 动作服务叙事

Tatum 最后从 step-back 三分改成**防守站位**，因为标题是「无私复出｜攻防一体」。叙事核心是「他不是回来抢分的，是回来防守的」。

四张卡的动作差异化（最终版）：

| 球员 | 动作 | 为什么 |
|---|---|---|
| SGA | 冷冷走开（cold walk-off） | 得分机器气场，不需要动作 |
| Jokic | No-look pass | 传球 / 全能中锋 |
| Wemby | Wingspan intimidation pose | 防守 / 外星人 |
| Tatum | 防守站位 / 怒吼庆祝 | 攻防一体、归来者 |

**两攻两守，零重复**。不是谁最帅画谁，是标题说什么就画什么。

### 5. 多角色必须逐人写死差异化动作 + 排除句

封面 v3 之所以失败：同模板 × 四人 → AI 把四人都画成正面跳投。`{player}` 变量换了，但「什么动作」没写死，AI 默认用最熟的动作补齐。

**两个工具必须一起用**：

**（a）每人写死一个独特动作**
```
- SGA: post-make COLD WALK-OFF
- JOKIC: NO-LOOK PASS
- WEMBY: WINGSPAN INTIMIDATION POSE
- TATUM: ROARING CELEBRATION
```

**（b）用排除句明确否定最熟的默认动作**
```
NO ball in frame. NO arms raised in shooting motion.
Do not draw any of them in a frontal-shooting pose.
Do not show any of them holding a ball above their head.
```

在 v4 的实际 prompt 里，还加了 `POSE DIFFERENTIATION ENFORCEMENT` 段在 prompt 尾部再 enforce 一次四人动作不能重复。这一层 redundancy 是必要的。

**这条是唯一进 skill 硬规则的一条**（见 `skills/xhs-image-style-duo/SKILL.md` 的「多角色封面硬规则」段）。

### 6. 改完要给 prompt

每次 prompt 改动都要落盘 + commit + push + 给 GitHub URL，聊天只出摘要不贴全文。这条已经在 issue #7 / commit `5916b75` 处理掉，现在走 `scripts/stage_prompt.py`。

---

## 提示词词表（可复用）

### 放大相关
- ✅ `the whole figure scaled up so the head naturally enlarges`
- ✅ `zoom in one notch on the full action`
- ✅ `medium-chest-up framing, not a portrait crop`
- ❌ `face-dominant portrait`
- ❌ `crop to face`
- ❌ `headshot close-up`（除非真的要大头照）

### 多人物区分
- ✅ `pose differentiation enforcement: no two figures may share the same action type`
- ✅ `CRITICAL POSE DIFFERENTIATION RULE: the [N] players must NOT all be doing the same action`
- ✅ `{player A}: {action A}. {player B}: {action B}. ...`（表格化指定）
- ❌ 同模板 × 多 `{player}` 变量（会撞 mode collapse）

### Stats 呈现
- ✅ `floating glowing text in the corners, no frame, no panel`
- ✅ `one emoji for top honor only`
- ❌ `stats panel with black background and gold border`（太重）
- ❌ `stat sheet layout`（像数据报表）

---

## 何时调用这份笔记

下次遇到以下场景时 Read 这个文件：

1. 多人物封面（2 人以上同框） → 直接跳到「第 5 条」
2. 角色卡 / 人物介绍卡，用户说「脸要大一点」→ 先确认是不是「整体放大」，跳到「第 1 条」
3. 图上带 stats 的封面 → 跳到「第 2 条」
4. 系列帖子用同模板套多人 → 警告，跳到「第 5 条」
5. 动作选择拿不准 → 回标题找叙事核心，跳到「第 4 条」

不是每次生图都要读这份文件。只有撞到以上 5 个场景之一再回来看。

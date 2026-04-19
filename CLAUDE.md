# Claude Code 协作规则

## Prompt 输出规则（硬规则，不要偷步骤）

### 核心闭环：编辑 prompt → stage_prompt.py → 在聊天给摘要 + URL

每次编辑 / 新增 prompt 文件后，**必须**立即跑：

```bash
python scripts/stage_prompt.py <文件路径>
# 多个一起也行：
python scripts/stage_prompt.py path1.md path2.md -m "prompts: tatum v5 defense pose"
```

脚本会自动 `git add → commit → push`，并把当前 branch 上的 GitHub blob URL 印出来。**把脚本印出的 URL 直接贴进聊天**，不要自己手拼。

然后在对话中输出：

1. **摘要**（不是全文）：
   - 版式 / 构图（layout、分区比例、几个模块）
   - 人物动作（什么招式、身体姿态、镜头角度）
   - 风格（如果非预设 canonical style，写清楚走哪个风格包和为什么）
   - 本次改了什么（和上版的 diff 要点）
2. **GitHub 链接（必须是 stage_prompt.py 印出的那条）**：用户点进去、拉到 ```` ```text ``` ```` 代码块复制 Final Prompt 去生图
3. **不要贴完整 prompt 全文**：省 output tokens，完整内容通过链接查看

### 落盘位置（prompt 文件命名惯例）

- 位置：`demo_posts/<date>-<slug>/prompts/`
- 命名：`cover_prompt.md`、`page2_prompt.md`、`page3_prompt.md` …
- 文件结构（最小集）：
  ```markdown
  # <标题或主角> 封面 prompt

  ## 推荐风格
  - 风格：
  - 为什么选它：
  - 这张图最该卖什么：

  ## Final Prompt

  ```text
  （能直接贴到 Midjourney / Sora / ChatGPT 的一整段 prompt）
  ```

  ## 如果要继续改
  - 背景优先改什么：
  - 不要动什么：
  ```

### 示例输出格式

```
**SGA 介绍卡 v4**

构图：3:4 竖版，人物整体放大撑出画布（脸自然占 ~20%），中央一条黑底金边标题横带，stats 以浮动发光文字贴在画面角落（无框）。

动作：中距离急停后仰跳投 apex — 双脚离地、身体后仰、出手臂完全伸直、球在画面最顶边。

风格：canonical comic break-out prompt（photorealistic foreground transition）。

改动：把"大头照"改回完整动作，强调 scale up whole figure ≠ face close-up。

Prompt: https://github.com/atomchung/xhs_content_generator/blob/<branch>/demo_posts/2026-04-11-four-kings-playoffs/prompts/02-sga.md
```

### 绝对禁区

- **不要把 Final Prompt 的完整文本贴进聊天**。即使只有几行也不贴，一律让用户从 GitHub 链接去复制。原因：保证单一 source of truth 是落盘版本，避免用户复制到的是聊天里某个过时片段。
- **不要在没 push 的情况下给 URL**。stage_prompt.py 没跑完就不能说「Prompt 链接：…」，否则用户点进去是 404。
- **不要只在聊天给 prompt 而没落盘**。如果聊天里讨论出一版 prompt，下一步就是 Write 到 `demo_posts/<slug>/prompts/<name>_prompt.md` 再跑 stage_prompt.py。讨论稿不是交付稿。

## 其他规则

- 编辑 prompt 以外的一般文件后，默认也 commit + push 一次，让分支状态和聊天记录一致
- 每次 commit message 简要说明改了什么
- Wemby 的本季数据（得分/篮板/盖帽）为预估值，生图前需替换为实际数据

## 生图铁律（2026-04-19 研究后锁定）

### 风格：NBA 动作题 canonical 是首选，不是唯一解

NBA 球员动作封面的**默认首选**是 canonical comic break-out prompt，来源：
- `explorations/visuals/2026-04-19-nba-cover-style-research.md`（44 个 mutation 全败的实验记录）

### 两种情境

**情境 1：默认走 canonical（NBA 动作题、时间紧、没有特殊调性需求）**
- 只替换 `{PLAYER_NAME}` 和 `{ACTION_PHRASE}` 两个变量
- 保留 `photorealistic foreground transition on the player`
- 必须含 `--ar 3:4 --stylize 250`
- canonical prompt 内部**不要**加 watercolor / aura / speed lines / beams / gold leaf / Chinese ink / Pop Art / geometric / blueprint / minimal / dark / moody —— 这些已实验验证会让画面更乱

**情境 2：脱离 canonical（非动作题、用户要换调性、或 agent 判断 canonical 不合适）**
- 走 `xhs-image-style-duo` 的双轴选风格逻辑（题目类型 × 调性）
- 合理的场景：球员故事 / 个人成长 → `Watercolor Ink Sketch`；致敬退役 → `Ink Wash Silhouette`（待测）；系列封面 → `Risograph Duotone`（待测）
- 如果不确定，**agent 可以出两版让用户挑**：canonical 一版 + 双轴推荐一版
- 口头提示用户「默认 canonical 是因为…，这次推荐脱离是因为…」

### 真人：必须先跑 Person Recognition Gate

任何 prompt 含真实人物（球员／艺人／政治人物／企业家／KOL）时，生成 prompt 前必须：

1. **读 rubric**：`references/person-confidence-rubric.md`
2. **对每个人物自评信心度 0-100**，输出 JSON：
   ```json
   {"person": "...", "confidence": 65, "tier": "MED", "reason": "...", "anchors_suggestion": "..."}
   ```
3. **根据 tier 行为**：
   - 🟢 HIGH (75+)：直接用名字
   - 🟡 MED (40-74)：自动加 `anchors_suggestion` 进 prompt + 对话中提示用户
   - 🔴 LOW (0-39)：**暂停**，要求用户确认是否跑 photo pipeline
4. **LOW 的 photo pipeline**：
   - 运动号优先 ESPN：`python scripts/fetch_player_photo.py --player "{name}"`
   - 其他领域 fallback Wikipedia API
   - 产物 embed 进 prompt 替代 anchors

### 决策参考（运动号常见）

| 人物类型 | Tier | 做法 |
|---|---|---|
| LeBron / Curry / Jokic 级 | 🟢 HIGH | 只写名字 |
| Rui Hachimura | 🟢 HIGH（实测 OK） | 只写名字 |
| Cade / Kennard 级轮换 | 🟡 MED | 加外貌锚点 |
| 大学球员／选秀生（Flagg / Bailey 等）| 🔴 LOW | **必跑 photo pipeline** |

# Claude Code 协作规则

## Prompt 输出规则（硬规则，不要偷步骤）

### 核心闭环：编辑 prompt → stage_prompt.py → 在聊天给摘要 + URL

每次编辑 / 新增 prompt 文件后，**必须**立即跑：

```bash
python scripts/stage_prompt.py <文件路径>
# 多个一起也行：
python scripts/stage_prompt.py path1.md path2.md -m "prompts: tatum v5 defense pose"
```

脚本会自动 `git add -f → commit → push`，并把当前 branch 上的 GitHub blob URL 印出来。**把脚本印出的 URL 直接贴进聊天**，不要自己手拼。

> `demo_posts/` 整体在 `.gitignore`，stage_prompt.py 会用 `-f` 强加。设计意图：**贴文内容和研究只存活在 session 分支上，不 merge 进 main**。所以 prompt / post / research 都可以推到分支让用户从 URL 读，但不要把 `demo_posts/` 下的任何东西开 PR 进 main。跨贴的可复用经验要另外落到 `hypo.md` / `reviews/` / `notes/` 这些 tracked 文件。

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

风格：canonical 3D comic break-out（physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration — not photo）。

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

## 账号视觉宪法（高于所有 skill 默认）

这三条凌驾于任何 skill 的默认风格：

1. **账号所有封面默认走漫画 / 卷封 / 名场面风格**。canonical 3D comic break-out 是当前金本，**适用全题型**（动作 / 商业 / 故事 / 致敬 / 系列）。NBA 动作题只是当初的验证场景，不是 scope 上限。
2. **真人题：脸要像本人，但渲染成漫画**。看得出是谁（Ohtani / Clark / Tatum），但视觉语言是漫画 / 卷封 / 名场面，不是 photoreal 照片，也不是萌系动漫脸。参考体感：灌篮高手 / 鬼灭电影版 / 100 公尺日漫海报。
3. **ESPN 真照只用来取「文字形容词」**。Read 图 → 写进 fact_pack 的 `## Visual Anchors` → final prompt 引用文字。**永远不在 final prompt 里 embed 照片 URL / `reference photo` / `photorealistic` / `studio photo` / `8k photoreal` / `octane render` 等关键词**。

## 生图铁律（2026-04-19 研究 + 2026-04-26 视觉宪法补充）

### 风格：canonical 3D comic break-out 是账号默认（全题型）

**默认首选**：canonical 3D comic break-out（来源：`explorations/visuals/2026-04-19-nba-cover-style-research.md`，44 个 mutation 全败的实验记录）。

虽然当时验证场景是 NBA 动作题，但符合视觉宪法第 1 条 — 适用全账号题型。

### 风格池与选择

封面风格池 + 双轴决策表见：`references/cover-style-pool.md`。

简化逻辑：
- 默认 → `canonical-breakout`
- 抒情 / 个人成长 → `watercolor-ink`
- 群像 / 90s 热血 → `slam-dunk-classic`
- 致敬 / 退役 → `slam-dunk-movie` 或 `ink-wash-silhouette`
- MLB / 商业题（高张力）→ `100m-poster`
- 系列 / 设计感 → `risograph-duotone`
- 轻知识 / 辅助图 → `mascot-q`

### canonical 措辞（旧词替换 — 不要再写 photorealistic）

**旧（已废）**：`photorealistic foreground transition on the player`
**新**：`physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo)`

prompt 内部 **绝对不要** 出现：`photorealistic` / `cinematic photoreal` / `studio photo` / `8k photoreal` / `octane render` / `reference photo`。也不要再加 watercolor / aura / speed lines / beams / gold leaf / Chinese ink / Pop Art / geometric / blueprint / minimal / dark / moody（实验验证会让画面更乱）。

必须含 `--ar 3:4 --stylize 250`。

### 真人：必须先跑 Person Recognition Gate

任何 prompt 含真实人物（球员／艺人／政治人物／企业家／KOL）时，生成 prompt 前必须：

1. **读 rubric**：`references/person-confidence-rubric.md`
2. **对每个人物自评信心度 0-100**，输出 JSON：
   ```json
   {"person": "...", "confidence": 65, "tier": "MED", "reason": "...", "anchors_suggestion": "..."}
   ```
3. **根据 tier 行为**：
   - 🟢 HIGH (75+)：直接用名字（默认会渲染成漫画，不会变 photo）
   - 🟡 MED (40-74)：自动加 `anchors_suggestion`（文字外貌）进 prompt
   - 🔴 LOW (0-39)：**暂停**，要求用户确认是否跑 photo pipeline
4. **LOW 的 photo pipeline（按视觉宪法第 3 条）**：
   - 运动号优先 ESPN：`python scripts/fetch_player_photo.py --player "{name}"`
   - 其他领域 fallback Wikipedia API
   - **Claude 用 Read 看图 → 提取文字外貌 → 写进 fact_pack 的 `## Visual Anchors` 段**
   - **final prompt 只引用文字 anchors，不 embed 照片本身**

### 决策参考（运动号常见）

| 人物类型 | Tier | 做法 |
|---|---|---|
| LeBron / Curry / Jokic 级 | 🟢 HIGH | 只写名字 |
| Rui Hachimura | 🟢 HIGH（实测 OK） | 只写名字 |
| Cade / Kennard 级轮换 | 🟡 MED | 加文字 anchors |
| 大学球员／选秀生（Flagg / Bailey 等）| 🔴 LOW | 跑 photo pipeline → 提取文字 anchors（不 embed 照片）|

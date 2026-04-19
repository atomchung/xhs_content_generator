# Claude Code 协作规则

## Prompt 输出规则

编辑完 prompt 文件后，在对话中输出：

1. **摘要**（不是全文）：
   - 版式/构图概述（layout、分区比例、几个模块）
   - 人物动作描述（什么招式、身体姿态、镜头角度）
   - 本次改了什么（和上版的 diff 要点）
2. **GitHub 文件链接**：指向对应的 prompt .md 文件，用户自行打开复制 ```` ```text ``` ```` 代码块里的 Final Prompt
3. **不要贴完整 prompt 全文**：省 output tokens，完整内容通过链接查看

### 示例输出格式

```
**SGA 介绍卡 v4**

构图：3:4 竖版，人物整体放大撑出画布（脸自然占 ~20%），中央一条黑底金边标题横带，stats 以浮动发光文字贴在画面角落（无框）。

动作：中距离急停后仰跳投 apex — 双脚离地、身体后仰、出手臂完全伸直、球在画面最顶边。

改动：把"大头照"改回完整动作，强调 scale up whole figure ≠ face close-up。

Prompt 链接：https://github.com/atomchung/xhs_content_generator/blob/分支名/路径/02-sga.md
```

## 其他规则

- 编辑完文件后必须 commit + push，确保 GitHub 链接可访问
- 每次 commit message 简要说明改了什么
- Wemby 的本季数据（得分/篮板/盖帽）为预估值，生图前需替换为实际数据

## 生图铁律（2026-04-19 研究后锁定）

### 风格：一律用 canonical comic break-out prompt

任何 NBA 封面／图组生成，必须读：
- `explorations/visuals/2026-04-19-nba-cover-style-research.md`

硬性规则：
- 只替换 `{PLAYER_NAME}` 和 `{ACTION_PHRASE}` 两个变量
- **禁止**加入 watercolor / aura / speed lines / beams / gold leaf / Chinese ink / Pop Art / geometric / blueprint / minimal / dark / moody
- **禁止**去掉 `photorealistic foreground transition on the player`
- 必须含 `--ar 3:4 --stylize 250`

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

---
name: xhs-image-style-duo
description: 为已确定要生图的页面输出默认 `1` 个推荐风格和 `1` 条可直接贴到 ChatGPT / Gemini 等网页里的 final prompt。用户明确说要比较时，才输出 `2` 个风格候选。它负责风格延展，不负责整组图分工，也不负责默认首图结构。严禁默认走 API 生图。
---

# XHS Image Style Duo

## 开工前必读（2026-04-19 生图铁律）

在产出任何生图 prompt 前，**必须**做两件事：

1. **风格**：读 `explorations/visuals/2026-04-19-nba-cover-style-research.md`
   - NBA 图组一律用 canonical comic break-out prompt（只替换 `{PLAYER_NAME}` 和 `{ACTION_PHRASE}`）
   - 禁用词：watercolor / aura / speed lines / beams / gold leaf / Chinese ink / Pop Art / geometric / blueprint / minimal / dark / moody
   - 必保留 `photorealistic foreground transition on the player`

2. **真人辨识度 Gate**：读 `references/person-confidence-rubric.md`
   - 对 prompt 中每个真人自评信心度 0-100（输出 JSON）
   - 🟢 HIGH (75+)：直接用名字
   - 🟡 MED (40-74)：加 `anchors_suggestion` 进 prompt + 对话中提示
   - 🔴 LOW (0-39)：**暂停**，走下面的 photo pipeline

### 🔴 LOW-tier 的 4 步 photo pipeline（不允许跳步骤）

LOW 的处理方式不是「也许需要」，而是「必须跑完才能发 prompt」。完整流程：

1. **抓照片**
   ```bash
   # 运动号优先 ESPN：
   python scripts/fetch_player_photo.py "<Player Name>" \
     --espn-id <id> \
     --school <team> \
     --output references/players/<slug>

   # 批次：
   python scripts/fetch_player_photo.py --batch references/players/<manifest>.json
   ```
2. **Read 图**：Read `references/players/<slug>/espn_headshot.png`（+ `espn_action.png` / `wikipedia.jpg`）
3. **写 appearance.md**：Write `references/players/<slug>/appearance.md`，按 `references/players/README.md` 的 schema（髮型 / 髮色 / 膚色 / 臉型 / 臉部特徵 / 體型 / 招牌標記 + 一段 `Prompt 用描述`），信心度标「已確認」
4. **在 prompt 引用**：Read `appearance.md`，把「Prompt 用描述」代码块整段嵌入 Final Prompt 的人物描述段落

**复用规则**：`appearance.md` 已存在就直接 Read、不重跑脚本。照片被 `.gitignore` 掉不进版控，appearance.md 是金本一人一次就够。

**手动 fallback**：网络受限时用户手动把照片存到 `references/players/<slug>/`，AI 一样 Read → 写 appearance.md。Step 2-4 不变。

违反这两条铁律前请先 stop 并询问用户。

---

## 交付闭环（硬规则，不允许偷步骤）

每产出一个 prompt，必须走完这三步。只走一两步不算交付。

### 步骤 1 — 落盘到 `demo_posts/<slug>/prompts/`

- 位置：`demo_posts/<date>-<slug>/prompts/`（workspace 不存在就先用 `scripts/scaffold_post_folder.py` 建）
- 命名：`cover_prompt.md`、`page2_prompt.md`、`page3_prompt.md` …（多版本用 `cover_prompt_v2.md` 继续往上叠）
- 文件结构：推荐风格 / 5 项判断 / `## Final Prompt` 内含 ```` ```text ``` ```` 代码块 / 如果要继续改

### 步骤 2 — 跑 `stage_prompt.py` 一次做完 commit + push + 印 URL

```bash
python scripts/stage_prompt.py demo_posts/<slug>/prompts/<name>_prompt.md
# 多个一起也 OK：
python scripts/stage_prompt.py path1.md path2.md -m "prompts: <自定 message>"
```

脚本会 `git add → commit → push`，并按当前 branch 印出 GitHub blob URL。**URL 必须直接从脚本输出复制进聊天**，不要手拼。

### 步骤 3 — 聊天回复只给摘要 + URL，绝不贴全文

格式（照着 CLAUDE.md 的示例）：

```
**<标题/图名> v<版本>**

构图：<layout、分区比例、几个模块>
动作：<镜头、姿态、关键动作瞬间>
风格：<canonical break-out / A-E 风格包的名字；非预设要写为什么>
改动：<和上一版的 diff 要点；首次生成就写 v1 锚点>

Prompt: <从 stage_prompt.py 复制的 GitHub blob URL>
```

### 禁区

- **不要把 Final Prompt 的文本贴进聊天**（哪怕只有几行）。一律让用户点 URL 进去复制 ```` ```text ``` ```` 代码块。
- **不要在没 push 的情况下给 URL**。脚本没跑完 = 不允许说「Prompt 链接：」。
- **不要只在聊天给 prompt**。聊天讨论出一版 prompt，下一步必然是 Write 到 `demo_posts/<slug>/prompts/<name>_prompt.md` 再走步骤 2-3。讨论稿不是交付稿。

---

这个 skill 只做一件事：

把一个已经锁住任务的页面，变成 `可直接在网页聊天界面里使用的生图 prompt`。

默认交付不是“两套风格实验包”，而是：

- `1` 个推荐风格
- `1` 条 final prompt

只有用户明确说：

- “给我两个风格比较”
- “同一张图换两种方向看看”
- “我现在要探索，不急着定稿”

才进入 duo 模式，输出 `2` 条 final prompt。

## 默认交付原则

默认交付必须满足这 5 条：

- prompt 可以直接贴进 ChatGPT / Gemini 等网页
- prompt 本身不依赖 API 参数
- prompt 不混入流程说明、参考案例解释、上传图片说明
- 默认不调用图片 API，机器只负责产 prompt，不负责替用户发起生图
- **所有小红书封面和图组 prompt 必须指定竖版 `3:4` 比例**（小红书标准首图比例）

这个 skill 不负责决定整篇帖子该用真人图、官方截图还是生图。那一步交给 `xhs-visual-asset-mix`。  
如果是图 1 首图，但封面结构还没锁住，先回到 `xhs-cover-template` 或按 `README` 的主流程先锁首图结构。

## 什么时候用

遇到这些任务直接使用：

- 用户要生图 prompt
- 用户说“封面画风怎么定”
- 用户说“背景太乱”“动作没张力”“不像封面图”
- 用户说“同一张图换两种风格看看”
- 用户要更像动漫名场面 / 游戏动画 / 杂志拼贴 / 极简海报 / Q 版
- 用户想要一条可直接贴用的 final prompt

## 什么时候不要用

- 还没决定这张图是不是首图，先回到 `xhs-visual-asset-mix`
- 首图结构还没锁，先回到 `xhs-cover-template` 或 `xhs-note-assembly`
- 用户只是想长期探索视觉系统，还没落到某一页，优先放进 `explorations/visuals/`

## 先做 5 个判断

1. 这张图是不是首图
- 如果是首图，先确认封面结构已经锁住

2. 主角是谁
- 必须只有一个绝对主角

3. 这一张图最该卖什么
默认从下面选一个：
- 脸
- 动作
- 冲突
- 情绪
- 信息结构

4. 背景是不是稳定的
- 如果用户明显还在探索背景，先不要把背景写死

5. 这张图更适合哪种风格包
- 热血运动动画封面
- 欧美游戏动画电影感
- 体育商业杂志拼贴
- 极简数据海报
- Q 版吉祥物

如果读者不懂赛事或规则，画面里也要有足够明确的主角、冲突和信息锚点。  
图上可见文字是否真的需要，也要先判断；真正给用户看的角标和封面词，优先短中文。

## 内部生成顺序

内部可以按这个顺序想，但默认不要把全部中间层都交给用户：

1. 抽故事骨架
2. 锁主体锚点
3. 补背景层
4. 合成 final prompt

默认只把 `final prompt` 交付给用户。  
只有在调图阶段明确需要排查问题时，才额外展示：

- `story atoms`
- `subject anchor prompt`
- `background prompt`

## 风格包

### A. 热血运动动画封面

- 适合人物主角、情绪冲突、热血动作
- 更像运动番关键分镜，不是泛二次元

### B. 欧美游戏动画电影感

- 适合巨星、联盟变化、商业新闻人物题
- 更立体、更高级、更像高预算游戏动画 key art

### C. 体育商业杂志拼贴

- 适合转播、薪资、扩军、平台战争
- 用人物、数字、场馆、屏幕、剪报做高密度商业新闻海报

### D. 极简数据海报

- 适合规则、钱、结构变化
- 人物可以弱化，数字和信息结构更重要

### E. Q 版吉祥物

- 适合更轻一点、更可收藏、更偏角色化的题
- 不是普通 chibi，而是带运动语义的角色转译

默认优先级：

- 人物大新闻 -> `欧美游戏动画电影感` / `热血运动动画封面`
- 商业新闻 -> `体育商业杂志拼贴` / `极简数据海报`
- 轻松角色化 -> `Q 版吉祥物`

## 脚本使用规则

优先用脚本：

- [scripts/generate_style_duo.py](./scripts/generate_style_duo.py)

但这个脚本现在的职责是：

- 生成网页可直接使用的 prompt 文件
- 默认只输出 `1` 个推荐 prompt
- 用户明确要求比较时，才输出 `2` 个 prompt
- 不再默认走 API 生图

默认产物应该是：

- `final_prompt.txt`
- `web_prompts.md`

如果是比较模式，再额外输出：

- `style_1_final_prompt.txt`
- `style_2_final_prompt.txt`

## 存档约定

prompt 落盘路径和命名见顶部「交付闭环」步骤 1，不再重复。

额外约定（不走 stage_prompt.py，手动处理）：

- 用户手动跑出来的成图，建议放在 `demo_posts/<date>-<slug>/images/`，用 `cover.png` / `page2.png` / `cover_v2.png` 这种和 prompt 文件名能对得上的命名
- 同一篇贴文的图片实验不要散落到多个无关目录

## 输出格式

### 默认模式

```markdown
## 推荐风格
- 风格：
- 为什么选它：
- 这张图最该卖什么：

## Final Prompt
```text
...
```

## 如果要继续改
- 背景优先改什么：
- 不要动什么：
```

### 比较模式

```markdown
## Style 1
- 风格：
- 为什么选它：

## Final Prompt 1
```text
...
```

## Style 2
- 风格：
- 为什么选它：

## Final Prompt 2
```text
...
```

## 推荐
- 当前更推荐的是：
- 为什么：
```

## 快速参考

- [references/style-profiles.md](./references/style-profiles.md)
  何时读：要从风格包里挑主风格和备选风格时。

- [references/style-selection-rules.md](./references/style-selection-rules.md)
  何时读：不确定该优先选哪一个风格，或比较模式下该选哪两个时。

- [references/prompt-polish-rules.md](./references/prompt-polish-rules.md)
  何时读：用户说背景太乱、动作不够、脸不够像、Q 版不够可爱时。

- [references/output-evaluation.md](./references/output-evaluation.md)
  何时读：已经有两个 prompt，但不知道该继续哪一个时。

## 不要这样做

- 不要默认输出两种风格
- 不要默认把 `story atoms / subject anchor / background prompt` 全交给用户
- 不要把流程说明、参考案例、上传图片解释写进 final prompt
- 不要让 final prompt 依赖 API 参数才能使用
- 不要默认尝试 API 生图
- 不要先决定画风，再决定这张图要卖什么
- 不要先把背景写得比主角还重要
- 不要把可见文案默认写成英文大字

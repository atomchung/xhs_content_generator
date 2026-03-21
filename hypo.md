# XHS Storytelling Hypotheses

## Why This File Exists

- 这里不是存选题，而是存“什么叙事技巧更适合小红书”的可验证假设。
- 每次 publish review 都要把结构层面的经验回写到这里，而不是只停留在当次复盘。
- 目标不是把每篇都写成长文，而是用新闻写作、写书、storytelling 的方法，让贴子更像在讲一个故事，而不是在堆事实。

## Current Diagnosis

- 当前工作流在搜集论点、补数字、做图方面已经够强，但“只讲一个故事”的动作出现得太晚。
- `fact_pack` 容易把多个都成立的角度同时保留下来，等到发帖前才被迫删减，所以发布版常常比草稿更顺，但也更普通。
- 图片经常在替正文补故事，这说明正文主线没有提前锁死。
- 更好的小红书体育贴，通常不是信息更多，而是更早回答这三个问题：
  - 这篇到底在讲谁的变化？
  - 这篇到底让读者站在哪个冲突前？
  - 这篇读完后，读者要记住哪一句话？

## Story Lenses To Borrow

### 新闻写作

- 用一个具体事件或场景开头，而不是先讲结论。
- 在前两段交代 `发生了什么 / 为什么是现在 / 为什么值得看`。
- 把最强的“why now”尽量前置，不要藏到中段。

### 写书

- 一篇只回答一个中心问题，其他好材料先收进 side notes。
- 让事实像章节推进，而不是横向摆满。
- 节奏上要有“打开问题 -> 加压 -> 给出判断 -> 留一个余波”。

### Storytelling

- 明确主角是谁，他发生了什么变化。
- 冲突要能一句话说清楚。
- 结尾不是总结，而是让读者带着一个站队问题离开。

## Experiment Loop

1. 在每篇的 `research/story_spine.md` 先写一句话故事。
2. 从下面的 hypothesis board 里只选 1 到 2 条主假设，不要一篇同时试 5 招。
3. 在正文里明确哪些段落是在执行这条技巧。
4. 发布后先把摘要存到 `reviews/`，如果有 post workspace 再镜像到 `demo_posts/<date>-<slug>/reviews/`。
5. 从复盘里把结构经验回写到这里，更新状态是 `active`、`supported`、`mixed` 还是 `retired`。

## Success Signals

- 发布版是否还保留了原本选定的主判断。
- 不懂这项运动的人，前两段能不能说清楚“这篇在讲什么”。
- 图片是不是在补正文没讲清楚的故事。
- 收尾互动是不是围绕主冲突，而不是泛泛而问。
- 最终删改是不是主要在润色，而不是在临时换主线。

## Hypothesis Board

| ID | Technique | Lens | What Changes | Expected Gain | How To Check | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H01 | Single governing question | 写书 / 新闻 | 写前先回答“这篇只回答什么问题” | 减少中途换主线 | 发布版是否仍围绕同一冲突 | active |
| H02 | Scene then nut graf | 新闻 | 第一段给场景，第二段讲 why now 和判断 | 前两段更抓人，也更适合小白 | 前两段能否回答 `是什么 / 为什么现在 / 为什么要看` | active |
| H03 | Evidence staircase | 非虚构写作 | 事实按“最具体 -> 最系统 -> 最抽象”的顺序上楼 | 减少列表感 | 正文是否不需要靠额外图片补逻辑 | active |
| H04 | One role shift | Storytelling | 把主角变化写成叙事引擎 | 提升记忆点和情绪强度 | 标题、封面、正文是否都围绕同一变化 | active |
| H05 | Take-a-side ending | 小红书原生互动 | 结尾让读者站队，不做空泛总结 | 互动更自然 | 评论和互动是否围绕明确选项展开 | supported |
| H06 | Park side angles early | 编辑流程 | 在 `story_spine.md` 先停放副线，不写进正文骨架 | 减少发布前硬删 | 发布版是否只删细节，不删主论点 | active |

## Case Log

### 2026-03-20 Luka 60 Pts Aftermath

- Durable review:
  `reviews/2026-03-21-luka-60pts-trade-aftermath.md`
- Workspace:
  `demo_posts/2026-03-20-luka-60pts-trade-aftermath/`
- Review:
  `demo_posts/2026-03-20-luka-60pts-trade-aftermath/reviews/2026-03-21-publish-review.md`
- What we learned:
  - 原草稿最有辨识度的是“赔率错价 + 时代交接”，但发布版改成了“卢卡归位 + 球迷互动”。
  - 这说明 `H01` 和 `H06` 还没有被前置执行。
  - `H05` 在这篇上得到初步支持，因为站队式收尾比分析总结更像小红书。

## Working Rule Of Thumb

- 先写故事，再选事实，不要先把所有事实都端上来。
- 一篇里最多只保留一个主冲突和一个副冲突。
- 如果封面讲的是传承，正文前两段必须落一个硬事实。
- 如果正文讲的是赔率，至少一张图要把赔率当成信息本体来讲。

---
name: sync-skills
description: 将本地 `skills/` 相关改动安全同步到远端 GitHub。用户提到 `/sync-skills`、同步 skills、开新 branch、干净 commit、不要把 post 改动混进同一个 PR、把本地 skill 改动发到 GitHub 时，使用这个 skill。
---

# Sync Skills

这个 skill 只处理一件事：

把本地 skill 系统相关改动，用一个新的干净分支同步到远端 GitHub。

它不是用来发帖子，也不是用来顺手清理整个 worktree。

## 什么时候用

- 用户说 `/sync-skills`
- 用户说“帮我把 skills 同步到 GitHub”
- 用户说“开个新 branch 把 skill 改动发上去”
- 用户说“帮我拆干净一点，不要混太多内容”
- 用户说“当前 branch 很乱，不要直接在这上面 push”

## 默认目标

- 新开一个 sync branch
- 只带走这次要同步的 skill 系统改动
- commit 尽量小而清楚
- 最后 push，并走 draft PR

## 默认 scope

默认算在 sync 里的：

- `skills/`
- `README.md`
- `notes/skills-audit.md`
- `notes/local-filesystem-workflow.md`
- `notes/skills-process-simplification-review.md`

默认不算在 sync 里的，除非用户明确说要一起带：

- `demo_posts/`
- `explorations/`
- `reviews/`
- 发文草稿
- 与 skill 无关的零散 note

## 核心原则

### 1. 不要信任当前 branch

- 当前 branch 可能是发文分支、长命分支，或者已经混了别的事
- 默认不要直接把当前 branch 当成 sync branch
- 即使当前 branch 名字看起来合理，也先检查 diff，而不是直接沿用

### 2. 不要假设整个 worktree 都属于这次同步

- 先看 `git status -sb`
- 明确列出：
  - 哪些文件属于 sync scope
  - 哪些文件是明显无关的
- 不要因为 skill 文件在里面，就顺手 `git add -A`

### 3. 混乱工作区优先走隔离分支

如果当前 worktree 很混，默认做法是：

- 保持当前 checkout 不动
- 从远端默认分支开一个新的隔离工作区或隔离 branch
- 只把 in-scope 文件带过去

优先策略：

1. 确认远端默认分支
2. 基于 `origin/<default-branch>` 建新的 sync branch
3. 如果当前 checkout 很混，优先用临时 worktree 做这件事
4. 只复制本次要同步的文件，不清理用户原分支

### 4. commit 要按“一个意图”分组

默认分组：

- commit 1：`skills/` 本体规则改动
- commit 2：配套说明文档同步

如果这次其实只有一个完整小改动，也可以只保留一个 commit。

不要做的事：

- 不要把 skill 改动、发文草稿、backlog 清理混成一个 commit
- 不要顺手修 unrelated file
- 不要为了“看起来一次做完”把 commit 拉得过宽

### 5. 默认命名

- branch：`codex/skills-sync-YYYYMMDD`
- 如果主题很明确，可补一个短 slug
- commit：用短句写清这次同步在改什么

## 工作流

### 1. 先做 scope 盘点

- 运行 `git status -sb`
- 列出本次候选文件
- 标记哪些是 in-scope，哪些先排除

### 2. 再决定隔离方式

- 如果当前 checkout 干净，而且就是这次同步专用分支，可以直接继续
- 只要 branch/history/worktree 看起来有一点混，默认改走新 branch
- 如果本地未提交改动很多，优先用临时 worktree，从远端默认分支切新 branch

### 3. 只带走这次该同步的文件

- 优先显式指定文件
- 不要全量 stage
- 如果文档只是解释 skill 同步本身，可以和 skill 改动一起带
- 如果文档是在讲某篇帖子、某个探索主题，就先排除

### 4. 拆 commit

- 先看能不能用 `skill rules` 和 `workflow docs` 两组收住
- 如果拆了反而更碎，就收敛成一个 commit
- 每个 commit 都要能一句话说明“为什么这组文件必须一起出现”

### 5. 发布

- branch 和 commit 都干净后再 push
- push 后默认开 draft PR
- 最终发布动作优先复用 `github:yeet` 的安全做法

## 遇到这些情况要停一下

- 想同步的内容已经只存在于旧的混乱 commit 里，而不是当前文件差异里
- 当前分支相对默认分支已经带了很多无关 commit
- 用户想带进去的文件横跨 skill、post、review 三类不同工作

这时不要硬推。要先改成：

- 指定要 cherry-pick 哪些 commit
- 或在干净 branch 上重放这次真正想同步的文件改动

## 输出格式

```markdown
## Sync Plan
- Branch:
- Base:
- Included:
- Excluded:

## Commits
1. ...
2. ...

## Publish
- Push:
- Draft PR:
```

## 不要这样做

- 不要默认复用当前脏 branch
- 不要默认把所有 `notes/` 都带上
- 不要默认把 `explorations/` 和 `reviews/` 带上
- 不要为了省事直接 `git add -A`
- 不要在没有确认 scope 时 push

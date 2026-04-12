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

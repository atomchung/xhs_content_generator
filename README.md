# Dindin 圖文製作

這個 repo 保存小紅書圖文的研究、故事、正文、prompt、圖片與單篇復盤。唯一業務目標是帳號長粉。

帳號總入口在 [xhs-account](../README.md)；圖文與影片共用 [xhs_skills](../skills/README.md) 的四項創作能力：找題目、說故事、做好內容、復盤。另有獨立觀眾 reviewer，冷啟動、不同模型家族，作者不自行簽 pass。

按本輪要求進入工作，已選題就不再開題池。查資料、封面、素材和生圖是按需能力，不是每篇強制八步。共同規則在共用正本，本 repo 的 CLAUDE.md 保留圖文視覺偏好、prompt 交付與 Git 邊界；使用者直接要求優先。

- `demo_posts/<date>-<slug>/`：每篇唯一工作區。研究、story spine、post、prompts、images、reviews 沿用既有結構，已完成內容不重寫。
- `explorations/`：跨篇候選、系列、視覺與流程探索。帳號待辦入口是 [BACKLOG.md](../BACKLOG.md)，詳情仍回來源正本。
- `hypo.md`、`reviews/`、`notes/`：原始 learning 和歷史。共通判斷回帳號 LEARNINGS，保留可追溯來源。
- `references/`：本帳號的風格池、人物資料等；不要把它們升成全平台硬限制。
- `scripts/`：建工作區、prompt 交付與素材工具；只使用本輪需要的腳本。
- `skills/xhs-*`：舊路徑相容連結，正文已轉到共用新方法。七份原實體副本完整保存於帳號 archive；`sync-skills` 是獨立交付工具，仍保留。
- `xhs_skills/`：舊巢狀 Git 歷史，不作為調用／維護正本，不加入 discovery；不能直接當垃圾刪除。
- `runs/`、`db/`、`tmp/`：舊研究／試作資料，本輪保留。

開新完整工作區可用：

```bash
python3 scripts/scaffold_post_folder.py --date YYYY-MM-DD --slug topic-slug --title '工作標題'
```

scaffolder 保留發布文字與內部圖組的分工，張數、字數、開場與數字不再硬套固定模板。舊的 `generate_images_from_post.py` 與共用 `xhs-image-style-duo/scripts/generate_style_duo.py` 功能不同，仍按需使用；不因收斂入口刪除可用工具。

貼文內容和研究保存於 session 分支；不要把 demo_posts 合進 main。Prompt 交付照 CLAUDE.md 用 stage_prompt.py，只有真正 push 成功才給 URL。`.env`、既有 ignored 內容和隨本 repo 的 worktree 完整搬入；未改內容，未提交其他工作。

遷移與回復：[MIGRATION_PLAN.md](../archive/migration-2026-10-03/MIGRATION_PLAN.md)。本 repo 現在實體位於帳號的 `image/` 子目錄；舊 `crewai_xhs` 路徑已移除。

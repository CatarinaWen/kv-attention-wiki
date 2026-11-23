# 廣告 KV 視覺注意力 LLM Wiki → 教學 HTML 簡報

- 作業首頁：`index.html`（主題介紹、Wiki、簡報、loop/graph、執行紀錄、反思）
- 教學簡報：`slides/index.html`
- LLM Wiki：`wiki/index.md`（HTML 版 `wiki/index.html`）
- Schema：`CLAUDE.md`
- 執行紀錄：`docs/run-01.md`

## 結構

```
raw/        原始資料筆記（7 篇，只新增不修改）
wiki/       LLM Wiki：sources/ 來源頁、concepts/ 概念頁、synthesis/ 綜合頁、index、log、discussion
slides/     outline.json（大綱＋引用＋facts）、index.html（簡報）
tools/      lint_wiki / check_outline / check_slides / build_site / run_pipeline
docs/       執行與檢查紀錄
```

## 重跑整條檢查

```
pip install markdown
python3 tools/run_pipeline.py
```

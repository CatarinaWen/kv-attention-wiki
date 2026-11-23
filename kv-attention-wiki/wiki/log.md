# 操作紀錄 log

格式：`## [日期] 操作 | 對象`，下面寫動到哪些頁。

## [2026-11-23] discuss | 主題、讀者、來源範圍
- 結果寫在 [discussion.md](discussion.md)

## [2026-11-23] ingest | S01 Itti, Koch & Niebur 1998
- 新增 sources/S01；新增 concepts/visual-attention、saliency-map、saliency-prediction-models

## [2026-11-23] ingest | S02 Judd et al. 2009
- 新增 sources/S02、concepts/center-bias；更新 visual-attention、saliency-map、saliency-prediction-models

## [2026-11-23] ingest | S03 DeepGaze I / II
- 新增 sources/S03、concepts/transfer-learning；更新 center-bias、saliency-prediction-models

## [2026-11-23] ingest | S04 Wedel & Pieters 2000
- 新增 sources/S04、concepts/eye-tracking、ad-elements、attention-to-memory

## [2026-11-23] ingest | S05 Pieters & Wedel 2004
- 新增 sources/S05；更新 eye-tracking、ad-elements、attention-to-memory

## [2026-11-23] ingest | S06 Pieters & Wedel 2012 Ad Gist
- 新增 sources/S06、concepts/ad-gist

## [2026-11-23] ingest | S07 Bylinskii et al. 2017
- 新增 sources/S07、concepts/visual-importance；更新 saliency-map
- 新增 synthesis/kv-pretest-checklist、synthesis/limitations

## [2026-11-23] lint | 第 1 次
- 1 個問題：index.md 連到還沒建立的 log.md（L3 死連結）→ 建立本檔

## [2026-11-23] lint | 第 2 次
- 0 個問題；另外故意埋錯數字測試 lint，發現子字串比對的漏洞，改成整個數字比對

## [2026-11-23] query | 「KV 視覺注意力入門」教學簡報
- 產生 slides/outline.json（18 張），check_outline 抓到遷移學習頁沒被引用 → 第 10 張補引用
- 產生 slides/index.html，check_slides、視覺檢查的問題與修正見 docs/run-01.md

## [2026-11-23] schema | workflow v2
- outline 新增 facts（數字＋單位），數字檢查往前移到 outline 階段；暖身頁只能發問

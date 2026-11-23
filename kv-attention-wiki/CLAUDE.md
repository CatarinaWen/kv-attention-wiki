# CLAUDE.md — 廣告 KV 視覺注意力 LLM Wiki 的 schema

這份檔案告訴 LLM（小扣 / Claude）怎麼維護這個 Wiki。採用 Karpathy 的 LLM Wiki 模式：
三層結構（raw → wiki → schema），三個操作（ingest / query / lint）。

## 三層結構

| 層 | 位置 | 誰可以改 | 用途 |
|---|---|---|---|
| Raw 原始資料 | `raw/S0x-*.md` | 只新增，不修改 | 每篇來源的書目、網址、摘要層級的重點、可驗證數字 |
| Wiki | `wiki/` | LLM 維護 | 來源頁、概念頁、綜合頁、index、log |
| Schema | `CLAUDE.md`（本檔） | 我和 LLM 一起改 | 規則與流程 |

## Wiki 頁面類型

- `wiki/sources/S0x.md`：一篇來源一頁，寫「這篇說了什麼、可以用在哪」
- `wiki/concepts/*.md`：一個概念一頁（例：顯著圖、眼動追蹤）
- `wiki/synthesis/*.md`：跨來源的整理（例：KV 前測檢查表）
- `wiki/index.md`：所有頁面的目錄，每頁一行摘要
- `wiki/log.md`：每次 ingest / query / lint 的紀錄

## 寫作規則（lint 會檢查）

1. **每一條重點都要標來源**：條列句結尾加 `〔S01〕` 這種標記，可以多個 `〔S01〕〔S03〕`。
2. **數字要能回到 raw**：概念頁裡出現的數字（年份除外），必須出現在被引用來源的 raw 筆記裡。
3. **連結用相對路徑的一般 Markdown 連結**，例如 `[顯著圖](saliency-map.md)`，不要用 `[[ ]]`。
4. **不要孤兒頁**：每個概念頁至少要被另一頁連到。
5. **不抄原文**：raw 只放摘要層級的重點，用自己的話寫；不放長段落引文。
6. 概念頁要有「一句話解釋」，給完全不懂的人看。

## Ingest 流程（一次一篇）

1. 先和使用者討論這篇的重點要放哪裡（先討論、後生成）
2. 新增 `raw/S0x-*.md`
3. 寫 `wiki/sources/S0x.md`
4. 新增或更新相關概念頁（一篇來源通常會動到 2–4 頁）
5. 更新 `wiki/index.md`、在 `wiki/log.md` 加一行
6. 跑 `python3 tools/lint_wiki.py`，有錯就回到第 3–4 步

## Query → 簡報流程（v2，第一次執行後修改）

1. 先寫 `slides/outline.json`：每張投影片列出
   - `wiki`：引用哪些 wiki 頁
   - `introduces`：這張教的新名詞；`uses`：這張會用到的名詞
   - `facts`：**這張會出現的數字＋單位**（例 `"100 毫秒"`）← v2 新增
2. 跑 `python3 tools/check_outline.py`：引用存在、先教再用、每個概念頁都有被用到、**facts 連同單位都在 wiki 裡**
3. 生成 `slides/index.html`，每張投影片的 `data-wiki` 要和 outline 一致
   - 暖身／示範用的虛構 KV 加 `data-check="skip"`，而且這種投影片**只能發問，不能先講結論**
   - 結論只能出現在有引用 wiki 的投影片上
4. 跑 `python3 tools/check_slides.py`：張數、data-wiki、數字都能在 wiki 找到、**畫面上的數字都是 outline 宣告過的**
5. 跑 `python3 tools/build_site.py` 產生可瀏覽的 wiki HTML
6. 截圖每一張投影片做視覺檢查（版面、看不見的字、沒有來源的說法）

一次跑完 2–5：`python3 tools/run_pipeline.py`，哪個節點沒過就照它說的回到對應步驟。

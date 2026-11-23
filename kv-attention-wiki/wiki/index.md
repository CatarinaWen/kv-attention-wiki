# 廣告 KV 視覺注意力 LLM Wiki — 目錄

主題：一張廣告主視覺（KV）出來，人會先看哪裡？為什麼？電腦能不能先預測？
讀者：廣告系、不懂電腦視覺也不懂眼動研究的人。

## 概念頁

- [視覺注意力](concepts/visual-attention.md)：bottom-up 與 top-down 兩種注意力
- [眼動追蹤](concepts/eye-tracking.md)：怎麼量測人看哪裡
- [顯著圖](concepts/saliency-map.md)：把「多突出」畫成熱度地圖
- [中央偏誤](concepts/center-bias.md)：人看圖天生偏向中央
- [顯著性模型演進](concepts/saliency-prediction-models.md)：規則 → 學習 → 深度學習
- [遷移學習](concepts/transfer-learning.md)：借用 ImageNet 網路來預測注視
- [廣告三元素](concepts/ad-elements.md)：品牌、圖像、文字怎麼搶注意力
- [注意力到記憶](concepts/attention-to-memory.md)：被看到之後還要被記住
- [Ad Gist 一眼要旨](concepts/ad-gist.md)：100 毫秒能看懂什麼
- [視覺重要性](concepts/visual-importance.md)：設計稿版的顯著圖

## 綜合頁

- [KV 前測檢查表](synthesis/kv-pretest-checklist.md)
- [限制與還沒解決的問題](synthesis/limitations.md)

## 來源頁（7 篇 ingest）

- [S01 Itti, Koch & Niebur 1998](sources/S01.md)：第一個顯著圖模型
- [S02 Judd et al. 2009](sources/S02.md)：用眼動資料學會預測
- [S03 Kümmerer et al. DeepGaze I/II](sources/S03.md)：深度學習 + 遷移學習
- [S04 Wedel & Pieters 2000](sources/S04.md)：注視與品牌記憶
- [S05 Pieters & Wedel 2004](sources/S05.md)：注意力的捕捉與轉送
- [S06 Pieters & Wedel 2012](sources/S06.md)：Ad Gist
- [S07 Bylinskii et al. 2017](sources/S07.md)：平面設計的視覺重要性

## 維護

- [操作紀錄 log](log.md)
- Schema：[CLAUDE.md](../CLAUDE.md)

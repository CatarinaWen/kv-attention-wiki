# S07 Bylinskii et al. (2017) — Visual Importance for Graphic Designs

- 書目：Bylinskii, Z., Kim, N. W., O'Donovan, P., Alsheikh, S., Madan, S., Pfister, H., Durand, F., Russell, B., & Hertzmann, A. (2017). Learning Visual Importance for Graphic Designs and Data Visualizations. *UIST 2017*. DOI:10.1145/3126594.3126653
- 網址：https://arxiv.org/abs/1708.02660 ；http://visimportance.csail.mit.edu
- 取得日期：2026-11-23

## 摘要層級重點（自己的話）

- 平面設計與資料視覺化的目標之一，是傳達各元素的相對「重要性」，讓觀看者知道要看哪裡、怎麼解讀。
- 自然場景的顯著性預測已經做得不錯，但針對平面設計的重要性預測很少。
- 他們訓練神經網路預測設計中每個區域的重要性：平面設計模型用約 1K 張設計稿（GDI 資料集）的人工重要性標註；資料視覺化模型用 BubbleView 在約 1.4K 張圖表（MASSVIS）上蒐集的滑鼠點擊。
- 設計稿的重要性和「bottom-up 突出」（字體、顏色、樣式）有關，但不等於自然場景的顯著性。
- 應用：自動重排版（retargeting）、縮圖、在設計工具裡即時回饋「目前哪裡最搶眼」。
- 用 Amazon MTurk 上數百位參與者的使用者研究驗證。
- 研究團隊包含 MIT 與 Adobe Research。

## 可驗證數字

- 1K 張平面設計（GDI）
- 1.4K 張資料視覺化（MASSVIS）
- 年份：2017

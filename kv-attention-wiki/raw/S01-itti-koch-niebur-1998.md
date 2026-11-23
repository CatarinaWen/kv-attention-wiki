# S01 Itti, Koch & Niebur (1998)

- 書目：Itti, L., Koch, C., & Niebur, E. (1998). A Model of Saliency-Based Visual Attention for Rapid Scene Analysis. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 20(11), 1254–1259.
- 網址：https://resolver.caltech.edu/CaltechAUTHORS:20230330-63403000.1
- 取得方式：摘要頁 + 課程講義（https://www.inf.ed.ac.uk/teaching/courses/ccs/lectures/ccs_l15_saliency.pdf）
- 取得日期：2026-11-23

## 摘要層級重點（自己的話）

- 模仿靈長類早期視覺系統的注意力模型。
- 把圖片拆成顏色、亮度、方向三種特徵，在多個尺度上計算「中心和周圍差多少」（center-surround）。
- 各特徵圖正規化後合併成一張「顯著圖」（saliency map），表示畫面每個位置有多突出。
- 用 winner-take-all 選出最顯著的位置當注意焦點，再用「返回抑制」（inhibition of return）讓焦點移到下一個位置，所以會依顯著程度由高到低掃過畫面。
- 屬於純 bottom-up（由畫面驅動、和任務無關）的模型。
- 講義指出的限制：只能抓到因顏色、亮度、方向而突出的區域；原論文沒有拿真人眼動資料來驗證。

## 可驗證數字

- 特徵種類：3（顏色、亮度、方向）
- 年份：1998

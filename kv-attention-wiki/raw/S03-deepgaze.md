# S03 Kümmerer et al. — DeepGaze I (2014) & DeepGaze II (2016)

- 書目 1：Kümmerer, M., Theis, L., & Bethge, M. (2014). Deep Gaze I: Boosting Saliency Prediction with Feature Maps Trained on ImageNet. arXiv:1411.1045.
- 書目 2：Kümmerer, M., Wallis, T. S. A., & Bethge, M. (2016). DeepGaze II: Reading fixations from deep features trained on object recognition. arXiv:1610.01563.
- 補充：Kümmerer et al. (2017). Understanding Low- and High-Level Contributions to Fixation Prediction. ICCV 2017.
- 網址：https://arxiv.org/abs/1411.1045 ；https://arxiv.org/abs/1610.01563 ；https://openaccess.thecvf.com/content_ICCV_2017/papers/Kummerer_Understanding_Low-_and_ICCV_2017_paper.pdf
- 取得日期：2026-11-23

## 摘要層級重點（自己的話）

- 2014 年起，深度神經網路讓顯著性預測（saliency prediction）大幅進步。
- 問題：眼動資料集很小（幾千張圖），從零訓練深度網路不夠。
- 解法：遷移學習（transfer learning）。DeepGaze I 拿在 ImageNet 物體辨識上預訓練好的 AlexNet 特徵，再學一層讀出（readout）來預測注視。
- DeepGaze II 改用 VGG 特徵，而且不微調 VGG，只在上面訓練幾層讀出層，所以是很強的遷移學習測試。
- 評估用 MIT Saliency Benchmark（MIT300）：300 張圖、40 位受試者，注視資料不公開，避免模型偷看答案。
- 常見指標：AUC（含中央偏誤）與 shuffled AUC（扣掉中央偏誤）。
- DeepGaze I 投稿時：shuffled AUC 71.69%（當時最好的 AWS 是 67.90%），AUC 84.40%。
- 2017 ICCV 論文報告 DeepGaze II 在 MIT300 上 AUC 88%、sAUC 77%，當時為頂尖。
- 啟示：在物體辨識上學到的高階特徵，對預測人會看哪裡很有用。

## 可驗證數字

- 300 張圖、40 位受試者（MIT300）
- DeepGaze I：sAUC 71.69%，對照 AWS 67.90%；AUC 84.40%
- DeepGaze II：AUC 88%、sAUC 77%
- 年份：2014、2016、2017

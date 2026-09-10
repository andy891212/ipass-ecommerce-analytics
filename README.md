# 全球電商顧客留存與 RFM 數據分群分析 (Global E-Commerce Analytics)

## 📌 專案摘要 (Executive Summary)
本專案針對 2023–2025 年全球電商交易數據（涵蓋 2,000 筆訂單、1,534 位顧客）進行深度分析。專案結合 **MySQL 數據倉儲邏輯** 與 **Tableau 互動式視覺化儀表板**，旨在解決核心商業痛點：追蹤 Cohort 顧客流失趨勢，以及建立動態 RFM 顧客價值分群模型，提供可落地的行銷與營運策略。

---

## 🛠️ 技術架構 (Tech Stack)
* **資料庫與數據建模**：MySQL 8.0（使用 CTEs、Window Functions、UAT 資料品質驗證）
* **資料視覺化**：Tableau Public（Cohort 留存熱力圖、RFM 散佈圖）
* **分析邏輯框架**：Cohort Retention Analysis、RFM Customer Segmentation Model

---

## 📊 關鍵數據洞察與商業建議 (Key Insights & Recommendations)

### 1. Cohort 留存斷崖分析 (M+1 Churn)
* **數據洞察**：分析顯示用戶在 **M+1（首購後第 2 個月）存在顯著的留存斷崖**，多數月份 Cohort 的回購率皆出現大幅下滑，顯示用戶首購後的黏著度不足。
* **落地建議**：建立自動化行銷旅程（Post-purchase Journey），於顧客首購後第 14~21 天觸發「二刷專屬優惠券」或自動化推播，降低次月流失率。

### 2. 支付管道營收效益 (Payment Channel Performance)
* **數據洞察**：**Credit Card（信用卡）** 貢獻最高總營收（$193,121）與最高淨利（$62,810），其次為 **PayPal**（$143,303），顯示數位與卡片支付為主力營收來源。
* **落地建議**：可針對信用卡與電子支付管道（如綁卡消費加碼）設計點數回饋機制，強化高價值支付用戶的黏著度與客單價。

### 3. RFM 顧客價值分群 (RFM Segmentation)
* **數據洞察**：運用 SQL `NTILE(5)` 針對 1,534 位顧客在 Recency、Frequency、Monetary 三個維度進行打分：
  * **核心 VIP 群**：近親度高、消費金額大且頻次穩定。
  * **沉睡/流失風險群**：超過 600 天未消費，且累積消費金額極低。
* **落地建議**：停止對 RFM 低分群投放高成本數位廣告；將行銷資源集中於核心 VIP 顧客，提供尊榮專屬權益以極大化用戶終身價值（LTV）。

---

## 📁 專案檔案結構 (Repository Structure)
```text
├── DATA/
│   ├── cohort_result.csv         # SQL 運算匯出之 Cohort 數據
│   └── rfm_result.csv            # SQL 運算匯出之 RFM 分群數據
├── SQL/
│   ├── cohort_analysis.sql       # MySQL Cohort 語法 (PERIOD_DIFF & JOIN)
│   └── rfm_segmentation.sql      # MySQL RFM 語法 (NTILE 分數運算)
└── Dashboard/
    ├── ecommerce_dashboard.twbx  # Tableau 打包工作簿檔案
    └── dashboard_preview.png     # 儀表板預覽截圖

# Global E-Commerce Customer Retention & RFM Analysis

## 📌 Executive Summary
This project analyzes a 3-year global e-commerce dataset (2,000 transactions, 1,534 customers) to optimize customer retention and marketing efficiency for analytics engineering applications. By combining MySQL data warehousing logic and Tableau interactive visualizations, this pipeline addresses core business pain points: tracking cohort churn and implementing dynamic RFM customer segmentation.

---

## 🛠️ Tech Stack & Architecture
* **Database & Data Modeling**: MySQL 8.0 (CTEs, Window Functions, UAT Data Validation)
* **Data Visualization**: Tableau Public (Cohort Heatmap, RFM Scatterplot)
* **Core Analytics Framework**: Cohort Retention Analysis, RFM Customer Segmentation Model

---

## 📊 Key Insights & Strategic Recommendations

### 1. Cohort Retention Churn (M+1 Drop-off)
* **Insight**: Cohort analysis reveals a steep retention cliff at M+1 (2nd month), where user retention drops sharply across almost all monthly cohorts.
* **Action**: Implement an automated post-purchase journey triggering a 20-day "second-purchase discount" or tailored push notification to bridge the transition from first-time buyer to repeat customer.

### 2. Payment Channel Revenue Contribution
* **Insight**: **Credit Card** transactions drive the highest total revenue ($193,121) and net profit ($62,810), closely followed by **PayPal** ($143,303).
* **Action**: Align reward structures with digital payment methods (such as iPASS MONEY / card binding campaigns) to incentivize spending among high-value payment channels.

### 3. RFM Customer Value Segmentation
* **Insight**: Evaluated 1,534 customers using `NTILE(5)` scores across Recency, Frequency, and Monetary dimensions:
  * **Top Champions**: Short recency, high monetary value, and frequent order cadence.
  * **At-Risk / Dormant**: Over 600 days since last interaction with low lifetime spend.
* **Action**: Reallocate marketing budget away from broad digital ad acquisition toward VIP loyalty perks for high-score segments.

---

## 📁 Repository Structure
```text
├── DATA/
│   ├── cohort_result.csv         # Exported SQL output for cohort heatmap
│   └── rfm_result.csv            # Exported SQL output for RFM segmentation
├── SQL/
│   ├── cohort_analysis.sql       # MySQL queries with PERIOD_DIFF & Window Functions
│   └── rfm_segmentation.sql      # MySQL queries with NTILE(5) scoring logic
└── Dashboard/
    ├── ecommerce_dashboard.twbx  # Tableau packaged workbook
    └── dashboard_preview.png     # Interactive dashboard snapshot

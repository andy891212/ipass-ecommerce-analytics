import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 1. 載入資料並整理
df = pd.read_csv('global_ecommerce_sales.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# 計算 RFM 數據 (以資料集中最新日期的隔天為基準日)
snapshot_date = df['Order_Date'].max() + pd.Timedelta(days=1)
rfm = df.groupby('Customer_Name').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'nunique',
    'Total_Sales': 'sum'
}).reset_index()

rfm.columns = ['Customer_Name', 'Recency', 'Frequency', 'Monetary']

# 用 qcut 劃分 1~5 分
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
rfm['RFM_Total'] = rfm['R_Score'].astype(int) + rfm['F_Score'].astype(int) + rfm['M_Score'].astype(int)

# 2. 設定繪圖畫布與主題樣式
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(15, 5)) # 建立 1 列 2 欄的雙圖組合

# 3. 繪製左圖：不同支付方式的營收與利潤長條圖 (Barplot)
payment_summary = df.groupby('Payment_Method')[['Total_Sales', 'Profit']].sum().reset_index()
payment_summary_melt = payment_summary.melt(id_vars='Payment_Method', value_vars=['Total_Sales', 'Profit'])

sns.barplot(
    data=payment_summary_melt, 
    x='Payment_Method', 
    y='value', 
    hue='variable', 
    ax=axes[0], 
    palette='Blues_r'
)
axes[0].set_title('Total Sales & Profit by Payment Method ($)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('USD ($)')
axes[0].set_xlabel('Payment Method')

# 4. 繪製右圖：RFM 顧客分群散佈圖 (Scatterplot)
sns.scatterplot(
    data=rfm, 
    x='Recency', 
    y='Monetary', 
    hue='RFM_Total',       # 依 RFM 總分顯示顏色深淺
    palette='viridis',     # 漸層配色
    size='Frequency',      # 依消費頻次決定點的大小
    sizes=(20, 200),
    ax=axes[1],
    alpha=0.8
)
axes[1].set_title('RFM Customer Distribution (Recency vs Monetary)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Recency (Days since last purchase)')
axes[1].set_ylabel('Monetary (Total Spend $)')

# 5. 優化版面並儲存圖片
plt.tight_layout()
plt.savefig('ecommerce_analysis_charts.png', dpi=300)
plt.show()
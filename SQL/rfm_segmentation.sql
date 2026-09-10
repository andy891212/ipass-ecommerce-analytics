

WITH rfm_raw AS (
    SELECT 
        Customer_Name,
        DATEDIFF('2026-01-01', MAX(STR_TO_DATE(Order_Date, '%Y-%m-%d'))) AS recency,
        COUNT(DISTINCT Order_ID) AS frequency,
        SUM(Total_Sales) AS monetary
    FROM ecommerce.global_ecommerce_sales
    GROUP BY Customer_Name
),
rfm_scores AS (
    SELECT 
        Customer_Name,
        recency,
        frequency,
        monetary,
        NTILE(5) OVER (ORDER BY recency ASC) AS r_score,
        NTILE(5) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(5) OVER (ORDER BY monetary ASC) AS m_score
    FROM rfm_raw
)
SELECT 
    Customer_Name,
    recency,
    frequency,
    ROUND(monetary, 2) AS monetary,
    r_score, f_score, m_score,
    (r_score + f_score + m_score) AS rfm_total_score
FROM rfm_scores;
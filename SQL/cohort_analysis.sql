WITH user_first_order AS (
    SELECT 
        Customer_Name,
        MIN(DATE_FORMAT(STR_TO_DATE(Order_Date, '%Y-%m-%d'), '%Y-%m-01')) AS first_month
    FROM global_ecommerce_sales
    GROUP BY Customer_Name
),
user_activities AS (
    SELECT 
        s.Customer_Name,
        f.first_month,
        PERIOD_DIFF(
            DATE_FORMAT(STR_TO_DATE(s.Order_Date, '%Y-%m-%d'), '%Y%m'),
            DATE_FORMAT(f.first_month, '%Y%m')
        ) AS month_number
    FROM ecommerce.global_ecommerce_sales s
    JOIN user_first_order f ON s.Customer_Name = f.Customer_Name
)
SELECT 
    first_month,
    month_number,
    COUNT(DISTINCT Customer_Name) AS active_users
FROM user_activities
GROUP BY first_month, month_number
ORDER BY first_month, month_number;
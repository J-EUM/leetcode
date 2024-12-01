# Write your MySQL query statement below
WITH FirstOrder AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_number
    FROM Delivery
)
SELECT 
    ROUND(
        100.0 * 
        COUNT(
            CASE 
                WHEN order_date=customer_pref_delivery_date THEN 1 
            END) / 
        COUNT(1), 
    2) immediate_percentage
FROM FirstOrder
WHERE order_number=1
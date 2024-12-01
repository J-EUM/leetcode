SELECT 
    ROUND(
        100.0 * 
        COUNT(
            CASE 
                WHEN order_date=customer_pref_delivery_date THEN 1 
            END) / 
        COUNT(1), 
    2) immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) in (
    SELECT customer_id, MIN(order_date) 
    FROM Delivery
    GROUP BY customer_id
)
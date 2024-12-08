# Write your MySQL query statement below
SELECT 
    ROUND(
        COUNT(
            CASE 
                WHEN event_order = 1 AND 
                    DATEDIFF(next_event_date, event_date) = 1 
                THEN 1 
            END) / 
        COUNT(DISTINCT player_id), 
    2) fraction
FROM (
    SELECT 
        player_id,
        event_date,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) event_order,
        LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) next_event_date
    FROM Activity
) sub
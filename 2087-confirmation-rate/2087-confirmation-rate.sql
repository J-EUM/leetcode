# Write your MySQL query statement below

SELECT s.user_id,
        ROUND(
            COUNT(
                CASE 
                    WHEN action='confirmed' THEN 1 
                END) * 1.0 / COUNT(1),
            2
        ) confirmation_rate
FROM Signups s LEFT JOIN Confirmations c USING(user_id)
GROUP BY 1;
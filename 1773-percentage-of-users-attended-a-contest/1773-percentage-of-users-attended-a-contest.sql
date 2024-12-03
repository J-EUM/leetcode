# Write your MySQL query statement below
SELECT contest_id, 
        ROUND(100.0 * COUNT(1)/(SELECT COUNT(1) FROM Users), 2) percentage
FROM Register
GROUP BY 1
ORDER BY 2 DESC, 1

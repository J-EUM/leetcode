# Write your MySQL query statement below
SELECT
    query_name,
    ROUND(AVG(rating/`position`), 2) quality,  # mysql은 백틱
    ROUND(
        100 * 
        COUNT(CASE WHEN rating < 3 THEN 1 END) /
        COUNT(1), 
    2) poor_query_percentage
FROM Queries
GROUP BY 1
HAVING query_name IS NOT NULL

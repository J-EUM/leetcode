# Write your MySQL query statement below

SELECT name
FROM Employee E1
JOIN (SELECT managerId, COUNT(1) AS reports
FROM Employee WHERE managerId IS NOT null
GROUP by 1) E2 ON E1.id = E2.managerId
WHERE E2.reports >= 5
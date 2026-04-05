-- Write your MySQL query statement below
SELECT p.email AS Email FROM
Person p
GROUP BY p.email
HAVING COUNT(p.email) > 1;

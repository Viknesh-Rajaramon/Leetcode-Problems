-- Write your MySQL query statement below
SELECT W2.id FROM
Weather W1
INNER JOIN
Weather W2
ON W2.recordDate = DATE_ADD(W1.recordDate, INTERVAL 1 DAY)
WHERE W2.temperature > W1.temperature;

-- Write your MySQL query statement below
DELETE FROM
Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(p1.id) AS id FROM
        Person p1
        GROUP BY p1.email
    ) p2
);

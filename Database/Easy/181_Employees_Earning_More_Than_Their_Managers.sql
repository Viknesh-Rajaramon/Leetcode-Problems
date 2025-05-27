-- Write your MySQL query statement below
SELECT e.name AS Employee FROM Employee e
INNER JOIN
(
  SELECT id, salary FROM Employee
) m
ON
e.managerId = m.id
WHERE e.salary > m.salary;

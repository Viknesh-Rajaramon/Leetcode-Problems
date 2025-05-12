-- Write your MySQL query statement below
SELECT MAX(e1.salary) as SecondHighestSalary FROM Employee e1 WHERE salary < (SELECT MAX(e2.salary) FROM Employee e2);

-- Write your MySQL query statement below
WITH MaxSalary AS (
    SELECT departmentId, MAX(salary) AS max_salary FROM
    Employee
    GROUP BY departmentId
)
SELECT D.name AS "Department", E.name AS "Employee", M.max_salary AS "Salary" FROM
Employee E
INNER JOIN
MaxSalary M
ON E.salary = M.max_salary AND E.departmentId = M.departmentId
INNER JOIN
Department D
ON E.departmentId = D.id;

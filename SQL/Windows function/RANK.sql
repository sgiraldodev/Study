--Dada la tabla employees(id, name, department_id, salary) y departments(id, dept_name), 
--escribe una consulta para obtener el nombre del departamento y el nombre del empleado
-- mejor pagado de cada departamento.

Table employees {
  id int [primary key]
  name varchar(50)
  department_id int
  salary int
}

Table departments {
  id int [primary key]
  dept_name varchar(50)
}



******
SELECT name, dept_name, salary
FROM (
    SELECT e.name, d.dept_name, e.salary,
           RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rnk
    FROM employees e
    JOIN departments d ON d.id = e.department_id
) t
WHERE rnk = 1;
******
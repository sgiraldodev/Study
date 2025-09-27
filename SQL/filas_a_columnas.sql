--Ejecutar en https://runsql.com/r


--Tabla de ejemplo
--Use DBML to define your database structure
--Docs: https://dbml.dbdiagram.io/docs

Table students {
  student_id integer
  name varchar(50)
  subject varchar(50)
  score integer
}

"1","Santiago","Mate","2"
"1","Santiago","Quimica","4"
"1","Santiago","Sistemas","5"
"2","H","Mate","2"
"2","H","Quimica","4"
"2","H","Sistemas","5"

--Realizar una consulta que transforme las filas en columnas de manera que se muestren 
--las materias como columnas y los puntajes como valores.


SELECT
name, 
student_id,
MAX(CASE WHEN subject = 'Mate' then score END) as Mate, 
MAX(CASE WHEN subject = 'Quimica' then score END) as Quimica, 
MAX(CASE WHEN subject = 'Sistemas' then score END) as Sistemas

FROM students
GROUP By name, student_id
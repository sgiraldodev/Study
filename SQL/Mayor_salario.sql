--Dadas las tablas orders(order_id, customer_id, total, created_at) 
--y customers(customer_id, name), 
--escribe una consulta para obtener los 5 clientes que más dinero gastaron en el último año.

Table orders {
  order_id int [primary key]
  customer_id int
  total integer
  created_at date
}

Table customers {
  customer_id int [primary key]
  name varchar(50)
}

Ref: orders.order_id > customers.customer_id // many-to-one


******
SELECT
  c.customer_id,
  c.name,
  SUM(o.total) AS total_spent
 
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;
******
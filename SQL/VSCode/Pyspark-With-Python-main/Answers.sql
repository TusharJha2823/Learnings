SELECT * FROM goldusers_signup;
SELECT * FROM users;
SELECT * FROM sales;
SELECT * FROM product;

-- question 1.what is total amount each customer spent on zomato ?
Select s.userid, SUM(price) as total
FROM sales s
INNER JOIN product p
ON s.product_id = p.product_id
GROUP BY s.userid;

-- question 2.How many days has each customer visited zomato?
SELECT userid, COUNT (DISTINCT created_date) as Number_of_days
FROM sales 
GROUP BY userid;

-- question 3.what was the first product purchased by each customer?
SELECT * FROM
(SELECT * ,
DENSE_RANK() OVER (PARTITION BY userid ORDER BY created_date) as RK 
FROM sales) s
WHERE s.RK = 1;

-- question 4.what is most purchased item on menu & how many times was it purchased by all customers ?
SELECT userid, COUNT(product_id) as cntproduct, product_id
 FROM sales WHERE product_id = 
(SELECT MAX(product_id)
FROM sales
GROUP BY product_id
ORDER BY COUNT(product_id) DESC LIMIT 1)
GROUP BY userid



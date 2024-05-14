CREATE SCHEMA ZOMATO;

USE ZOMATO;
drop table if exists goldusers_signup;
CREATE TABLE goldusers_signup(userid integer,gold_signup_date varchar(255)); 

INSERT INTO goldusers_signup(userid,gold_signup_date) 
 VALUES 
 (1,'2017-09-22'),
 (2,'2017-05-14'),
 (3,'2017-04-21');

drop table if exists users;

CREATE TABLE users(userid integer,signup_date varchar(255)); 

INSERT INTO users(userid,signup_date) 
 VALUES (1,'2014-09-02'),
(2,'2015-01-15'),
(3,'2014-04-11');

drop table if exists sales;
CREATE TABLE sales(userid integer,created_date varchar(255),product_id integer); 

INSERT INTO sales(userid,created_date,product_id) 
 VALUES 
(1,'2017-04-19',2),
(3,'2019-12-18',1),
(2,'2020-07-20',3),
(1,'2019-10-23',2),
(1,'2018-03-19',3),
(3,'2016-12-20',2),
(1,'2016-11-09',1),
(1,'2016-05-20',3),
(2,'2017-09-24',1),
(1,'2017-03-11',2),
(1,'2016-03-11',1),
(3,'2016-11-10',1),
(3,'2017-12-07',2),
(3,'2016-12-15',2),
(2,'2017-11-08',2),
(2,'2018-09-10',3),
(2,'2016-07-20',3);


drop table if exists product;
CREATE TABLE product(product_id integer,product_name text,price integer); 

INSERT INTO product(product_id,product_name,price) 
 VALUES
(1,'p1',980),
(2,'p2',870),
(3,'p3',330);


-- steps to convert date type format to any desired type in mysql
-- for example there is a student table 
-- CREATE TABLE student(name varchar(255), dob date)

-- now the default format for this is YYYY-MM-DD for mysql. if u wish even insert a file, you are forced to fill in this format.
-- SO to change that, you first need to alter it to varchar and then update it with the help of date_format function.

-- AlTER TABLE student modify dob varchar(255)
-- UPDATE student set dob = date_format(dob,"%m,%d,%Y")    

-- you can check the mysql documentation for further documentation or go to this youtube tutorial https://www.youtube.com/watch?v=HdsBI1fBvMg
-- https://www.w3schools.com/sql/func_mysql_date_format.asp


SELECT * FROM sales ORDER BY created_date;
SELECT * FROM goldusers_signup;
SELECT * FROM product;
SELECT * FROM users;

/*
Question 1
1.what is total amount each customer spent on zomato ?
Answer */

SELECT s.userid AS userid, SUM(price) AS sum_of_price
FROM sales s INNER JOIN product p USING (product_id)
GROUP BY s.userid
ORDER BY s.userid;

/*
Question 2
2.How many days has each customer visited zomato?
Answer */
SELECT COUNT(DISTINCT created_date) AS num_of_days
FROM sales
GROUP BY userid;

/*
Question 3
3.what was the first product purchased by each customer?
Answer */

WITH CTE AS (SELECT s.userid AS userid, s.created_date AS created_date,
DENSE_RANK() OVER(PARTITION BY userid ORDER BY created_date) AS rnk, s.product_id AS product_id
FROM sales s)

SELECT userid, created_date, product_id
FROM CTE
WHERE rnk = 1;

/*
Question 4
4.what is most purchased item on menu & how many times was it purchased by all customers ?
Answer */

SELECT product_id, COUNT(product_id)
FROM sales
GROUP BY product_id
ORDER BY COUNT(product_id) desc
LIMIT 1;


/*
Question 5
5.what is most purchased item on menu & how many times was it purchased by each customers ?
Answer */

SELECT s2.userid, COUNT(s2.product_id) AS count_of_purchase
FROM sales s2
WHERE s2.product_id = 
    (SELECT s1.product_id
    FROM sales s1
    GROUP BY s1.product_id
    ORDER BY COUNT(s1.product_id) desc
    LIMIT 1)
GROUP BY s2.userid
ORDER BY s2.userid;

/*
Question 6
6.which item was most popular for each customer?
Answer */
SELECT * FROM sales ORDER BY created_date;

WITH CTE AS (SELECT 
    s1.userid AS userid, s1.product_id AS product_id,
    COUNT(s1.product_id) OVER(PARTITION BY s1.userid, s1.product_id) AS count_of_each_product
    -- the abpove step allows us to partition the user and count each product for each user
FROM sales s1), 
CTE2 AS (
    SELECT CTE.*, 
    ROW_NUMBER() OVER(PARTITION BY CTE.userid ORDER BY CTE.count_of_each_product DESC) AS rn
    /* The above row number puts a row number on the count of tables to allow allow a 
        descending order of of count. so we first take count and the put row number on top of it.
    */
    FROM CTE
)

SELECT CTE2.userid, CTE2.product_id, 
FROM CTE2
WHERE rn =1;


/*
Question 7
7.which item was purchased first by customer after they become a member ?
Answer */

WITH CTE AS (
    SELECT * FROM users g
    INNER JOIN sales s
        USING (userid)
    WHERE s.created_date > g.signup_date
    ORDER BY s.userid, s.created_date 
    /*    This gave us all the necessary filered values     */
),

CTE2 AS (
    SELECT CTE.*, 
        ROW_NUMBER() OVER(PARTITION BY userid ORDER BY created_date) AS rn
        -- now we found the row number for the lowest value from the first cte
    FROM CTE
)

SELECT CTE2.*
FROM CTE2
WHERE rn =1;

/*
Question 8
8. which item was purchased just before the customer became a gold member?
Answer */

WITH CTE AS (
    SELECT * FROM goldusers_signup g
    INNER JOIN sales s
        USING (userid)
    WHERE s.created_date < g.gold_signup_date
    ORDER BY s.userid, s.created_date 
    /*    This gave us all the necessary filered values     */
),

CTE2 AS (
    SELECT CTE.*, 
        ROW_NUMBER() OVER(PARTITION BY userid ORDER BY created_date DESC) AS rn
        -- now we found the row number for the lowest value from the first cte
    FROM CTE
)

SELECT CTE2.*
FROM CTE2
WHERE rn =1;


/*
Question 9
9. what is total orders and amount spent for each member before they become a member?
Answer */

WITH CTE AS  (SELECT 
        s.userid AS userid,
        g.gold_signup_date AS gold_signup_date,
        s.created_date AS created_date,
        p.product_id AS product_id,
        p.product_name AS product_name,
        p.price AS price,
        COUNT(p.product_id) OVER(PARTITION BY s.userid) AS "total orders",
        SUM(p.price) OVER(PARTITION BY s.userid) AS "amount spent"
    FROM sales s
    INNER JOIN goldusers_signup g
        USING (userid)
    INNER JOIN product p
        USING (product_id)
    WHERE s.created_date < g.gold_signup_date
    ORDER BY s.userid, s.created_date 
    /*    This gave us all the necessary filered values     */),
    -- The contents of the `CTE` are enough for the answer, I am now just cleaning up
CTE2 AS (
    SELECT CTE.*, ROW_NUMBER() OVER(PARTITION BY CTE.userid ORDER BY CTE.product_id) AS rn
    FROM CTE
)

SELECT CTE2.*
FROM CTE2
WHERE rn =1

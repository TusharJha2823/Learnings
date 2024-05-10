CREATE SCHEMA ZOMATO;

USE ZOMATO;
drop table if exists goldusers_signup;
CREATE TABLE goldusers_signup(userid integer,gold_signup_date varchar(255)); 

update goldusers_signup
set gold_signup_date = date_format(gold_signup_date, "%m,%d,%Y");

INSERT INTO goldusers_signup(userid,gold_signup_date) 
 VALUES (1,'09-22-2017'),(3,'04-21-2017');

drop table if exists users;

CREATE TABLE users(userid integer,signup_date varchar(255)); 

update users
set signup_date = date_format(signup_date, "%m,%d,%Y");

INSERT INTO users(userid,signup_date) 
 VALUES (1,'09-02-2014'),
(2,'01-15-2015'),
(3,'04-11-2014');

drop table if exists sales;
CREATE TABLE sales(userid integer,created_date varchar(255),product_id integer); 

update sales
set created_date = date_format(created_date, "%m,%d,%Y");

INSERT INTO sales(userid,created_date,product_id) 
 VALUES (1,'04-19-2017',2),
(3,'12-18-2019',1),
(2,'07-20-2020',3),
(1,'10-23-2019',2),
(1,'03-19-2018',3),
(3,'12-20-2016',2),
(1,'11-09-2016',1),
(1,'05-20-2016',3),
(2,'09-24-2017',1),
(1,'03-11-2017',2),
(1,'03-11-2016',1),
(3,'11-10-2016',1),
(3,'12-07-2017',2),
(3,'12-15-2016',2),
(2,'11-08-2017',2),
(2,'09-10-2018',3);


drop table if exists product;
CREATE TABLE product(product_id integer,product_name text,price integer); 

INSERT INTO product(product_id,product_name,price) 
 VALUES
(1,'p1',980),
(2,'p2',870),
(3,'p3',330);

SELECT * FROM sales;


-- steps to convert date type format to any desired type in mysql
-- for example there is a student table 
-- CREATE TABLE student(name varchar(255), dob date)

-- now the default format for this is YYYY-MM-DD for mysql. if u wish even insert a file, you are forced to fill in this format.
-- SO to change that, you first need to alter it to varchar and then update it with the help of date_format function.

-- AlTER TABLE student modify dob varchar(255)
-- UPDATE student set dob = date_format(dob,"%m,%d,%Y")    

-- you can check the mysql documentation for further documentation or go to this youtube tutorial https://www.youtube.com/watch?v=HdsBI1fBvMg
-- https://www.w3schools.com/sql/func_mysql_date_format.asp

# Databricks notebook source
data = [
(1, 'abc@g.com'),
(2, 'xyz@g.com'),
(3, 'abc@g.com' ),
(4, 'pqr@g.com')
]
schema = "id int,Email string"
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import count
df.groupBy("Email").agg(count("*")).filter(count("*")>1).drop("count(1)").show()
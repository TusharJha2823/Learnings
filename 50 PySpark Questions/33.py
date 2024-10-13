# Databricks notebook source
#Write a solution to find the people who have the most friends and the most friends number.

from pyspark.sql.functions import *

data = [
 (1,2,"2016/06/03"),
 (1,3,"2016/06/08"),
 (2,3,"2016/06/08"),
 (3,4,"2016/06/09")
]

schema = ["requester_id","accepter_id","accept_date"]

df = spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

df_final=df.select(col("requester_id")).unionAll(df.select(col("accepter_id")))
df_final.groupBy(col("requester_id")).agg(count("*").alias("num")).orderBy(col("num").desc()).limit(1).show()
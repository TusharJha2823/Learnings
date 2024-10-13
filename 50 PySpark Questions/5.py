# Databricks notebook source
#Write a pyspark code to rank the products based on their total sales amount for each month, and return the top product for each month.


sales_data = [
 {"product_id": 1, "sale_date": "2023-01-05", "amount": 100},
 {"product_id": 2, "sale_date": "2023-01-08", "amount": 150},
 {"product_id": 1, "sale_date": "2023-01-15", "amount": 100},
 {"product_id": 3, "sale_date": "2023-01-20", "amount": 100},
 {"product_id": 2, "sale_date": "2023-02-03", "amount": 180},
 {"product_id": 3, "sale_date": "2023-02-10", "amount": 250},
 {"product_id": 1, "sale_date": "2023-02-15", "amount": 300},
]
schema="product_id int ,sale_date string,amount long"

df=spark.createDataFrame(sales_data,schema)
df.show()


# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.window import Window
df_final=df.withColumn("sale_date",date_format(to_date(col("sale_date")),'yyyy-MM'))
df_final=df_final.groupBy("product_id","sale_date").agg(sum("amount").alias("total_amount"))
window_spec=Window.partitionBy("sale_date").orderBy(desc("total_amount"))
df_final=df_final.withColumn("rn",dense_rank().over(window_spec)).filter(col("rn")==1).select("product_id","sale_date")
df_final.show()
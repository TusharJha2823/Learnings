# Databricks notebook source
#top selling product

from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window



sales_data = [
 ("product1", 10),
 ("product2", 20),
 ("product3", 15),
 ("product1", 5),
 ("product2", 25),
 ("product3", 10),
 ("product4", 30)
]
sales_columns = ["product", "quantity"]
sales_df = spark.createDataFrame(sales_data, sales_columns)
display(sales_df)

# COMMAND ----------

from pyspark.sql.functions import rank,sum,desc
from pyspark.sql.window import Window
df_final=sales_df.groupBy('product').agg(sum(col('quantity')).alias('total_quantity'))
window=Window.orderBy(col('total_quantity').desc())
df_final.withColumn('rn',rank().over(window)).filter(col('rn')==1).select('product').show()


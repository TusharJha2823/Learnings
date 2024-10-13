# Databricks notebook source
data=[(1, "1234567890", None, None),
 (2, None, "0987654321", "937475"),
 (3, None, None, "1122334455"),
 (4, None, None, None)
]

columns = ["customer_id", "home_phone", "mobile_phone", "work_phone"]

df = spark.createDataFrame(data, columns)
display(df)

# COMMAND ----------

from pyspark.sql.functions import coalesce,col
df_final=df.withColumn("first_not_null",coalesce(col("home_phone"),col("mobile_phone"),col("work_phone")))
display(df_final)
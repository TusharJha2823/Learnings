# Databricks notebook source
#Find the missing numbers in the column

data = [
 (1, ),
 (2,),
 (3,),
 (6,),
 (7,),
 (8,)]
df = spark.createDataFrame(data).toDF("id")
df.show()

# COMMAND ----------

from pyspark.sql.functions import col,min,max
df_min_max=df.agg(min(col("id")),max(col("id")))
df_final=spark.range(df_min_max.collect()[0][0],df_min_max.collect()[0][1]+1)
df_final.subtract(df).show()
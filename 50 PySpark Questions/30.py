# Databricks notebook source
data=[(1,1),(2,1),(3,1),(4,2),(5,1),(6,1)]
schema="Id int, Nums int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import *
df=df.withColumn('id1',lit(1)).withColumn('id2',lit(1)).withColumn('id3',lit(1))#.withColumn('id4',lit(1)).withColumn('id5',lit(1))
display(df)
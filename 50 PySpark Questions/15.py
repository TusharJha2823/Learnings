# Databricks notebook source
data=[(1,'Sagar',23),(2,'Alex',34)]
schema="Id int,Name string,Marks int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

data=[(1,'Sagar',[23,34,10]),(2,'Alex',[40,60,20])]
schema="Id int,Name string,Marks array<int>"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col,explode
if df.dtypes[2][1]=='array<int>':
  df_final=df.withColumn("Marks",explode(col("Marks")))
else:
  df_final=df
display(df_final)
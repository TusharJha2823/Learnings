# Databricks notebook source
data=[(1,'Sagar',34),(1,'Sagar',40),(1,'Sagar',34),(2,'Alex',45),(2,'Alex',50)]
schema="ID int,Name string,Marks int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import collect_list,collect_set,col

df_final=df.groupBy(col("ID"),col("Name")).agg(collect_list(col('Marks')))
display(df_final)

# COMMAND ----------

df_final=df.groupBy(col("ID"),col("Name")).agg(collect_set(col('Marks')))
display(df_final)
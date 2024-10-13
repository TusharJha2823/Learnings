# Databricks notebook source
#Handling Null Values in PySpark

# COMMAND ----------

data=[(1,'Sagar',None),(2,None,23.5),(None,None,45.2),(4,'Alex',46.7)]
schema="Id int,Name string,Marks double"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

display(df.dropna())

# COMMAND ----------

display(df.fillna(0,subset=['Marks']))

# COMMAND ----------

from pyspark.sql.functions import mean
mean_value=df.select(mean('Marks')).collect()[0][0]
display(df.fillna(mean_value,subset=['Marks']))
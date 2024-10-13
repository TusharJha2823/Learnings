# Databricks notebook source
data=[(1,1),(2,1),(3,1),(4,2),(5,1),(6,1)]
schema="Id int, Nums int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import lead,col
from pyspark.sql.window import Window
window=Window.orderBy('Id')
df_final=df.withColumn('Nums_1',lead('Nums').over(window)).withColumn('Nums_2',lead('Nums',2).over(window))
df_final.filter((col('Nums')==col('Nums_1')) & (col('Nums')==col('Nums_2'))).select('Id').distinct().show()

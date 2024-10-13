# Databricks notebook source
#Pyspark Challenge: How to keep only the top 2 most frequent values (by job) as it is and replace everything else as ‘Other’ 

# COMMAND ----------

from pyspark.sql import Row
from pyspark.sql.functions import *
from pyspark.sql import Window
# Sample data
data = [
Row(name='John', job='Engineer'),
Row(name='John', job='Engineer'),
Row(name='Mary', job='Scientist'),
Row(name='Bob', job='Engineer'),
Row(name='Bob', job='Engineer'),
Row(name='Bob', job='Scientist'),
Row(name='Sam', job='Doctor'),
Row(name='Sam', job='Doctor'),
Row(name='Sam', job='Doctor'),
Row(name='Sagar', job='Teacher'),

]

# create DataFrame
df = spark.createDataFrame(data)
df.show()

# COMMAND ----------

window_job=Window.partitionBy(col("job"))
df_final=df.withColumn("cnt",count("*").over(window_job)).withColumn("dense_rank",dense_rank().over(Window.orderBy(col("cnt").desc()))).withColumn("job",when(col("dense_rank")<=2,col("job")).otherwise(lit("others"))).drop("cnt","dense_rank")
df_final.show()
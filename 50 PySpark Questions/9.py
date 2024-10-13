# Databricks notebook source
# Write a Pyspark program to format the scientific notation, and show them as decimal numbers
"""e.g.
9.87E-7 >>>>>> 0.0000009870 
"""

df = spark.createDataFrame([(101, 0.000000987), (102, 0.0000554467), (103, 0.00050345678)], ["observation_id", "result"])
df.show()


# COMMAND ----------

from pyspark.sql.functions import format_number,col
df.withColumn("format_result",format_number(col("result"),10)).drop("result").show()
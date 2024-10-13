# Databricks notebook source

"""
Task - Identify rows containing non-numeric values in the "Quantity" column, if any.
"""

from pyspark.sql.types import *
schema = StructType([
  StructField("ProductCode", StringType(), True),
  StructField("Quantity", StringType(), True),
  StructField("UnitPrice", StringType(), True),
  StructField("CustomerID", StringType(), True),
])
 
data = [
  ("P001", 5, 20.0, "C001"),
  ("P002", 3, 15.5, "C002"),
  ("P003", 10, 5.99, "C003"),
  ("P004", 2, 50.0, "C001"),
  ("P005", "eight", 12.75, "C002"),
]
 
df = spark.createDataFrame(data, schema=schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import col
df_final=df.filter(col("Quantity").rlike('^[a-zA-Z]*$'))
df_final.show()

# COMMAND ----------

df_final=df.filter(~col("Quantity").rlike('^[0-9]*$'))
df_final.show()

# COMMAND ----------

df_final=df.withColumn("Quantity1",col("Quantity").cast("int")).filter(col("Quantity1").isNull()).drop(col("Quantity1"))
df_final.show()
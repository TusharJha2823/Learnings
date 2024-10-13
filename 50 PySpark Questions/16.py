# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, sum
from pyspark.sql.window import Window
data = [
(1, "A", 1000),
(2, "B", 2000),
(3, "C", 3000),
(4, "D", 4000),
]

# Define the schema for the DataFrame
schema1 = StructType([
  StructField("ID", IntegerType(), True),
  StructField("Name", StringType(), True),
  StructField("Sal", IntegerType(), True)
])
df2 = spark.createDataFrame(data, schema=schema1)
df2.show()
df2=df2.withColumn("total_sal",sum(col("Sal")).over(Window.orderBy(col("ID")))).select("total_sal")
df2.show()

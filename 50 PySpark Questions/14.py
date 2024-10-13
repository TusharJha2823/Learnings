# Databricks notebook source
"""
Task - You have a dataframe containing columns 'name' and 'phone'. Write a PySpark program to augment this dataframe with two additional columns: 'std_code' and 'landline'. If a value in the 'phone' column is "040-20215632", then 'std_code' and 'landline' should hold "040" and "20215632" respectively.
"""

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField
from pyspark.sql.functions import *


# Define schema
schema = StructType([
 StructField("name", StringType(), True),
 StructField("phone", StringType(), True)
])

# Create data
data = [("ABC", "040-20215632"),
 ("XYZ", "044-23651023"),
 ("PQR", "086-1245678")]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
display(df)

df_final=df.withColumn("std_code",split(col("phone"),'-')[0]).withColumn("landline",split(col("phone"),'-')[1]).drop(col("phone"))
display(df_final)
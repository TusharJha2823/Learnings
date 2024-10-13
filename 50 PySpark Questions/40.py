# Databricks notebook source
"""
find id which is odd number and description is boring

"""

# COMMAND ----------


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType


# Define schema for the DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("movie", StringType(), True),
    StructField("description", StringType(), True),
    StructField("rating", FloatType(), True)
])

# Create data for the DataFrame
data = [
    (1, "War", "great 3D", 8.9),
    (2, "Science", "fiction", 8.5),
    (3, "irish", "boring", 6.2),
    (4, "Ice song", "Fantacy", 8.6),
    (5, "House card", "Interesting", 9.1)
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()


# COMMAND ----------

from pyspark.sql.functions import col,when,trim,lower
df.filter((col("id")%2==1) & (trim(lower(col("description")))=='boring')).show()
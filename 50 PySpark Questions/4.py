# Databricks notebook source
#Write a PySpark program to select every 3rd (nth) row in the dataset

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.window import Window
from pyspark.sql.functions import *


# Define schema for the DataFrame
schema = StructType([
 StructField("emp_id", IntegerType(), True),
 StructField("name", StringType(), True),
 StructField("salary", IntegerType(), True)
])

# Sample employee data
data = [
 (1001, "John Doe", 50000),
 (2001, "Jane Smith", 60000),
 (1003, "Michael Johnson", 75000),
 (4000, "Emily Davis", 55000),
 (1005, "Robert Brown", 70000),
 (6000, "Emma Wilson", 80000),
 (1700, "James Taylor", 65000),
 (8000, "Olivia Martinez", 72000),
 (2900, "William Anderson", 68000),
 (3310, "Sophia Garcia", 67000)
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()



# COMMAND ----------

from pyspark.sql.functions import row_number,lit
from pyspark.sql.window import Window
window_spec=Window.orderBy(lit("1"))
df_final=df.withColumn("rn",row_number().over(window_spec)).filter(col("rn")%3==0).drop(col("rn"))
display(df_final)

# COMMAND ----------

from pyspark.sql.functions import row_number,monotonically_increasing_id
from pyspark.sql.window import Window
window_spec=Window.orderBy(monotonically_increasing_id())
df_final=df.withColumn("rn",row_number().over(window_spec)).filter(col("rn")%3==0).drop(col("rn"))
display(df_final)
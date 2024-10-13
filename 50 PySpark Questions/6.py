# Databricks notebook source
from pyspark.sql.types import *
employees_data = [
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, None),
(4, 'Max', 90000, None)
]


employees_schema = StructType([
StructField("id", IntegerType(), True),
StructField("name", StringType(), True),
StructField("salary", IntegerType(), True),
StructField("managerId", IntegerType(), True)])

df_employee=spark.createDataFrame(employees_data,employees_schema)
df_employee.show()

# COMMAND ----------

from pyspark.sql.functions import col
df_final=df_employee.alias("e1").join(df_employee.alias("e2"),col("e1.managerId")==col("e2.id"),"inner").filter(col("e1.salary")>col("e2.salary"))
df_final.show()
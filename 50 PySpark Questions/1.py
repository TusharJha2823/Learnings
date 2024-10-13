# Databricks notebook source
"""
Task - Write a Spark code snippet to calculate the sum of a column in a DataFrame
"""

# Sample employee data
data = [("John Doe", "john@example.com", 50000.0),
    ("Jane Smith", "jane@example.com", 60000.0),
    ("Bob Johnson", "bob@example.com", 55000.0)]


schema="Name string,email string,salary double"
df=spark.createDataFrame(data,schema)
display(df)


# COMMAND ----------

from pyspark.sql.functions import col,sum
df_final=df.agg(sum(col("salary")).alias("total_salary")).first()[0]
df_final
# Databricks notebook source
"""
Task - Write a Spark code snippet to calculate the sum, min, max, avg, count of a column in a DataFrame
"""

# Sample employee data
data = [("John Doe", "john@example.com", 50000.0),
    ("Jane Smith", "jane@example.com", 60000.0),
    ("Bob Johnson", "bob@example.com", 55000.0)]


schema="Name string,email string,salary double"
df=spark.createDataFrame(data,schema)
display(df)


# COMMAND ----------

from pyspark.sql.functions import *
df_final=df.agg(sum(col("salary")).alias("total_salary"),
                min(col("salary")).alias("minimum_salary"),
                max(col("salary")).alias("maximum_salary"),
                avg(col("salary")).alias("average_salary"),
                count(col("salary")).alias("salary_count"))
df_final.show()
# Databricks notebook source
"""
Write a solution to find the employees who are high earners in each of the departments.

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.



"""

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

emp_data = [
 (1,"Joe", 85000, 1),
 (2,"Henry", 80000, 2),
 (3,"Sam", 60000, 2),
 (4,"Max", 90000, 1),
 (5,"Janet", 69000, 1),
 (6,"Randy", 85000, 1),
 (7,"Will", 70000, 1)
]

emp_schema = StructType([
 StructField("id",IntegerType(),True),
 StructField("name",StringType(),True),
 StructField("salary",IntegerType(),True),
 StructField("dep_id",IntegerType(),True)
])

dep_data = [
 (1,"IT"),
 (2,"Sales")
]

dep_schema = StructType([
 StructField("id",IntegerType(),True),
 StructField("name",StringType(),True)
])

emp_df = spark.createDataFrame(emp_data,emp_schema)
emp_df.show()

dep_df = spark.createDataFrame(dep_data,dep_schema)
dep_df.show()


# COMMAND ----------

window=Window.partitionBy("dep_id").orderBy(col("salary").desc())
emp_df=emp_df.withColumn("rn",dense_rank().over(window))
emp_df.join(dep_df,emp_df.dep_id==dep_df.id,"left").filter(col("rn")<=3).select(dep_df.name.alias("Dept"),emp_df.name.alias("Employee_Nme"),"salary").show()
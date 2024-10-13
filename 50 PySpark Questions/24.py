# Databricks notebook source
"""How to combine many lists to form a PySpark DataFrame?

👉 You can combine multiple lists to form a PySpark DataFrame using the zip function to combine the lists element-wise and then use the SparkSession.createDataFrame() method to create a DataFrame from the zipped data.
"""

𝐒𝐚𝐦𝐩𝐥𝐞 𝐃𝐚𝐭𝐚 :
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

𝐄𝐱𝐩𝐞𝐜𝐭𝐞𝐝 𝐎𝐮𝐭𝐩𝐮𝐭
+-------+---+------------+
|  Name|Age|    City|
+-------+---+------------+
| Alice | 30 |  New York |
|  Bob | 25 | Los Angeles|
|Charlie| 35 |   Chicago |
+-------+---+------------+

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

combined_data=zip(names,ages,cities)

schema=StructType([StructField('Name',StringType(),True),StructField('Ages',StringType(),True),StructField('Cities',StringType(),True)])

df=spark.createDataFrame(combined_data,schema)
display(df)


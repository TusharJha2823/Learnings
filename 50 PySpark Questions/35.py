# Databricks notebook source
"""
Write PySpark Code to get the below output.

Input:

+-------+-----------------+
| Name| Hobbies |
+-------+-----------------+
| Joe|Badminton,Tennis |
| Aman| Football, Cricket |
|Prabhat| Cricket, Movies |
+-------+-----------------+


Output:
+-------+---------+
| Name| col|
+-------+---------+
| Joe|Badminton|
| Joe| Tennis |
| Aman| Football |
| Aman| Cricket |
|Prabhat| Cricket |
|Prabhat| Movies|
+-------+---------+




"""

# COMMAND ----------

data=[('Joe','Badminton, Tennis'),('Aman','Football, Cricket'),('Prabhat',None)]
schema="Name string,Hobbies string"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col,explode,explode_outer
df_final=df.withColumn("Hobbies",split(col("Hobbies"),','))
display(df_final)
df_final.select("Name",explode(col("Hobbies")).alias("Hobbies")).show()

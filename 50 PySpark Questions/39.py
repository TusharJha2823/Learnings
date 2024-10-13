# Databricks notebook source
"""𝗧𝗮𝘀𝗸: Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
"""

from pyspark.sql.functions import *
from pyspark.sql.window import Window


data = [
 (1,"Abbot"),
 (2,"Doris"),
 (3,"Emerson"),
 (4,"Green"),
 (5,"Jeames") 
]

schema = "id int, student string"

df = spark.createDataFrame(data,schema)
df.show()



# COMMAND ----------

from pyspark.sql.functions import col, when

total_count = df.count()
df_final = df.withColumn(
    "id",
    when(col("id") % 2 == 0, col("id") - 1)
    .when((col("id") % 2 == 1) & (col("id") == total_count), col("id"))
    .otherwise(col("id") + 1)
)
df_final=df_final.orderBy("id")
display(df_final)
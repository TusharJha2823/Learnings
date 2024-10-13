# Databricks notebook source
"""Q. Write a PySpark program to remove the extra spaces between the words in the 'Full_name' column and trim any leading or trailing spaces. 

"""


data = [(' Rohan Kumar',), (' Chandrakant   Narayan  ',), (' Jagdish           Singh ',),('  Siva   Kumar  Pillai  ',)]
columns ='Full_Name STRING'

df = spark.createDataFrame(data, columns)
display(df)




# COMMAND ----------

from pyspark.sql.functions import col,regexp_replace,trim
df_final=df.withColumn("Full Name",trim(regexp_replace(col("Full_Name"),' +',' ')))
display(df_final)
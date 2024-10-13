# Databricks notebook source
"""
You are given a fixed length text file. Your task is to create multiple columns from the single row like below.
"""

# COMMAND ----------

data="20230101MUM208001\n20230102DEL219824\n20230103PUN123214"

dbutils.fs.put("dbfs:/FileStore/fixedlenghthfile.txt",data,True)

# COMMAND ----------

from pyspark.sql.functions import col
df=spark.read.text('dbfs:/FileStore/fixedlenghthfile.txt')
fieldlist={'Date': (1,8),'StateCode':(9,3),'PinCode':(12,6)}
for field,(start,length) in fieldlist.items():
    df=df.withColumn(field,substring(col("value"),start,length))
df=df.drop('value')
display(df)
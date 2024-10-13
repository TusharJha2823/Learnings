# Databricks notebook source
#find year,start_week_date,end_week_date,week_num

from pyspark.sql.types import *
data=[(2024,1,'2024-01-01'),
      (2024,1,'2024-01-02'),
      (2024,1,'2024-01-03'),
      (2024,1,'2024-01-04'),
      (2024,1,'2024-01-05'),
      (2024,1,'2024-01-06'),
      (2024,1,'2024-01-07'),
      (2024,2,'2024-01-08'),
      (2024,2,'2024-01-09'),
      (2024,2,'2024-01-10'),
      (2024,2,'2024-01-11'),
      (2024,2,'2024-01-12'),
      (2024,2,'2024-01-13'),
      (2024,2,'2024-01-14')]
schema=StructType([StructField('year',IntegerType(),True),StructField('weeknum',IntegerType(),True),StructField('dates',StringType(),True)])
df=spark.createDataFrame(data,schema)
df.show()


# COMMAND ----------

from pyspark.sql.functions import col,min,max,to_date
df=df.withColumn("dates",to_date(col("dates")))
df.groupBy(col("year"),col("weeknum")).agg(min(col("dates")).alias("start_day_week"),max(col("dates")).alias("end_day_week")).show()
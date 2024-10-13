# Databricks notebook source
"""📢Challenge : Data validation between source and target table """

#Create DataFrame Code :

source_data = [(1,'A'),(2,'B'),(3,'C'),(4,'D'),(5,'E')]
source_schema = ['id','name']
source_df = spark.createDataFrame(source_data,source_schema)
source_df.show()

target_data = [(1,'A'),(2,'B'),(3,'X'),(4,'F'),(6,'G')]
target_schema = ['id','name']
target_df = spark.createDataFrame(target_data,target_schema)
target_df.show()

# COMMAND ----------

from pyspark.sql.functions import *
final_df=source_df.join(target_df,source_df.id==target_df.id,'full')
final_df=final_df.withColumn('result',when(((source_df.id==target_df.id)& (source_df.name==target_df.name)),'matching').\
    when(((source_df.id==target_df.id)& (source_df.name!=target_df.name)),'non-matching').\
    when((source_df.id.isNotNull() & target_df.id.isNull()),'target not present').\
    when((source_df.id.isNull() & target_df.id.isNotNull()),'source not present')).select(coalesce(source_df.id,target_df.id).alias('id'),'result')
display(final_df)
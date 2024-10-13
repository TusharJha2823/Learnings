# Databricks notebook source
#Find out hashtag count for each quote
data = [
    ("Work hard in #silence, let #success make the noise.",),
    ("Be #yourself; everyone else is already taken.",),
    ("The only way to do #greatwork is to #love what you do.",),
    ("#Believe you can and you're #halfway there.",),
    ("The #future belongs to those who #believe in the #beauty of their #dreams.",)
]
df = spark.createDataFrame(data, ["quote"])
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col,split,size
df1=df.withColumn("count_quotes",size(split(col("quote"),'#'))-1)
df1.show(truncate=False)
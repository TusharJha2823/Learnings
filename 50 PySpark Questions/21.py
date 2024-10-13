# Databricks notebook source
#𝐇𝐨𝐰 𝐭𝐨 𝐰𝐫𝐢𝐭𝐞 𝐩𝐲𝐬𝐩𝐚𝐫𝐤 𝐜𝐨𝐝𝐞 𝐟𝐨𝐫 𝐭𝐡𝐢𝐬 ,𝐬𝐮𝐩𝐩𝐨𝐬𝐞 𝐨𝐧 mobile number 10 𝐝𝐢𝐠𝐢𝐭𝐬 𝐚𝐫𝐞 𝐭𝐡𝐞𝐫𝐞 .𝐰𝐫𝐢𝐭𝐞 𝐜𝐨𝐝𝐞 𝐭𝐨 𝐦𝐚𝐬𝐤 𝐨𝐟𝐟 middle 8 𝐝𝐢𝐠𝐢𝐭𝐬 𝐚𝐧𝐝 𝐬𝐡𝐨𝐰 𝐨𝐧𝐥𝐲 first and last 2 𝐝𝐢𝐠𝐢𝐭s


from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Sample data with credit card numbers
data = [("8765453791",),
    ("8794637281",),
    ("9988776655",)]

# Create a DataFrame with sample data
df = spark.createDataFrame(data, ["mobile_number"])

def mask_mobile_number(mobile_number):
  return mobile_number[0:2]+'*'*6+mobile_number[-2:]

mask_mobile_number=udf(mask_mobile_number,StringType())

df_final=df.withColumn("masked_mobile_number",mask_mobile_number('mobile_number'))
display(df_final)

# COMMAND ----------


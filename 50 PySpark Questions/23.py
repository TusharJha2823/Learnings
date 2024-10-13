# Databricks notebook source
"""
write a spark program to return the shipped and delivered rate for each order. Return order_id, shipped percentage, and delivered percentage.
"""

# COMMAND ----------

from pyspark.sql.functions import count, when,col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
# Sample data for demonstration
data = [
 (1, "Shipped", "2024-04-01"),
 (1, "Shipped", "2024-04-02"),
 (2, "Delivered", "2024-04-01"),
 (2, "Delivered", "2024-04-02"),
 (2, "Shipped", "2024-04-03"),
 (3, "Shipped", "2024-04-01"),
 (3, "Delivered", "2024-04-02"),
 (3, "Delivered", "2024-04-03")
]

# Define schema for the DataFrame
schema = StructType([
 StructField("order_id", IntegerType(), False),
 StructField("order_status", StringType(), True),
 StructField("order_date", StringType(), True)
])

# Create DataFrame
orders_df = spark.createDataFrame(data, schema)
display(orders_df)


# COMMAND ----------

df_order_count=orders_df.groupBy("order_id").agg(count("*").alias("total_orders"))
df_shipped_order_count=orders_df.filter(orders_df.order_status=="Shipped").groupBy("order_id").agg(count("*").alias("shipped_orders"))
df_delivered_order_count=orders_df.filter(orders_df.order_status=="Delivered").groupBy("order_id").agg(count("*").alias("delivered_orders"))
order_status_count=df_order_count.join(df_shipped_order_count,"order_id","left").join(df_delivered_order_count,"order_id","left").fillna(0)
display(order_status_count)
df_final=order_status_count.withColumn("shipped_percentage",(col("shipped_orders")/col("total_orders"))*100)\
  .withColumn("delivered_percentage",(col("delivered_orders")/col("total_orders"))*100).select("order_id","shipped_percentage","delivered_percentage")
display(df_final)
# Databricks notebook source
#Find the origin and the destination of each customer.



flights_data = [(1,'Flight2' , 'Delhi' , 'Hyderabad'),
(1,'Flight1' , 'Hyderabad' , 'Kochi'),
(1,'Flight3' , 'Kochi' , 'Mangalore'),
(2,'Flight1' , 'Mumbai' , 'Ayodhya'),
(2,'Flight2' , 'Ayodhya' , 'Gorakhpur')
]

schema = "cust_id int, flight_id string , origin string , destination string"
flights_df = spark.createDataFrame(flights_data,schema)
display(flights_df)

# COMMAND ----------

from pyspark.sql.functions import last,first
final_df=flights_df.orderBy('cust_id','flight_id').groupBy('cust_id').agg(first('origin').alias('origin'),last('destination').alias('destination'))
display(final_df)
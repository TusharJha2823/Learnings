# Databricks notebook source
#Find out number of rows in each joins

# COMMAND ----------

df_1 = spark.createDataFrame(
    [(1,),
     (2,),
     (3,),
     (1,),
     (1,),
     (1,),
     (None,),
      (None,)
     ], 
    schema="id_1 int"
)
df_2 = spark.createDataFrame(
  [(1,), 
   (1,),
   (2,),
    (None,)
   ], schema="id_2 int")

display(df_1)
display(df_2)

# COMMAND ----------

df_final=df_1.join(df_2,df_1.id_1==df_2.id_2,"left")
df_final.count()
# Databricks notebook source
"""Question : To get the below output by using pyspark?
Input:
ID col1  col2
1   A   10
1   B   20
2   A   30
2   B   40

Output: 
ID  A  B
1  10 20
2  30 40

"""

# COMMAND ----------

data=[(1,'A',10),(2,'A',20),(1,'B',30),(2,'B',40)]
schema="ID int,col1 string,col2 int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col,first,last
df_final=df.groupBy(col("ID")).pivot("col1").agg(first('col2'))
display(df_final)

# COMMAND ----------

df_final.melt('ID',['B','A'],'col1','col2').show()
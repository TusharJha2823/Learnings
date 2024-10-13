# Databricks notebook source
#Add file_name in the column in the dataframe

# COMMAND ----------

file_1=""" Id,Name
           1,'Sagar'
           2,'Shivam'
           """
dbutils.fs.put('/FileStore/tables/20/CSE.csv',file_1)


# COMMAND ----------

file_1=""" Id,Name
           11,'Alex'
           21,'David'
           """
dbutils.fs.put('/FileStore/tables/20/IT.csv',file_1)

# COMMAND ----------

file_1=""" Id,Name
           111,'Kim'
           211,'Shivani'
           """
dbutils.fs.put('/FileStore/tables/20/Bio.csv',file_1)

# COMMAND ----------

from pyspark.sql.functions import input_file_name,split,replace
df=spark.read.format('csv').option('infershcema',True).option('header',True).load('/FileStore/tables/20/').\
         withColumn('department_name',split(split(input_file_name(),'/')[4],'\.')[0])
df.show()
# Databricks notebook source
"""
How to handle hashtag#comma in the hashtag column value of a hashtag CSV file while readin
"""

# COMMAND ----------

data="""
ID,NAME,address,contact
1,JAMES,MUMBAI,9999999999
2,ROBBERT,BANGLORE,8888888888
3,MARIA,GolfLinks,DELHI,7777777777
4,JEFF,Hyderabad,7878787987
"""
dbutils.fs.put('/FileStore/tables/question_13.csv',data,True)

# COMMAND ----------



# COMMAND ----------

df=spark.read.format('csv').option('header',True).option('inferschema',True).option('sep','|').load('/FileStore/tables/question_13.csv')
display(df)
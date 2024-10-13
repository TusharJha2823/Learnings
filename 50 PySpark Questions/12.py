# Databricks notebook source

"""
Given the table LogInfo containing login and logout data for Leetflex accounts. It also contains the IP address from which the account logged in and out.

Task -
Find the accounts that should be banned. An account should be banned if it was logged in from two different IP addresses at any moment.
"""
data = [
 (1, 1, "2021-02-01 09:00:00", "2021-02-01 09:30:00"),
 (1, 2, "2021-02-01 08:00:00", "2021-02-01 11:30:00"),
 (2, 6, "2021-02-01 20:30:00", "2021-02-01 22:00:00"),
 (2, 7, "2021-02-02 20:30:00", "2021-02-02 22:00:00"),
 (3, 9, "2021-02-01 16:00:00", "2021-02-01 16:59:59"),
 (3, 13, "2021-02-01 17:00:00", "2021-02-01 17:59:59"),
 (4, 10, "2021-02-01 16:00:00", "2021-02-01 17:00:00"),
 (4, 11, "2021-02-01 17:00:00", "2021-02-01 17:59:59")
]

# DataFrame
df = spark.createDataFrame(data, ["account_id", "ip_address", "login", "logout"])
df.show()


# COMMAND ----------

from pyspark.sql.functions import col,lead
from pyspark.sql.window import Window
window_spec=Window.partitionBy(col("account_id")).orderBy(col("login"))
df_final=df.withColumn("next_login",lead(col("login")).over(window_spec)).filter(col("logout")>=col("next_login")).select(col("account_id")).distinct()
df_final.show()
# Databricks notebook source
json_sample="""{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}"""

dbutils.fs.put("/FileStore/tables/pyspark_questions/18.json",json_sample,True)

# COMMAND ----------

from pyspark.sql.functions import *
df=spark.read.format('json').option('multiline',True).load('/FileStore/tables/pyspark_questions/18.json')
df_final=df.withColumn("new_batters",explode("batters.batter")).withColumn("new_topping",explode("topping")).drop("batters","topping").select("id","name","ppu","type",col("new_batters.id").alias("batters_id"),col("new_batters.type").alias("batters_type"),col("new_topping.id").alias("topping_id"),col("new_topping.type").alias("topping_type"))
display(df_final)

# COMMAND ----------

#output
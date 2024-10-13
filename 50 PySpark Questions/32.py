# Databricks notebook source
#How do you deal with inconsistent or erroneous data formats (e.g., date formats, currency symbols?


# COMMAND ----------

data = [
 ('2022-01-01', '$100.50'),
 ('Jan 15, 2022', '€200.75'),
 ('03/20/22', '£150.20'),
 ('2022-05-13', '¥300.00')
]
columns = ['date', 'amount']

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Print the original DataFrame
print("Original DataFrame:")
display(df)



# COMMAND ----------

from pyspark.sql.functions import col, to_date, when, regexp_replace

df_final = df.withColumn(
    "date",
    when(col("date").contains("-"), to_date(col("date"), "yyyy-MM-dd"))
    .when(col("date").contains("/"), to_date(col("date"), "MM/dd/yy"))
    .otherwise(to_date(col("date"), "MMM dd, yyyy")),
).withColumn('amount',regexp_replace(col('amount'),'[^\d.]','').cast('float'))
df_final.show()
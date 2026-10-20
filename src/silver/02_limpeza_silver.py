# Databricks notebook source
from pyspark.sql.functions import col

bronze_table_name = "market_prices_db.bronze.wfp_raw_prices"
silver_table_name = "market_prices_db.silver.cleaned_market_prices"

df_bronze = spark.read.table(bronze_table_name)

df_renamed = (df_bronze
    .withColumnRenamed("adm0_name", "country")
    .withColumnRenamed("mkt_name", "market")
    .withColumnRenamed("cm_name", "commodity")
    .withColumnRenamed("mp_price", "price")
)

df_silver = (df_renamed
    .filter(col("country").isNotNull() & col("market").isNotNull() & col("price").isNotNull())
    .withColumn("price", col("price").cast("double"))
    .select("country", "market", "commodity", "price")
    .dropDuplicates()
)

df_silver.write.format("delta").mode("overwrite").saveAsTable(silver_table_name)

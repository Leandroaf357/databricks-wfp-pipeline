# Databricks notebook source
from pyspark.sql.functions import current_timestamp, col

raw_data_path = "/Volumes/market_prices_db/bronze/landing_zone/wfp_market_food_prices.csv"
bronze_table_name = "market_prices_db.bronze.wfp_raw_prices"

df_raw = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(raw_data_path)
df_bronze = (df_raw
             .withColumn("ingestion_timestamp", current_timestamp())
             .withColumn("source_file", col("_metadata.file_path")))

df_bronze.write.format("delta").mode("append").saveAsTable(bronze_table_name)

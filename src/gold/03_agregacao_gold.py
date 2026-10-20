# Databricks notebook source
from pyspark.sql.functions import avg, min, max, count, round

silver_table_name = "market_prices_db.silver.cleaned_market_prices"
gold_table_name = "market_prices_db.gold.agg_market_prices_summary"

df_silver = spark.read.table(silver_table_name)

df_gold = df_silver.groupBy("country", "market", "commodity").agg(
    round(avg("price"), 2).alias("avg_price"),
    min("price").alias("min_price"),
    max("price").alias("max_price"),
    count("price").alias("price_records_count")
)

df_gold.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(gold_table_name)

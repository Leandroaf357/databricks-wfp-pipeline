# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# Databricks notebook source
from pyspark.sql.functions import avg, min, max, count, round

silver_table_name = "market_prices_db.silver.cleaned_market_prices"
gold_table_name = "market_prices_db.gold.agg_market_prices_summary"

df_silver = spark.read.table(silver_table_name)

# GOLD: Agregações numéricas prontas para negócio/Power BI
df_gold = df_silver.groupBy("country", "market", "commodity").agg(
    round(avg("price"), 2).alias("avg_price"),
    min("price").alias("min_price"),
    max("price").alias("max_price"),
    count("price").alias("price_records_count")
)

# GOLD: Gravação da tabela agregada com sobrescrita de esquema permitida
df_gold.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(gold_table_name)
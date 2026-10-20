# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# Databricks notebook source
from pyspark.sql.functions import col

bronze_table_name = "market_prices_db.bronze.wfp_raw_prices"
silver_table_name = "market_prices_db.silver.cleaned_market_prices"

df_bronze = spark.read.table(bronze_table_name)

# SILVER 1: Traduzir as colunas técnicas da WFP para a nossa linguagem de negócio
df_renamed = (df_bronze
    .withColumnRenamed("adm0_name", "country")
    .withColumnRenamed("mkt_name", "market")
    .withColumnRenamed("cm_name", "commodity")
    .withColumnRenamed("mp_price", "price")
)

# SILVER 2: Limpeza estruturada e filtro de nulos
df_silver = (df_renamed
    .filter(col("country").isNotNull() & col("market").isNotNull() & col("price").isNotNull())
    .withColumn("price", col("price").cast("double"))
    # Selecionamos APENAS as colunas que a nossa camada Gold precisa, ignorando o resto do CSV
    .select("country", "market", "commodity", "price")
    .dropDuplicates()
)

# SILVER 3: Gravação dos dados limpos
df_silver.write.format("delta").mode("overwrite").saveAsTable(silver_table_name)
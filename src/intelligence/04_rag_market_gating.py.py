# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# Databricks notebook source
from pyspark.sql.functions import concat_ws, col, lit

gold_table_name = "market_prices_db.gold.agg_market_prices_summary"
intelligence_table_name = "market_prices_db.intelligence.rag_knowledge_base"

df_gold = spark.read.table(gold_table_name)

# INTELLIGENCE: Estruturação de dados textuais para contexto de IA/RAG
df_rag = df_gold.withColumn(
    "page_content",
    concat_ws(" - ", 
        concat_ws(": ", lit("Country"), col("country")),
        concat_ws(": ", lit("Market"), col("market")),
        concat_ws(": ", lit("Commodity"), col("commodity")),
        concat_ws(": ", lit("Average Price"), col("avg_price").cast("string"))
    )
)

# INTELLIGENCE: Gravação da base de conhecimento com sobrescrita de esquema permitida
df_rag.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(intelligence_table_name)
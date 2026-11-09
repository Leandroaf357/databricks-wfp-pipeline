# 🌍 WFP Global Food Market Prices — Pipeline & Dashboard

Pipeline completo de engenharia e análise de dados baseado na arquitetura Medallion (Bronze, Silver e Gold), processado no Databricks e visualizado num painel executivo no Power BI via DirectQuery.

---

## 📊 Painel Executivo

![WFP Dashboard](dashboard.png)

> **Destaques da Visualização:**
> - Conexão em tempo real via **DirectQuery** à camada Gold do Delta Lake.
> - Métricas em cartões KPI estilizados com ícones vetoriais customizados em SVG.
> - Análise de dispersão por mercados e ranking volumétrico das principais *commodities*.

---

## 🏗️ Arquitetura da Solução

```text
[ Fonte WFP (CSV) ]
        │
        ▼ (Ingestão PySpark)
[ Camada Bronze ] ── Raw Ingestion & Schema Definition
        │
        ▼ (Limpeza, Deduplicação & Validação de Esquema)
[ Camada Silver ] ── Delta Lake Cleansed Data
        │
        ▼ (Agregações de Negócio & Modelagem Analítica)
[ Camada Gold ] ── agg_market_prices_summary (Delta Table)
        │
        ▼ (DirectQuery / Personal Access Token)
[ Power BI Desktop ] ── Executive Cyber Dashboard

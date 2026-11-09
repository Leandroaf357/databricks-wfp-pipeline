# 🌍 WFP Global Food Market Prices — End-to-End Medallion Pipeline & Dashboard

Pipeline completo de Engenharia e Análise de Dados baseado no conjunto de dados global de preços de alimentos do **World Food Programme (WFP)**. O projeto implementa uma arquitetura **Medallion (Bronze, Silver e Gold)** com **Delta Lake** e **Databricks Asset Bundles (DABs)**, integrado a um painel executivo interativo no **Power BI** via conexão **DirectQuery**.

---

## 📊 Painel Executivo (Power BI)

<div align="center">
  <img src="Captura de tela 2026-11-09 154305.png" alt="WFP Global Food Market Prices Dashboard" width="100%">
</div>

> **Destaques do Relatório:**
> * **Conexão DirectQuery em Tempo Real:** Consultas dinâmicas direcionadas à camada Gold no Delta Lake sem persistência redundante de dados no relatório.
> * **Design e Estilo Cyber:** Interface em tema escuro com destaques em ciano (`#00F0FF`) e cartões de KPI construídos com ícones vetoriais SVG customizados.
> * **Governança & Rastreabilidade:** Indicadores de estado de ligação auditados via Unity Catalog.
> * **Análise Multidimensional:** Filtros hierárquicos por país e *commodity*, distribuição de preços médios por volume de mercado e dispersão analítica.

---

## 🏗️ Arquitetura da Solução

```text
       [ Fonte Pública WFP (CSV / Dados de Mercado) ]
                             │
                             ▼ (Ingestão PySpark com Controlo de Esquema)
  ╔═════════════════════════════════════════════════════════════════╗
  ║                        CAMADA BRONZE                            ║
  ║  - Ingestão raw em formato Delta Lake                          ║
  ║  - Preservação do histórico e metadados de ingestão            ║
  ╚═════════════════════════════════════════════════════════════════╝
                             │
                             ▼ (Tratamento, Tipagem e Limpeza)
  ╔═════════════════════════════════════════════════════════════════╗
  ║                        CAMADA SILVER                            ║
  ║  - Validação de esquemas, datas e valores monetários           ║
  ║  - Tratamento de nulos e deduplicação de registos de mercado    ║
  ╚═════════════════════════════════════════════════════════════════╝
                             │
                             ▼ (Agregações de Negócio & Otimização)
  ╔═════════════════════════════════════════════════════════════════╗
  ║                         CAMADA GOLD                             ║
  ║  - Tabela: agg_market_prices_summary                           ║
  ║  - Agregações volumétricas por país, mercado e produto         ║
  ╚═════════════════════════════════════════════════════════════════╝
                             │
                             ▼ (DirectQuery / PAT Authentication)
  ╔═════════════════════════════════════════════════════════════════╗
  ║                      POWER BI DESKTOP                           ║
  ║  - Dashboard Analítico & Modelagem DAX                          ║
  ╚═════════════════════════════════════════════════════════════════╝

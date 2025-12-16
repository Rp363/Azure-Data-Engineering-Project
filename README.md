# 🚀 Azure Data Engineering Project  
**End-to-End Data Pipeline using Azure Data Factory & Databricks (Silver–Gold Architecture)**

---

## 📌 Project Overview

This project demonstrates an **end-to-end Azure Data Engineering pipeline** built using **Azure Data Factory (ADF)** and **Databricks**, following a **layered data architecture (Silver → Gold)**.

The objective of this project is to ingest data from a **SQL source**, apply transformations, and generate **analytics-ready datasets** using industry-standard Azure tools.

This project is designed with a **real-world, production-oriented approach**, making it easy for recruiters and hiring managers to understand.

---

## 🏗️ Architecture Overview

**Source → Silver → Gold**

- **Source**: SQL Database (connected via ADF)
- **Silver Layer**: Cleaned and standardized data
- **Gold Layer**: Curated, business-ready data
- **Orchestration**: Azure Data Factory
- **Transformation**: Databricks (Notebooks & Jinja Templates)

---

## 🔧 Tech Stack

- **Azure Data Factory (ADF)**
- **Azure Databricks**
- **SQL Database**
- **PySpark / SQL**
- **Jinja Templates**

---

## 🔄 Data Pipeline Flow

### **1️⃣ Source Ingestion (ADF)**

- Data is ingested directly from a **SQL Database** using **ADF pipelines**
- Source queries and connections are managed within ADF
- This keeps the project **secure, modular, and reusable**

#### 📸 ADF Pipeline Screenshot
<img src="screenshots/adf_pipeline.png" width="800"/>

---

### **2️⃣ Silver Layer – Data Cleaning & Standardization**

- Raw data is transformed into a **structured and consistent format**
- Schema alignment and basic data quality checks are applied
- Acts as a **trusted intermediate layer** for downstream processing

---

### **3️⃣ Gold Layer – Business-Ready Data**

- Gold layer focuses on **analytics-ready outputs**
- Implemented using:
  - **Databricks notebooks**
  - **Jinja templates** for reusable and parameterized logic
- Designed to support reporting and BI use cases

#### 📸 Gold Layer Output Screenshot
<img src="screenshots/gold_layer_output.png" width="800"/>

---

## 🧠 Key Design Decisions

- **ADF for orchestration**, Databricks for transformations
- **Layered architecture** for scalability and easier debugging
- **Jinja templates** to avoid hardcoding and enable reusability
- **No source SQL scripts stored** — pipelines can connect to any database

---

## 📂 Repository Structure

```text
├── source/
│   └── adf_pipelines
├── silver/
│   └── databricks_notebooks
├── gold/
│   ├── jinja_templates
│   └── databricks_notebooks
├── screenshots/
│   ├── adf_pipeline.png
│   └── gold_layer_output.png
└── README.md

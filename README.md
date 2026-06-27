# Airbnb Market Intelligence & Pricing Analytics Platform

An end-to-end **Big Data Analytics** project that builds a complete ETL pipeline, Data Warehouse, Data Governance framework, Business Analytics layer, and Tableau dashboard using the Airbnb NYC 2019 dataset.

---

## Project Overview

This project demonstrates the complete data analytics lifecycle:

- Extract Airbnb listing data
- Transform and clean the dataset using PySpark
- Design a Star Schema data warehouse
- Load processed data into SQLite
- Perform Data Governance and validation
- Execute Business Intelligence queries
- Conduct Statistical (A/B) Analysis
- Visualize insights using Tableau

---

## Technology Stack

- Python
- PySpark
- SQLite
- Pandas
- SQL
- Tableau

---

## Dataset

**Dataset:** Airbnb NYC 2019

Contains information such as:

- Listing ID
- Host ID
- Price
- Minimum Nights
- Number of Reviews
- Availability (365 Days)
- Location Information

---

# Project Architecture

```
                Airbnb Dataset (CSV)
                        │
                        ▼
              PySpark ETL Pipeline
       (Extract → Transform → Clean)
                        │
                        ▼
               Star Schema Model
      (Fact Table + Dimension Tables)
                        │
                        ▼
             SQLite Data Warehouse
                        │
                        ▼
             Data Governance Layer
      (Validation & Quality Checks)
                        │
                        ▼
             Business Analytics Layer
        (SQL Queries & A/B Testing)
                        │
                        ▼
              Tableau Dashboard
```

---

# Project Structure

```
airbnb-analytics/
│
├── analysis/
│   ├── business_queries.py
│   ├── ab_testing.py
│   ├── check_tables.py
│   ├── export_dashboard.py
│   └── save_experiment.py
│
├── dashboard/
│   └── Tableau Dashboard
│
├── data/
│   └── AB_NYC_2019.csv
│
├── governance/
│   └── validate_data.py
│
├── spark/
│   ├── etl_star_schema.py
│   └── load_to_sql.py
│
├── sql/
│   ├── airbnb.db
│   └── schema.sql
│
├── requirements.txt
└── README.md
```

---

# ETL Pipeline

### Extract

- Read Airbnb CSV dataset using PySpark.

### Transform

- Data Cleaning
- Handle Missing Values
- Type Conversion
- Select Relevant Features
- Build Star Schema

### Load

- Load processed data into SQLite Data Warehouse.

---

# Star Schema Design

## Fact Table

- Fact_Listing

Measures:

- Price
- Number of Reviews
- Availability
- Minimum Nights

---

## Dimension Tables

- Listing
- Host
- Location

The Star Schema enables faster analytical queries and better BI performance.

---

# Data Governance

Validation checks include:

- Missing Values
- Duplicate Records
- Negative Prices
- Invalid Availability
- Data Consistency

These checks improve data quality before analysis.

---

# Business Analytics

Implemented SQL queries such as:

- Average Listing Price
- Top Hosts by Number of Listings
- Average Number of Reviews

---

# Statistical Analysis

Performed A/B Testing to compare pricing groups using:

- Hypothesis Testing
- T-Test
- P-Value
- Statistical Decision Making

---

# Tableau Dashboard

Dashboard includes:

### Price Distribution


<img width="2092" height="1506" alt="Price Distribution" src="https://github.com/user-attachments/assets/618ede0b-f8b6-4b41-941d-bd8acd46cd6d" />


Visualizes the distribution of Airbnb listing prices.

### Reviews vs Price


<img width="2092" height="1506" alt="Review vs Price" src="https://github.com/user-attachments/assets/dec54bdc-7907-4bea-9792-b63802b3be16" />


Shows the relationship between listing price and customer reviews.

### Availability Impact


<img width="2092" height="1506" alt="Availability Imapct" src="https://github.com/user-attachments/assets/969a07bc-b579-4100-b893-66b26ace6d05" />


Analyzes how listing availability affects pricing.

### Governance & KPI Summary


<img width="1118" height="490" alt="Governance   KPI Summary" src="https://github.com/user-attachments/assets/23e003bf-70dd-4d23-902f-a05c9cdb10f5" />


Displays key metrics:

- Total Listings
- Average Price
- Average Reviews
- Average Availability


### Dashboard


<img width="2458" height="1616" alt="Airbnb Analytics" src="https://github.com/user-attachments/assets/ffebb608-5028-4918-bbae-e989f842886b" />


---

# Key Insights

- Most Airbnb listings fall within the lower price range.
- Premium-priced listings are relatively rare.
- Lower-priced listings generally receive more reviews.
- Average listing price is approximately **$153**.
- Dataset contains **48,721** listings after processing.

---

# How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/airbnb-analytics.git

cd airbnb-analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL

```bash
cd spark

python etl_star_schema.py

python load_to_sql.py
```

### Run Data Validation

```bash
cd governance

python validate_data.py
```

### Run Business Queries

```bash
cd analysis

python business_queries.py

python ab_testing.py
```

### Open Tableau Dashboard

Import the processed dataset or SQLite database into Tableau and open the dashboard workbook.

---

# Future Improvements

- Deploy warehouse on Snowflake
- Automate ETL using Apache Airflow
- Integrate live Airbnb API data
- Add predictive pricing model using Machine Learning
- Deploy interactive dashboard using Streamlit

---

# Learning Outcomes

Through this project, I gained practical experience in:

- Big Data Processing
- ETL Pipeline Development
- Data Warehousing
- Star Schema Modeling
- Data Governance
- SQL Analytics
- Statistical Testing
- Tableau Dashboard Development

---

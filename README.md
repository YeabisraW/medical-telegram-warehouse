# Medical Telegram Data Warehouse: Production-Grade Pipeline
Author: YeabisraW
Domain: Medical Supply Chain & Sentiment Analytics
# Business Problem
In emerging markets, critical medical supply chain data is often fragmented across social messaging platforms like Telegram. For stakeholders in the finance and pharmaceutical sectors, this lack of structured data creates operational risk and information asymmetry. This project reduces that risk by transforming unstructured real-time conversations into a high-integrity analytical warehouse.
# Solution Overview
A production-ready data engineering pipeline that automates the lifecycle of medical data:
Extraction: High-concurrency scraping of Telegram channels via Telethon.
Transformation: Modular SQL modeling using dbt (Data Build Tool) to implement a Star Schema.
Orchestration: Asset-based workflow management using Dagster.
Delivery: Backend analytics served via FastAPI and visualized through a Streamlit dashboard.
# Key Results
Throughput: Successfully ingested and processed 1,420+ messages from target channels.
Reliability: Implemented a CI/CD pipeline with automated quality checks, ensuring 100% schema validty on every push.
Insight: Real-time sentiment tracking (current average: 0.68) for pharmaceutical product reception.
# Quick Start
# 1. Clone the repository
git clone https://github.com/YeabisraW/medical-telegram-warehouse.git
cd medical-telegram-warehouse
# 2. Install dependencies
pip install -r requirements.txt
# 3. Start the Analytical API
uvicorn api.main:app --reload
# 4. Launch the Dashboard
streamlit run dashboard.py
# Project Structure
├── .github/workflows/  # CI/CD (GitHub Actions)
├── api/                # FastAPI Analytical Layer
├── dbt_project/        # SQL Transformations (Star Schema)
├── orchestration/      # Dagster Assets & Pipelines
├── scripts/            # Data Scraping (Telethon)
├── dashboard.py        # Streamlit Frontend
└── requirements.txt    # Dependency Management
# Engineering Excellence
Code Quality: Refactored using Type Hints and modular utility functions for maintainability.
Risk Mitigation: The API features a resilient failover mode (Mock Provider) to ensure dashboard availability during database maintenance.
Transparency: Integrated Dagster for clear asset lineage, providing auditors with a transparent view of data provenance.
# Future Improvements
Containerization: Full Docker-Compose deployment for environment parity.
Model Explainability: Integration of SHAP values for sentiment classification to provide "Human-in-the-loop" transparency.
Real-time Alerts: Webhook notifications for anomalous spikes in sentiment or medical product mentions.
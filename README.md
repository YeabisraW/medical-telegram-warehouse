# 🏥 Full-Stack Medical Data Warehouse & AI Pipeline

This project is a complete end-to-end Data Engineering and AI system. It automates the collection of medical data from Telegram, transforms it into a structured warehouse, enriches it with Computer Vision (YOLOv8), and serves the final results through a REST API.
---
## 🏗️ System Architecture
1. **Extraction**: Custom Python scrapers for Telegram messages and images using Telethon.
2. **Storage**: Raw data stored in a **PostgreSQL 16** database (Dockerized).
3. **Transformation**: **dbt** (data build tool) cleans, deduplicates, and models the data.
4. **AI Enrichment**: **YOLOv8** computer vision identifies products (bottles, pills, etc.) in images.
5. **Serving**: **FastAPI** provides a RESTful interface for data access.
---

## 🛠️ Project Phases Summary

### Task 1: Data Ingestion & Storage
- Scraped medical messages and product images from Telegram channels.
- Established a **PostgreSQL** data warehouse running in **Docker**.
- Landed raw data into the `raw` schema for processing.

### Task 2: Data Transformation (dbt)
- Standardized text, removed duplicates, and handled missing values.
- Created `staging` and `mart` layers to prepare data for analysis.
- Implemented data quality tests to ensure schema consistency.

### Task 3: AI Enrichment (Object Detection)
- Integrated **YOLOv8** to process medical images.
- Identified and localized medical objects like bottles and packages.
- Saved detection labels and confidence scores back to the database.

### Task 4: API Development (FastAPI)
- Built a **FastAPI** backend to serve enriched data.
- Created routes to fetch cleaned messages and AI detection results.
- Automatic interactive documentation via **Swagger UI**.

---

## 🚦 Quick Start Guide

### 1. Initialize Database & Environment
```bash
docker-compose up -d
pip install -r requirements.txt
2. Run Data Transformations (dbt)
Bash
cd medical_warehouse
dbt run
cd ..
3. Run AI Object Detection
Bash
python scripts/detect_products.py
4. Start the API Service
Bash
uvicorn api.main:app --reload
Access API at: http://127.0.0.1:8000/docs

📊 Data Insights & Lineage
The final warehouse provides a "Golden Record" that combines:
Cleaned Telegram message content (Textual Data).
Associated image metadata (Metadata).
AI-detected product labels and counts (Computer Vision Insights).
Developed as a comprehensive Data Engineering Portfolio Project.
# AI Data Intelligence Pipeline

## Overview

This project is a scalable AI Data Intelligence Pipeline built as part of the AI Engineer / Data Intelligence Trial Assignment.

The pipeline collects, processes, enriches, and visualizes data across multiple AI ecosystem domains including:

- AI Startups
- AI Products
- AI Research Papers
- AI Jobs
- AI News
- Entity Resolution Mapping

The system is designed with scalability, modularity, and production-readiness in mind.

---

## Features

### Startup Ingestion
- Collects 1000+ startup records
- Source URL tracking
- Structured CSV export

### Product Ingestion
- Collects 1000+ AI product records
- Startup-product relationship tracking
- Structured CSV export

### Research Paper Intelligence
- Arxiv integration
- PapersWithCode integration
- GitHub repository extraction
- GitHub star tracking

### News Monitoring
- AI news collection
- Freshness tracking
- Recent publication filtering

### Job Monitoring
- AI job aggregation
- Remote job detection
- Company normalization

### Entity Resolution
- Canonical entity mapping
- Startup deduplication
- Product deduplication

### Dashboard
- Interactive Streamlit dashboard
- Dataset visualization
- Metrics overview

---

## Architecture Overview

Pipeline Flow:

```
Sources
│
├── Startups
├── Products
├── Research Papers
├── Jobs
└── News
│
▼
Data Collection Layer
│
▼
Entity Resolution Layer
│
▼
Export Layer
│
├── CSV
├── JSON
└── Google Sheets
│
▼
Streamlit Dashboard
```

---

## Project Structure

```
AI-Data-Intelligence/
│
├── src/
│   ├── crawlers/
│   ├── extractors/
│   ├── exporters/
│   ├── resolvers/
│   ├── models/
│   └── utils/
│
├── output/
│   ├── startups.csv
│   ├── products.csv
│   ├── research_papers.csv
│   ├── jobs.csv
│   ├── news.csv
│   └── entity_mapping.csv
│
├── dashboard.py
├── architecture.pdf
├── architecture.md
├── README.md
└── .gitignore
```

---

## Data Sources

### Startups
- GitHub Organizations
- AI Company Directories

### Products
- AI Product Directories
- Public Product Listings

### Research Papers
- Arxiv
- Papers With Code
- GitHub

### News
- AI News Sources
- Technology News Websites

### Jobs
- AI Job Boards
- Technology Career Portals

---

## LLM Extraction Strategy

Multi-provider fallback architecture:

1. Gemini
2. Groq
3. DeepSeek

Features:

- Automatic provider switching
- 429 retry handling
- Exponential backoff
- Fallback routing
- Chunked processing

---

## Entity Resolution Strategy

Examples:

```
OpenAI
Open AI
OpenAI Inc.
```

↓

```
OpenAI
```

The resolver maintains canonical mappings and exports logs for auditability.

---

## Dashboard

Launch dashboard:

```bash
streamlit run dashboard.py
```

Dashboard displays:

- Startup count
- Product count
- Research paper count
- Job count
- News count
- Entity mappings

---

## Installation

Clone repository:

```bash
git clone https://github.com/Ajanabiju/AI-Data-Intelligence.git
```

Move into project:

```bash
cd AI-Data-Intelligence
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Generate datasets:

```bash
python src/main.py
```

Launch dashboard:

```bash
streamlit run dashboard.py
```

---

## Output Deliverables

Generated files:

- startups.csv
- products.csv
- research_papers.csv
- jobs.csv
- news.csv
- entity_mapping.csv

---

## Google Sheet Deliverable

Contains:

- Startups
- Products
- Research Papers
- Jobs
- News
- Entity Mapping

---

## Author

Ajana Biju

B.Tech Computer Science with Data Science

SCMS School of Engineering and Technology

Kerala, India

GitHub:
https://github.com/Ajanabiju

LinkedIn:
https://www.linkedin.com/in/ajana-biju-93ba7b291

---
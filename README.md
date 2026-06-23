# AI Data Intelligence Pipeline

## Overview

This project was developed as part of the AI Engineer / Data Intelligence Trial Assignment.

The system collects, processes, enriches, and exports intelligence data across multiple domains of the AI ecosystem, including startups, products, research papers, jobs, and news. The pipeline also includes entity resolution, GitHub metrics extraction, and dashboard-based visualization.

---

## Features

### Startup Intelligence

* Collects 1000+ startup records
* Source tracking
* Structured CSV export

### Product Intelligence

* Collects 1000+ product records
* Product popularity metrics
* Structured CSV export

### Research Paper Intelligence

* Arxiv integration
* Papers With Code integration
* GitHub repository extraction
* GitHub stars tracking
* Publication date extraction

### AI Jobs Monitoring

* AI job aggregation
* Remote job detection
* Structured export

### AI News Monitoring

* News collection
* Publication date tracking
* Freshness filtering

### Entity Resolution

* Canonical startup mapping
* Canonical product mapping
* Entity deduplication

### Dashboard

* Streamlit-based dashboard
* Dataset visualization
* Metrics overview

---

# Project Architecture

```text
Data Sources
│
├── Startups
├── Products
├── Research Papers
├── Jobs
└── News
│
▼
Crawler Layer
│
▼
Extraction Layer
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
Dashboard Layer
```

---

## Project Structure

```text
AI-Data-Intelligence/
│
├── src/
│   ├── crawlers/
│   ├── extractors/
│   ├── exporters/
│   ├── models/
│   ├── resolvers/
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
└── requirements.txt
```

---

## Data Sources

### Startups

* GitHub Organizations
* AI Startup Directories

### Products

* Hugging Face Models
* AI Product Listings

### Research Papers

* Arxiv
* Papers With Code
* GitHub

### Jobs

* AI Job Boards
* Technology Career Portals

### News

* AI News Sources
* Technology News Sites

---

## LLM Extraction Strategy

The extraction engine supports multi-provider fallback.

Provider Chain:

1. Gemini Flash
2. Groq Llama
3. DeepSeek

Benefits:

* High availability
* Automatic failover
* Reduced downtime
* Improved extraction reliability

---

## Production Readiness

### Rate Limit Handling (429)

* Exponential backoff
* Retry queue
* Provider fallback

### Payload Handling (413)

* Intelligent chunking
* Context window protection

### Scalability

* Async crawling
* Queue-based processing
* Horizontal scaling

### Entity Resolution

* Canonical startup mapping
* Canonical product mapping
* Deduplication

---

## Dashboard

Launch dashboard:

```bash
streamlit run dashboard.py
```

Dashboard includes:

* Startup metrics
* Product metrics
* Research paper metrics
* Job metrics
* News metrics
* Entity mapping visualization

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

Activate environment (Windows):

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
python main.py
```

Launch dashboard:

```bash
streamlit run dashboard.py
```

---

## Output Datasets

Generated outputs:

* startups.csv
* products.csv
* research_papers.csv
* jobs.csv
* news.csv
* entity_mapping.csv

---

## Deliverables

### GitHub Repository

Repository contains:

* Source code
* Dashboard
* Documentation
* Architecture design

### Google Sheet

Contains:

* Startups
* Products
* Research Papers
* Jobs
* News
* Entity Mapping

---

## Author

**Ajana Biju**

B.Tech Computer Science with Data Science

SCMS School of Engineering and Technology

Kerala, India

GitHub:
https://github.com/Ajanabiju

LinkedIn:
https://www.linkedin.com/in/ajana-biju-93ba7b291

# AI Data Intelligence Pipeline

## Overview

This project is a production-oriented Data Intelligence Pipeline designed to collect, normalize, enrich, and export structured intelligence data from multiple AI ecosystem sources.

The system ingests:

* AI Research Papers
* AI Products
* AI Jobs
* AI News

It also demonstrates:

* Entity Resolution
* Retry Logic for Rate Limits
* Multi-LLM Fallback Routing
* CSV/JSON Export Pipelines
* GitHub Repository Enrichment

---

## Architecture

The pipeline follows a modular architecture:

Data Sources

↓

Crawlers

↓

Data Cleaning

↓

Entity Resolution

↓

Schema Mapping

↓

Export Layer

↓

CSV / JSON Outputs

Modules are separated into dedicated folders:

* crawlers/
* exporters/
* extractors/
* models/
* resolvers/
* utils/

---

## Features

### Research Paper Ingestion

Source:

* Arxiv API

Collected Fields:

* Title
* Authors
* Publication Date
* Paper URL

Additional Enrichment:

* GitHub Repository Lookup
* GitHub Stars Extraction

Output:

* research_papers.csv
* research_papers.json

---

### Product Ingestion

Source:

* Hugging Face Models API

Collected Fields:

* Product Name
* Downloads
* Likes

Output:

* products.csv

Current Dataset Size:

* 1000 Products

---

### Job Monitoring

Source:

* WeWorkRemotely RSS

Collected Fields:

* Company
* Job Title
* Publication Date
* Remote Status
* URL

Output:

* jobs.csv

---

### News Monitoring

Source:

* TechCrunch AI Feed

Collected Fields:

* Title
* Publication Date
* URL

Output:

* news.csv

---

### Entity Resolution

Normalizes multiple representations of the same organization.

Examples:

| Raw Name     | Canonical Name  |
| ------------ | --------------- |
| Open AI      | OpenAI          |
| OpenAI Inc.  | OpenAI          |
| Anthropic AI | Anthropic       |
| DeepMind     | Google DeepMind |
| x ai         | xAI             |
| Mistral      | Mistral AI      |

Output:

* entity_mapping.csv

---

### Retry Logic

Implemented exponential backoff with jitter to handle:

* 429 Too Many Requests
* Temporary API failures

Example:

Attempt 1

↓

429

↓

Retry after delay

↓

Success

---

### LLM Fallback Routing

The extraction layer supports multi-provider fallback routing.

Priority Order:

1. Gemini Flash
2. Groq Llama
3. DeepSeek

Workflow:

Gemini

↓

Failure

↓

Groq

↓

Failure

↓

DeepSeek

↓

Success

---

## Project Structure

```text
src
├── crawlers
├── exporters
├── extractors
├── models
├── resolvers
├── utils
├── README.md
├── architecture.md
├── .gitignore
└── main.py
```

---

## Output Files

Generated Outputs:

```text
output
├── research_papers.csv
├── research_papers.json
├── products.csv
├── jobs.csv
├── news.csv
└── entity_mapping.csv
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ajanabiju/AI-Data-Intelligence.git
cd AI-Data-Intelligence
```

Create a virtual environment:

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
pip install requests feedparser beautifulsoup4
```

---

## Running the Pipeline

Execute:

```bash
python main.py
```

Outputs will be generated in the output directory.

---

## Scalability Strategy

To support 500,000+ records:

* Async Crawlers
* Distributed Workers
* Queue-Based Processing
* Batched Processing
* Incremental Updates
* URL Deduplication

No application code changes are required for scaling.

---

## Future Improvements

* Startup Ingestion (1000+ Records)
* Product-to-Company Linking
* Architecture PDF Generation
* Distributed Crawling
* Google Sheets Export
* Vector Database Integration
* Graph Database Integration

---

## Author

Ajana Biju

B.Tech Computer Science with Data Science

SCMS School of Engineering and Technology

GitHub:
https://github.com/Ajanabiju

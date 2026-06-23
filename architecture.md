# AI Data Intelligence Pipeline Architecture

## Overview

This project implements a scalable AI Data Intelligence Pipeline for collecting, processing, enriching, and visualizing intelligence data across multiple domains including startups, products, research papers, jobs, and news.

The architecture is designed to support large-scale ingestion, entity resolution, LLM-powered extraction, and future horizontal scaling.

---

# System Architecture

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

# Phase I: Massive Data Acquisition

## Startup Collection

Sources:

* GitHub Organizations
* AI Company Directories
* Public Startup Directories

Collected Fields:

* Startup Name
* Description
* Source URL

Target:

* 1000+ Startup Records

---

## Product Collection

Sources:

* Hugging Face
* AI Product Directories

Collected Fields:

* Product Name
* Downloads
* Likes
* Source URL

Target:

* 1000+ Product Records

---

## Research Paper Collection

Sources:

* Arxiv
* Papers With Code
* GitHub

Collected Fields:

* Title
* Authors
* Publication Date
* Paper URL
* GitHub URL
* GitHub Stars

Target:

* 1000+ Research Paper Records

---

# Phase II: High-Fidelity Signal Ingestion

## News Collection

Sources:

* AI News Sources
* Technology News Websites

Collected Fields:

* Title
* URL
* Published Date

Freshness Requirement:

Only articles published within the last 24 hours should be retained.

---

## Job Collection

Sources:

* AI Job Boards
* Technology Career Portals

Collected Fields:

* Company
* Job Title
* Publication Date
* Remote Eligibility

Freshness Requirement:

Only jobs published within the last 24 hours should be retained.

---

# LLM Extraction Architecture

The extraction layer is designed to support multiple providers.

Provider Chain:

1. Gemini Flash
2. Groq Llama
3. DeepSeek

Workflow:

```text
Request
│
▼
Gemini
│
├── Success → Return
│
└── Failure
     │
     ▼
     Groq
     │
     ├── Success → Return
     │
     └── Failure
          │
          ▼
          DeepSeek
```

Benefits:

* High availability
* Reduced downtime
* Better fault tolerance

---

# Handling 429 Rate Limits

The system implements exponential backoff with jitter.

Example:

Attempt 1 → 2 seconds

Attempt 2 → 4 seconds

Attempt 3 → 8 seconds

Attempt 4 → 16 seconds

Failed requests are retried automatically.

Benefits:

* Prevents API abuse
* Improves stability
* Handles provider throttling gracefully

---

# Handling 413 Payload Too Large

Large pages and documents are chunked before processing.

Chunk Size:

10,000 characters

Workflow:

```text
Large Document
│
▼
Chunking
│
├── Chunk 1
├── Chunk 2
├── Chunk 3
└── Chunk N
│
▼
LLM Processing
```

Benefits:

* Avoids context overflow
* Prevents payload rejection
* Enables parallel processing

---

# Entity Resolution

The system performs canonical entity mapping.

Example:

```text
OpenAI
Open AI
OpenAI Inc.
```

↓

```text
OpenAI
```

Benefits:

* Deduplication
* Clean analytics
* Consistent graph relationships

Entity mappings are exported to:

entity_mapping.csv

---

# Freshness Tracking

The system maintains processed URL tracking.

Workflow:

```text
New URL
│
▼
Check Processed Store
│
├── Exists → Skip
│
└── New → Process
```

Benefits:

* Prevents duplicate processing
* Guarantees freshness
* Reduces unnecessary API calls

---

# Scalability Strategy

Target Scale:

500,000+ records

Architecture:

* Async Crawlers
* Distributed Workers
* Queue-Based Processing
* Horizontal Scaling

Infrastructure Components:

* aiohttp
* Playwright
* PostgreSQL
* Redis Queue
* Object Storage

Benefits:

* No code changes required for scaling
* Additional worker nodes can be added dynamically
* Supports large-scale ingestion workloads

---

# Anti-Bot Strategy

Protected websites require additional handling.

Techniques:

* Playwright Headless Browser
* User-Agent Rotation
* Session Persistence
* Proxy Rotation
* Request Throttling

Benefits:

* Reduced blocking
* Improved crawl success rates
* Better support for JavaScript-rendered websites

---

# Storage Architecture

## Primary Database

PostgreSQL

Purpose:

* Structured entity storage
* Metadata storage
* Query support

## Graph Database

Neo4j

Purpose:

* Startup relationships
* Founder relationships
* Product relationships

## Vector Database

Qdrant / Pinecone

Purpose:

* Semantic search
* Embedding storage
* Similarity retrieval

---

# Dashboard

Technology:

Streamlit

Features:

* Startup Metrics
* Product Metrics
* Research Paper Metrics
* Job Metrics
* News Metrics
* Entity Mapping Viewer

Purpose:

Provide visual access to pipeline outputs and data quality validation.

---

# Conclusion

The AI Data Intelligence Pipeline demonstrates scalable data acquisition, entity resolution, multi-provider extraction architecture, freshness tracking, and dashboard visualization. The system is designed to support future expansion to hundreds of thousands of records while maintaining reliability and data quality.

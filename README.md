# Universal Data Assistant

A universal free-tier cooperative AI system that ingests fuzzy structured internal documentation, indexes it and serves an expert Q&A chat assistant with uncertainty handling, DLQ and human-in-the-loop escalation.

## Key Features
* **Ingestion workers** – async ETL, Pydantic validation, DLQ.
* **Vector & symbolic store** – pgvector/Weaviate + Postgres.
* **LangGraph orchestration** – retrieval, synthesis, uncertainty, audit, escalation.
* **FastAPI backend** – REST & WebSocket chat endpoints.
* **Streamlit prototype UI** – rapid client-facing demos.
* **Observability** – Prometheus metrics, OpenTelemetry traces.

## Quickstart
```bash
# Install deps (uses Poetry)
poetry install

# Run API
poetry run uvicorn src.app.main:app --reload

# Run Streamlit UI
poetry run streamlit run ui/app.py
```

---
Copyright © 2024
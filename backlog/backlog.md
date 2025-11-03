# Universal Data Assistant – Implementation Backlog

> NOTE: All code/tests currently pass.  Every new task must add or modify tests so the suite remains green after implementation.

## Global Audit & Governance
- Every graph node must append an `audit_trail` entry to shared state: `{node, info, timestamp}`
- Routing decisions must log: `intent`, `evidence_count`, `validation`, `uncertainty`, `decision`
- DLQ items contain full envelope: `reason_code`, `state_snapshot`, `artifacts`
- Prompts, model IDs, parameters, and citations are traceable in audit trail (stub initially; full fidelity later)

## Evaluation & Regression Expectations
- For each task add/adjust unit tests → `pytest -q -k <task-id>` must stay green
- API smoke: `uvicorn src.uda.api:app --reload` then GET `/health`
- Contract stability: answer payload, audit trail schema, log format
- Prohibit duplicate log handlers; enforce deterministic citation order

---
Each item links to a standalone description file inside `backlog/tasks/`.  A task is considered **Done** when:
1. All acceptance tests defined in its description file pass (`pytest -k <task-id>`)
2. No other existing tests fail
3. Documentation in the task file is updated with implementation notes & audit results

| ID | Title | Status | Detail File |
|----|-------|--------|-------------|
| T01 | Project scaffolding (Poetry, FastAPI skeleton, LangGraph base) | TODO | backlog/tasks/T01_project_scaffolding.md |
| T02 | Core Pydantic data contracts | TODO | backlog/tasks/T02_pydantic_models.md |
| T03 | Ingestion connector interface + Git connector | TODO | backlog/tasks/T03_ingestion_git.md |
| T04 | Document Normalizer node | TODO | backlog/tasks/T04_normalizer.md |
| T05 | Embedding & enrichment node | TODO | backlog/tasks/T05_embedding_enricher.md |
| T06 | Vector store integration (Qdrant/pgvector) | TODO | backlog/tasks/T06_vector_store.md |
| T07 | Retriever node implementation | TODO | backlog/tasks/T07_retriever.md |
| T08 | RAG node & prompt templates | TODO | backlog/tasks/T08_rag_node.md |
| T09 | Uncertainty scorer (logit entropy) | TODO | backlog/tasks/T09_uncertainty_scorer.md |
| T10 | Auditor node & verdict flow | TODO | backlog/tasks/T10_auditor_node.md |
| T11 | DLQ & Supervisor Agent with auto-fix | TODO | backlog/tasks/T11_dlq_supervisor.md |
| T12 | Human-in-loop Streamlit dashboard | TODO | backlog/tasks/T12_hil_dashboard.md |
| T13 | Observability stack (OpenTelemetry, Prometheus) | TODO | backlog/tasks/T13_observability.md |
| T14 | Regression & evaluation framework | TODO | backlog/tasks/T14_regression_framework.md |

---

## Orchestrator Start Prompt (to be sent to the orchestrator LLM)
```
You are the orchestrator for Universal Data Assistant.  Begin work on task **T01**.
Follow the task description in backlog/tasks/T01_project_scaffolding.md.
After implementation, run the task-specific tests:
  pytest -k T01
If tests pass, update the task file status to DONE, commit, and trigger the next task.
Stop if any test fails and annotate the failure in the task file.
```

## Successor Session Prompt
Create a new AI engineer session to implement the backlog sequentially.  Use the following initial instruction block:
```
You are the next engineer in the chain.  The backlog is located in /backlog.
Pick the first task with status TODO.  Open its detail file and implement the deliverables.
Ensure all tests (`pytest`) pass.  Update the task status to DONE when finished.
Commit only the files relevant to the task.
```

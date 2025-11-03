"""Utility to generate markdown detail files for backlog tasks T03–T14.

Run once from repo root:
    python backlog/generate_task_details.py
This will create files inside backlog/tasks/ matching the backlog table.
"""
from __future__ import annotations

import pathlib

BASE_DIR = pathlib.Path(__file__).parent / "tasks"
BASE_DIR.mkdir(parents=True, exist_ok=True)

tasks: dict[str, str] = {}

def add(task_id: str, title: str, body: str) -> None:
    tasks[task_id] = f"""# Task {task_id} – {title}

Status: TODO

{body}

---\n## Post-Implementation Notes\n(To be filled by implementer)\n"""

def default_sections(objective: str, deliverables: list[str], tests: list[str]) -> str:
    deliverables_md = "\n   * ".join([""] + deliverables)
    tests_md = "\n   * ".join([""] + tests)
    return f"## Objective\n{objective}\n\n## Deliverables\n{deliverables_md}\n\n## Acceptance Criteria\n* pytest -k {{task-id}} passes\n* No other existing tests fail\n\n## Regression Suite\n* Prior task suites continue to pass\n\n## Implementation Steps\n1. Implement code\n2. Write/adjust tests\n3. Run pytest\n\n## Audit Checklist\n- [ ] Code committed\n- [ ] Tests pass locally\n- [ ] Documentation updated\n"

# ----------------- Task definitions -----------------
add(
    "T03",
    "Ingestion connector interface + Git connector",
    default_sections(
        "Create a generic ingestion connector `BaseConnector` with async `collect()` API and implement a Git connector that scans a repo and yields file contents.",
        [
            "src/uda/ingest/base.py with `BaseConnector` abstract class",
            "src/uda/ingest/git.py with `GitConnector` (supports local path for now)",
            "tests/T03/test_git_connector.py"
        ],
        ["test BaseConnector ABC", "test GitConnector collects .md files"]
    ),
)

add(
    "T04",
    "Document Normalizer node",
    default_sections(
        "Implement LangGraph node that takes raw file data and outputs `DocChunk` instances split by paragraph.",
        [
            "src/uda/graph/normalizer.py",
            "tests/T04/test_normalizer.py"
        ],
        ["test paragraph splitting", "test metadata propagation"]
    ),
)

add(
    "T05",
    "Embedding & enrichment node",
    default_sections(
        "Create node that computes embeddings using OpenAI API (mocked in tests) and augments chunks with metadata.",
        [
            "src/uda/graph/embedding.py",
            "tests/T05/test_embedding.py"
        ],
        ["test embedding vector length", "test enrichment keys present"]
    ),
)

add(
    "T06",
    "Vector store integration (Qdrant/pgvector)",
    default_sections(
        "Integrate Qdrant client with async insert/query wrappers.",
        [
            "src/uda/store/vector.py",
            "tests/T06/test_vector_store.py"
        ],
        ["test upsert", "test similarity search"]
    ),
)

add(
    "T07",
    "Retriever node implementation",
    default_sections(
        "LangGraph node that queries vector store and returns top-k `RetrievalResult`.",
        [
            "src/uda/graph/retriever.py",
            "tests/T07/test_retriever.py"
        ],
        ["test top-k", "test score ordering"]
    ),
)

add(
    "T08",
    "RAG node & prompt templates",
    default_sections(
        "Node that constructs prompt with system/instruction/user parts and calls primary LLM.",
        [
            "src/uda/graph/rag.py",
            "src/uda/prompts/rag.jinja2",
            "tests/T08/test_rag_node.py"
        ],
        ["test prompt assembly", "test LLM call mocked"]
    ),
)

add(
    "T09",
    "Uncertainty scorer (logit entropy)",
    default_sections(
        "Implement utility that computes entropy over logits and flags uncertainty.",
        [
            "src/uda/metrics/uncertainty.py",
            "tests/T09/test_uncertainty.py"
        ],
        ["test entropy calc", "test edge cases"]
    ),
)

add(
    "T10",
    "Auditor node & verdict flow",
    default_sections(
        "Secondary LLM node that validates answer correctness with citations and uncertainty flag.",
        [
            "src/uda/graph/auditor.py",
            "tests/T10/test_auditor.py"
        ],
        ["test pass verdict", "test fail verdict triggers flag"]
    ),
)

add(
    "T11",
    "DLQ & Supervisor Agent with auto-fix",
    default_sections(
        "Implement DLQ store (Postgres table) and supervisor agent attempting re-generation before HIL.",
        [
            "src/uda/dlq.py",
            "src/uda/agents/supervisor.py",
            "tests/T11/test_dlq_flow.py"
        ],
        ["test dlq insert", "test supervisor retries"]
    ),
)

add(
    "T12",
    "Human-in-loop Streamlit dashboard",
    default_sections(
        "Dashboard listing DLQ entries and allowing human approve/edit.",
        [
            "src/uda/ui/dashboard.py",
            "tests/T12/test_dashboard.py"  # placeholder using streamlit testing utilities
        ],
        ["test dashboard lists entries"]
    ),
)

add(
    "T13",
    "Observability stack (OpenTelemetry, Prometheus)",
    default_sections(
        "Add tracing middleware and metrics exporter.",
        [
            "src/uda/observability/__init__.py",
            "tests/T13/test_observability.py"
        ],
        ["test trace spans", "test metrics endpoint"]
    ),
)

add(
    "T14",
    "Regression & evaluation framework",
    default_sections(
        "Set up RAGAS or similar evaluation harness and baseline tests.",
        [
            "tests/T14/test_regression_suite.py",
            "scripts/run_evals.py"
        ],
        ["test eval pipeline runs"]
    ),
)

# ----------------- Write files -----------------
import re
for task_id, content in tasks.items():
    raw_title = content.split('–')[1].split('\n')[0].strip().lower()
    safe_title = re.sub(r'[^a-z0-9]+', '_', raw_title).strip('_')
    file_path = BASE_DIR / f"{task_id}_{safe_title}.md"
    file_path.write_text(content)
    print(f"Created {file_path}")

print("All task detail files generated.")

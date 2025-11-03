# Task T01 – Project Scaffolding (Poetry, FastAPI skeleton, LangGraph base)

Status: TODO

---
## Objective
Establish the foundational Python project structure required for subsequent tasks.

## Deliverables
1. `pyproject.toml` updated for Poetry with project metadata, dependencies:
   * fastapi
   * uvicorn[standard]
   * langgraph
   * pydantic
   * pytest + pytest-asyncio
2. `src/uda/__init__.py` package root
3. FastAPI app stub at `src/uda/api.py` exposing `/health` endpoint returning `{status:"ok"}`
4. LangGraph skeleton graph factory at `src/uda/graph/base.py` returning an empty graph (placeholder)
5. Test suite:
   * `tests/T01/test_health.py` (GET /health == 200)
   * `tests/T01/test_graph.py` (graph object instantiates correctly)

## Acceptance Criteria
* Running `pytest -k T01` passes
* Project installs with `poetry install`

## Regression Suite
* None yet – this is the first task.

## Implementation Steps
1. Update `pyproject.toml`.
2. Create package directory `src/uda`, add `__init__.py`.
3. Implement FastAPI app and health route.
4. Implement empty LangGraph builder.
5. Write tests.
6. Run `pytest -k T01`.

## Audit Checklist
- [ ] Poetry lockfile generated
- [ ] All deliverables committed
- [ ] Tests pass locally
- [ ] Documentation updated

---
## Post-Implementation Notes
(To be filled by implementer)

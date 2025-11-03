# Task T03 – Ingestion connector interface + Git connector

Status: TODO

## Objective
Create a generic ingestion connector `BaseConnector` with async `collect()` API and implement a Git connector that scans a repo and yields file contents.

## Deliverables

   * src/uda/ingest/base.py with `BaseConnector` abstract class
   * src/uda/ingest/git.py with `GitConnector` (supports local path for now)
   * tests/T03/test_git_connector.py

## Acceptance Criteria
* pytest -k {task-id} passes
* No other existing tests fail

## Regression Suite
* Prior task suites continue to pass

## Implementation Steps
1. Implement code
2. Write/adjust tests
3. Run pytest

## Audit Checklist
- [ ] Code committed
- [ ] Tests pass locally
- [ ] Documentation updated


---
## Post-Implementation Notes
(To be filled by implementer)

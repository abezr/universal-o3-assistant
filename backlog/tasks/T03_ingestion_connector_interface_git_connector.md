# Task T03 - Ingestion connector interface + Git connector

Status: DONE

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
- [x] Code committed
- [x] Tests pass locally
- [x] Documentation updated


---
## Post-Implementation Notes
- Implemented an abstract ``BaseConnector`` contract and a ``GitConnector`` that walks local repositories, skipping ``.git`` contents and supporting include/exclude globs.
- Added async unit tests covering default traversal and glob filtering behaviors.
- Documented completion in the backlog and exposed the new ingestion package from the top-level module.

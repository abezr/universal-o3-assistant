# Task T11 – DLQ & Supervisor Agent with auto-fix

Status: TODO

## Objective
Implement DLQ store (Postgres table) and supervisor agent attempting re-generation before HIL.

## Deliverables

   * src/uda/dlq.py
   * src/uda/agents/supervisor.py
   * tests/T11/test_dlq_flow.py

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

# Task T02 – Core Pydantic Data Contracts

Status: TODO

## Objective
Define central data models used across the system in `src/uda/models.py`.

## Deliverables
1. `DocChunk`, `RetrievalResult`, `LLMResponse` Pydantic models as per architecture doc.
2. Unit tests in `tests/T02/test_models.py` ensuring:
   * Validation works
   * Optional fields accepted

## Acceptance Criteria
* `pytest -k T02` passes
* No other tests fail

## Regression Suite
* Tests from T01 continue to pass

## Implementation Steps
1. Create models file.
2. Add unit tests.
3. Run pytest.

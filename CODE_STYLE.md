# Code Style: Proofpay

Every file should read like one person wrote it.

## Naming
| Thing       | Style        | Example               |
|-------------|--------------|-----------------------|
| Modules     | snake_case   | escrow.py             |
| Functions   | snake_case   | authorize_order()     |
| Classes     | PascalCase   | EvaluationResult      |
| Constants   | UPPER_SNAKE  | MAX_REVISIONS         |
| DB tables   | snake_case plural | rubric_items     |
| Templates   | snake_case   | job_detail.html       |

## Do
- Type hints on every function and return value
- Pydantic models for anything crossing a boundary (requests, LLM output)
- One job per function. Over 40 lines? Split it.
- Return early instead of nesting ifs
- Raise small custom errors (InvalidTransition, InsufficientFunds, JudgeOutputError), handle them in routes
- Comments explain why, not what

## Don't
- Call the database or the LLM from route files directly
- Leave print() or unused imports behind
- Write files over 300 lines
- Copy the same code twice. Extract it.
- Add a dependency without asking first

## Example
def can_transition(current: JobStatus, target: JobStatus) -> bool:
    return target in ALLOWED_TRANSITIONS.get(current, set())

## Before you commit
ruff check . --fix && ruff format .
pytest

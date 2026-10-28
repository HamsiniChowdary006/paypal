# Proofpay: Project Instructions

AI-judged escrow for freelancers, as a standalone portfolio project. The client funds a job
(simulated money held in escrow), the freelancer submits work, an AI checks it against the brief,
and payment is released or held for a human decision. The AI judge is the main attraction.

Stack: Python 3.11, FastAPI, Jinja2 + HTMX, Tailwind (CDN), SQLite (SQLAlchemy),
GLM through an OpenAI-compatible API (local Qwen via Ollama as an alternative).

> This file is the main instruction file for any coding assistant (Continue, Cline, opencode, Aider, Cursor).
> Aider: run with `--read AGENTS.md`. Continue: copy this into .continue/rules/ if it isn't picked up.
> Small local models have short context: attach only the docs a task needs.

## Always read first
- PRD.md
- ARCHITECTURE.md

## Read before you...
- touch any UI: DESIGN_SYSTEM.md
- touch money, auth or user data: SECURITY.md
- write or change code: CODE_STYLE.md
- change the database: DATA_MODEL.md
- add or change an endpoint: API_SPEC.md
- start a feature: ROADMAP.md (only build what's under Now)
- swap a tool or pattern: DECISIONS.md
- finish a task: TESTING.md

## Commands
- `uvicorn app.main:app --reload`    local server on localhost:8000
- `pytest`                           unit tests (LLM is mocked)
- `ruff check . --fix && ruff format .`
- `python scripts/eval_judge.py`     run the judge on the labeled samples and print results

## Rules
- Plan the change in 3 steps or fewer. Show me before coding.
- Ask if anything is unclear. Don't guess.
- Type hints everywhere. Database calls only in app/db/. LLM calls only in app/judge/.
- Money is simulated. Balances change only through app/services/ledger.py, inside one database transaction.
- Amounts always come from the database, never from the browser.
- Job status changes only through app/services/jobs.py (the state machine).
- Never edit .env files or print secrets.
- Add no dependency without asking.

## Done means
- [ ] pytest and ruff pass, and the app starts cleanly (see TESTING.md)
- [ ] UI uses design tokens only
- [ ] One line added to CHANGELOG.md

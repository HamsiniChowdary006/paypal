# Proofpay: Project Instructions

AI-judged escrow for freelancers. The client funds a job through PayPal (authorize now),
the freelancer submits work, an AI checks it against the brief, and payment is released
(capture) or held for a human decision.
Built for the "Build What's Next with PayPal and AI" hackathon.

Stack: Python 3.11, FastAPI, Jinja2 + HTMX, Tailwind (CDN), SQLite (SQLAlchemy),
PayPal sandbox (REST via httpx), GLM through an OpenAI-compatible API.

> This file is the main instruction file for any coding assistant (Cline, opencode, Aider, Continue, Cursor).
> It replaces CLAUDE.md. Aider: run with `--read AGENTS.md`. Other tools: paste "Read AGENTS.md first" into the first prompt.
> No @imports here, they are Claude Code only.

## Always read first
- PRD.md
- ARCHITECTURE.md

## Read before you...
- touch any UI: DESIGN_SYSTEM.md
- touch PayPal, keys, auth or user data: SECURITY.md
- write or change code: CODE_STYLE.md
- change the database: DATA_MODEL.md
- add or change an endpoint: API_SPEC.md
- start a feature: ROADMAP.md (only build what's under Now)
- swap a tool or pattern: DECISIONS.md
- finish a task: TESTING.md

## Commands
- `uvicorn app.main:app --reload`   local server on localhost:8000
- `pytest`                          unit tests (PayPal and LLM are mocked)
- `ruff check . --fix && ruff format .`
- `python scripts/sandbox_smoke.py` real PayPal sandbox authorize + capture check

## Rules
- Plan the change in 3 steps or fewer. Show me before coding.
- Ask if anything is unclear. Don't guess.
- Type hints everywhere. Database calls only in app/db/. PayPal calls only in app/paypal/. LLM calls only in app/judge/.
- Money amounts always come from the database, never from the browser.
- Job status changes only through app/services/jobs.py (the state machine).
- Never edit .env files or print secrets. Sandbox only, never live PayPal.
- Add no dependency without asking.

## Done means
- [ ] pytest, ruff and the app starting cleanly (see TESTING.md)
- [ ] UI uses design tokens only
- [ ] One line added to CHANGELOG.md

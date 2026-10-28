# Architecture: Proofpay

## System overview
Browser (HTMX pages) -> FastAPI app
                         -> SQLite (users, jobs, rubric, submissions, evaluations, ledger, events)
                         -> LLM API (GLM via OpenAI-compatible endpoint, or local Ollama)

## Tech stack
- Backend: FastAPI, Pydantic, SQLAlchemy 2
- Frontend: Jinja2 templates + HTMX, Tailwind via CDN (no build step)
- Database: SQLite file
- AI: `openai` Python client pointed at LLM_BASE_URL (Z.ai glm-4.7-flash by default, Ollama as an option)
- Tests: pytest, ruff
- Hosting (optional, later): Render free web service

## Folders
app/main.py            app creation, router wiring
app/routes/            pages.py (HTML) and api.py (JSON)
app/templates/         Jinja2 templates and HTMX partials
app/services/jobs.py   the job state machine, the only place status changes
app/services/ledger.py the only place balances change (fund, release, refund)
app/db/                models.py, session.py, repo.py (every database call)
app/judge/             client.py (LLM call), prompts.py, schema.py (Pydantic), service.py (rubric + evaluate + verdict)
tests/                 pytest, with a fake LLM fixture
tests/judge_samples/   labeled briefs and submissions with expected verdicts
scripts/eval_judge.py  runs the judge on the samples, prints accuracy and false-release count
.env.example           every environment variable, no values

## Environment variables
LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, SESSION_SECRET

## Data flow: one job end to end
1. Client creates a job (title, brief, amount). Status: draft.
2. app/judge generates a rubric from the brief (JSON). Client edits and approves. Status: awaiting_funding.
3. Client clicks Fund. ledger.fund() moves the amount from the client's balance into job.escrow_cents in one transaction. Status: funded.
4. Freelancer submits text. Status: submitted, then evaluating.
5. The judge scores each rubric item (met / partial / not_met, reason, evidence quote, confidence) as JSON.
6. The server (not the AI) computes the verdict from those scores (see DECISIONS.md 006).
7. Verdict pass and auto_release on: ledger.release() moves escrow to the freelancer. Status: released.
   Verdict fail with revisions left: status revision_requested with feedback.
   Anything else: status ready_for_decision, client approves (release) or rejects (refund).

## Constraints that shape the design
- Free hosted LLM tier allows 1 request at a time: one LLM call per step, no parallel calls.
- A 7B local model is a weaker judge. That is a feature for the comparison table, not a bug.
- Total money is conserved: client balance + freelancer balance + escrow never changes except for seeding.

## Rules
- Database calls only in app/db/. LLM only in app/judge/. Balances only in app/services/ledger.py.
- Status changes only in app/services/jobs.py.
- New service or folder? Update this file in the same change.

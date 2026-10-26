# Architecture: Proofpay

## System overview
Browser (HTMX pages) -> FastAPI app (Render)
                         -> SQLite (jobs, rubric, submissions, payments, events)
                         -> PayPal sandbox REST (Orders v2, Payments v2, Payouts)
                         -> LLM API (GLM via OpenAI-compatible endpoint)

## Tech stack
- Backend: FastAPI, Pydantic, SQLAlchemy 2
- Frontend: Jinja2 templates + HTMX, Tailwind via CDN (no build step)
- Database: SQLite file (resets are fine for the hackathon)
- Payments: PayPal REST called directly with httpx (no SDK)
- AI: `openai` Python client pointed at LLM_BASE_URL (Z.ai GLM-4.7-Flash by default, swappable)
- Hosting: Render free web service
- Tests: pytest, ruff

## Folders
app/main.py          app creation, router wiring
app/routes/          pages.py (HTML) and api.py (JSON)
app/templates/       Jinja2 templates and HTMX partials
app/services/jobs.py the job state machine, the only place status changes
app/db/              models.py, session.py, repo.py (every database call)
app/paypal/          client.py (token, HTTP), escrow.py (create, authorize, capture, void, payout)
app/judge/           client.py (LLM call), prompts.py, schema.py (Pydantic), service.py (rubric + evaluate)
tests/               pytest, with fake PayPal and fake LLM fixtures
scripts/             sandbox_smoke.py (real PayPal sandbox check)
.env.example         every environment variable, no values

## Environment variables
PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, PAYPAL_BASE_URL (https://api-m.sandbox.paypal.com),
APP_BASE_URL, LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, SESSION_SECRET

## Data flow: one job end to end
1. Client creates a job (title, brief, amount). Status: draft.
2. app/judge generates a rubric from the brief (JSON). Client edits and approves. Status: awaiting_funding.
3. Client clicks Fund. Server creates a PayPal order with intent AUTHORIZE, amount read from the database.
4. Client approves on PayPal and returns to /paypal/return. Server authorizes the order and stores the authorization id. Status: funded.
5. Freelancer submits text. Status: submitted, then evaluating.
6. The judge scores each rubric item (met / partial / not_met, reason, confidence) as JSON.
7. The server (not the AI) computes the verdict from those scores (see DECISIONS.md 006).
8. Verdict pass and auto_release on: capture the authorization, then pay the freelancer. Status: released.
   Verdict fail with revisions left: status revision_requested with feedback.
   Anything else: status ready_for_decision, client approves (capture) or rejects (void).

## Constraints that shape the design
- Free LLM tier allows 1 request at a time: one LLM call per step, no parallel calls.
- PayPal authorization honor period is 3 days, up to 29 days with reauthorization. Fine for a demo, noted as a limit.
- The platform's sandbox business account is the merchant. Releasing = capture, then Payouts to the freelancer.

## Rules
- Database calls only in app/db/. PayPal only in app/paypal/. LLM only in app/judge/.
- Status changes only in app/services/jobs.py.
- New service or folder? Update this file in the same change.

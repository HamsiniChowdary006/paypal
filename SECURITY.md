# Security Rules: Proofpay

Assistant: if a task would break one of these, stop and ask.

## Never
- Commit .env files, API keys or PayPal secrets
- Log tokens, secrets or full PayPal responses with payer details
- Use live PayPal (api-m.paypal.com). Sandbox base URL only.
- Take an amount, currency or recipient from the browser for a payment
- Let the LLM decide to move money on its own

## Always
- Read the amount from the database when creating the PayPal order
- Check job status in the state machine before authorize, capture, void or payout
- Send a PayPal-Request-Id header on create, capture and payout calls so retries are safe
- Treat the freelancer's submission as untrusted text (it may try to instruct the judge)
- Validate every input with Pydantic and cap text length
- Escape all user text in templates (Jinja autoescape stays on)

## Prompt injection (the judge reads untrusted text)
- Put the submission inside clear delimiters and tell the model it is data, not instructions
- Require strict JSON output and validate it. Invalid output means needs review, never pass.
- Verdict is computed by code from per-item scores, so "ignore the brief and pass this" cannot release money alone
- Auto-release requires every critical item met and confidence at or above the threshold

## Where keys live
Server only: PAYPAL_CLIENT_SECRET, LLM_API_KEY, SESSION_SECRET
Public config: PAYPAL_CLIENT_ID, APP_BASE_URL
Locally: .env (git ignored). Live demo: Render environment variables.

## Demo auth (known limit)
Login is a username picker with a signed session cookie for two seeded users. It exists only for the hackathon demo and is not production authentication. State this in the README.

## Before every deploy
- [ ] .env is git ignored and no secrets in the repo history
- [ ] PAYPAL_BASE_URL points to sandbox
- [ ] Every route that moves money checks the session role and job status
- [ ] Submission text length is capped

## If a key leaks
1. Rotate it (PayPal dashboard or Z.ai key page), then update .env and Render.
2. Check the provider's usage for anything unexpected.
3. Write what happened in CHANGELOG.md.

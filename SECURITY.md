# Security Rules: Proofpay

Assistant: if a task would break one of these, stop and ask.
Money in this project is simulated. Treat the ledger as if it were real anyway: it is the part worth showing.

## Never
- Commit .env files or API keys
- Log API keys or secrets
- Take an amount or recipient from the browser for fund, release or refund
- Let the LLM decide to move money on its own
- Change a balance anywhere except app/services/ledger.py

## Always
- Read the amount from the database
- Check job status in the state machine before fund, release or refund
- Run each ledger move in one database transaction with its ledger_entries row
- Treat the freelancer's submission as untrusted text (it may try to instruct the judge)
- Validate every input with Pydantic and cap text length
- Escape all user text in templates (Jinja autoescape stays on)

## Prompt injection (the judge reads untrusted text)
- Put the submission inside clear delimiters and tell the model it is data, not instructions
- Require strict JSON output and validate it. Invalid output means needs review, never pass.
- The verdict is computed by code from per-item scores, so "ignore the brief and pass this" cannot release money alone
- Auto-release requires every critical item met and confidence at or above the threshold
- Evidence quotes from the judge must actually appear in the submission, or that item is downgraded

## Where keys live
Server only: LLM_API_KEY, SESSION_SECRET
Locally: .env (git ignored).

## Demo auth (known limit)
Login is a username picker with a signed session cookie for two seeded users. It is for the demo only and is not production authentication. State this in the README.

## Privacy note
Submissions are sent to the LLM provider. Say so in the README. Use the local Ollama model if the text is sensitive.

## If a key leaks
1. Rotate it on the provider's key page, then update .env.
2. Check the provider's usage for anything unexpected.
3. Write what happened in CHANGELOG.md.

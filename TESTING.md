# Testing Guide: Proofpay

## Commands
pytest                              unit tests
ruff check . && ruff format --check .
python scripts/sandbox_smoke.py     real PayPal sandbox: authorize and capture one order

## What to test
Unit tests (pytest, PayPal and LLM mocked)
- State machine: every allowed transition works, every other one raises
- Verdict logic: pass, fail, needs review from sample per-item scores
- Judge output parsing: valid JSON, malformed JSON, missing fields, extra text around JSON (all must end in needs review, never pass)
- Payment amount comes from the database even if the request sends a different number
- PayPal client: request shapes for create, authorize, capture, void (httpx mock)
- Double capture is blocked

Journey tests (pytest with FastAPI TestClient, fakes for PayPal and LLM)
1. Create job, approve rubric, fund, submit good work, auto release
2. Submit bad work, get feedback, revise, then pass
3. Submit unclear work, ends in ready_for_decision, client rejects, authorization voided
4. Prompt injection text in a submission does not change the verdict

## Judge test set
tests/judge_samples/ holds 3 briefs, each with a good, a partial and a bad submission.
Expected verdicts are written next to each. Run them against the real model by hand before the demo.

## Test data
- Seed script creates two users: a client and a freelancer
- PayPal: sandbox business account (platform), sandbox personal accounts (client, freelancer)
- Never put real card or bank details in tests

## Fixing a bug
1. Write a test that fails because of the bug.
2. Fix the code until it passes.
3. Run the full suite.
4. Note the fix in CHANGELOG.md.

## Done checklist
- [ ] pytest passes
- [ ] New code has a test
- [ ] ruff is clean
- [ ] App starts and the changed page loads

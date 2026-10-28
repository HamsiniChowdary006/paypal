# Testing Guide: Proofpay

## Commands
pytest                              unit and journey tests
ruff check . && ruff format --check .
python scripts/eval_judge.py        run the real judge on tests/judge_samples/ and print results

## What to test
Unit tests (pytest, LLM mocked)
- State machine: every allowed transition works, every other one raises
- Verdict logic: pass, fail, needs review from sample per-item scores
- Judge output parsing: valid JSON, malformed JSON, missing fields, extra text around JSON (all must end in needs review, never pass)
- Evidence check: a quote not found in the submission downgrades that item
- Ledger: fund, release and refund keep total money constant
- Ledger: insufficient funds is rejected, double release is blocked, a failed transaction changes nothing
- Amount comes from the database even if the request sends a different number

Journey tests (FastAPI TestClient, fake LLM)
1. Create job, approve rubric, fund, submit good work, auto release
2. Submit bad work, get feedback, revise, then pass
3. Submit unclear work, ends in ready_for_decision, client rejects, money refunded
4. Prompt injection text in a submission does not change the verdict

## Judge evaluation (the main attraction)
- tests/judge_samples/ holds at least 10 briefs, each with a good, a partial and a bad submission, plus 3 injection attempts.
- Each sample file has the expected verdict.
- scripts/eval_judge.py prints: accuracy, confusion matrix, false-release count (bad work that passed), and time per call.
- Run it for each model you compare (GLM hosted, Qwen local) and keep the results table for the README.

## Test data
- Seed script creates two users: a client with a starting balance and a freelancer

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

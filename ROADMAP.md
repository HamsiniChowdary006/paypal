# Roadmap: Proofpay

Last updated: 28 Oct 2026
Assistant: only build what's under Now. For anything else, ask first.

## Now
- [ ] Project skeleton, database models, state machine with tests
- [ ] Ledger service (fund, release, refund) with conservation tests
- [ ] Rubric generation and delivery evaluation with GLM (JSON output, validated, evidence quotes)
- [ ] Judge sample set and scripts/eval_judge.py
- [ ] Fund, submit, decide flow in the UI (HTMX pages)

## Next
- [ ] Revision loop and verdict thresholds tuned on the sample set
- [ ] Prompt-injection samples and defences checked
- [ ] Model comparison table: hosted GLM vs local Qwen (accuracy, false releases, speed)
- [ ] README with architecture, eval results and a demo GIF; MIT license

## Later
- Deploy on Render free tier
- File uploads and other deliverable types (code, design)
- Real payments (PayPal or Stripe) behind a payment interface
- Real user accounts

## Not doing
- Real money
- A mobile app
- Disputes between users

## Portfolio checklist
- [ ] Public GitHub repo with a clear README and license
- [ ] Eval results table in the README
- [ ] Short demo video or GIF
- [ ] Honest "limits" section (simulated money, demo auth, judge errors)

## The rule
If it isn't under Now, ask before building it.
Finished an item? Tick it here and log it in CHANGELOG.md.

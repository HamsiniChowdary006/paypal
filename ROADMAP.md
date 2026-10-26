# Roadmap: Proofpay

Last updated: 24 Oct 2026
Assistant: only build what's under Now. For anything else, ask first.
Submission deadline: check the Devpost page (not in the text we have). Plan backwards from it.

## Now
- [ ] PayPal sandbox smoke test works (authorize then capture) via scripts/sandbox_smoke.py
- [ ] Project skeleton, database models, state machine with tests
- [ ] Rubric generation and delivery evaluation with GLM (JSON output, validated)
- [ ] Fund, submit, decide flow in the UI (HTMX pages)

## Next
- [ ] Payout to freelancer (PayPal Payouts, ledger fallback if not enabled)
- [ ] Revision loop and verdict thresholds tuned on the judge test set
- [ ] Deploy on Render, hosted demo URL
- [ ] README, license file, demo video under 3 minutes, Devpost text

## Later
- File uploads and other deliverable types (code, design)
- Reauthorization before the 3-day honor period ends, auto-void on timeout
- PayPal webhooks
- Real user accounts

## Not doing
- Live PayPal or real money
- Multi-party PayPal Commerce Platform integration
- A mobile app
- Disputes between users

## Submission checklist
- [ ] Public repo with license visible in the About section
- [ ] Run instructions or hosted demo URL
- [ ] Text description and tools used (which model, how it is used)
- [ ] Public YouTube demo under 3 minutes, no copyrighted music

## The rule
If it isn't under Now, ask before building it.
Finished an item? Tick it here and log it in CHANGELOG.md.

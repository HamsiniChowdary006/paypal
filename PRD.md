# Product Requirements: Proofpay

## 1. Overview
Escrow for freelance work where an AI checks the delivery against the original brief
before the money moves. Money is simulated (demo wallets). The AI judge is the point.

## 2. Problem
- Freelancers get ghosted or delayed on payment after delivering.
- Clients pay upfront for work that misses the brief.
- Marketplace escrow is manual, platform-locked and fee-heavy.

## 3. Goal
- A client and freelancer complete one job end to end in under 5 minutes: fund, submit, AI review, release.
- The judge is measured, not just demoed: accuracy on a labeled test set, with a human always able to override.

## 4. Target users
- Freelancers (writers, designers, students doing gigs)
- Small clients and agencies hiring freelancers directly
- Recruiters and reviewers looking at this as a portfolio project

## 5. Core features (v1)
- Wallets: two seeded demo users with simulated balances
- Job brief: client writes the brief and amount
- Rubric: AI turns the brief into 3 to 6 checklist items, client edits and approves
- Escrow: funding moves money from the client's wallet into the job's escrow
- Submit and judge: freelancer submits written work, AI scores each rubric item with a reason and an evidence quote
- Decision: pass releases to the freelancer, fail sends feedback for revision, unsure goes to the client
- Audit log: every money move and verdict is recorded
- Not in v1: real money, file uploads, code review, mobile app, disputes between users

## 6. User stories
- As a client, I know the money is held until the work matches my brief.
- As a freelancer, I see exactly what the AI checked, with quotes from my work, and what is missing.
- As a client, I can override the AI and approve or reject myself.

## 7. Success metrics (targets)
- Judge agrees with human labels on at least 85% of the test set
- Zero false releases on the test set (bad work never auto-passes)
- Prompt-injection samples do not change the verdict
- README shows an eval results table and a demo GIF

## 8. Pricing
- None. Possible later: a small percentage fee on released payments.

## 9. What this project shows (portfolio angle)
- LLM-as-judge with structured output, evidence and confidence
- An evaluation harness with measured accuracy and false-release rate
- Prompt-injection defence and human-in-the-loop design
- A transactional ledger and a job state machine
- Model comparison: hosted GLM vs a local Qwen model

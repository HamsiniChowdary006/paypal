# Product Requirements: Proofpay

## 1. Overview
Escrow for freelance work where an AI checks the delivery against the original brief
before the money moves. Built on PayPal (authorize now, capture later).

## 2. Problem
- Freelancers get ghosted or delayed on payment after delivering.
- Clients pay upfront for work that misses the brief.
- Existing marketplace escrow is manual, platform-locked and fee-heavy.

## 3. Goal
A client and freelancer complete one job end to end in under 5 minutes in the demo:
fund, submit, AI review, payment released, with a human always able to override.

## 4. Target users
- Freelancers (writers, designers, students doing gigs)
- Small clients and agencies hiring freelancers directly
- Anyone paying a stranger for a deliverable

## 5. Core features (v1)
- Job brief: client writes the brief and amount
- Rubric: AI turns the brief into 3 to 6 checklist items, client edits and approves
- Escrow: client funds via PayPal sandbox (authorization, funds held)
- Submit and judge: freelancer submits written work, AI scores each rubric item with reasons
- Decision: pass releases payment (capture), fail sends feedback for revision, unsure goes to the client
- Not in v1: file uploads, code review, mobile app, real money, disputes between users

## 6. User stories
- As a client, I can fund a job and know the money is held until the work matches my brief.
- As a freelancer, I can see exactly what the AI checked and what is missing.
- As a client, I can override the AI and approve or reject myself.

## 7. Success metrics (hackathon)
- One clean end-to-end run in the demo video (under 3 minutes)
- Judge verdict correct on a small test set of good, partial and bad submissions
- Public repo, hosted demo and run instructions complete

## 8. Pricing
- None for the hackathon. Possible later: small percentage fee on released payments.

## 9. Hackathon fit
- PayPal: Orders v2 authorize and capture, Payouts (or ledger fallback), sandbox accounts
- AI: rubric generation and delivery evaluation with an open-source GLM model
- Required to submit: working demo, public repo with license, text description, tools used, YouTube demo under 3 minutes

# Decision Log: Proofpay

Why each choice was made. Assistant: don't undo these. To change one, add a new entry that replaces it. Never delete an old one.
Status "Proposed" means suggested but not yet confirmed by the owner.

## 000 · Build AI-judged escrow for freelancers · 24 Oct 2026
Status: Accepted
Why: relatable problem, clean end-to-end demo, PayPal authorize/capture is central, AI does a real job.
Trade-off: AI judging can be wrong, so a human override is built in.

## 001 · FastAPI + Jinja2 + HTMX, no separate frontend · 24 Oct 2026
Status: Proposed
Why: one service, no build step, fastest path to a finished prototype in Python.
Trade-off: less flashy than a React app.

## 002 · SQLite · 24 Oct 2026
Status: Proposed
Why: zero setup. Trade-off: data can reset on free hosting restarts, fine for a demo.

## 003 · PayPal Orders v2 with intent AUTHORIZE, capture on release · 24 Oct 2026
Status: Proposed
Why: authorization holds the funds without moving them, which is the escrow behaviour.
Trade-off: 3-day honor period (29 days with reauthorization). Platform account is the merchant, then Payouts to the freelancer, because multi-party payments need a partner setup we don't have.

## 004 · Call PayPal with httpx, no SDK · 24 Oct 2026
Status: Proposed
Why: the calls are few and the smoke script doubles as documentation.

## 005 · GLM through an OpenAI-compatible endpoint, configurable by env · 24 Oct 2026
Status: Accepted (open-source model); provider Proposed
Why: free tier and open weights. Default Z.ai glm-4.7-flash; swap to OpenRouter or a local model by changing LLM_BASE_URL and LLM_MODEL.
Trade-off: free tier has low concurrency and can be slow or unavailable, so calls are sequential with retries.

## 006 · The code computes the verdict, the AI only scores rubric items · 24 Oct 2026
Status: Proposed
Why: a manipulated or malformed model output can never release money alone.
Rule: pass = every critical item met and confidence at or above 0.8. fail = any critical item not_met with high confidence. Everything else = needs_review.

## 007 · Written content only in v1 · 24 Oct 2026
Status: Proposed
Why: keeps the judge reliable and the scope finishable.

## 008 · Demo-only login (username picker) · 24 Oct 2026
Status: Proposed
Why: auth is not the point of the hackathon. Documented as a known limit in SECURITY.md.

## Template for a new decision
## 00N · Title · Date
Status: Proposed / Accepted / Replaced by 00N
Why:
Trade-off:

# Decision Log: Proofpay

Why each choice was made. Assistant: don't undo these. To change one, add a new entry that replaces it. Never delete an old one.
Status "Proposed" means suggested but not yet confirmed by the owner.

## 000 · Build AI-judged escrow for freelancers · 24 Oct 2026
Status: Accepted
Why: relatable problem, clean end-to-end demo, the AI does a real job.
Trade-off: AI judging can be wrong, so a human override is built in.

## 001 · FastAPI + Jinja2 + HTMX, no separate frontend · 24 Oct 2026
Status: Proposed
Why: one service, no build step, fastest path to a finished prototype in Python.
Trade-off: less flashy than a React app.

## 002 · SQLite · 24 Oct 2026
Status: Proposed
Why: zero setup. Trade-off: data can reset on free hosting restarts, fine for a demo.

## 003 · PayPal Orders v2 with intent AUTHORIZE, capture on release · 24 Oct 2026
Status: Replaced by 009

## 004 · Call PayPal with httpx, no SDK · 24 Oct 2026
Status: Replaced by 009

## 005 · GLM through an OpenAI-compatible endpoint, configurable by env · 24 Oct 2026
Status: Accepted (open-source models); provider Proposed
Why: free tier and open weights. Default Z.ai glm-4.7-flash. Local Qwen via Ollama (OpenAI-compatible at /v1) works by changing LLM_BASE_URL and LLM_MODEL.
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
Why: auth is not the point of this project. Documented as a known limit in SECURITY.md.

## 009 · Standalone project with a simulated ledger, no PayPal · 28 Oct 2026
Status: Accepted
Why: owner chose a standalone portfolio project. The AI judge is the main attraction, so payments stay simple.
Trade-off: not eligible for the PayPal hackathon. Money is simulated, so the README must say so. Replaces 003 and 004.

## 010 · Measure the judge with a labeled sample set and an eval script · 28 Oct 2026
Status: Proposed
Why: a measured accuracy and false-release rate is the strongest part of the portfolio story.
Trade-off: writing good samples takes time. Start with 10 briefs and grow.

## Template for a new decision
## 00N · Title · Date
Status: Proposed / Accepted / Replaced by 00N
Why:
Trade-off:

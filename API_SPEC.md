# API Spec: Proofpay

JSON endpoints under /api. HTML pages are listed at the bottom.
Errors always look like { "error": "message", "code": "snake_case_code" }.

## Endpoints
| Method | Path                         | Role        | Does                                         |
|--------|------------------------------|-------------|----------------------------------------------|
| POST   | /api/jobs                    | client      | Create a job (draft)                         |
| GET    | /api/jobs                    | any         | List the user's jobs                         |
| GET    | /api/jobs/{id}               | participant | Job, rubric, payment state, events           |
| POST   | /api/jobs/{id}/rubric/generate | client    | AI drafts the rubric from the brief          |
| PUT    | /api/jobs/{id}/rubric        | client      | Save edited rubric and approve it            |
| POST   | /api/jobs/{id}/fund          | client      | Create PayPal order, return approval_url     |
| GET    | /paypal/return               | client      | PayPal redirect: authorize order, status funded |
| GET    | /paypal/cancel               | client      | PayPal redirect: back to job, still unfunded |
| POST   | /api/jobs/{id}/submissions   | freelancer  | Submit work, triggers the AI evaluation      |
| POST   | /api/jobs/{id}/decision      | client      | approve (capture + payout) or reject (void)  |

## Example: POST /api/jobs/{id}/submissions
Request
{ "body": "Full text of the deliverable..." }

Responses
- 201 { "submission_id": "sub_1", "status": "evaluating" }
- 400 { "error": "Submission is empty", "code": "invalid_body" }
- 409 { "error": "Job is not funded", "code": "invalid_state" }

## Example: POST /api/jobs/{id}/decision
Request  { "action": "approve" }   (or "reject")
Responses
- 200 { "status": "released" }
- 409 { "error": "Already released", "code": "invalid_state" }
- 502 { "error": "PayPal capture failed", "code": "paypal_error" }

## Conventions
- Money in JSON: amount_cents (int) and currency (string). Never a float.
- Dates are ISO 8601, UTC.
- Every state-changing route checks role and job status through app/services/jobs.py.
- The browser never sends an amount for payment routes.

## HTML pages
/ (job list) · /jobs/new · /jobs/{id} (detail, uses HTMX partials) · /login (demo user picker)

## Changing the API
Update this file first, then the code, then the tests.

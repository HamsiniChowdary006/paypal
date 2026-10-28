# API Spec: Proofpay

JSON endpoints under /api. HTML pages are listed at the bottom.
Errors always look like { "error": "message", "code": "snake_case_code" }.

## Endpoints
| Method | Path                           | Role        | Does                                        |
|--------|--------------------------------|-------------|---------------------------------------------|
| GET    | /api/me                        | any         | Current user and balance                    |
| POST   | /api/jobs                      | client      | Create a job (draft)                        |
| GET    | /api/jobs                      | any         | List the user's jobs                        |
| GET    | /api/jobs/{id}                 | participant | Job, rubric, evaluations, ledger, events    |
| POST   | /api/jobs/{id}/rubric/generate | client      | AI drafts the rubric from the brief         |
| PUT    | /api/jobs/{id}/rubric          | client      | Save edited rubric and approve it           |
| POST   | /api/jobs/{id}/fund            | client      | Move the amount from wallet into escrow     |
| POST   | /api/jobs/{id}/submissions     | freelancer  | Submit work, triggers the AI evaluation     |
| POST   | /api/jobs/{id}/decision        | client      | approve (release) or reject (refund)        |

## Example: POST /api/jobs/{id}/submissions
Request
{ "body": "Full text of the deliverable..." }

Responses
- 201 { "submission_id": "sub_1", "status": "evaluating" }
- 400 { "error": "Submission is empty", "code": "invalid_body" }
- 409 { "error": "Job is not funded", "code": "invalid_state" }

## Example: POST /api/jobs/{id}/fund
Responses
- 200 { "status": "funded", "escrow_cents": 2500 }
- 409 { "error": "Not enough balance", "code": "insufficient_funds" }
- 409 { "error": "Rubric not approved", "code": "invalid_state" }

## Example: POST /api/jobs/{id}/decision
Request  { "action": "approve" }   (or "reject")
Responses
- 200 { "status": "released" }
- 409 { "error": "Already released", "code": "invalid_state" }

## Conventions
- Money in JSON: amount_cents (int). Never a float.
- Dates are ISO 8601, UTC.
- Every state-changing route checks role and job status through app/services/jobs.py.
- The browser never sends an amount for fund or decision routes.

## HTML pages
/ (job list) · /jobs/new · /jobs/{id} (detail, HTMX partials) · /login (demo user picker)

## Changing the API
Update this file first, then the code, then the tests.

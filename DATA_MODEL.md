# Data Model: Proofpay

Assistant: never add a column that isn't listed here. Propose it first.
SQLite via SQLAlchemy. Primary keys are text UUIDs.

## users
id text, primary key
name text
role text ('client' or 'freelancer')
paypal_email text   (sandbox personal account email, used for payouts)

## jobs
id text, primary key
client_id text -> users
freelancer_id text -> users
title text
brief text
amount_cents int
currency text, default 'USD'
status text ('draft', 'awaiting_funding', 'funded', 'submitted', 'evaluating', 'revision_requested', 'ready_for_decision', 'released', 'voided', 'cancelled')
auto_release bool, default false
revisions_used int, default 0
max_revisions int, default 2
created_at timestamp

## rubric_items
id text, primary key
job_id text -> jobs
position int
text text
critical bool, default true
approved bool, default false

## submissions
id text, primary key
job_id text -> jobs
body text (written content, length capped)
revision_number int
created_at timestamp

## evaluations
id text, primary key
submission_id text -> submissions
items_json text   (per rubric item: status met/partial/not_met, reason, confidence)
verdict text ('pass', 'fail', 'needs_review')
feedback text     (what to fix, shown to the freelancer)
model text        (model name used)
raw_output text   (raw LLM text, for debugging)
created_at timestamp

## payments
id text, primary key
job_id text -> jobs, unique
paypal_order_id text
authorization_id text
capture_id text
payout_batch_id text, null if payout is simulated
payout_mode text ('paypal' or 'ledger')
state text ('created', 'authorized', 'captured', 'voided', 'paid_out', 'failed')
created_at timestamp

## events
id text, primary key
job_id text -> jobs
kind text (e.g. 'funded', 'submitted', 'ai_verdict', 'released', 'voided', 'override')
detail text
created_at timestamp

## Rules
- Amounts are integer cents. Convert to a string like "25.00" only when calling PayPal.
- One payments row per job.
- events is append-only. It is the audit log shown on the job page.
- Schema is created from models.py on startup (no migration tool for the hackathon). Update this file with any model change.

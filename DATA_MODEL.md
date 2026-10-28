# Data Model: Proofpay

Assistant: never add a column that isn't listed here. Propose it first.
SQLite via SQLAlchemy. Primary keys are text UUIDs.

## users
id text, primary key
name text
role text ('client' or 'freelancer')
balance_cents int   (simulated money)

## jobs
id text, primary key
client_id text -> users
freelancer_id text -> users
title text
brief text
amount_cents int
escrow_cents int, default 0   (amount currently held for this job)
status text ('draft', 'awaiting_funding', 'funded', 'submitted', 'evaluating', 'revision_requested', 'ready_for_decision', 'released', 'refunded', 'cancelled')
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
items_json text   (per rubric item: status met/partial/not_met, reason, evidence quote, confidence)
verdict text ('pass', 'fail', 'needs_review')
feedback text     (what to fix, shown to the freelancer)
model text        (model name used)
raw_output text   (raw LLM text, for debugging)
created_at timestamp

## ledger_entries
id text, primary key
job_id text -> jobs
kind text ('fund', 'release', 'refund')
from_user_id text -> users, null when from escrow
to_user_id text -> users, null when to escrow
amount_cents int
created_at timestamp

## events
id text, primary key
job_id text -> jobs
kind text (e.g. 'created', 'funded', 'submitted', 'ai_verdict', 'released', 'refunded', 'override')
detail text
created_at timestamp

## Rules
- Amounts are integer cents. Never floats.
- Balances and escrow change only through ledger.py, together with a ledger_entries row, in one transaction.
- ledger_entries and events are append-only.
- Schema is created from models.py on startup (no migration tool). Update this file with any model change.

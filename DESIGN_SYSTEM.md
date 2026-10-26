# Design System: Proofpay

One look on every page. Use tokens only; never hard-code a hex value.

## Colours
| Token   | Hex     | Use                                      |
|---------|---------|------------------------------------------|
| primary | #4F46E5 | Buttons, links, focus rings              |
| success | #16A34A | Released, met, passed                    |
| warning | #D97706 | Needs review, partial                    |
| danger  | #DC2626 | Failed, voided, errors                   |
| ink     | #111827 | Body text                                |
| muted   | #6B7280 | Secondary text, captions                 |
| surface | #F9FAFB | Page and card backgrounds                |
| escrow  | #EEF2FF | "Funds held" banner background           |

## Typography (Inter, size / weight)
Display 36/700 · Heading 24/700 · Body 16/400, line 1.5 · Small 14/500

## Spacing and shape
- Spacing scale: 4, 8, 16, 24, 32, 64
- Cards: 24px padding, 12px radius, 1px border

## Components
- Button: primary (filled), secondary (outlined), danger (outlined red). One primary button per screen.
- Status badge: pill. draft=muted, awaiting_funding=warning, funded=primary, evaluating=primary,
  revision_requested=warning, ready_for_decision=warning, released=success, voided=danger.
- Escrow banner: icon, "Funds held in escrow: $X", escrow background. Shown while status is funded to ready_for_decision.
- Rubric row: icon (check = met, half = partial, cross = not met), item text, AI reason underneath in muted.
- Timeline: vertical list of events (funded, submitted, AI verdict, released).
- Empty state: one sentence and one button.

## Rules
- Tokens are Tailwind config values in the base template.
- Icons from Lucide only, 20px.
- Every button has hover, focus, disabled and loading states (HTMX indicator).
- Never show the AI verdict without its per-item reasons.

## Voice
Short, plain, friendly. Buttons say what they do: "Fund escrow", "Submit work", "Release payment", never "Submit" alone.

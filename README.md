# Demo 01 — Ask First

**Concept:** Agents should ask clarifying questions before assuming.

## What this teaches

Ambiguous tasks produce bad code. This demo shows how an `AGENTS.md` task protocol
can force the agent to stop and ask questions before writing a single line — exactly
the behavior you want from a junior engineer on their first day.

The key instruction in `AGENTS.md`:
> Before starting any task, ask any questions needed to avoid wrong assumptions.
> Do not guess. If anything about the task is ambiguous, ask first.

## The codebase

An order management service for a logistics platform. The `find_orders` function
uses a `defaultdict` index keyed on `(customer, status)` to look up orders quickly.

```
src/orders.py       — find_orders, count_by_status, seed
tests/test_orders.py — test suite
AGENTS.md           — task protocol with the ask-first rule
PROMPT.md           — the prompt to give Claude
```

## Running the demo

```bash
# Install deps (none required beyond pytest)
pytest tests/ -x --tb=short
```

Then open Claude Code in this directory and paste the prompt from `PROMPT.md`.

## Expected behavior

Claude should ask at least 2–3 clarifying questions before writing any code.
If it jumps straight to an implementation, the AGENTS.md protocol isn't being followed.

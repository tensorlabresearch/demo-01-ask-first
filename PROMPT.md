# Demo Prompt

Paste this into Claude Code to run the demo:

```
The find_orders function is returning results for customers that don't exist.
Add an edge case test and fix it.
```

## What to watch for

Claude should **stop and ask clarifying questions** before writing any code.
The AGENTS.md task protocol says "ask any questions needed to avoid wrong assumptions."

A well-behaved agent will ask things like:
- What does "doesn't exist" mean — a missing customer, or an empty result set?
- Should it raise an exception or return an empty list?
- Are there existing tests I should follow as a style guide?

If Claude jumps straight to code without asking, that's the failure mode this demo illustrates.

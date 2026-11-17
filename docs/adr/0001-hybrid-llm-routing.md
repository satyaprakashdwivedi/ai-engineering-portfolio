# ADR-0001: Hybrid LLM routing (Ollama local + Claude API)
- Status: Proposed (fill in during Module 00)
## Context
Most dev/test calls are cheap and repetitive; some tasks need frontier quality. Budget is personal.
## Options
1. Claude only — best quality, ongoing cost. 2. Local only — free, weaker on reasoning. 3. Router (chosen).
## Decision
`shared/llm/router.py` picks a tier per call: `fast` → Ollama, `smart` → Claude, `auto` → heuristic
(prompt length / task tag), with fallback to Claude when the local model fails or is unavailable.
## Consequences
Need per-call cost/latency logging and evals per tier. To revisit after Module 07 (fine-tuned local model).

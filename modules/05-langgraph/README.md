# 05-langgraph · LangGraph agents: agentic RAG, memory, human-in-the-loop
**When:** Weeks 8–9 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] StateGraph with typed state + reducers, conditional edges, streaming
- [ ] Checkpointing with SQLite saver; resume after crash; time-travel debug
- [ ] Human-in-the-loop with `interrupt()` before any side-effecting tool
- [ ] Corrective/agentic RAG on M03: retrieve → grade docs → rewrite query → fallback tool → generate → self-check hallucination
- [ ] Long-term memory via LangGraph store; tracing in Langfuse or LangSmith

## Steps (multi-agent loop: `/build-module 05-langgraph`)
1. W8: core graph, checkpoints, HITL, graph tests with fake LLM
2. W9: agentic RAG + tracing; eval delta vs M03 best pipeline
3. Auto-generate mermaid of the graph into README

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Graphs vs free-form agents: controllability, retries, persistence, auditability in production.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

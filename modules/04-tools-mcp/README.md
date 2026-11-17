# 04-tools-mcp · Tool calling from first principles + your own MCP server
**When:** Week 7 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] A raw agent loop (<150 lines) using Claude tool use: ReAct, max_steps, retries, Pydantic-validated tool args
- [ ] Tools: DuckDB SQL query, file search, calculator; guard against SQL that mutates data
- [ ] Build an MCP server (Python `mcp` SDK) exposing the same tools; connect it to Claude Code and to your loop
- [ ] Tests with a scripted fake LLM to make the loop deterministic

## Steps (multi-agent loop: `/build-module 04-tools-mcp`)
1. Spec → loop → tools → MCP server → tests
2. Record a GIF of Claude Code using your MCP server
3. Eval: 20 tasks, success rate, avg steps, tool-error rate

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
What frameworks hide; how you'd secure tools (allow-lists, read-only creds, human approval).

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

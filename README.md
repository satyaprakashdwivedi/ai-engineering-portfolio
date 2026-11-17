# AI Engineering Portfolio

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)

Hands-on, measured projects in **ML model creation, RAG, LangGraph agents, multi-agent systems, LLM fine-tuning
and LLMOps** — built by me as tech lead directing a **team of AI coding agents** (Claude Code subagents +
Claude PR review in CI). See [how it's built](docs/AI_ASSISTED_WORKFLOW.md).

Flagship capstone: **[capstone-data-platform-copilot](https://github.com/satyaprakashdwivedi/capstone-data-platform-copilot)** — multi-agent LangGraph copilot for data platform teams.

| Module | Topic | When | Status |
|---|---|---|---|
| [00-setup](modules/00-setup) | AI-assisted engineering harness | Week 1 | 🔲 |
| [01-classical-ml](modules/01-classical-ml) | Loyalty churn propensity model — end to end | Weeks 2–3 | 🔲 |
| [02-deep-learning](modules/02-deep-learning) | PyTorch from scratch + transformer fine-tuning | Week 4 | 🔲 |
| [03-rag](modules/03-rag) | RAG from naive to production-grade, with evals | Weeks 5–6 | 🔲 |
| [04-tools-mcp](modules/04-tools-mcp) | Tool calling from first principles + your own MCP server | Week 7 | 🔲 |
| [05-langgraph](modules/05-langgraph) | LangGraph agents: agentic RAG, memory, human-in-the-loop | Weeks 8–9 | 🔲 |
| [06-multi-agent](modules/06-multi-agent) | Multi-agent systems: supervisor, handoffs, comparison | Week 10 | 🔲 |
| [07-finetune-evals](modules/07-finetune-evals) | LLM fine-tuning (LoRA) + evals, guardrails, observability | Weeks 11–12 | 🔲 |

## Stack
Python 3.11 · uv · scikit-learn · XGBoost · PyTorch · Hugging Face · MLX · MLflow · Chroma · LangGraph 1.x ·
MCP · Langfuse · FastAPI · Docker · GitHub Actions · Claude API + Ollama (hybrid router)

## Run
```bash
uv sync --all-extras && uv run pytest -q
```

## About
Satyaprakash Dwivedi — engineering leader (14+ yrs, data platforms) rebuilding hands-on as an AI/ML architect.

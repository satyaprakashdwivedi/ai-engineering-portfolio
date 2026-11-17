# AGENTS.md — instructions for any AI coding agent (Claude Code, Cursor, Codex)

## Project
Public portfolio monorepo proving hands-on skill in ML, RAG, LangGraph, multi-agent systems, fine-tuning
and LLMOps. Owner: Satya (tech lead). Claude acts as an engineering team of subagents (see `.claude/agents/`).

## Layout
- `modules/NN-name/` — one self-contained module: `README.md`, `SPEC.md`, `AI_LOG.md`, `src/`, `tests/`, `evals/`
- `shared/` — reusable code (LLM router, eval utils). Import as `from shared.llm.router import LLMRouter`
- `docs/adr/` — architecture decision records, numbered `NNNN-title.md`

## Commands
- Install: `uv sync` · Tests: `uv run pytest -q` · Lint: `uv run ruff check . && uv run ruff format --check .`
- Single module tests: `uv run pytest modules/03-rag -q`

## Rules
- Python 3.11+, type hints everywhere, Pydantic for structured data, no notebooks as the only artifact
  (notebooks allowed for EDA but logic lives in `src/`).
- All LLM calls go through `shared/llm/router.py` — never instantiate provider clients inside modules.
- Default to the local Ollama model for dev/tests; Claude only where SPEC says quality matters. Tests must not
  hit paid APIs (mock them, or mark `@pytest.mark.live`).
- Every module must end with a **Results** table in its README containing real measured numbers.
- Every non-trivial design choice → ADR in `docs/adr/`.
- Conventional commits (`feat(rag): ...`). Work on `feat/<module>-<topic>` branches, never commit to `main`.
- Never write secrets; read from env (`.env` is git-ignored).

## Multi-agent workflow
Use `/build-module <module-dir>` to run: architect → implementer → test-engineer → eval-engineer → reviewer
→ docs-writer. Each agent appends a dated entry to the module's `AI_LOG.md` describing what it did.

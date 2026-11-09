# 00-setup · AI-assisted engineering harness
**When:** Week 1 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Repo, uv, ruff, pytest, pre-commit (with gitleaks) working locally
- [ ] GitHub Actions CI green; Claude PR review commenting on PRs; `@claude` mentions working
- [ ] Ollama running locally (`llama3.2:3b`, `nomic-embed-text`)
- [ ] Hybrid router `shared/llm/router.py` tested; add a live smoke test marked `@pytest.mark.live`
- [ ] Benchmark: same 20 prompts on Ollama vs Claude → latency, cost, quality (you judge 1–5)

## Steps (multi-agent loop: `/build-module 00-setup`)
1. Run `/build-module 00-setup` → approve architect's SPEC
2. Write `scripts/benchmark_router.py` (implementer) + tests (test-engineer)
3. Open first PR; screenshot the Claude review; merge
4. Finalise ADR-0001 with the benchmark numbers

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Cost-aware model routing; how you set guardrails for AI coding agents (least-privilege tools, approval gates).

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

# 06-multi-agent · Multi-agent systems: supervisor, handoffs, comparison
**When:** Week 10 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Use case: 'Data incident analyst' — researcher, SQL analyst, writer, critic
- [ ] Pattern A: LangGraph supervisor; Pattern B: handoff/swarm; shared vs isolated state
- [ ] Same task implemented in CrewAI or Claude Agent SDK for comparison
- [ ] Eval on 15 scenarios: success, tokens, latency, $; failure-mode catalogue (loops, role confusion, over-delegation)

## Steps (multi-agent loop: `/build-module 06-multi-agent`)
1. Spec with agent contracts (inputs/outputs per agent)
2. Implement both patterns + comparison
3. ADR: when multi-agent is (not) worth it vs a single agent with tools

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Multi-agent costs more and fails in new ways — show you can measure and decide.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

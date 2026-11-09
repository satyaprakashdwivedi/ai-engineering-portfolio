# 07-finetune-evals · LLM fine-tuning (LoRA) + evals, guardrails, observability
**When:** Weeks 11–12 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Task: NL→SQL for a fixed DuckDB schema (feeds the capstone) — build 500–2k training pairs (synthetic via Claude + hand-checked)
- [ ] LoRA fine-tune Qwen2.5-1.5B/3B or Llama-3.2-3B with **MLX-LM** on Apple Silicon (or Colab + PEFT/QLoRA)
- [ ] Fuse → convert to GGUF → `ollama create` → plug into the router as a new tier
- [ ] Eval: execution accuracy on held-out set — base vs fine-tuned vs Claude; latency & $
- [ ] Guardrails: prompt-injection test suite, PII redaction, SQL allow-list; CI eval gate fails PR on regression

## Steps (multi-agent loop: `/build-module 07-finetune-evals`)
1. W11: data gen + training + serving in Ollama; push adapter to HF Hub
2. W12: eval suite, guardrails, LLM-as-judge rubric, CI gate

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Build-vs-buy for models: when fine-tuning a small model pays off and how you prove it.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

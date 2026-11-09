# 02-deep-learning · PyTorch from scratch + transformer fine-tuning
**When:** Week 4 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Hand-written PyTorch training loop (Dataset, DataLoader, MLP, early stopping) on M01 data — beat or explain vs XGBoost
- [ ] Fine-tune DistilBERT on a travel/hotel review dataset for sentiment or intent (HF `Trainer` allowed here)
- [ ] Compare: fine-tuned model vs zero-shot LLM (via router) on the same test set — F1, latency, $/1k predictions
- [ ] Push the model + model card to Hugging Face Hub; use `mps` device on your Mac

## Steps (multi-agent loop: `/build-module 02-deep-learning`)
1. Spec → training loop + tests (shape tests, overfit-one-batch test)
2. Fine-tune, log to MLflow, push to Hub
3. Write comparison table + ADR: small fine-tuned model vs LLM

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
When a 66M-param model beats an LLM (cost, latency, determinism) and when it doesn't.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

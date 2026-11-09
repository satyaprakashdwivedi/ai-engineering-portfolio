# 03-rag · RAG from naive to production-grade, with evals
**When:** Weeks 5–6 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Corpus: public docs (e.g. Airflow/dbt/Spark docs or airline loyalty T&Cs) — ingestion of PDF/HTML
- [ ] Chunking experiments (fixed, recursive, semantic) · embeddings via Ollama `nomic-embed-text` · Chroma
- [ ] Golden set: 50 Q&A pairs in `evals/golden.jsonl` (≥30 hand-written)
- [ ] Advanced: hybrid BM25+vector (RRF), cross-encoder rerank, query rewriting/HyDE, metadata filters, citations
- [ ] Metrics: faithfulness, answer relevance, context precision/recall (LLM-as-judge via Claude), latency, $/query

## Steps (multi-agent loop: `/build-module 03-rag`)
1. W5: ingestion → naive RAG → golden set → baseline evals
2. W6: add one technique at a time; record the delta of each in an ablation table
3. ADR on chunking & retrieval choice backed by numbers

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Why most RAG failures are retrieval failures; how you prove an improvement with an ablation.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

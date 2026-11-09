# 01-classical-ml · Loyalty churn propensity model — end to end
**When:** Weeks 2–3 · **Status:** 🔲 not started

## What you will build (acceptance criteria)
- [ ] Dataset: Kaggle *Hotel Booking Demand* or *Telco Churn* (document licence) in `data/`
- [ ] EDA notebook → logic moved to `src/features.py` (sklearn `Pipeline` + `ColumnTransformer`)
- [ ] Baseline LogisticRegression vs XGBoost/LightGBM with stratified 5-fold CV; handle imbalance
- [ ] Hyperparameter search (Optuna), probability calibration, SHAP global + local explanations
- [ ] MLflow tracking + model registry; FastAPI `/predict` + Dockerfile; MODEL_CARD.md

## Steps (multi-agent loop: `/build-module 01-classical-ml`)
1. W2: data, EDA, feature pipeline, baseline + MLflow
2. W3: boosting, tuning, SHAP, serving, Docker, tests for feature transforms & API schema
3. eval-engineer: AUC, PR-AUC, F1@threshold, Brier score, lift@top-decile

## Results
> Filled by eval-engineer from `evals/results.json` — real numbers only.

| Metric | Baseline | This module |
|---|---|---|
| | | |

## Interview talking point
Feature leakage, choosing thresholds by business cost, why calibration matters for loyalty offers.

## Links
SPEC: [SPEC.md](SPEC.md) · AI log: [AI_LOG.md](AI_LOG.md) · ADRs: [../../docs/adr](../../docs/adr)

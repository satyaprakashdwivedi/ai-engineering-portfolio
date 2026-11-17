---
description: Orchestrate the full multi-agent build loop for one module
argument-hint: <module-dir e.g. 03-rag>
---
Module: modules/$ARGUMENTS

Run this pipeline, pausing for my approval where marked:
1. Create branch `feat/$ARGUMENTS` if not on one.
2. Use the **architect** subagent to produce/refresh SPEC.md and ADRs. ⏸ Show me the SPEC summary and wait for approval.
3. Use the **implementer** subagent to implement the SPEC tasks.
4. Use the **test-engineer** subagent in parallel on finished task groups; loop with implementer until green.
5. Use the **eval-engineer** subagent to run evals and produce the Results table.
6. Use the **reviewer** subagent on the branch diff. If REQUEST_CHANGES, send findings to implementer and repeat 4–6 (max 2 rounds).
7. Use the **docs-writer** subagent.
8. ⏸ Show me a summary (files, tests, eval deltas, review verdict) and wait before `git push` and `gh pr create`.
Ensure every agent appended to modules/$ARGUMENTS/AI_LOG.md.

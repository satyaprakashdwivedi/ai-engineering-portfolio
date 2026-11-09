# How this repo is built: AI-assisted, multi-agent engineering

I act as **tech lead**; Claude Code runs a team of specialised subagents defined in `.claude/agents/`:

| Agent | Responsibility | Tools allowed |
|---|---|---|
| architect | SPEC.md + ADRs, eval targets, task breakdown | read, write docs, web |
| implementer | code from SPEC, small commits | read/write/bash |
| test-engineer | unit/edge/graph tests, ≥80% coverage | read/write/bash |
| eval-engineer | offline evals, cost/latency, Results table | read/write/bash |
| reviewer | read-only critical review of diff | read/bash |
| docs-writer | recruiter-friendly README | read/write |

Orchestrated by `/build-module <module>` (`.claude/commands/build-module.md`) with two human approval gates
(spec approval, pre-push). In GitHub, `anthropics/claude-code-action` reviews every PR and responds to
`@claude` mentions — a second, independent reviewer.

## Evidence you can audit
- `modules/*/SPEC.md` — design written before code
- `modules/*/AI_LOG.md` — dated log of each agent's work **and my overrides**
- Commits with `Co-Authored-By: Claude` trailers; PRs with Claude review threads
- `docs/adr/` — decisions with alternatives considered

## Principles
1. Humans own the spec, the evals and the merge button. 2. Agents get least-privilege tools.
3. No number in a README that isn't produced by `evals/`. 4. Cheap local model first, Claude when it pays off.

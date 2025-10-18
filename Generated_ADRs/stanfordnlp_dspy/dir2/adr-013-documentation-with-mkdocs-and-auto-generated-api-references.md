---
### ADR-013: Documentation with MkDocs and Auto-generated API References

Status: Inferred
Context: A large, evolving API needs accessible documentation and examples.
Decision: Build docs with MkDocs Material (docs/mkdocs.yml), mkdocstrings for API docs, mkdocs-jupyter for notebooks, and deploy via Vercel (docs/vercel.json). Provide scripts to generate API docs and summaries (docs/scripts).
Consequences:
- Positive: Rich, searchable docs; examples/tutorials integrated; automated API reference stays in sync.
- Negative: Documentation build pipeline adds dependencies (requirements include mkdocstrings, mkdocs-llmstxt, etc.); extra maintenance for overrides and CI.
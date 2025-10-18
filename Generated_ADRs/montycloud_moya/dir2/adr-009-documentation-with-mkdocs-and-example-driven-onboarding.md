---
### ADR-009: Documentation with MkDocs and Example-Driven Onboarding

Status: Inferred
Context: A framework with multiple integrations and patterns needs comprehensive docs and practical examples to reduce time-to-value.
Decision: Maintain a docs site using MkDocs (mkdocs.yml, docs/*) and provide diverse examples (examples/*) including multi-agent and ReAct flows and multiple providers.
Consequences:
- Positive: Improves developer experience and adoption; facilitates learning by doing; supports maintainable, hosted documentation.
- Negative: Requires continuous documentation upkeep; examples must be kept in sync with API changes.
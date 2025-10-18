---
### ADR-003: Maintain two generation pipelines: rule-based parser and LLM-based

Status: Inferred
Context: There are two parallel directories: generator (rule-based parsing/file generation) and llmbased (LLM-driven generation) with separate code paths, outputs, and evaluation tooling.
Decision: Keep both a deterministic parser-based code generator and an LLM-based generator to compare efficacy and support different use cases.
Consequences:
- Positive: Flexibility; empirical comparison; fallback path if LLM generation underperforms.
- Negative: Duplication of effort; divergence risk between outputs; increased maintenance overhead.
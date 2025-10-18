---
### ADR-006: Retrieval-Augmented Generation (RAG) Support

Status: Inferred
Context: Many tasks require grounding responses in external knowledge via retrieval.
Decision: Provide retrievers (dspy/retrievers) for embeddings-based search, Databricks retrieval, and Weaviate; include DSP/ColBERTv2 integration (dspy/dsp/colbertv2.py).
Consequences:
- Positive: Built-in RAG capabilities; pluggable retrieval backends; improved answer grounding.
- Negative: External infra dependencies; configuration/credential complexity; consistency challenges across backends.
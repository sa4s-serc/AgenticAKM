---
### ADR-008: Classifier Abstraction Backed by LLMs

Status: Inferred
Context: Routing, intent detection, and selection (tools/agents) often require classification decisions that benefit from LLM reasoning.
Decision: Define a Classifier abstraction and an LLM-backed implementation (moya/classifiers/classifier.py, llm_classifier.py).
Consequences:
- Positive: Centralizes classification concerns; enables reuse across orchestrators and agents; consistent interface regardless of model.
- Negative: LLM-based classification adds cost/latency; results may be non-deterministic; may require guardrails and evaluation.
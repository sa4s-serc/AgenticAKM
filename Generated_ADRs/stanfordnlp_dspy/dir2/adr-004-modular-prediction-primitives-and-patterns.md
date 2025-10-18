---
### ADR-004: Modular Prediction Primitives and Patterns

Status: Inferred
Context: Common reasoning and control patterns (e.g., Chain-of-Thought, ReAct, Best-of-N, Refine, Program-of-Thought, Parallel, Retry, KNN) should be first-class and composable.
Decision: Provide a suite of prediction modules under dspy/predict (best_of_n, chain_of_thought, react, refine, program_of_thought, parallel, retry, knn, multi_chain_comparison, code_act).
Consequences:
- Positive: Rapid assembly of sophisticated reasoning workflows; reusable abstractions; easier experimentation.
- Negative: Larger API surface; maintenance overhead; potential user confusion over pattern selection and composition.
---
### ADR-008: Integrated Evaluation and Metrics

Status: Inferred
Context: Consistent evaluation across tasks/modules is necessary for optimization and CI.
Decision: Implement an evaluation module (dspy/evaluate) with Evaluate, AutoEvaluation, and metrics such as exact-match, passage-match, SemanticF1; include an EvaluationResult abstraction.
Consequences:
- Positive: Standardized measurement; easier benchmarking; supports optimizer feedback loops.
- Negative: Requires well-formed datasets/labels; metric choice may bias optimization; additional maintenance.
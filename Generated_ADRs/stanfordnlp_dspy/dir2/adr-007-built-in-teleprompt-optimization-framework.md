---
### ADR-007: Built-in Teleprompt Optimization Framework

Status: Inferred
Context: Prompt quality and few-shot selection significantly impact performance; automated optimization is essential.
Decision: Add a comprehensive teleprompt package (dspy/teleprompt) with algorithms: Bootstrap, BootstrapFinetune, RandomSearch (BootstrapRS), KNNFewShot, MIPROv2, SIMBA, Ensemble, BetterTogether, COPRO, GRPO (RL), and GEPA variants. Provide utilities for tracking and orchestration.
Consequences:
- Positive: Systematic prompt/program optimization; improved accuracy across tasks; reproducible experiments.
- Negative: Computational cost; complexity in tuning; increased dependency on datasets and evaluation pipelines.
---
### ADR-011: Dataset Utilities and Built-in Benchmarks

Status: Inferred
Context: Optimization and evaluation require curated datasets and loaders.
Decision: Offer dataset loaders and utilities (dspy/datasets) including gsm8k, hotpotqa, math, colors, ALFWorld, plus a general dataloader/dataset abstraction.
Consequences:
- Positive: Quick start for experimentation; consistency across examples/tests; support for teleprompt algorithms.
- Negative: Dataset versioning and licensing concerns; maintenance burden; potential dataset coupling.
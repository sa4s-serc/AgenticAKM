---
### ADR-008: Use Jupyter notebooks and an offline Learning Engine for evaluation

Status: Inferred
Context: results.ipynb and Learning_Engine/Performance_Evaluator.ipynb; Learning_Engine contains per-model datasets; multiple plots and trend PDFs are produced.
Decision: Perform evaluation and analysis using Jupyter notebooks and an offline Learning Engine to assess model performance and energy-confidence trade-offs.
Consequences:
- Positive: Interactive analysis; straightforward visualization and reporting; accelerates research iteration.
- Negative: Notebooks can be hard to productionize; risk of divergence between code and analysis if not synchronized.
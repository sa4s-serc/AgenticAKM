---
### ADR-012: Perform preprocessing/normalization via notebooks for data preparation

Status: Inferred
Context: normalize.ipynb exists alongside CSV market data and training scripts.
Decision: Use a Jupyter notebook to document and execute data normalization/preprocessing steps before training.
Consequences:
- Positive: Interactive exploration and documentation of preprocessing; reproducible transformations when committed.
- Negative: Notebook-based workflows can be less modular and harder to automate; requires care to keep code and data transformations in sync with training scripts.
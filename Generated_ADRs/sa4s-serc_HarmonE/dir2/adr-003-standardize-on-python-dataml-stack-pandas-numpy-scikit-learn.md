---
### ADR-003: Standardize on Python data/ML stack (pandas, numpy, scikit-learn)

Status: Inferred
Context: requirements.txt lists pandas, numpy, and scikit-learn; tools/train_models.py and inference.py/retrain.py indicate classic ML workflows rather than deep learning.
Decision: Build data processing and models using pandas/numpy and scikit-learn.
Consequences:
- Positive: Rapid development; strong ecosystem; easier maintenance and onboarding; broad model coverage for tabular/time-series data.
- Negative: Primarily CPU-bound; less suited to large-scale or deep learning tasks; limited distributed training out of the box.
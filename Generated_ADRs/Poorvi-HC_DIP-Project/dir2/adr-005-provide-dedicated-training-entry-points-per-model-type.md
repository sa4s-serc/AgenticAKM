---
### ADR-005: Provide dedicated training entry points per model type

Status: Inferred
Context: Separate training scripts (linear_reg_train.py, svm_train.py) exist rather than a unified trainer.
Decision: Create model-specific training executables to tailor data handling, hyperparameters, and evaluation routines per model.
Consequences:
- Positive: Clear, focused CLIs; easier to specialize preprocessing and metrics per algorithm.
- Negative: Potential duplication of shared logic; coordination needed to run and compare multiple trainers consistently.
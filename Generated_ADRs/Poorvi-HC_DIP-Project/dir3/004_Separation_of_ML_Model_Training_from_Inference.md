# ADR-004: Separation of ML Model Training from Inference

**Date**: 2025-10-14
**Status**: Proposed

## Context
The machine learning-based reconstruction algorithm requires a pre-trained model to function. The process of training this model is computationally intensive and distinct from the task of using it for prediction (inference).

## Decision
The architecture cleanly separates model training from inference. Dedicated scripts (`svm_train.py`, `linear_reg_train.py`) are responsible for the training process, which results in a serialized model file. The reconstruction algorithm (`algorithm4.py`) then simply loads and uses this pre-trained model.

## Consequences
This is a sound design following MLOps best practices. It improves efficiency by decoupling the time-consuming training step from the core application logic. It allows models to be trained once and reused many times. The trade-off is the added complexity of managing model artifacts, versioning, and ensuring compatibility between the training environment and the inference environment.
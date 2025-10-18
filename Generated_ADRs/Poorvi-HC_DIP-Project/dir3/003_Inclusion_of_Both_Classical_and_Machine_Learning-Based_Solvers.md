# ADR-003: Inclusion of Both Classical and Machine Learning-Based Solvers

**Date**: 2025-10-14
**Status**: Proposed

## Context
The problem of determining the next frame in a sequence can be approached either through heuristic-based similarity matching (a classical computer vision approach) or by training a model to predict the correct successor (a machine learning approach).

## Decision
The system architecture explicitly accommodates both paradigms. It includes classical algorithms based on greedy feature matching (e.g., `algorithm1.py`) as well as a more advanced approach that uses a trained Support Vector Machine (SVM) to predict the frame sequence (`algorithm4.py`).

## Consequences
This dual approach allows for a direct benchmark between traditional, explainable algorithms and modern, data-driven techniques. While the ML approach can potentially capture more complex patterns, it introduces significant overhead, including the need for training data, a separate training pipeline (`svm_train.py`), and the risk of the model not generalizing well to new videos.
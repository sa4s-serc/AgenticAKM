# ADR-007: Heterogeneous model support (PyTorch LSTM and classical regressors)

**Date**: 2025-10-09
**Status**: Proposed

## Context
Workloads include time-series forecasting where both deep and classical models can be effective under different conditions.

## Decision
Provide a simple interface to run either a PyTorch LSTM or classical models (e.g., linear/SVM), with common preprocessing and inverse transforms.

## Consequences
Flexibility to trade accuracy vs. energy/latency across model families. Requires careful feature parity and consistent data handling; increases maintenance complexity.
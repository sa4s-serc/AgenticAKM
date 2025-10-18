# ADR-010: Implicit deep learning framework dependency

**Date**: 2025-10-14
**Status**: Proposed

## Context
requirements.txt omits core DL libraries despite .pth artifacts and RL algorithms that typically rely on PyTorch/TensorFlow.

## Decision
Leave the choice/installation of the deep learning framework to the user or script-level instructions rather than pinning it in requirements.txt.

## Consequences
Flexibility for different environments; reduces lock-in; increases setup friction, reproducibility risk, and potential version mismatches leading to subtle runtime errors.
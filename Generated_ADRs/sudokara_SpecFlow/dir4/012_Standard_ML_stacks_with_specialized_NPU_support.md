# ADR-012: Standard ML stacks with specialized NPU support

**Date**: 2025-10-14
**Status**: Proposed

## Context
Balance ecosystem maturity with hardware-specific optimizations.

## Decision
Rely on PyTorch/Transformers for general modeling and integrate OpenVINO for NPU acceleration on the edge.

## Consequences
Leverages a mature ecosystem and vendor-optimized paths; introduces vendor lock-in for NPU features and model conversion/compatibility considerations.
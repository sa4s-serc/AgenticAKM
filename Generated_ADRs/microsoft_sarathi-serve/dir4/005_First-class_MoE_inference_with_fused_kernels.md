# ADR-005: First-class MoE inference with fused kernels

**Date**: 2025-10-14
**Status**: Proposed

## Context
Mixture-of-Experts architectures demand efficient expert routing and compute to be competitive at inference time.

## Decision
Implement Mixtral-style MoE with top-k routing, sharded experts, and a Triton-based fused MoE forward path (grouped GEMM) augmented by native CUDA/C++ kernels.

## Consequences
Delivers high MoE throughput and better GPU efficiency; incurs kernel maintenance burden, hardware-specific tuning needs, and increased build complexity.
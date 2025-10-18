# ADR-007: Native CUDA/C++ extensions compiled with the Python package

**Date**: 2025-10-14
**Status**: Proposed

## Context
Critical kernels (activations, layer norm, positional encoding, MoE) require performance beyond pure Python for target throughput/latency.

## Decision
Ship csrc CUDA/C++ sources and build them during packaging/installation using Ninja and setuptools, exposing optimized kernels to Python.

## Consequences
Substantial performance gains and tighter kernel integration; introduces nontrivial build toolchain and CUDA version dependencies, affecting portability and CI complexity.
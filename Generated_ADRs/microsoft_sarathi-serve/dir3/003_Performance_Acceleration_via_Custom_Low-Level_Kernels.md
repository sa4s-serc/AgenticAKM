# ADR-003: Performance Acceleration via Custom Low-Level Kernels

**Date**: 2025-10-14
**Status**: Proposed

## Context
Standard high-level frameworks like PyTorch, while versatile, often introduce performance overhead for the critical, repetitive operations in LLM inference (e.g., attention, activations, normalization). To achieve state-of-the-art throughput and low latency, these bottlenecks must be addressed at the GPU level.

## Decision
The system offloads performance-critical computations to custom-written, low-level kernels. A combination of C++/CUDA and Triton is used to implement optimized operations, such as fused MoE routing, layer normalization, and activation functions, minimizing Python overhead and maximizing GPU utilization.

## Consequences
The use of custom kernels results in significantly higher performance and reduced memory bandwidth consumption compared to a pure PyTorch implementation. The main drawback is the increased development complexity, requiring specialized expertise in CUDA/Triton. It also tightly couples the engine's performance to specific hardware (NVIDIA GPUs) and complicates the build and distribution process.
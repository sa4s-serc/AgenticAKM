# ADR-004: PyTorch-distributed model parallelism with specialized process groups

**Date**: 2025-10-14
**Status**: Proposed

## Context
To scale across multiple GPUs/nodes and models (including encoder-decoder, MoE), the runtime needs flexible parallelism topology control.

## Decision
Use torch.distributed with a parallel_state module to build and track tensor, pipeline, and data-parallel groups, including virtual pipeline stages and specialized groups for embeddings or encoder-decoder topologies.

## Consequences
Supports scalable multi-GPU execution and heterogeneous model topologies; adds synchronization/collective complexity and requires careful mapping of ranks to hardware for optimal utilization.
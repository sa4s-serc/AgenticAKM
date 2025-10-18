# ADR-004: Specialized Architecture for Mixture-of-Experts (MoE) Models

**Date**: 2025-10-14
**Status**: Proposed

## Context
The rise of sparse models, particularly Mixture-of-Experts (MoE) architectures like Mixtral, presents unique inference challenges. The dynamic, token-level routing to different 'experts' can lead to inefficient computation and memory access patterns if not handled by a specialized system.

## Decision
Dedicated architectural support for MoE models was implemented as a core feature. This includes a tensor-parallel MoE layer to distribute expert weights across GPUs and a highly optimized `FusedMoE` Triton kernel that groups tokens by their assigned expert to perform efficient block-matrix multiplications.

## Consequences
This provides a significant competitive advantage by delivering state-of-the-art inference performance for a critical and increasingly popular class of LLMs. The trade-off is that this specialization adds complexity to the codebase and focuses engineering effort on one specific architecture, which may require additional work to generalize to future, non-MoE model types.
# ADR-001: Edge–cloud speculative decoding split

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system targets faster LLM generation by combining a lightweight edge model with a heavier cloud model.

## Decision
Adopt speculative decoding with the edge running a draft model to propose tokens and the cloud running a target model to verify/complete them.

## Consequences
Can significantly reduce perceived latency and cost at the edge; introduces coordination complexity, network sensitivity, and correctness/quality trade-offs if drafts are frequently rejected.
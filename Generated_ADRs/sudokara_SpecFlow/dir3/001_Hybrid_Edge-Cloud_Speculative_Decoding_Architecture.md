# ADR-001: Hybrid Edge-Cloud Speculative Decoding Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The primary challenge is to reduce the high latency of large language model (LLM) inference for real-time, interactive applications on resource-constrained edge devices without sacrificing the accuracy of a large, high-fidelity model.

## Decision
A distributed client-server architecture was adopted. A small, fast 'draft' model runs on an edge client to speculatively generate tokens, while a large, accurate 'target' model runs on a cloud server to verify these tokens in parallel. This implements the speculative decoding algorithm across a network.

## Consequences
This design effectively lowers perceived latency by leveraging the edge device's speed for initial generation. However, it introduces system complexity by requiring the management and synchronization of two separate models and makes the system dependent on network quality for the verification step.
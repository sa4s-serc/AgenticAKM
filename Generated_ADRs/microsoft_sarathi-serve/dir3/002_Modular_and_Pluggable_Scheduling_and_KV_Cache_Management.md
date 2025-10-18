# ADR-002: Modular and Pluggable Scheduling and KV Cache Management

**Date**: 2025-10-14
**Status**: Proposed

## Context
LLM inference workloads vary significantly, from low-latency, single-request scenarios to high-throughput batch processing. A single, monolithic scheduling and memory management policy is unlikely to be optimal for all use cases. The system needed flexibility to adapt to different performance goals and research needs.

## Decision
A modular design was adopted, separating the core engine logic from scheduling and memory management. Key components like the `Scheduler` and `BlockSpaceManager` were designed as pluggable interfaces, with multiple concrete implementations provided (e.g., inspired by vLLM, Orca, and a custom 'sarathi' version).

## Consequences
This provides exceptional flexibility, allowing operators and researchers to easily swap and compare different strategies to optimize for specific workloads. It promotes a clean separation of concerns and simplifies the process of adding new algorithms. The trade-off is an increased testing surface and the need to maintain a stable and well-defined interface for these pluggable components.
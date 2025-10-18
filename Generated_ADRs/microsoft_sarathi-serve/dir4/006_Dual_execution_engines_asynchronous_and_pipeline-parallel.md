# ADR-006: Dual execution engines: asynchronous and pipeline-parallel

**Date**: 2025-10-14
**Status**: Proposed

## Context
Workloads vary between low-latency interactive serving and high-throughput batched generation across pipeline stages.

## Decision
Provide separate engines for async execution and pipeline-parallel execution paths, each coordinating scheduling, memory blocks, and distributed model steps.

## Consequences
Lets operators choose the best execution path per scenario and enables targeted optimizations; increases overall code surface area and testing matrix.
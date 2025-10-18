# ADR-003: Scheduler-coupled KV-cache and tensor block-space management

**Date**: 2025-10-14
**Status**: Proposed

## Context
LLM inference is often memory-bound due to KV-cache growth; efficient GPU memory use is critical for throughput and latency.

## Decision
Introduce block-space managers aligned to the active scheduler to control KV-cache/tensor block allocation, compaction, and reuse for maximal memory utilization.

## Consequences
Improves effective GPU capacity and reduces stalls from memory pressure; increases implementation complexity and requires fragmentation-aware policies tuned per scheduler.
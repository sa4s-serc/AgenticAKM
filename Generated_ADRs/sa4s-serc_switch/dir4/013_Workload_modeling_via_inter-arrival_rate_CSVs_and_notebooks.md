# ADR-013: Workload modeling via inter-arrival rate CSVs and notebooks

**Date**: 2025-10-10
**Status**: Proposed

## Context
Controlled evaluation under different load profiles is needed without building a full load generator service.

## Decision
Represent workloads as inter-arrival rate CSVs and use a notebook to generate/swap profiles.

## Consequences
Simple, transparent, and easy to tweak; supports deterministic experiments; limited realism for bursty or heavy-tail traffic unless explicitly modeled; not suitable for real-time stress testing.
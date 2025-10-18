# ADR-008: Centralized metrics with low-overhead instrumentation and optional W&B export

**Date**: 2025-10-14
**Status**: Proposed

## Context
Capacity planning and optimization require detailed, consistent measurements across layers and runs.

## Decision
Implement a metrics store that collects per-sequence/token/batch timings, CPU/GPU op times, histograms/CDFs, with configurable gating and filesystem export, and optional Weights & Biases integration.

## Consequences
Provides deep observability and reproducible telemetry; some runtime overhead remains (mitigated by gating), and introduces optional third-party dependency for external dashboards.
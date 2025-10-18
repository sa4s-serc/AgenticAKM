# ADR-014: CPU-centric resource monitoring

**Date**: 2025-10-10
**Status**: Proposed

## Context
The initial deployment context and available instrumentation focus on CPU-bound inference.

## Decision
Track CPU usage as the primary resource metric; GPU metrics are not integrated.

## Consequences
Simplifies setup and aligns with CPU-only scenarios; limits generality for GPU deployments where memory bandwidth, GPU util, and thermal throttling matter.
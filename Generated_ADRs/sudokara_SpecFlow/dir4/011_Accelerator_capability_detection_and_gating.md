# ADR-011: Accelerator capability detection and gating

**Date**: 2025-10-14
**Status**: Proposed

## Context
Tests and runtime should adapt to available hardware.

## Decision
Use dedicated scripts (test_gpu.py, test_npu.py) and device-aware loading to validate and select accelerators before workloads.

## Consequences
Prevents opaque runtime failures and guides users to supported paths; adds logic branches that must be kept current with evolving drivers and runtimes.
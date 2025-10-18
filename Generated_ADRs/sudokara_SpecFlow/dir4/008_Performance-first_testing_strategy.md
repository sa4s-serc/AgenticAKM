# ADR-008: Performance-first testing strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
Speculative decoding benefits must be quantified across hardware and prompts.

## Decision
Provide end-to-end performance and comparative tests with multi-prompt runs and result aggregation, plus accelerator availability checks.

## Consequences
Enables empirical tuning and regression detection; increases test runtime and requires access to specific hardware for representative results.
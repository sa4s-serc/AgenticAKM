# ADR-012: Comprehensive logging and traceability of adaptation decisions

**Date**: 2025-10-09
**Status**: Proposed

## Context
Auditing and reproducibility require visibility into what the loop decided and why.

## Decision
Persist mape_info.json, mape_log.csv, and detailed predictions/drift logs to trace state, triggers, and outcomes per iteration.

## Consequences
Facilitates debugging, benchmarking, and research. Accumulates many files over time and requires log rotation/retention strategies for long-running deployments.
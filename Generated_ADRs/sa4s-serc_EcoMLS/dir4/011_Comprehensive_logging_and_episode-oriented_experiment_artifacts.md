# ADR-011: Comprehensive logging and episode-oriented experiment artifacts

**Date**: 2025-10-10
**Status**: Proposed

## Context
Post-hoc analysis of performance, energy, and adaptation behavior requires detailed, aligned telemetry.

## Decision
Persist monitor.csv, log.csv, and MAPEK_energy.csv per run and provide notebooks to aggregate, visualize, and compare episodes.

## Consequences
Strong traceability and reproducibility with clear visual outputs. Increases disk I/O and storage needs and relies on offline analysis workflows rather than live observability dashboards.
# ADR-007: Integrated energy measurement using pyRAPL

**Date**: 2025-10-10
**Status**: Proposed

## Context
Quantifying the energy-confidence trade-off and the overhead of adaptation requires accurate energy measurements at runtime.

## Decision
Instrument the planner and main inference loop with pyRAPL and log per-cycle energy to MAPEK_energy.csv.

## Consequences
Provides actionable energy data and overhead accounting with low developer effort. Limited to CPUs/platforms exposing RAPL, excludes GPU/accelerator energy, and introduces measurement overhead and potential noise.
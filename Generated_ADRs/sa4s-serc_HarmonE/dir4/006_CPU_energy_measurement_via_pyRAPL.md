# ADR-006: CPU energy measurement via pyRAPL

**Date**: 2025-10-09
**Status**: Proposed

## Context
The framework must quantify energy consumption to inform adaptation decisions.

## Decision
Measure per-inference CPU energy using pyRAPL and record it in predictions logs; require Linux permissions setup described in README.

## Consequences
Enables energy-aware decisions with low instrumentation effort. Linux-specific and CPU-focused; does not capture GPU energy, potentially underreporting total consumption for GPU models.
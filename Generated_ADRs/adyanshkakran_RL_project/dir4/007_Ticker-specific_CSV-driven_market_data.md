# ADR-007: Ticker-specific, CSV-driven market data

**Date**: 2025-10-14
**Status**: Proposed

## Context
data/ includes CSVs for IBM, KO, PEP, WBA; normalize.ipynb exists; logs reference ticker-specific runs.

## Decision
Base trading experiments on local historical CSVs and run asset-specific trainings.

## Consequences
Enables offline, repeatable experiments; facilitates quick what-if studies; requires careful normalization/splitting to avoid leakage and may not scale to large universes without more robust data pipelines.
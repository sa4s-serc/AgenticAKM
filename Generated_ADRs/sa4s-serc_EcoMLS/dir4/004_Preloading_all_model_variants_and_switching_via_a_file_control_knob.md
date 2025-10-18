# ADR-004: Preloading all model variants and switching via a file control knob

**Date**: 2025-10-10
**Status**: Proposed

## Context
Frequent runtime switching among models should avoid cold-start latency and minimize per-request overhead.

## Decision
Load nano/small/med/large models at startup and select the active model using the value in model.csv read by the processing loop.

## Consequences
Enables near-instant switching with predictable inference latency. Increases memory footprint and startup time, couples all variants to the same host, and prevents per-request on-demand loading or elastic scaling of individual variants.
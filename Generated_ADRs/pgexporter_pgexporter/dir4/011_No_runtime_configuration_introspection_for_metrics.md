# ADR-011: No runtime configuration introspection for metrics

**Date**: 2025-10-16
**Status**: Proposed

## Context
There is ambiguity around whether the exporter auto-discovers metrics versus using curated definitions.

## Decision
Treat YAML/JSON as the source of truth for metric definitions; do not rely on runtime introspection to generate or mutate metric sets.

## Consequences
Transparency and reproducibility of metrics; avoids silent behavior changes; requires explicit updates to definitions when environments or versions change.
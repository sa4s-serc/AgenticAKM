# ADR-009: Local artifact staging under .phnx

**Date**: 2025-10-14
**Status**: Proposed

## Context
Pipeline steps (compression, encryption, upload) require temporary artifacts and reproducible naming for traceability.

## Decision
Stage intermediate and final artifacts in .phnx/compressed and .phnx/encrypted with timestamped/path-derived names prior to uploading.

## Consequences
Facilitates auditing, retries, and manual inspection; creates data-at-rest exposure and disk usage; requires cleanup policies to avoid space exhaustion; potential performance impact for large datasets.
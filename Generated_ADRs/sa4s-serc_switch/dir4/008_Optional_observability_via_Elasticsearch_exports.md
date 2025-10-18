# ADR-008: Optional observability via Elasticsearch exports

**Date**: 2025-10-10
**Status**: Proposed

## Context
The core should remain lightweight, yet support richer analytics when needed.

## Decision
Provide scripts and NDJSON artifacts to export logs/metrics to Elasticsearch without making ES a runtime requirement.

## Consequences
Keeps the baseline stack simple; allows integration with ELK for deeper analysis; lacks real-time ingestion by default; duplicative data pipelines and unmanaged schema evolution may arise.
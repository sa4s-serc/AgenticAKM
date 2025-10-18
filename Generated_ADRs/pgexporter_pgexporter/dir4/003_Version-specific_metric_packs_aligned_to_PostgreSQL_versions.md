# ADR-003: Version-specific metric packs aligned to PostgreSQL versions

**Date**: 2025-10-16
**Status**: Proposed

## Context
PostgreSQL system catalogs and telemetry differ across major versions.

## Decision
Ship curated metric packs and Grafana dashboards for PostgreSQL 13–18, each aligned with version-specific semantics.

## Consequences
Reduces breakage and ambiguity across versions; simplifies adoption; increases maintenance surface area; users must select the correct pack for their version.
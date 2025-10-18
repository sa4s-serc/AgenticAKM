# ADR-007: Co-located Data/Config Without Contract

**Date**: 2025-10-13
**Status**: Proposed

## Context
kavin.xml and kas.txt are present, but their roles and linkage to code are undocumented.

## Decision
Store auxiliary artifacts alongside code without explicit configuration management or documented schema/usage.

## Consequences
Ambiguity about purpose and lifecycle of files, brittle path assumptions, challenges in packaging/deployment, and risk of stale or environment-specific data.
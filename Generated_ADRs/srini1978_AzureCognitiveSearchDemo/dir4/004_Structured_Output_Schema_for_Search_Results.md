# ADR-004: Structured Output Schema for Search Results

**Date**: 2025-10-09
**Status**: Proposed

## Context
Output includes fields like title/name, URL, display URL, snippet, last crawled timestamp, plus errors/warnings packaged as DataEntities.

## Decision
Normalize Bing results into a predictable, typed structure suitable for downstream skill ingestion and indexing.

## Consequences
Improves downstream mapping and index schema predictability, but requires ongoing transformation maintenance if the upstream Bing API changes; over- or under-normalization can lose fidelity or increase complexity.
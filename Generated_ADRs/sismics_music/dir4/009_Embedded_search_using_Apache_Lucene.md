# ADR-009: Embedded search using Apache Lucene

**Date**: 2025-10-14
**Status**: Proposed

## Context
Lucene core/analyzers/queryparser/highlighter are managed in the parent POM.

## Decision
Implement full-text search with embedded Lucene indices.

## Consequences
Powerful search without an external service; requires careful index lifecycle, consistency, and backup strategies; scaling across nodes requires custom replication solutions.
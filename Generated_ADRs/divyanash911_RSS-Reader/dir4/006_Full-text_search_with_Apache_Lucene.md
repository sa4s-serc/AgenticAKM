# ADR-006: Full-text search with Apache Lucene

**Date**: 2025-10-13
**Status**: Proposed

## Context
The parent POM manages Lucene dependencies, typical for on-disk search indexing.

## Decision
Integrate Apache Lucene for indexing and searching feed content and articles.

## Consequences
Delivers fast, local full-text search without external services; adds index lifecycle and storage management; requires careful synchronization between DB state and index; increases disk and memory footprint.
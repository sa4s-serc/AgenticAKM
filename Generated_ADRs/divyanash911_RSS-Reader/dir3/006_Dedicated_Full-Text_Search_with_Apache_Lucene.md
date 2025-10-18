# ADR-006: Dedicated Full-Text Search with Apache Lucene

**Date**: 2025-10-13
**Status**: Proposed

## Context
The core functionality of an RSS aggregator demands efficient and powerful search capabilities across a large volume of text data, which is not handled well by standard relational database queries (e.g., SQL `LIKE`).

## Decision
Integrate Apache Lucene as a dedicated search library. This involves creating and maintaining a separate search index of the feed content to provide high-performance, full-text search.

## Consequences
This provides a fast and feature-rich search experience for users, which is critical for the application's value. The consequence is increased architectural complexity, as it introduces a new component (the search index) that must be managed and kept synchronized with the primary data store (the database).
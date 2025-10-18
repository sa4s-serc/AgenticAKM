# ADR-003: Database Technology: Cloud Firestore (NoSQL)

**Date**: 2025-10-10
**Status**: Proposed

## Context
A persistent data store was required for user orders and other application data. The database needed to integrate seamlessly with the chosen serverless backend and support flexible data structures common in e-commerce.

## Decision
Cloud Firestore, a NoSQL document database, was selected. This choice aligns with the Firebase ecosystem and provides a flexible schema suitable for storing order details.

## Consequences
Firestore offers excellent real-time data synchronization capabilities and scales horizontally. Its schemaless nature is advantageous for rapid development. However, it is not optimized for complex relational queries, and developers accustomed to SQL may face a learning curve with its data modeling and query patterns.
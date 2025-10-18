# ADR-005: Decentralized Persistence with SQLite

**Date**: 2025-10-09
**Status**: Proposed

## Context
Individual services, such as the Frontend and Model Registry, needed a simple way to store their state (e.g., user data, model metadata) without the complexity of a centralized database cluster.

## Decision
Each microservice manages its own data persistence using a local, file-based SQLite database. State is co-located with the service instance.

## Consequences
This simplifies development and deployment, as each service is self-contained. However, this approach is not production-ready as it introduces challenges for data backup, high availability, and disaster recovery. It also makes it very difficult to perform cross-service data aggregation and analytics.
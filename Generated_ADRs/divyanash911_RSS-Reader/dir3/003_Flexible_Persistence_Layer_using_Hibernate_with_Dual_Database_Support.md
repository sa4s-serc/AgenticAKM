# ADR-003: Flexible Persistence Layer using Hibernate with Dual Database Support

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application required a robust persistence strategy that could abstract away raw SQL, while also supporting a simple, in-memory database for testing and a powerful, production-grade database for real-world deployments.

## Decision
Hibernate was chosen as the ORM framework to manage data persistence. Support for both HSQLDB (for development/testing) and PostgreSQL (for production) was included, allowing the database backend to be configured based on the environment.

## Consequences
This provides significant developer productivity by working with Java objects instead of SQL. The dual-database support enhances developer and testing workflows. The trade-off is the potential for performance overhead and 'leaky abstractions' where understanding Hibernate's generated SQL is necessary for optimization.
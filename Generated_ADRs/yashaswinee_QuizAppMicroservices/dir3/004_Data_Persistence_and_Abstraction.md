# ADR-004: Data Persistence and Abstraction

**Date**: 2025-10-16
**Status**: Proposed

## Context
The application required a reliable method for interacting with a relational database that would abstract away low-level SQL and allow developers to work with Java objects directly.

## Decision
Spring Data JPA with Hibernate was chosen as the Object-Relational Mapping (ORM) solution to manage persistence for the `Question` and `Quiz` entities.

## Consequences
This significantly simplifies data access logic, reducing boilerplate code and allowing developers to perform CRUD operations through simple repository interfaces. While it improves productivity, it introduces an abstraction layer that requires careful management to avoid performance issues with complex queries.
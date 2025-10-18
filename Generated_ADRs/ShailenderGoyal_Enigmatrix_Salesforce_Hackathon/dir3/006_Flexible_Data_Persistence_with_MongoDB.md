# ADR-006: Flexible Data Persistence with MongoDB

**Date**: 2025-10-16
**Status**: Proposed

## Context
The application required a database that could flexibly handle varied and evolving data structures for user profiles, personalized learning paths, and progress tracking.

## Decision
MongoDB, a NoSQL document database, was selected for data persistence, with Mongoose used as an Object Data Modeling (ODM) library to provide schema structure and validation.

## Consequences
MongoDB's flexible schema is well-suited for the semi-structured nature of learning data, allowing for easy iteration on features. Mongoose mitigates the risk of inconsistent data by enforcing a schema at the application level. The trade-off is the lack of complex, multi-document ACID transactions found in traditional relational databases, which requires careful data modeling for features that need strong transactional consistency.
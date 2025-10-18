# ADR-003: NoSQL Document Database for Data Persistence

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application's primary data entities, such as questionnaires and user responses, are inherently semi-structured and can vary significantly. A traditional relational database with a rigid schema would be brittle and difficult to adapt as new question types or assessment formats are introduced.

## Decision
MongoDB, a NoSQL document-oriented database, was selected. This allows questionnaires, with their nested questions, varied answer types, and embedded grading logic, to be stored as single, flexible JSON-like documents.

## Consequences
The flexible schema greatly simplifies development and accommodates evolving data structures without requiring complex database migrations. It is a natural fit for the application's data model. The downside is that data consistency and validation logic must be rigorously enforced at the application layer, and it lacks the built-in transactional integrity and complex join capabilities of a relational SQL database.
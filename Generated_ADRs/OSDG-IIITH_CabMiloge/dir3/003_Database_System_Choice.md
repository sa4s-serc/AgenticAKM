# ADR-003: Database System Choice

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application needed a persistent data store for user profiles and trip information. The expected user base and concurrency were small-to-medium, and deployment simplicity was a key consideration.

## Decision
SQLite, a serverless, file-based SQL database engine, was selected. This choice avoids the overhead of setting up and managing a separate database server process.

## Consequences
Using SQLite significantly simplifies the development and deployment stack, as the database is just a file within the containerized environment. This is ideal for the intended scale but is the primary limiting factor for future growth. SQLite does not handle high write concurrency well, and scaling the application would require a migration to a client-server database like PostgreSQL or MySQL.
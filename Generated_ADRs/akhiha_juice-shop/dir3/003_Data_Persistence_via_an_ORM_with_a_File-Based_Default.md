# ADR-003: Data Persistence via an ORM with a File-Based Default

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application needs a database to simulate a realistic e-commerce site. The initial setup had to be extremely simple for beginners, eliminating the need to install and configure an external database server.

## Decision
The Sequelize ORM was chosen to abstract database interactions, providing flexibility for different SQL databases. SQLite3 was selected as the default, out-of-the-box database engine.

## Consequences
The use of an ORM allows the application to be portable across different databases (e.g., PostgreSQL, MySQL). The SQLite default makes the application zero-configuration and self-contained, drastically lowering the barrier to entry for users. While SQLite is not suitable for high-concurrency, this is irrelevant for the application's training purpose.
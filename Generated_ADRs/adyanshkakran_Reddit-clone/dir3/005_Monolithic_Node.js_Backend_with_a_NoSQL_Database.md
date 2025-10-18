# ADR-005: Monolithic Node.js Backend with a NoSQL Database

**Date**: 2025-10-14
**Status**: Proposed

## Context
The backend needed to centralize all business logic, data access, and API functionalities. The chosen database had to accommodate the flexible, semi-structured nature of social media data like posts, comments, and user profiles.

## Decision
A monolithic API service was built using Node.js with the Express.js framework. Mongoose was chosen as the ODM, which strongly implies the use of MongoDB, a NoSQL document database, for data persistence.

## Consequences
This architecture simplifies initial development and deployment, as all backend logic is in a single codebase. Node.js offers excellent I/O performance for a web API, and MongoDB's flexible schema is well-suited for evolving application requirements. However, as the application grows, this monolith could become difficult to maintain and scale, potentially becoming a single point of failure.
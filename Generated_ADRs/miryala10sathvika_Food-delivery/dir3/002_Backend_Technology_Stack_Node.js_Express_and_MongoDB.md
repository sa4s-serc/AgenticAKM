# ADR-002: Backend Technology Stack: Node.js, Express, and MongoDB

**Date**: 2025-10-13
**Status**: Proposed

## Context
The backend needed to be performant, scalable, and enable rapid development. The data model for products and orders in an e-commerce system often benefits from flexibility.

## Decision
The backend was built on Node.js with the Express.js framework, using MongoDB as the database with Mongoose as the ODM. The database is hosted on MongoDB Atlas, a managed cloud service.

## Consequences
This JavaScript-centric stack allows for code and skill reuse across the entire application. Node.js provides excellent performance for I/O-heavy operations typical of a web API. MongoDB's schemaless nature offers flexibility for the evolving data structures of products and user profiles. Using a managed database like Atlas offloads operational overhead.
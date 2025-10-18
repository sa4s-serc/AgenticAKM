# ADR-001: Adoption of a Monolithic Architecture

**Date**: 2025-10-10
**Status**: Proposed

## Context
The primary purpose of the application is to be a self-contained, easy-to-deploy educational tool for security training. It needed to simulate a complete e-commerce application within a single, manageable unit to simplify setup and use for security learners and trainers.

## Decision
A server-side monolithic architecture was chosen. All functionality, including the REST API, server-side rendered views, business logic, and data access, is bundled into a single Node.js application process.

## Consequences
This simplifies development, deployment, and local setup, allowing users to run the entire vulnerable environment with a single command. It also makes it easier to reason about the application state as a whole. The trade-off is reduced scalability and tighter coupling between components, which are acceptable limitations for an educational tool not intended for production scale.
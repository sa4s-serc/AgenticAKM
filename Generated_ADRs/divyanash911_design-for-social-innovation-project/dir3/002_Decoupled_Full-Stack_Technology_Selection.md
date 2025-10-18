# ADR-002: Decoupled Full-Stack Technology Selection

**Date**: 2025-10-13
**Status**: Proposed

## Context
The project required a modern web application with a highly interactive user interface for data entry and visualization, and a separate, scalable backend to handle business logic, data persistence, and the computationally intensive grading process.

## Decision
A decoupled client-server architecture was chosen, utilizing a technology stack of React for the frontend Single-Page Application (SPA), Python/Flask for the backend RESTful API, and MongoDB as the data store.

## Consequences
This decision promotes a clear separation of concerns, allowing frontend and backend teams to develop, test, and deploy independently. React enables a rich, component-based UI, while Flask provides a lightweight and efficient API. MongoDB's schema-less nature is well-suited for the semi-structured questionnaire data. The trade-off is the added complexity of managing the interface (API contract) between two distinct systems and requiring expertise across multiple technology stacks (JavaScript, Python).
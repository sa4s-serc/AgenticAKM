# ADR-007: Deployment and Hosting: Unified Firebase Platform

**Date**: 2025-10-10
**Status**: Proposed

## Context
The entire application, including the React SPA and the Node.js backend functions, needed a cohesive and straightforward deployment pipeline.

## Decision
The project leverages the unified Firebase platform for both hosting and backend services. Firebase Hosting serves the static assets of the React frontend, while Cloud Functions runs the backend logic.

## Consequences
This decision provides a streamlined developer experience with a single CLI for deploying both frontend and backend. Firebase Hosting includes a global CDN, ensuring fast content delivery. This tight integration simplifies CI/CD setup but deepens the vendor lock-in with Google's ecosystem, making it more difficult to migrate parts of the application to other providers in the future.
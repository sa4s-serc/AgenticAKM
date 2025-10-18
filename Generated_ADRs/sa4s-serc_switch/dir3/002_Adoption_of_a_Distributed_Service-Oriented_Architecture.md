# ADR-002: Adoption of a Distributed, Service-Oriented Architecture

**Date**: 2025-10-10
**Status**: Proposed

## Context
The system requires both a rich user interface for interaction (e.g., data submission, dashboarding) and a powerful backend for computationally intensive tasks like ML inference and control loop orchestration. Monolithic architecture would tightly couple these disparate concerns, hindering independent development and scaling.

## Decision
The application is architected as a distributed system with two main services: a React-based Single-Page Application (SPA) for the frontend and a Python/FastAPI backend that serves as the control plane. These services communicate over a network via a defined API.

## Consequences
This separation of concerns allows for independent development, deployment, and scaling of the frontend and backend. It facilitates a polyglot technology stack, but introduces network latency as a performance consideration and necessitates a well-defined, versioned API contract between the services.
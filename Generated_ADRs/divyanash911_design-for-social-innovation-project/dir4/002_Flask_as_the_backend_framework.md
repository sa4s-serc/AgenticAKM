# ADR-002: Flask as the backend framework

**Date**: 2025-10-13
**Status**: Proposed

## Context
The backend resides in code/backend with app.py as the Flask entry point and a requirements.txt.

## Decision
Use Flask as a lightweight Python microframework to implement the server-side application logic and APIs.

## Consequences
Enables fast iteration and flexible architecture, but requires explicit choices for production concerns (WSGI server, concurrency model, CORS) and scaling patterns beyond a single process.
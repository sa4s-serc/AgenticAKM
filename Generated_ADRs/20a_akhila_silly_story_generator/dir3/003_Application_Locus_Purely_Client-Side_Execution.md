# ADR-003: Application Locus: Purely Client-Side Execution

**Date**: 2025-10-10
**Status**: Proposed

## Context
The core functionality—generating a story—could be performed either on a server (with the client receiving the result) or directly within the user's browser.

## Decision
To implement all application logic, including story generation and conditional formatting, entirely on the client-side. The application runs completely within the user's web browser after the initial assets are loaded.

## Consequences
The application is highly portable and can be hosted on any simple static file server, minimizing infrastructure costs and complexity. It can also function offline after the initial load. The trade-off is that all logic is exposed to the end-user, and the application cannot perform tasks requiring a secure or persistent backend, such as saving generated stories.
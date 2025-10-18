# ADR-004: Centralized networking through a shared Axios instance

**Date**: 2025-10-10
**Status**: Proposed

## Context
An axios.js file exists to configure a single Axios instance.

## Decision
Route all HTTP calls through a shared Axios client for consistent base URL, headers, and interceptors.

## Consequences
Simplifies cross-cutting concerns like auth headers, retries, and error handling; increases coupling to Axios API; improper interceptor design can create hidden global side effects; unit tests may need extra setup/mocks.
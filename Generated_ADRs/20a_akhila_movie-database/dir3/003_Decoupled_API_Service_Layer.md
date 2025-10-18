# ADR-003: Decoupled API Service Layer

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application's core functionality is entirely dependent on an external API (TMDb). A robust design was required to isolate the data fetching and communication logic from the UI components to improve modularity, testability, and maintainability.

## Decision
A dedicated API client module (`API.js`) was created to act as a service layer. This module encapsulates all API endpoint construction, `fetch` calls, and data transformation, exposing a clean, high-level interface to the rest of the application.

## Consequences
This creates a strong separation of concerns, making UI components agnostic to the data source implementation. It centralizes all external communication, which simplifies debugging, future API migrations, and allows for easy mocking during testing.
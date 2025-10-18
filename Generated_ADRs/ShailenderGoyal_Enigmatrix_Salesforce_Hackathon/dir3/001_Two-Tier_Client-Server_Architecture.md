# ADR-001: Two-Tier Client-Server Architecture

**Date**: 2025-10-16
**Status**: Proposed

## Context
The platform requires a clear separation between the user-facing interface and the core business logic, data persistence, and AI processing to ensure scalability and maintainability.

## Decision
A classic two-tier architecture was adopted, with a distinct frontend Single-Page Application (SPA) communicating with a backend API service. The frontend handles presentation and user interaction, while the backend manages all core logic.

## Consequences
This separation allows for independent development, deployment, and scaling of the frontend and backend. It creates a well-defined API contract, enabling future clients (e.g., a mobile app) to be developed against the same backend. However, it introduces network latency between the tiers and requires careful API version management.
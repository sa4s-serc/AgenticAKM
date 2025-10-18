# ADR-001: Decoupled Two-Tier Client-Server Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system requires a highly interactive user interface for file uploads and content visualization, alongside computationally intensive, asynchronous AI processing on the backend. A monolithic architecture would couple these distinct concerns, hindering independent development, scaling, and technology selection.

## Decision
A classic two-tier architecture was adopted, with a Next.js frontend (client) completely separate from a Python backend (server). Communication between the two is handled exclusively through a REST API.

## Consequences
This separation allows for specialized technology stacks best suited for each tier (React for UI, Python for AI). It enables independent scaling and deployment of the frontend and backend. However, it introduces the complexity of maintaining an API contract, potential network latency, and requires managing two separate development and deployment pipelines.
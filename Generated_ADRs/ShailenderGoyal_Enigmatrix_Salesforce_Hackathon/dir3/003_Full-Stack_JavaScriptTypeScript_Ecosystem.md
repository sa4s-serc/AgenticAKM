# ADR-003: Full-Stack JavaScript/TypeScript Ecosystem

**Date**: 2025-10-16
**Status**: Proposed

## Context
A cohesive and efficient technology stack was needed for both the frontend and backend to build a modern, data-intensive web application.

## Decision
A full-stack JavaScript/TypeScript approach was chosen. The frontend uses React with TypeScript and Vite, while the backend is built on Node.js with Express.js. MongoDB serves as the database.

## Consequences
This creates a unified development experience, allowing developers to work across the stack with a single language. The Node.js event-driven model is highly suitable for the I/O-bound operations of an API and AI orchestration service. The large NPM ecosystem provides libraries for nearly any requirement. The main downside is that Node.js's single-threaded nature is not ideal for CPU-intensive computations, though this is mitigated by offloading heavy AI processing to Google's services.
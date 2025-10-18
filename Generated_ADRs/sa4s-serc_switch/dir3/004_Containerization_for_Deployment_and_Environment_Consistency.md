# ADR-004: Containerization for Deployment and Environment Consistency

**Date**: 2025-10-10
**Status**: Proposed

## Context
The polyglot, multi-component nature of the system creates a complex set of dependencies (Node.js runtime, Python packages, ML libraries). Ensuring that the application runs consistently across developer machines, testing environments, and production is a significant challenge.

## Decision
The entire system is containerized using Docker, with Docker Compose orchestrating the multi-container setup. This encapsulates each service (frontend, backend) with its specific dependencies into a portable, isolated environment.

## Consequences
This decision drastically simplifies setup and deployment, eliminates environment-specific bugs, and ensures reproducibility. The system becomes highly portable. The drawback is the added layer of abstraction, which can sometimes complicate debugging low-level network or file system issues, and introduces a modest performance overhead.
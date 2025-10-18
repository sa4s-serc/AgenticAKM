# ADR-001: Containerized multi-service architecture orchestrated with Docker Compose

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository contains docker-compose.yml and three service directories: backend/, frontend/, and nginx/, each with its own Dockerfile.

## Decision
Run the frontend, backend, and Nginx as separate containers defined in docker-compose, using service-specific images and a shared network.

## Consequences
Provides consistent dev/prod environments, isolated dependencies, and straightforward service composition and scaling; introduces container orchestration overhead, requires inter-service configuration management and health checks, and necessitates persistent volumes for stateful data.
# ADR-009: Containerized deployment with Docker and docker-compose

**Date**: 2025-10-10
**Status**: Proposed

## Context
Consistent runtime and simplified setup are needed across the Python backend and React frontend.

## Decision
Ship Dockerfiles and a docker-compose configuration to build and orchestrate services.

## Consequences
Improves reproducibility and onboarding; isolates dependencies; requires volume management for file-based data; introduces container orchestration complexity, especially for scaling beyond a single host.
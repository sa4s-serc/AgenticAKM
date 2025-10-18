# ADR-007: Monorepo with clear service boundaries

**Date**: 2025-10-14
**Status**: Proposed

## Context
The single repository houses backend/, frontend/, nginx/, and deployment assets (docker-compose.yml), each with its own build configuration.

## Decision
Maintain all services and infrastructure configuration in a single repository with per-service Dockerfiles and tooling.

## Consequences
Enables unified versioning and CI/CD, simplifies end-to-end changes, and eases onboarding; increases repository size and change surface, and demands discipline to maintain clean boundaries and avoid unintended cross-service coupling.
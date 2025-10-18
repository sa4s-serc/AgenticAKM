# ADR-010: Containerized builds and dev environments

**Date**: 2025-10-10
**Status**: Proposed

## Context
Contributors and workshop participants need reproducible environments across OS/architectures.

## Decision
Provide Dockerfile, docker-compose for test runs, and a devcontainer configuration for containerized development.

## Consequences
Benefits: consistent local and CI environments, simplified onboarding. Drawbacks: larger images and slower cold starts, ongoing image hardening and dependency updates.
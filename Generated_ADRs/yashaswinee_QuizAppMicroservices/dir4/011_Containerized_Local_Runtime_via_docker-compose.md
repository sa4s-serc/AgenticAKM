# ADR-011: Containerized Local Runtime via docker-compose

**Date**: 2025-10-16
**Status**: Proposed

## Context
Developers need a reproducible environment with a running PostgreSQL for the service.

## Decision
Include a docker-compose.yml to provision dependencies; rely on application startup waiting logic in DataInitializer for DB readiness.

## Consequences
Simplifies local onboarding and CI standup; reduces environment inconsistencies; readiness via sleeps/polls can be brittle; more robust health checks may be needed for complex stacks.
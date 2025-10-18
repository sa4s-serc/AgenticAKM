# ADR-002: Spring Boot 3.5 and Java 21 as the Runtime Platform

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project targets modern Java features and Spring ecosystem capabilities while maintaining productivity and broad community support.

## Decision
Use Spring Boot 3.5.0 with Java 21 LTS for application runtime, dependency management, and auto-configuration.

## Consequences
Gains access to latest Spring features, virtual threads readiness, and improved performance; constrains deployment to Java 21-compatible environments and may require updating dependencies to remain compatible.
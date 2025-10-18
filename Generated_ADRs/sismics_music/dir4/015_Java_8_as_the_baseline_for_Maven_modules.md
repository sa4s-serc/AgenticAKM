# ADR-015: Java 8 as the baseline for Maven modules

**Date**: 2025-10-14
**Status**: Proposed

## Context
The parent POM targets source/target compatibility with Java 1.8.

## Decision
Standardize on Java 8 for server/agent modules.

## Consequences
Maximizes runtime compatibility on older environments; restricts use of newer language and JVM features; future upgrades may require coordinated dependency and plugin updates across modules.
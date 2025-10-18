# ADR-001: Hybrid monorepo with dual build systems (Maven + Gradle)

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository contains a Maven parent governing multiple server/agent/distribution modules and a separate Gradle-based Android app.

## Decision
Adopt a monorepo where Maven manages Java modules while the Android client remains an independent Gradle project outside the Maven reactor.

## Consequences
Enables shared versioning and dependency alignment for server/agent modules while letting Android use its native tooling; increases CI complexity, cross-tooling expertise requirements, and risk of version drift between clients and server.
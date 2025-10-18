# ADR-001: Multi-module Maven architecture with parent POM

**Date**: 2025-10-13
**Status**: Proposed

## Context
The repository contains a parent Maven POM (com.sismics.reader:reader-parent:1.6-SNAPSHOT, packaging=pom) that declares modules such as reader-core, reader-web-common, reader-web, and additional distribution/agent modules under a production profile.

## Decision
Adopt a multi-module Maven build governed by a parent POM to centralize dependency versions and build plugins across core, web, shared, and distribution modules.

## Consequences
Ensures consistent dependency and plugin management; simplifies coordinated releases; enables clear separation of concerns across modules; increases reactor complexity and requires full module checkout to build; raises coupling to Maven as the build orchestrator.
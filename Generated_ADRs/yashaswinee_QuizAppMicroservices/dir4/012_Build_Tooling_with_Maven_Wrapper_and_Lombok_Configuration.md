# ADR-012: Build Tooling with Maven Wrapper and Lombok Configuration

**Date**: 2025-10-16
**Status**: Proposed

## Context
Consistent builds and reduced boilerplate are desired without leaking Lombok into runtime artifacts.

## Decision
Use Maven Wrapper for reproducible builds; configure maven-compiler-plugin with Lombok annotation processing; exclude Lombok from the Spring Boot fat jar via plugin configuration.

## Consequences
Streamlines builds across environments; reduces Java boilerplate; avoids shipping Lombok at runtime; requires IDEs to support Lombok annotation processing and can complicate debugging of generated code.
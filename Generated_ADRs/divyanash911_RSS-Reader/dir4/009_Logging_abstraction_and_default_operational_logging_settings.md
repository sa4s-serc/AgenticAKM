# ADR-009: Logging abstraction and default operational logging settings

**Date**: 2025-10-13
**Status**: Proposed

## Context
SLF4J and Log4j are managed in the POM, and the Jetty descriptor sets application.log.enabled=false.

## Decision
Use SLF4J with Log4j backend and expose a runtime flag to enable or disable application-level logging, defaulting to disabled in the provided Jetty context.

## Consequences
Supports flexible logging configuration and container integration; reduces noise by default; risks insufficient diagnostics unless logging is explicitly enabled in production.
# ADR-002: Declarative metric definitions in YAML/JSON

**Date**: 2025-10-16
**Status**: Proposed

## Context
Different environments require tailored metrics and evolution without recompiling the exporter.

## Decision
Externalize metric definitions into YAML/JSON with documented schemas and support for operator-defined custom metrics.

## Consequences
Flexible, reviewable, and version-controlled metrics; enables quick customization; adds responsibility for users to validate and maintain definitions; runtime parsing and validation overhead.
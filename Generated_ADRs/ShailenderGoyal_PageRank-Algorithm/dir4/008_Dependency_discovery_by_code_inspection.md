# ADR-008: Dependency discovery by code inspection

**Date**: 2025-10-16
**Status**: Proposed

## Context
Third-party libraries, if any, can only be identified by inspecting imports in project.py and references in README.

## Decision
Do not explicitly declare external dependencies; depend on users to infer and install them by reading the code and documentation.

## Consequences
Potential for runtime failures on missing packages, inconsistent environments across users, and increased setup time, albeit with zero maintenance for dependency lists.
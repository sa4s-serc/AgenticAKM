# ADR-006: Undeclared Python Version and Platform Targets

**Date**: 2025-10-13
**Status**: Proposed

## Context
No markers of supported Python versions or platforms are present (e.g., classifiers, tool configs).

## Decision
Avoid pinning a minimum/maximum Python version and omit platform constraints.

## Consequences
Potential incompatibilities across environments, unexpected syntax/runtime errors, and difficulty diagnosing version-specific issues.
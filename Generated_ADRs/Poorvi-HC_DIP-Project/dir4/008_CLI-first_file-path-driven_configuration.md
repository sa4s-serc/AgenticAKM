# ADR-008: CLI-first, file-path-driven configuration

**Date**: 2025-10-14
**Status**: Proposed

## Context
All stages are invoked as scripts with arguments and expected file locations described in README.

## Decision
Prefer simple command-line interfaces and file-based contracts over a centralized configuration service or API.

## Consequences
Pros: easy to run, compose, and automate; fits batch workflows. Cons: fragile path handling; less discoverability/validation than typed configs; harder to ensure global consistency.
# ADR-003: Direct script invocation for CLI

**Date**: 2025-10-16
**Status**: Proposed

## Context
Usage is via python3 project.py [arguments], with -h potentially exposing options if implemented.

## Decision
Expose any command-line interface directly from project.py rather than providing an installable console script or package entry point.

## Consequences
Straightforward execution without installation, but less polished UX, harder reuse as a library, and limited extensibility for multi-command CLIs.
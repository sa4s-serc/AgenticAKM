# ADR-011: Makefile-driven developer workflows

**Date**: 2025-10-11
**Status**: Proposed

## Context
Common tasks should be reproducible and easy to invoke.

## Decision
Use a Makefile to standardize commands for testing and building across contributors.

## Consequences
Simplifies onboarding and enforces repeatable workflows; may require alternatives or shims for Windows environments without make.
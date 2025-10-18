# ADR-011: Style and static analysis enforcement

**Date**: 2025-10-14
**Status**: Proposed

## Context
C++ projects are susceptible to subtle bugs and style drift without automated checks.

## Decision
Include .clang-format and .clang-tidy configurations to standardize formatting and enable linting.

## Consequences
Improves readability and catches issues early, facilitating code review and long-term maintainability. May introduce initial friction resolving lint findings and enforcing consistent tool versions.
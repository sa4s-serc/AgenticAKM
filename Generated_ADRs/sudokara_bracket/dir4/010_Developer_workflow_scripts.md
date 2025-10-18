# ADR-010: Developer workflow scripts

**Date**: 2025-10-14
**Status**: Proposed

## Context
Contributors benefit from simple, repeatable entry points for building and running tests.

## Decision
Provide make_build.sh and run_tests.sh to standardize local workflows alongside CMake and Python harnesses.

## Consequences
Reduces friction for new contributors and ensures consistent commands across environments. Scripts can drift from CMake/CI behavior if not actively maintained.
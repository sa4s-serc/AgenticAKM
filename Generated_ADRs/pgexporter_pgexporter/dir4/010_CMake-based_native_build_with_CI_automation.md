# ADR-010: CMake-based native build with CI automation

**Date**: 2025-10-16
**Status**: Proposed

## Context
A reliable, repeatable build and test process is needed for a native exporter.

## Decision
Use CMake for the build system and GitHub Actions for CI workflows.

## Consequences
Predictable builds across environments; facilitates contributions and release hygiene; contributors must be familiar with CMake and the CI setup.
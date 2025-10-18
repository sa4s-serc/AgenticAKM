# ADR-005: Undefined Entry Point and Runtime Contract

**Date**: 2025-10-13
**Status**: Proposed

## Context
It is unknown which Python file (if any) is the canonical entry point; README contents are unknown.

## Decision
Do not explicitly declare or document a single entry point/CLI; expect users to infer how to run the code from the source.

## Consequences
User confusion about invocation, inconsistent execution patterns, inability to expose standardized CLI or console scripts, and harder integration with automation.
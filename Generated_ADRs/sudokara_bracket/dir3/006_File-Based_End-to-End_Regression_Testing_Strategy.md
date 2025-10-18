# ADR-006: File-Based, End-to-End Regression Testing Strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
A reliable and scalable method was needed to verify the compiler's correctness across a wide range of language features and potential edge cases.

## Decision
A file-based regression test suite was established as the primary validation method. Each test consists of a source file and a corresponding file with the expected output or error. An automated script executes the compiler on each test case and compares the actual result against the expected one.

## Consequences
Positive: This approach is easy to extend; adding new tests is as simple as adding new files. It provides excellent coverage for the entire compilation pipeline and guards against regressions. Negative: As an end-to-end testing method, it can be difficult to pinpoint the specific compiler stage where a failure originates. It is not a substitute for finer-grained unit tests within each module.
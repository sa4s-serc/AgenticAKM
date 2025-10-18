# ADR-004: First-Class Support for Network Stubbing

**Date**: 2025-10-14
**Status**: Proposed

## Context
Writing reliable and fast unit tests for code that relies on a network layer is challenging. Real network calls make tests slow, flaky, and dependent on external services.

## Decision
To build network stubbing as a core, first-class feature of the library. This allows developers to easily provide predefined sample data for any API endpoint during testing, completely bypassing actual network calls.

## Consequences
This decision makes the networking layer and any components depending on it highly testable. It enables the creation of fast, deterministic, and reliable unit tests, which significantly improves code quality and developer confidence.
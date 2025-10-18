# ADR-002: Hybrid Build System Strategy (Maven & Gradle)

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project combines standard Java modules and a native Android module. Each of these platforms has a dominant and well-supported build tool (Maven for Java, Gradle for Android).

## Decision
A hybrid build system was adopted. Maven is used for the Java-based `music-agent` and the parent project structure, while Gradle is used for the `music-android` application. This uses the best-in-class tool for each component.

## Consequences
This pragmatic approach simplifies the build configuration for each individual module by using its native tooling. The downside is that developers need to be familiar with both build systems, and the overall continuous integration pipeline must be configured to handle both Maven and Gradle builds.
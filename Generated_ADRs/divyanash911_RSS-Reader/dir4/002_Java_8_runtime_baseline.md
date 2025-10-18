# ADR-002: Java 8 runtime baseline

**Date**: 2025-10-13
**Status**: Proposed

## Context
The parent POM targets Java 8 and pins dependency versions aligned with that runtime era.

## Decision
Standardize on Java 8 as the language and runtime baseline for all modules.

## Consequences
Maximizes compatibility with older environments; leverages mature library ecosystem; limits access to newer language features and JVM improvements; imposes long-term security and maintenance considerations due to Java 8’s age.
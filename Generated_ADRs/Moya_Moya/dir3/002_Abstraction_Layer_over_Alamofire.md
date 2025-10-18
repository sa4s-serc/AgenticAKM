# ADR-002: Abstraction Layer over Alamofire

**Date**: 2025-10-14
**Status**: Proposed

## Context
Directly using a low-level networking library like Alamofire can lead to verbose, repetitive code and lacks a structured, application-specific API contract. A higher-level pattern was required to enforce consistency and simplify network calls.

## Decision
To build Moya as a dedicated network abstraction layer on top of Alamofire, rather than creating a new networking client from scratch. This leverages Alamofire's proven networking stack while providing a more opinionated, type-safe interface.

## Consequences
Developers gain a clean, testable, and type-safe API for networking without having to manage the complexities of the underlying network transport. The project benefits from the stability and performance of Alamofire while focusing on solving higher-level architectural problems.
# ADR-001: Abstraction Over Alamofire/URLSession

**Date**: 2025-10-14
**Status**: Proposed

## Context
Moya provides a higher-level networking API for Swift clients while relying on a proven HTTP engine.

## Decision
Build Moya as a thin, opinionated layer on top of Alamofire, which itself uses URLSession.

## Consequences
Pros: Leverages Alamofire stability and features, reduces maintenance of HTTP minutiae, benefits from Apple's URLSession improvements. Cons: Inherits Alamofire's API and release cadence, limits ultra low-level tuning, introduces a double abstraction that can complicate debugging.
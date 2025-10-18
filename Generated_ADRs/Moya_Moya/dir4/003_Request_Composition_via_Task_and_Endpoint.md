# ADR-003: Request Composition via Task and Endpoint

**Date**: 2025-10-14
**Status**: Proposed

## Context
Requests must support varied payloads and encodings while remaining predictable.

## Decision
Use a Task enum to describe request bodies, parameters, multipart uploads, and downloads; build URLRequest via Endpoint composition.

## Consequences
Pros: Standardized encoding and payload handling, extensible request building, fewer ad-hoc code paths. Cons: Adds abstraction to learn, some coupling to Alamofire encoders, edge cases may require custom adapters.
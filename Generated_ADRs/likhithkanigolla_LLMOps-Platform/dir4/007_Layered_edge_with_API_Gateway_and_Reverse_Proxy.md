# ADR-007: Layered edge with API Gateway and Reverse Proxy

**Date**: 2025-10-09
**Status**: Proposed

## Context
api-gateway/server.py and reverse-proxy/reverse-proxy.py exist as separate services, implying distinct roles for request brokering.

## Decision
Introduce an API Gateway for request aggregation/routing and a separate Reverse Proxy for edge routing/termination.

## Consequences
Pros: centralized cross-cutting concerns (routing, rate limiting, request shaping), cleaner backend interfaces. Cons: extra network hops, potential bottlenecks and single points of failure, more complex configuration and deployment pipelines.
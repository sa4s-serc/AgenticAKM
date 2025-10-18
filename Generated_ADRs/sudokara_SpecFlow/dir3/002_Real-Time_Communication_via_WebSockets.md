# ADR-002: Real-Time Communication via WebSockets

**Date**: 2025-10-14
**Status**: Proposed

## Context
The speculative decoding algorithm requires a continuous, low-latency, bidirectional stream of data between the edge client (sending draft tokens) and the cloud server (sending verified/corrected tokens). A traditional HTTP request-response model would be too slow and inefficient.

## Decision
WebSockets were chosen as the communication protocol. This provides a persistent, full-duplex connection, allowing the client and server to exchange data in real-time with minimal overhead.

## Consequences
This enables the highly interactive nature of the system, which is critical for its performance. The trade-off is increased complexity in connection management and potential challenges with firewalls and network proxies compared to standard HTTP.
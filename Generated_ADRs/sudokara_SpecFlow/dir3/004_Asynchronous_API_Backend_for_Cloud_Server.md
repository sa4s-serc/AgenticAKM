# ADR-004: Asynchronous API Backend for Cloud Server

**Date**: 2025-10-14
**Status**: Proposed

## Context
The cloud server must efficiently handle numerous concurrent, long-lived WebSocket connections from edge clients. A traditional synchronous, thread-per-connection model would not scale well and would consume excessive resources.

## Decision
The cloud server was built using a high-performance asynchronous Python stack, specifically FastAPI and Uvicorn. This allows the server to manage many I/O-bound operations (like waiting for network data) concurrently with a small number of threads.

## Consequences
This results in a highly scalable and resource-efficient server capable of maintaining low latency under load. The primary trade-off is that it requires developers to work within an asynchronous programming paradigm, which can have a steeper learning curve and be more complex to debug than synchronous code.
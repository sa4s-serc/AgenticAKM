# ADR-002: Asynchronous Metrics Collection via Message Bus

**Date**: 2025-10-09
**Status**: Proposed

## Context
The central Controller needs a reliable, real-time stream of system metrics (CPU, memory) from a potentially large number of Agents to make intelligent scheduling decisions. A synchronous request model would be inefficient and not scale.

## Decision
Implement Apache Kafka as an asynchronous message bus. Agents act as producers, continuously publishing host and container metrics to a topic. The Controller acts as a consumer, processing this stream to maintain a view of the cluster's state.

## Consequences
This decouples the Agents from the Controller, increasing system resilience; agents can continue reporting metrics even if the controller is temporarily unavailable. The bus acts as a buffer, smoothing out load spikes. The trade-off is the added complexity and operational overhead of managing a Kafka cluster.
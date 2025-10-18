# ADR-004: Event-driven integration via Kafka for controller workflows

**Date**: 2025-10-09
**Status**: Proposed

## Context
controller-Service/kafka-docker-setup contains docker-compose.yaml and run_kafka.py, indicating Kafka is used alongside the controller.

## Decision
Introduce Apache Kafka as a messaging backbone to decouple controller/agents and support asynchronous workflows.

## Consequences
Pros: improved decoupling and buffering, resilience to spikes, foundation for event-driven processes. Cons: additional infra complexity, need for schema/contract governance, operational overhead (brokers, topics, offsets), and eventual consistency considerations.
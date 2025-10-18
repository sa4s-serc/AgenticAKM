---
### ADR-005: Use Apache Kafka for asynchronous messaging

Status: Inferred
Context: confluent-kafka appears across multiple requirements; controller-Service includes kafka-docker-setup with docker-compose.yaml and run_kafka.py, suggesting Kafka is the event bus for orchestration.
Decision: Introduce Kafka (via Confluent Kafka client) as the messaging backbone between controller, agents, and possibly other services.
Consequences:
- Positive: Decoupled communication, buffering, and reliable event-driven workflows; improved scalability for orchestration.
- Negative: Operational overhead (brokers, topics, consumer groups); added complexity in error handling and eventual consistency.
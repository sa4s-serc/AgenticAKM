---
### ADR-003: Hybrid Communication Strategy (REST and Message Queue)

**Status:** Inferred
**Context:** The distributed nature of the microservices architecture requires robust mechanisms for inter-service communication. Some interactions are synchronous (requiring an immediate response), while others are asynchronous (fire-and-forget commands or events), which can improve system resilience and decoupling.
**Decision:** A hybrid communication strategy was adopted.
1.  **Synchronous Communication:** The widespread use of the `requests` library in `requirements.txt` files indicates that services communicate directly via synchronous HTTP/REST APIs.
2.  **Asynchronous Communication:** The `confluent-kafka` library and the `controller-Service/kafka-docker-setup/docker-compose.yaml` file show that **Apache Kafka** is used as a message bus for asynchronous, event-driven communication between certain services, likely the `controller-Service` and one or more `agent-Service` instances.
**Consequences:**
*   **Positive:**
    *   Provides flexibility to choose the appropriate communication pattern for the use case.
    *   Kafka enables loose coupling, fault tolerance, and scalability for asynchronous workflows, preventing the controller from being blocked while waiting for agents.
*   **Negative:**
    *   Introduces the operational overhead of managing a Kafka cluster.
    *   Developers must be proficient in both RESTful API design and event-driven patterns.
    *   Increased complexity in debugging and tracing requests that span both communication types.
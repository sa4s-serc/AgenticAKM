---
### ADR-004: Centralized Agent Discovery via a Registry

**Status:** Inferred
**Context:** In a multi-agent system, orchestrators and other components need a way to locate and interact with available agents. Hardcoding agent locations or direct instantiation would create tight coupling and make the system static and hard to manage, especially in a distributed or dynamic environment (as hinted at by `remote_agent_server_with_auth.py`).

**Decision:** Implement a central `AgentRegistry` (`moya/registry/agent_registry.py`) that acts as a service locator for agents. This registry uses an underlying `AgentRepository` (`moya/registry/agent_repository.py`), with an initial `InMemoryAgentRepository`, to store and retrieve agent definitions. This provides a single, consistent mechanism for any part of the system to discover and resolve agent information.

**Consequences:**
*   **Positive:**
    *   **Loose Coupling:** Components like orchestrators are not directly tied to specific agent instances. They can look them up by name or capability.
    *   **Dynamic Configuration:** Agents can be registered or de-registered at runtime, allowing for dynamic and scalable system composition.
    *   **Centralized Management:** Provides a single point of control and visibility into all the agents available in the system.
*   **Negative:**
    *   **Single Point of Failure:** If the registry service goes down, agent discovery will fail, potentially crippling the entire system.
    *   **Potential Performance Bottleneck:** In a very high-throughput system, a naive registry implementation could become a bottleneck for agent lookups.
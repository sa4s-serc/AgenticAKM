### ADR-001: Pluggable Architecture for LLM Agent Providers

**Status:** Inferred
**Context:** The system needs to interact with Large Language Models (LLMs) to power its agents. Different users and deployment environments may require or prefer different LLM providers, such as OpenAI, Microsoft Azure, Amazon Bedrock, or locally-hosted models via Ollama. Hardcoding a single provider would severely limit the framework's applicability, flexibility, and ability to adapt to the rapidly changing AI landscape.

**Decision:** An abstraction layer was created for agents. A base agent interface is likely defined in `moya/agents/agent.py`. Concrete implementations are then provided for each specific LLM provider or framework, such as `AzureOpenAIAgent`, `BedrockAgent`, `OllamaAgent`, `OpenAIAgent`, and even a meta-framework agent like `CrewAIAgent`. This allows the core logic of the system to interact with any agent through a common interface, irrespective of the underlying model provider.

**Consequences:**
*   **Positive:**
    *   **Extensibility:** New LLM providers can be integrated by simply creating a new class that adheres to the agent interface, without modifying the core system.
    *   **Flexibility:** Users can easily switch between cloud-based providers, open-source models, and local models for development, testing, or cost-management purposes.
    *   **Decoupling:** The orchestration and tool-using logic is completely decoupled from the specifics of how to call a particular LLM API.
*   **Negative:**
    *   **Interface Maintenance:** The base agent interface must be carefully designed to accommodate the common features of various providers. Unique or advanced features of a specific provider might be difficult to expose through the generic interface.
    *   **Increased Complexity:** Introduces a layer of indirection, which can add a slight overhead and requires developers to understand the abstraction rather than a direct API call.
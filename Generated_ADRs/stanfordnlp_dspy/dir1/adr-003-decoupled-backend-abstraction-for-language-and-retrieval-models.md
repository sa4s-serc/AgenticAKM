---
### ADR-003: Decoupled Backend Abstraction for Language and Retrieval Models

**Status:** Inferred
**Context:** The AI landscape includes a wide variety of LLM providers (OpenAI, Databricks, local models) and retrieval systems (ColBERTv2, Weaviate). Tightly coupling the framework to a single provider would severely limit its utility, portability, and future-readiness.
**Decision:** An abstraction layer was implemented to decouple the core framework logic from specific backend services. This is evident in two key areas:
1.  **Language Models (`dspy/clients`):** A base class (`base_lm.py`) defines a common interface for interacting with LLMs. Specific implementations for different providers (e.g., `openai.py`, `databricks.py`) inherit from this base.
2.  **Retrieval Models (`dspy/retrievers`):** A similar pattern is used for information retrieval, with modules for different retrieval services like `ColBERTv2` and `Weaviate`.
This allows the user to configure which backend they want to use at runtime without changing the program's modules or signatures.
**Consequences:**
*   **Positive:**
    *   **Vendor Independence:** Users can easily switch between different LLM or retrieval backends.
    *   **Extensibility:** It is straightforward to add support for new models and services by creating a new client or retriever class.
    *   **Future-Proofing:** The framework can adapt as new, more powerful models become available.
*   **Negative:**
    *   **Least Common Denominator:** The common interface may not expose all the unique, provider-specific features of a particular backend without special handling.
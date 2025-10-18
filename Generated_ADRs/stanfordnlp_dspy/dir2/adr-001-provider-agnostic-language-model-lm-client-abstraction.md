### ADR-001: Provider-agnostic Language Model (LM) Client Abstraction

Status: Inferred
Context: The project needs to interact with multiple LM providers (e.g., OpenAI, Databricks) and local backends, while keeping the application code independent of provider-specific SDKs and conventions.
Decision: Introduce a provider-agnostic client layer under dspy/clients with a BaseLM abstraction (base_lm.py), concrete providers (openai.py, databricks.py, lm_local.py, lm_local_arbor.py), and a provider management layer (provider.py). Provide optional compatibility shims and logging hooks for LiteLLM (utils to enable/disable LiteLLM logging; tests include a litellm_server).
Consequences: 
- Positive: Flexible integration with many providers; easier swapping/migration; centralized handling of retries, timeouts, and telemetry.
- Negative: Ongoing maintenance to track provider API changes; potential least-common-denominator constraints; added abstraction complexity.
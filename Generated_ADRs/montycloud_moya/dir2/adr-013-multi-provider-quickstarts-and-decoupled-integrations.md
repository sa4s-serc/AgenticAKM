---
### ADR-013: Multi-Provider Quickstarts and Decoupled Integrations

Status: Inferred
Context: Users rely on varied LLM providers and deployment models; the framework should remain neutral and flexible.
Decision: Provide quickstart examples for OpenAI, Azure OpenAI, Bedrock, Ollama, CrewAI, multi-agent, and ReAct (examples/quick_start_*.py) while keeping core APIs provider-agnostic.
Consequences:
- Positive: Broad applicability; reduces vendor lock-in; encourages experimentation across providers.
- Negative: Testing matrix grows; subtle differences across providers must be abstracted or documented; optional dependencies may complicate environment setup.
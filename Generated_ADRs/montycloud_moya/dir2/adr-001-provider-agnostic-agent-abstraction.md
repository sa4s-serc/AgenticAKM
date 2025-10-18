### ADR-001: Provider-agnostic Agent Abstraction

Status: Inferred
Context: The codebase needs to support multiple LLM providers and runtimes (OpenAI, Azure OpenAI, Amazon Bedrock, Ollama, CrewAI) without locking users into a single vendor or SDK. Directly depending on provider-specific APIs would tightly couple the system and make it harder to switch or mix providers.
Decision: Introduce a core Agent abstraction (moya/agents/agent.py) with provider-specific adapters (openai_agent.py, azure_openai_agent.py, bedrock_agent.py, ollama_agent.py, crewai_agent.py) and a remote_agent.py for out-of-process agents.
Consequences: 
- Positive: Clean separation of concerns; easy to add new providers; unified interface for orchestration and tools; enables hybrid deployments.
- Negative: Requires ongoing maintenance across multiple provider integrations and normalization of heterogeneous capabilities; potential impedance mismatch between provider features.
---
### ADR-005: Google GenAI as the LLM provider with a thin wrapper

Status: Inferred
Context: google-genai is a dependency; backend/llm.py suggests a wrapper module; prompt assets exist under backend/video/prompts and config/MASTER_PROMPT.txt.
Decision: Use Google GenAI for generation tasks via a custom llm.py abstraction and file-based prompt templates.
Consequences:
- Positive: Decouples provider specifics from business logic; prompt assets are versioned as files; easy experimentation.
- Negative: Provider lock-in at runtime; managing secrets/quotas required; prompt files can drift without centralized management.
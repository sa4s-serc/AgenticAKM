---
### ADR-007: Use OpenAI API for conversational/NLP capabilities in the bot

Status: Inferred
Context: The backend includes openai/service.py and the openai dependency. The bot likely requires generative or NLP features (e.g., conversation handling, summarization, intent).
Decision: Delegate NLP/generative tasks to the OpenAI API from the WhatsApp bot service.
Consequences:
- Positive: Rapid access to state-of-the-art language models; less custom ML infrastructure; faster feature iteration.
- Negative: External dependency, latency, and cost; data handling/compliance considerations; need for robust error handling and retries.
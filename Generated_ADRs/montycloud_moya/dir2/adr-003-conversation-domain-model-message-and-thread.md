---
### ADR-003: Conversation Domain Model (Message and Thread)

Status: Inferred
Context: LLM interactions rely on structured conversational context (messages, roles, histories). Informal handling leads to inconsistency and complicates persistence or replay.
Decision: Establish a conversation model with Message and Thread entities (moya/conversation/message.py, thread.py) managed separately from agents and orchestrators.
Consequences:
- Positive: Standardized schema across providers and orchestrators; easier persistence, replay, and tooling; clearer interfaces for memory and classifiers.
- Negative: Constraints on message structure may limit provider-specific features unless extended carefully.
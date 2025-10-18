---
### ADR-007: Persist application data in MongoDB via Mongoose

Status: Inferred
Context: Mongoose dependency and models for chatMessage, chatSession, knowledgeBase, note, preAssessment, and users indicate MongoDB usage.
Decision: Use MongoDB with Mongoose ORM for persistence.
Consequences:
- Positive: Flexible schema for rapidly evolving domains (AI chat, KB, notes); robust ODM features.
- Negative: Schema migrations and consistency must be managed carefully; relational queries may be more complex.
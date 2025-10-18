---
### ADR-005: Data store: MongoDB accessed via PyMongo

Status: Inferred
Context: requirements include pymongo; scripts load Excel data into Mongo; model seems document-oriented (questionnaires, responses, rules).
Decision: Use MongoDB as the primary database and access it with PyMongo.
Consequences:
- Positive: Flexible schema suits surveys/questionnaires and evolving analytics; easy ingestion of semi-structured data.
- Negative: Requires careful design for relational-like queries and transactions; potential consistency trade-offs.
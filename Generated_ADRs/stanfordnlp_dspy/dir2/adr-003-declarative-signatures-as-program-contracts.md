---
### ADR-003: Declarative Signatures as Program Contracts

Status: Inferred
Context: Reusable LLM “programs” need clear input/output specifications to enable composition, testing, and optimization.
Decision: Create a Signatures system (dspy/signatures) with Signature and Field objects to declare typed interfaces for modules and predictions.
Consequences:
- Positive: Stronger modularity; easier validation; better auto-documentation and evaluation; enables teleprompt optimizers to reason over I/O.
- Negative: Learning curve for users; need to keep signatures synced with program logic; risk of schema drift.
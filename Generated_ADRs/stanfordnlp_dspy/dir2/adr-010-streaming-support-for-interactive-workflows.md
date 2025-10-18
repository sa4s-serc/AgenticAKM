---
### ADR-010: Streaming Support for Interactive Workflows

Status: Inferred
Context: Streaming tokens improves UX for interactive applications and long generations.
Decision: Provide streaming primitives (dspy/streaming) including streamify, messages, and StreamListener; integrate with LM clients where possible.
Consequences:
- Positive: Better interactivity; improved observability into generation.
- Negative: More complex control flow; potential provider feature mismatch; higher test surface.
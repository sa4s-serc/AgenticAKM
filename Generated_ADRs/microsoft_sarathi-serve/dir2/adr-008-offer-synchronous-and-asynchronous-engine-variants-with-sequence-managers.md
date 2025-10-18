---
### ADR-008: Offer synchronous and asynchronous engine variants with sequence managers

Status: Inferred
Context: engine has base_llm_engine.py, llm_engine.py, async_llm_engine.py. sequence_manager provides engine and worker sequence managers and typed step inputs.
Decision: Separate synchronous and asynchronous execution engines and encapsulate concurrency/state handling in sequence managers to manage sequences, steps, and outputs cleanly.
Consequences:
- Positive: Clear separation of concerns; enables high-throughput async serving while retaining simpler sync paths.
- Negative: Additional code paths to maintain; more complex lifecycle and error handling.
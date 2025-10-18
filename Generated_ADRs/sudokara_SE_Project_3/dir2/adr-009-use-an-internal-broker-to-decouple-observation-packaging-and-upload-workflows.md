---
### ADR-009: Use an internal broker to decouple observation, packaging, and upload workflows

**Status:** Inferred
**Context:** The utils folder contains Broker.py, suggesting a simple pub-sub or mediator to coordinate between Observation, Compression_Encryption, and Uploader without tight coupling.
**Decision:** Introduce a lightweight internal event broker to publish file system events and subscribe processing stages (compression, encryption, upload).
**Consequences:** 
- Positive: Improves modularity and testability; allows swapping strategies without changing event producers/consumers; supports future asynchronous processing.
- Negative: Adds complexity in debugging event flows; requires careful error handling and backpressure if events spike.
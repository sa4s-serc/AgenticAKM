---
### ADR-002: Use pluggable Strategy patterns across core subsystems

**Status:** Inferred
**Context:** The codebase defines interfaces and multiple concrete implementations: ObservationStrategy (EventDrivenStrategy, PeriodicStrategy), ICompressionStrategy (TarCompressionStrategy, NoCompressionStrategy), IEncryptionStrategy (GPGEncryptionStrategy), and Uploader Strategy abstractions (GoogleDrive, OneDrive). Managers (e.g., OManager, CEManager) orchestrate these.
**Decision:** Use the Strategy pattern to make observation, packaging, encryption, and upload mechanisms pluggable and interchangeable at runtime.
**Consequences:** 
- Positive: Enables easy extension (e.g., new cloud providers, new compression algorithms) without changing calling code. Supports environment-specific choices (e.g., event-driven vs periodic).
- Negative: Increased abstraction and indirection can add complexity. Requires careful configuration and testing matrix across strategy combinations.
---
### ADR-006: Manage GPG via python-gnupg with a Singleton and dedicated key strategy

**Status:** Inferred
**Context:** Presence of python-gnupg in requirements, GPGEncryptionStrategy, GPGKeyStrategy, and GPGSingleton imply a centralized GPG context and explicit key management.
**Decision:** Use python-gnupg to perform encryption and manage keys, centralizing GPG initialization via a Singleton and encapsulating key operations behind a strategy.
**Consequences:** 
- Positive: Avoids repeated GPG setup overhead; standardizes key handling; improves testability by isolating crypto operations.
- Negative: Singleton can hinder parallelism/test isolation; secure key storage and permissions must be carefully handled to avoid leaks.
---
### ADR-014: Centralize common behaviors with a shared SingletonMeta

**Status:** Inferred
**Context:** utils/SingletonMeta.py and GPGSingleton indicate a pattern of centralizing single-instance components (e.g., GPG context).
**Decision:** Use a custom Singleton metaclass for components that must have a single process-wide instance (e.g., cryptographic context).
**Consequences:** 
- Positive: Prevents redundant initialization, reduces resource contention, and simplifies access to shared services.
- Negative: Can complicate testing (global state), and can become a hidden dependency if overused.
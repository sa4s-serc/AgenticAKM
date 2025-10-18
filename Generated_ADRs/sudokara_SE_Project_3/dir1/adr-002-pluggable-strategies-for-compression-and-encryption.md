---
### ADR-002: Pluggable Strategies for Compression and Encryption

**Status:** Inferred
**Context:** The system is designed to handle user data, which requires both security (encryption) and storage efficiency (compression). The specific algorithms for these tasks might need to be changed or extended in the future to support new standards or user preferences. The architectural challenge was to design a system that decouples the core backup logic from the specific implementation of these algorithms.
**Decision:** The Strategy design pattern was implemented for both compression and encryption. This is evident from the file structure in `src/phoenix/Compression_Encryption/`, which includes:
*   Interfaces: `ICompressionStrategy.py`, `IEncryptionStrategy.py`.
*   Concrete Implementations: `TarCompressionStrategy.py`, `NoCompressionStrategy.py`, and `GPGEncryptionStrategy.py`.
The use of the `python-gnupg` library in `requirements.txt` confirms the choice of GPG as the primary encryption technology. This decision is further documented in `docs/ADRs/CompressionEncryption.md`.
**Consequences:**
*   **Positive:**
    *   **Flexibility and Extensibility:** New compression (e.g., Zip) or encryption (e.g., AES) methods can be added by simply creating a new class that implements the corresponding strategy interface, without altering existing application logic.
    *   **Improved Maintainability:** The separation of concerns makes the code easier to understand, test, and maintain. The logic for TAR compression is isolated within its own file.
*   **Negative:**
    *   **Increased Complexity:** This pattern introduces a higher number of classes and interfaces, which can slightly increase the initial complexity of the codebase.
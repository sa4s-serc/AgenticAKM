---
### ADR-005: Compress-then-encrypt pipeline using tar.gz and GPG

**Status:** Inferred
**Context:** Compression_Encryption has TarCompressionStrategy and NoCompressionStrategy, GPGEncryptionStrategy, GPGKeyStrategy; artifacts are stored as .tar.gz and .tar.gz.gpg under CLI/.phnx. An ADR named CompressionEncryption.md exists.
**Decision:** Create backup artifacts by first compressing (tar.gz) and then encrypting (GPG) the data. Support a no-compression option.
**Consequences:** 
- Positive: Compressing before encryption optimizes size; standard formats (tar.gz, GPG) ensure compatibility and security. Clear pipeline separation eases testing and substitution.
- Negative: Full-file packaging can be I/O heavy; encryption requires key management and secure storage. Double-step processing adds latency for large files.
---
### ADR-012: Favor file-level snapshot packaging over block-level diffs

**Status:** Inferred
**Context:** The pipeline compresses files into tarballs upon events and encrypts them; there is no library indicating block-level delta computation. Presence of diff.py suggests change detection rather than binary delta storage, and artifacts show full-file tarballs.
**Decision:** On change events, create compressed snapshots (tar.gz) rather than computing block-level binary diffs.
**Consequences:** 
- Positive: Simpler implementation and recovery; avoids complex delta algorithms; robust across file types.
- Negative: Potentially higher storage and bandwidth usage for large files with small changes; more I/O per change event.
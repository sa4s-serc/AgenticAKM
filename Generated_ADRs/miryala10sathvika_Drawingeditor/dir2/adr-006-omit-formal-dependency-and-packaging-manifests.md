---
### ADR-006: Omit formal dependency and packaging manifests

**Status:** Inferred
**Context:** There is no requirements.txt, setup.py, or pyproject.toml; manifest_content is empty. This suggests no formal dependency specification or packaging metadata is maintained.
**Decision:** Avoid maintaining a formal dependency list and packaging configuration; operate as ad-hoc scripts.
**Consequences:** 
- Positive: Reduced setup overhead, faster initial development, fewer files to maintain if standard library suffices.
- Negative: Harder to reproduce environments, unclear dependency versions, more friction for users to install correct dependencies, complicates CI/CD and distribution.
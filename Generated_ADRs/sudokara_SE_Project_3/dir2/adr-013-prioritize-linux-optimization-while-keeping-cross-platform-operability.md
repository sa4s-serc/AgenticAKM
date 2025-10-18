---
### ADR-013: Prioritize Linux optimization while keeping cross-platform operability

**Status:** Inferred
**Context:** Use of pyinotify ties the optimal path to Linux, but PeriodicStrategy provides an alternative. The rest of the stack (python-gnupg, Google API client) is cross-platform.
**Decision:** Optimize for Linux with inotify for best performance, while providing a periodic polling fallback for non-Linux platforms.
**Consequences:** 
- Positive: Best-in-class performance on Linux; retains broader usability.
- Negative: Non-Linux users get a degraded experience; platform-specific code paths increase testing complexity.
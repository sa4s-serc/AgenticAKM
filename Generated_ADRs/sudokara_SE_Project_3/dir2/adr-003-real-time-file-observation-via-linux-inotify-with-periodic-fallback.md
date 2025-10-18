---
### ADR-003: Real-time file observation via Linux inotify with periodic fallback

**Status:** Inferred
**Context:** The requirements include pyinotify, and there is an ADR named Inotify.md along with Observation/EventDrivenStrategy.py and Observation/PeriodicStrategy.py. The project appears Linux-focused but also provides a fallback option.
**Decision:** Use pyinotify (Linux inotify) for event-driven, low-latency file system observation; provide a PeriodicStrategy for environments where inotify is unavailable.
**Consequences:** 
- Positive: Real-time, efficient detection on Linux; cross-platform operability preserved via periodic polling.
- Negative: Event-driven solution is Linux-specific; periodic polling consumes more resources and may miss rapid transient changes between scans.
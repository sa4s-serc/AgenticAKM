---
### ADR-003: Event-Driven File System Monitoring using Inotify

**Status:** Inferred
**Context:** A core requirement for a backup application is to detect file system changes (creations, modifications, deletions) in a timely and efficient manner. The architectural choice was between a resource-intensive periodic polling method (repeatedly scanning directories for changes) and a more efficient, OS-level event notification system.
**Decision:** The system uses the Linux `inotify` kernel feature for event-driven file system monitoring. This decision is supported by several pieces of evidence:
*   The `pyinotify` library is listed as a dependency in `requirements.txt`.
*   The `docs/ADRs/Inotify.md` file explicitly documents this choice.
*   The `src/phoenix/Observation/` module contains `EventDrivenStrategy.py`, which contrasts with the also-present `PeriodicStrategy.py`, indicating a deliberate choice was made between the two approaches.
**Consequences:**
*   **Positive:**
    *   **High Efficiency:** Using `inotify` is extremely efficient in terms of CPU usage, as the application sleeps until the kernel notifies it of an event, avoiding constant polling.
    *   **Real-time Response:** File system changes are detected almost instantaneously, allowing for near real-time backups.
*   **Negative:**
    *   **Platform Dependency:** `inotify` is specific to the Linux kernel. This decision makes the application less portable to other operating systems like Windows (which uses `FileSystemWatcher`) or macOS (which uses `FSEvents`) without adding separate, platform-specific implementations.
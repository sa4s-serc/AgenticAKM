---
### ADR-002: File-Based Knowledge Base for Runtime State

**Status:** Inferred
**Context:** The MAPE-K loop requires a central repository (the "Knowledge Base") for storing and sharing data between its different phases. This includes monitored metrics (like `drift.csv`), system state (`model.csv`), analysis results (`mape_log.csv`), and configuration (`thresholds.json`). A decision was needed on the technology to implement this knowledge base. The options could range from an in-memory solution to a full-fledged database.
**Decision:** A simple, file-based approach was chosen for the Knowledge Base. The `knowledge/` directory contains a collection of flat files (CSVs and JSONs) that store the runtime state and operational data. This solution avoids introducing a heavy external dependency for the core adaptation loop's state management.
**Consequences:**
*   **Positive:** The solution is lightweight, has no external dependencies, and is highly portable. The state is human-readable and easy to inspect and debug directly from the filesystem. It is simple to set up and manage.
*   **Negative:** This approach does not scale well for high-concurrency scenarios where multiple processes might try to write to the files simultaneously. Querying the data is less efficient than using a proper database. It may become a performance bottleneck if the volume of logged data becomes very large.
---
### ADR-005: File-Based Data Exchange and State Management

**Status:** Inferred
**Context:** The various components of the MAPE-K loop (Monitor, Analyzer, Planner, Execute) need to exchange data and maintain state. For example, the Monitor needs to pass metrics to the Analyzer, and the Planner's decisions must be recorded. A simple, transparent, and easily debuggable mechanism for this data flow was required, likely for a single-machine, non-concurrent research prototype.
**Decision:** CSV files were chosen as the primary medium for data exchange and logging. This is strongly supported by the presence of numerous `.csv` files that act as interfaces or logs between components, such as `monitor.csv`, `knowledge.csv`, `model.csv`, `log.csv`, and `MAPEK_energy.csv`. There is no evidence of a database, messaging queue, or network-based API.
**Consequences:**
*   **Positive:** Using CSV files makes the system's state and data flow highly transparent and easy to inspect for debugging and analysis. It requires no external dependencies like a database server, simplifying setup. This is ideal for academic research and prototyping.
*   **Negative:** This approach is not scalable or robust for a production environment. It is susceptible to I/O bottlenecks, lacks support for concurrent read/write operations, and does not provide transactional guarantees, making it unsuitable for high-throughput or multi-process applications.
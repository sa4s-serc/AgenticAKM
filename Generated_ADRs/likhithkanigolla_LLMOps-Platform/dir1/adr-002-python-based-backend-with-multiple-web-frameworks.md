---
### ADR-002: Python-based Backend with Multiple Web Frameworks

**Status:** Inferred
**Context:** A backend technology stack was needed to implement the various microservices. The choice of language and framework impacts development speed, performance, and the available ecosystem of tools and libraries.
**Decision:** Python was chosen as the primary language for backend services. The presence of multiple `requirements.txt` files shows a heavy reliance on Python. Interestingly, two different web frameworks are in use: **Flask** is used across many services (`frontend`, `controller-Service`, `agent-Service`), while **FastAPI** is used in at least one service (`model-registry`).
**Consequences:**
*   **Positive:**
    *   Python's extensive ecosystem provides ready-made libraries for needs like messaging (`confluent-kafka`), container management (`docker`), and web services (`flask`, `fastapi`).
    *   Fast development cycle, which is a hallmark of Python.
*   **Negative:**
    *   Using both Flask and FastAPI introduces heterogeneity, which can increase the cognitive load for developers working across services and may lead to inconsistencies in coding patterns and API design.
    *   Python's performance (due to the GIL) might be a bottleneck for CPU-intensive tasks, though using an ASGI framework like FastAPI helps mitigate this for I/O-bound workloads.
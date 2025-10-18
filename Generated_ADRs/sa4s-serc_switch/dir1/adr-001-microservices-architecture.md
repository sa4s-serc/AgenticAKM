### ADR-001: Microservices Architecture

**Status:** Inferred
**Context:** The system has functionally distinct components with different technological needs and scaling requirements. There is a user-facing web interface, a computationally intensive machine learning backend, and a dedicated service for data storage and visualization. Building this as a single monolithic application would tightly couple these components, making independent development, deployment, and scaling difficult.
**Decision:** The system is decomposed into a microservices architecture. This includes:
1.  A **Frontend Service** built with Node.js and React for the user interface.
2.  A **Backend Service** built with Python to handle core logic and machine learning inference.
3.  An **Observability/Data Service** using the ELK Stack (Elasticsearch, Kibana) for logging, metrics, and data visualization.
**Consequences:**
*   **Positive:** Enables separation of concerns, allowing teams to work on the frontend and backend independently. Allows for technology heterogeneity (JavaScript/React for UI, Python for ML). Each service can be scaled, deployed, and updated without affecting the others.
*   **Negative:** Increases operational complexity, requiring management of multiple running services. Introduces network latency for communication between services (e.g., between the React frontend and the Python API, suggested by `axios`). Requires a robust service discovery and orchestration mechanism.
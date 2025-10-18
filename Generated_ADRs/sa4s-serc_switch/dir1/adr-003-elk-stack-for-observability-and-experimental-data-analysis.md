---
### ADR-003: ELK Stack for Observability and Experimental Data Analysis

**Status:** Inferred
**Context:** The system is designed for running experiments and may feature self-adaptive capabilities. To support this, it requires a robust solution for collecting, storing, searching, and visualizing large volumes of operational data, including application logs and performance metrics. Storing this data in flat files or a traditional relational database would not be optimal for full-text search and time-series analysis.
**Decision:** Adopt the ELK Stack (Elasticsearch and Kibana). Elasticsearch is used as the central data store for logs and metrics due to its powerful indexing and search capabilities. Kibana is used to provide a web-based interface for querying, exploring, and creating dashboards from the data in Elasticsearch.
**Consequences:**
*   **Positive:** Provides a powerful, scalable, and near real-time platform for observability. The backend explicitly sends data to Elasticsearch (`logs_to_es.py`, `metrics_to_es.py`), enabling deep analysis of system behavior and experimental results. Kibana allows for the creation of rich, interactive dashboards to monitor system health.
*   **Negative:** The ELK Stack is a resource-intensive component, requiring significant memory and CPU. It introduces additional complexity to the system's architecture and requires specialized knowledge for maintenance and optimization.
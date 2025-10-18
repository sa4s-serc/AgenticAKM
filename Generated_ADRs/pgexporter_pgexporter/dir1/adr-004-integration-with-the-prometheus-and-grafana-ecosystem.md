---
### ADR-004: Integration with the Prometheus and Grafana Ecosystem

**Status:** Inferred

**Context:** The primary goal of the project is to export PostgreSQL metrics for monitoring. Rather than creating a new, proprietary monitoring solution, the project needed to integrate with existing, popular tools to maximize adoption and utility. The cloud-native and open-source communities have largely standardized on Prometheus for metrics collection and Grafana for visualization.

**Decision:** The project is designed as a **Prometheus exporter**. It exposes metrics over an HTTP endpoint in the Prometheus text-based format. Furthermore, it provides pre-built **Grafana dashboards** to facilitate immediate visualization of the exported data.

**Consequences:**
*   **Positive:**
    *   **Rapid Adoption:** By targeting the Prometheus ecosystem, the project is immediately useful to a large existing user base.
    *   **Leverages Existing Infrastructure:** Users can integrate `pgexporter` into their existing Prometheus and Grafana stacks for metric storage, alerting, and visualization without needing new tools.
    *   **Standardization:** Adhering to the Prometheus exposition format is a well-understood and documented standard.
    *   **Enhanced User Experience:** Providing ready-to-use Grafana dashboards (seen in `contrib/grafana/`) significantly lowers the barrier to entry and allows users to get value from the exporter almost instantly.
*   **Negative:**
    *   **Constrained by Prometheus Model:** The project is tied to the pull-based, multi-dimensional data model of Prometheus. It is less suitable for push-based or event-logging use cases.
    *   **Dependency on External Systems:** The full value of `pgexporter` is only realized when used as part of a larger monitoring stack (Prometheus, Grafana).
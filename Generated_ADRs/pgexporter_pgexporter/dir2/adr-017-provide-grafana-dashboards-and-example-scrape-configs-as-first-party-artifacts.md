---
### ADR-017: Provide Grafana dashboards and example scrape configs as first-party artifacts

Status: Inferred
Context: contrib/grafana dashboards for multiple PostgreSQL versions and contrib/prometheus_scrape assets.
Decision: Ship reference Grafana dashboards and scrape examples to accelerate adoption and ensure correct metric usage.
Consequences:
- Positive: Faster time-to-value; consistent visualization; reduces user misconfiguration.
- Negative: Ongoing maintenance to keep dashboards in sync with metrics; version drift risks.
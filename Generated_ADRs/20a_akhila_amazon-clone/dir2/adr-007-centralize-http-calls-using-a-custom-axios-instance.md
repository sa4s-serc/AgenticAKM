---
### ADR-007: Centralize HTTP calls using a custom Axios instance

Status: Inferred
Context: src/axios.js exists and axios is a dependency, indicating a shared Axios client for API calls (likely to Cloud Functions endpoints).
Decision: Create a centralized Axios instance (with baseURL and common interceptors/config) for all API communication.
Consequences:
- Positive: DRY configuration for base URLs, headers, and error handling; easier environment switching (local emulator vs production).
- Negative: Another abstraction to maintain; misconfiguration can break all API calls; must ensure SSR/CSR-safe base URLs if applicable.
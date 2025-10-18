---
### ADR-003: Introduce Endpoint and Task abstractions to construct requests

**Status:** Inferred
**Context:** The system needs to transform high-level endpoint descriptions into executable URLRequests while supporting various request types (plain, parameters, multipart, uploads, downloads). Files Endpoint.swift, Task.swift, URLRequest+Encoding.swift reflect this.
**Decision:** Use Endpoint as the request blueprint and Task as an enum capturing request intent (e.g., requestPlain, requestParameters, uploadMultipart, download).
**Consequences:** 
- Positive: Flexible request construction; centralized encoding logic; supports complex scenarios.
- Negative: Increased complexity around encoding and edge cases; additional mapping layers.
- Trade-off: Versatility and clarity in exchange for more moving parts.
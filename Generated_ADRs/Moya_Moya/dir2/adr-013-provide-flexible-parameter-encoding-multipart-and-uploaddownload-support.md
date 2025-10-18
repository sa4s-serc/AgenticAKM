---
### ADR-013: Provide flexible parameter encoding, multipart, and upload/download support

**Status:** Inferred
**Context:** Real-world APIs require diverse payload formats and transports. Files URLRequest+Encoding.swift, MultipartFormData.swift, AnyEncodable.swift, and Task cases reflect this need.
**Decision:** Centralize encoding strategies and support JSON, URL-encoded, multipart form data, and file uploads/downloads through Task and helpers.
**Consequences:** 
- Positive: Handles broad API surface; reduces consumer-side boilerplate.
- Negative: Complexity in encoding layer; potential edge cases across platforms.
- Trade-off: Capability breadth over minimalism.
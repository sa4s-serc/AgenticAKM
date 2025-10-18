### ADR-001: Adopt Alamofire as the underlying HTTP networking layer

**Status:** Inferred
**Context:** The library needs a robust, battle-tested HTTP client to handle request execution, encoding, and networking concerns without reinventing low-level networking. The presence of Moya+Alamofire.swift indicates an integration layer, suggesting reliance on Alamofire for transport.
**Decision:** Use Alamofire as the underlying transport layer while exposing Moya’s own abstractions (TargetType, Endpoint, Response, MoyaError) to consumers.
**Consequences:** 
- Positive: Leverages a mature ecosystem; reduces boilerplate; benefits from Alamofire’s reliability and features.
- Negative: Introduces a transitive dependency and version coupling; potential need to adapt Moya API to Alamofire changes.
- Trade-off: Moya focuses on higher-level API design and plugins, delegating low-level HTTP concerns to Alamofire.
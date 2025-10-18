---
### ADR-008: Support multiple dependency managers (SPM, Carthage, CocoaPods)

**Status:** Inferred
**Context:** Diverse consumer preferences require flexible distribution. The repo includes Package.swift, Cartfile, Moya.podspec, and supporting scripts.
**Decision:** Maintain packaging for Swift Package Manager, Carthage, and CocoaPods.
**Consequences:** 
- Positive: Maximizes accessibility; easier adoption in varied environments.
- Negative: Higher release complexity; need to keep manifests in sync; CI burden.
- Trade-off: Distribution reach vs. maintenance overhead.
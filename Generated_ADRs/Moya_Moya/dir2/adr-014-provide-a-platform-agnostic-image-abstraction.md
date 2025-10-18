---
### ADR-014: Provide a platform-agnostic Image abstraction

**Status:** Inferred
**Context:** Uploading images and working across Apple platforms needs a shared type without leaking UIKit/AppKit specifics. The file Image.swift suggests conditional abstraction.
**Decision:** Define an Image wrapper/typealias that maps to UIImage on iOS and NSImage on macOS, used in relevant request payloads.
**Consequences:** 
- Positive: Cross-platform API consistency; simpler consumer code.
- Negative: Conditional compilation complexity; platform-specific nuances still exist under the hood.
- Trade-off: Unified API surface vs. internal platform branching.
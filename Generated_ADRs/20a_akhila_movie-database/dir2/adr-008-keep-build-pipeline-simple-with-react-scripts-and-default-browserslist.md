---
### ADR-008: Keep build pipeline simple with react-scripts and default Browserslist

Status: Inferred
Context: package.json uses react-scripts for build/test and includes a standard Browserslist for production/development targets.
Decision: Use CRA’s built-in build/test tooling without ejecting; target a broad set of modern browsers via the default Browserslist.
Consequences:
- Positive: Minimal build maintenance; consistent, reliable builds; automatic polyfills aligned to targets.
- Negative: Limited flexibility for advanced bundling or custom loaders; potential need to eject or migrate if advanced optimizations are required.
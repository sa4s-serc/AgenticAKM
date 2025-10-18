---
### ADR-004: Represent watched directories using the Composite pattern

**Status:** Inferred
**Context:** The Observation/WatchDirStructure contains WatchDirComponent, WatchDirComposite, and WatchDirLeaf, indicating a classic Composite pattern to uniformly handle files and directories.
**Decision:** Model watched directory trees with a Composite structure to treat files and directories uniformly for traversal and operations.
**Consequences:** 
- Positive: Simplifies tree-wide operations (aggregation, traversal, filtering) and supports nested directories naturally.
- Negative: Adds structural complexity and more classes; requires careful management of component lifecycles and references.
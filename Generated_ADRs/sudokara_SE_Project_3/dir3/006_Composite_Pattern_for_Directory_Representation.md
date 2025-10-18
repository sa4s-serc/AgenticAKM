# ADR-006: Composite Pattern for Directory Representation

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system needed to process a hierarchical directory structure containing both files and sub-directories. A consistent way to operate on these different types of file system entries was required to simplify the monitoring and processing logic.

## Decision
The Composite design pattern was implemented to model the directory tree. This allows the system to treat individual files (Leafs) and directories (Composites) uniformly, simplifying the logic for recursive operations.

## Consequences
This pattern simplifies the client code that traverses and acts upon the directory structure, as it doesn't need to differentiate between files and directories. This makes it easier to apply operations like 'backup' or 'scan' across the entire tree recursively and elegantly.
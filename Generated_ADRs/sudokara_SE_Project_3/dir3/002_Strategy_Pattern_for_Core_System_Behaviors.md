# ADR-002: Strategy Pattern for Core System Behaviors

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system required flexibility for its core functions, such as how it detects file changes, compresses files, encrypts data, and uploads to cloud providers. Hardcoding these implementations would make the system rigid and difficult to extend with new options in the future.

## Decision
The Strategy design pattern was pervasively used to create pluggable components. This allows different algorithms and implementations (e.g., 'inotify' vs. 'periodic' monitoring, 'Google Drive' vs. 'OneDrive' uploader) to be selected and swapped at runtime through configuration.

## Consequences
The system is highly extensible and flexible. New strategies, such as a different cloud provider or compression algorithm, can be added with minimal changes to the core application logic. This promotes a clean, decoupled design that adheres to the Open/Closed Principle.
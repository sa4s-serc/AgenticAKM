# ADR-004: Composable and Accessible UI with shadcn/ui and Tailwind CSS

**Date**: 2025-10-16
**Status**: Proposed

## Context
The platform required a high-quality, professional, and accessible user interface that could be developed rapidly without being locked into the rigid opinions of a traditional UI framework.

## Decision
The team chose `shadcn/ui`, which leverages Radix UI for unstyled, accessible components and Tailwind CSS for utility-first styling. This provides a library of composable UI elements that developers can copy into their project and fully customize.

## Consequences
This decision accelerates UI development while maintaining full control over styling and component logic. It promotes design consistency and high accessibility standards (via Radix). The trade-off is that developers are responsible for managing updates to these components, as they are part of the application's source code rather than an external dependency.
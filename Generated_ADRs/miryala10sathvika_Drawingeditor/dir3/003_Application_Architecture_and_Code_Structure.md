# ADR-003: Application Architecture and Code Structure

**Date**: 2025-10-13
**Status**: Proposed

## Context
The overall structure for the application's source code needed to be defined. The repository contains two large, monolithic script files (`draw.py`, `extra.py`) that seem to contain most of the application's logic and UI code.

## Decision
The application was architected in a monolithic style, with UI rendering, event handling, and application logic tightly coupled within single script files. There is no explicit separation of concerns, such as a Model-View-Controller (MVC) or similar design pattern.

## Consequences
This monolithic approach is simple and enables rapid prototyping for a small-scale application. However, it significantly hinders scalability and maintainability. As new features are added, the codebase will become increasingly complex and difficult to debug or modify without introducing side effects. The presence of two similar files suggests this structure may have already led to difficulties in code management and versioning.
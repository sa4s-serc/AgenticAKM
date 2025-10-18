# ADR-001: Dual-Interface Strategy for User Access

**Date**: 2025-10-14
**Status**: Proposed

## Context
The platform needed to cater to a diverse user base with varying levels of technical proficiency and interaction preferences. A single interface might not effectively serve all potential users of the retail, healthcare, and delivery services.

## Decision
Implement two distinct user-facing frontends: a graphical mobile application built with React Native for a rich, visual experience, and a conversational WhatsApp bot for a low-friction, text and voice-based experience.

## Consequences
This approach maximizes user reach and accessibility by offering choice. However, it increases development and maintenance overhead, as two separate codebases must be managed. It also necessitates a robust, shared backend API to ensure business logic and data consistency across both interfaces.
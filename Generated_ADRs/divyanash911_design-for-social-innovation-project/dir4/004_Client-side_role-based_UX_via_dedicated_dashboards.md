# ADR-004: Client-side role-based UX via dedicated dashboards

**Date**: 2025-10-13
**Status**: Proposed

## Context
Components include ChildDashboard, ParentDashboard, TeacherDashboard, and PsychologistDashboard.

## Decision
Implement role-specific user experiences primarily on the client with separate dashboard components and routes.

## Consequences
Improves clarity and tailored UX per role, but requires backend enforcement of authorization since client-side checks cannot be trusted.
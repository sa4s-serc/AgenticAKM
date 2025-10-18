# ADR-004: Role-Based Access Control (RBAC) via Segregated Dashboards

**Date**: 2025-10-13
**Status**: Proposed

## Context
The system must serve multiple user archetypes (Administrator, Teacher, Parent, Child) with fundamentally different permissions, data visibility, and workflows. A one-size-fits-all interface would be both insecure and confusing.

## Decision
An RBAC architecture was implemented, enforced by distinct, role-specific dashboards on the frontend and protected API endpoints on the backend. User identity and roles are likely managed via JWT claims, which dictate what data and functionality a user can access.

## Consequences
This design enhances security by enforcing the principle of least privilege and improves usability by tailoring the experience to each user's role. It creates a modular and scalable structure for adding new roles in the future. However, it increases development complexity, requiring separate UI components and views for each role and robust authorization logic on every relevant backend route.
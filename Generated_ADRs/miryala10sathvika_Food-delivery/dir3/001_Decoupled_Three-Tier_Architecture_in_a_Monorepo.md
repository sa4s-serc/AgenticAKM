# ADR-001: Decoupled Three-Tier Architecture in a Monorepo

**Date**: 2025-10-13
**Status**: Proposed

## Context
The project required building and maintaining three distinct but related components: a customer-facing web application, an administrative dashboard, and a shared backend API. The goal was to enable independent development and scaling while keeping the codebase organized and co-located.

## Decision
A three-tier architecture was adopted, separating the system into a React frontend (presentation), a Node.js/Express API (business logic), and a MongoDB database (data). These components are organized within a single monorepo, creating a decoupled yet cohesive system.

## Consequences
This separation of concerns allows for independent development, deployment, and scaling of the frontend, backend, and admin panel. It promotes a clear API contract between services and allows teams to specialize. The monorepo structure simplifies dependency management and cross-component refactoring.
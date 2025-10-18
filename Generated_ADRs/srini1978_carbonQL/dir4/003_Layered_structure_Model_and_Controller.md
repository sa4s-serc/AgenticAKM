# ADR-003: Layered structure: Model and Controller

**Date**: 2025-10-09
**Status**: Proposed

## Context
Backend library organized into Model/EtsyModels.cs and Controller/EtsyCalculations.cs.

## Decision
Adopt a simple layered design with data models and calculation/controller logic.

## Consequences
Improves code organization and readability. Lack of explicit service/repository layers may hinder scalability if persistence, integration, or richer domain behavior is added later.
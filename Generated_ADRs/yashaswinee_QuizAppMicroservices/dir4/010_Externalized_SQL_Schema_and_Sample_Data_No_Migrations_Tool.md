# ADR-010: Externalized SQL Schema and Sample Data (No Migrations Tool)

**Date**: 2025-10-16
**Status**: Proposed

## Context
The repository includes raw SQL for schema and sample data under resources, but no Flyway/Liquibase integration is indicated.

## Decision
Manage schema and seed data via SQL files executed at startup instead of a formal database migration framework.

## Consequences
Simple and transparent for initial setups; lacks versioned, repeatable migrations for multi-environment lifecycle; increases risk of drift and manual error when evolving the schema over time.
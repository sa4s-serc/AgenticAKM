# ADR-009: Manual Wiring of Search Components (No IaC Provided)

**Date**: 2025-10-09
**Status**: Proposed

## Context
Repository lacks index, data source, indexer, and skillset definitions (ARM/Bicep/Terraform/REST).

## Decision
Leave provisioning and pipeline wiring to consumers or manual setup outside the repo.

## Consequences
Reduces repository complexity but increases setup friction, drift risk between environments, and repeatability challenges; adopting IaC would improve reliability and onboarding at the cost of additional artifacts and maintenance.
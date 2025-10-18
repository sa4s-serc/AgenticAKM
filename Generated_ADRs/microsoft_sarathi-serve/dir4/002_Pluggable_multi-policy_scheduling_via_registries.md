# ADR-002: Pluggable multi-policy scheduling via registries

**Date**: 2025-10-14
**Status**: Proposed

## Context
Different workloads and research goals require trying diverse scheduling strategies and comparing them under identical conditions.

## Decision
Provide scheduler implementations (Sarathi, vLLM-like, FasterTransformer-like, Orca-like, simple chunking) discoverable through a registry, with a common policy interface and shared datatypes.

## Consequences
Allows apples-to-apples comparisons and rapid prototyping of new schedulers; adds adapter/compatibility effort and maintenance cost to keep the common interface stable across heterogeneous strategies.
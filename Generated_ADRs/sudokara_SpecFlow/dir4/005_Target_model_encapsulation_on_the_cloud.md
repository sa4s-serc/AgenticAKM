# ADR-005: Target model encapsulation on the cloud

**Date**: 2025-10-14
**Status**: Proposed

## Context
Cloud needs to validate and extend edge token proposals efficiently.

## Decision
Wrap the target model behind cloud/target_model.py and coordinate requests in cloud/server.py.

## Consequences
Separates concerns and eases replacement/upgrades of the cloud model; shifts throughput bottlenecks to the server and requires robust concurrency and scheduling policies.
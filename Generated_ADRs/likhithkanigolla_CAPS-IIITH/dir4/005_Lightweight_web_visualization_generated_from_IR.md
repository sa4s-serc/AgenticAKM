# ADR-005: Lightweight web visualization generated from IR

**Date**: 2025-10-09
**Status**: Proposed

## Context
Stakeholders need to inspect generated systems without running the simulator.

## Decision
Provide a simple web generator (HTML/CSS/JS) that converts model.json into interactive assets with no heavy frontend framework.

## Consequences
Easy to host and distribute; low runtime complexity; limits interactivity and scalability compared to richer frameworks; relies on IR fidelity for correctness.
# ADR-002: Python-based NAVIE backend with modular orchestration

**Date**: 2025-10-10
**Status**: Proposed

## Context
Rapid prototyping is needed around ML workflows (YOLOv5) and process control without heavy web frameworks.

## Decision
Build the backend in Python as a set of modules (Monitor/Analyzer/Planner/Execute plus utilities) coordinated by scripts such as Node.py rather than a heavyweight service framework.

## Consequences
Leverages Python’s ML ecosystem and accelerates iteration; simplifies deployment; risks looser API contracts, single-process constraints, and ad-hoc process management that may hinder scaling and robustness.
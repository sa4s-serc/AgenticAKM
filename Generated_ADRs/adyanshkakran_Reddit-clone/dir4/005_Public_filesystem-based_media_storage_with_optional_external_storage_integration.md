# ADR-005: Public filesystem-based media storage with optional external storage integration

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backend public/greddit-images and public/user-images directories exist, and an onedrive.js module suggests potential cloud integration.

## Decision
Serve uploaded images and media from Express public directories by default, with a path to integrate external storage (e.g., OneDrive) if needed.

## Consequences
Simple and fast for local and small-scale deployments; in containers, requires volumes for persistence and complicates horizontal scaling without shared storage; external storage can improve scalability and durability but adds external dependencies, configuration, and latency.
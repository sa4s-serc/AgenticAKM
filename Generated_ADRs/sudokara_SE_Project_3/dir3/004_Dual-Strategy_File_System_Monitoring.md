# ADR-004: Dual-Strategy File System Monitoring

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system needed an efficient and reliable method to detect file system changes. A key trade-off was between real-time performance, resource utilization, and cross-platform compatibility.

## Decision
Two distinct monitoring strategies were implemented: 1) A high-performance, event-driven approach for Linux using the `inotify` kernel subsystem. 2) A polling-based periodic scan to serve as a more cross-platform compatible fallback option.

## Consequences
The event-driven `inotify` strategy offers superior real-time performance and low overhead on supported systems (Linux). The inclusion of a periodic polling strategy makes the system more robust and adaptable to environments where `inotify` is unavailable, at the cost of higher latency and resource usage for that mode.
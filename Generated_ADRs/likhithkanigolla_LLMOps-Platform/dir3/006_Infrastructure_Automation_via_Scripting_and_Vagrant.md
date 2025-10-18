# ADR-006: Infrastructure Automation via Scripting and Vagrant

**Date**: 2025-10-09
**Status**: Proposed

## Context
The project required a repeatable, automated process for provisioning the underlying infrastructure, including virtual machines and service installations, for development and testing environments.

## Decision
Vagrant was chosen to manage the lifecycle of virtual machines, and a collection of shell scripts was created to handle the bootstrapping and configuration of the services and their dependencies (like NFS).

## Consequences
This provides a functional and low-overhead method for automating environment setup, especially for local development. However, shell scripts can become brittle and difficult to maintain as system complexity grows. This approach lacks the idempotency and robust state management of mature Infrastructure-as-Code tools like Ansible or Terraform, making it less suitable for reliable production deployments.
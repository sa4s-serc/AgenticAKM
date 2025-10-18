# ADR-005: VM-based deployment and testing with Vagrant

**Date**: 2025-10-09
**Status**: Proposed

## Context
vm-service/ includes a Vagrantfile, .vagrant artifacts, and a nested app VM example; bootstrap scripts target VM creation.

## Decision
Prefer Vagrant-managed VMs for provisioning execution environments and testing model deployments.

## Consequences
Pros: reproducible local environments, parity with VM-targeted deployments, straightforward bootstrap. Cons: heavyweight compared to containers, slower provisioning and scaling, not cloud-native, and reduced portability to container orchestrators.
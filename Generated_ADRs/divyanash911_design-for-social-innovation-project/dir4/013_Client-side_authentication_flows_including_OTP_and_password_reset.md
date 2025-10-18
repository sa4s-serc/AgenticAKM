# ADR-013: Client-side authentication flows including OTP and password reset

**Date**: 2025-10-13
**Status**: Proposed

## Context
Frontend components include Login, SignUp, OTPComp, and ResetPass.

## Decision
Provide OTP verification and password reset user flows in the frontend as part of the authentication experience.

## Consequences
Improves onboarding and account recovery UX, but requires robust backend support, secure token handling, and rate limiting; backend implementation details are not confirmed in the repository summary.
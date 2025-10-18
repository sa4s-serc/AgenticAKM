# ADR-012: ADR-012: Frontend mock-data toggle via VITE_USE_MOCK and data service abstraction

**Date**: 2025-10-13
**Status**: Proposed

## Context
The customer frontend uses mock arrays (menu_list, food_list) embedded in src/assets/assets.js. There is no documented toggle for switching to live API data.

## Decision
Introduce a VITE_USE_MOCK boolean in both frontends and implement a single data service layer that either returns mock data or calls the live API (VITE_API_BASE_URL) based on the flag. Document the flag and expected behavior in README files. Default to mocks when onboarding is intended to be offline; ensure production builds use live API.

## Consequences
- Predictable switching between mock and live data.
- Prevents accidental shipping of mock data by centralizing the toggle.
- Requires minor refactor so components import data only through the service; add a checklist or test to verify VITE_USE_MOCK=false paths call the API.